try:
    from typing import Union, Optional
except ImportError:
    pass

from botball import wallaby
from .CameraTrackingColor import CameraTrackingColor
from .Rectangle import Rectangle


class Camera(object):
    """
    Represents a USB camera connected to the robot.
    """

    _tracking_color: CameraTrackingColor

    @property
    def tracking_color(self) -> CameraTrackingColor:
        """ 
        The current color of which objects the camera will track.

        Setting this value to a different color will trigger a camera update and
        may block the thread briefly.
        """
        return self._tracking_color

    @tracking_color.setter
    def tracking_color(self, value: CameraTrackingColor):
        if type(value) is str:
            self._tracking_color = CameraTrackingColor(value)
        else:
            self._tracking_color = value

        self._change_color_to(self._tracking_color)
        self.refresh()

    @property
    def height(self) -> int:
        """
        The height of the camera frame in pixels, offset by
        `Camera.camera_height_offset`.
        """
        return wallaby.get_camera_height() - self.camera_height_offset

    def __init__(self, tracking_color: Union[CameraTrackingColor, str]):
        """ 
        Initializes the camera with a tracking color. The camera should only be 
        used inside a `with` statement; for example:

        >>> with Camera(tracking_color="red") as camera:
        ...     print(camera.number_of_objects())

        - `tracking_color`: This can either be a CameraTrackingColor or a
        string representing a CameraTrackingColor, which will be
        automatically converted.

        - **Warning:** If the camera is not connected to the robot, then the
        program will crash as defined in `wallaby`.
        """
        self.tracking_color = tracking_color

    def __enter__(self):
        wallaby.camera_open()
        self._change_color_to(self._tracking_color)
        self.refresh()

    def __exit__(self, exception_type, exception_value, traceback):
        wallaby.camera_close()

    # - Refreshing camera

    def refresh(self, frames: Optional[int] = None):
        """
        Refreshes the camera by collecting the number of frames specified in
        `Camera.number_of_updates_during_refresh` to make the object tracking
        more accurate. Blocks the thread until finished.

        You shouldn't normally need to call this method yourself; it is called
        automatically during initialization and when the camera's tracking color
        is changed.

        - `frames`: If provided, this number of frames will be fetched instead.
        """
        number_of_times = frames or self.number_of_updates_during_refresh

        for _ in range(number_of_times):
            wallaby.camera_update()

    # - Constants

    camera_channel: int = 0
    """
    The camera channel on which to check for objects. This shouldn't need to 
    be changed if you use the provided configuration files.

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """

    object_confidence_threshold: float = 0.42
    """
    The minimum value returned by `wallaby`'s `get_object_confidence()` for 
    an object to be recognized as "trackable".

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """

    number_of_updates_during_refresh: int = 20
    """
    The number of frames the camera should fetch during a refresh (eg. during
    initialization or a change in the active tracking color) before tracking
    objects in the output. The higher the number, the more accurate object
    tracking will be, but the longer it will take for refreshes to occur.

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """

    camera_height_offset: int = 15
    """
    The number of pixels to offset the camera boundaries to make object tracking
    more accurate.

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """

    # - Changing color 

    def _change_color_to(self, tracking_color: CameraTrackingColor):
        # The name of the configuration file to get the tracking info from. The 
        # .conf extension should NOT be provided.
        conf_name = "detect-" + str(tracking_color)

        success = wallaby.camera_load_config(bytes(conf_name)) == 1

        if not success:
            raise EnvironmentError(f"Error while loading tracking color configuration file for color '{str(tracking_color)}'")

    # - Object presence

    def number_of_objects(self) -> int:
        """
        The number of objects currently in the field of view.
        """
        return wallaby.get_object_count(self.camera_channel)

    def object_is_present(self) -> bool:
        """
        Whether an object of the current tracking color is present in the field 
        of view.
        """
        return self.number_of_objects() >= 1

    # - Bounding box

    def object_bbox(self, object_number: int = 0) -> Optional[Rectangle]:
        """
        Returns the bounding box for an object in the field of view, or `None`
        if the object is not found.
        """
        if self.number_of_objects() <= object_number:
            return None

        return wallaby.get_object_bbox(self.camera_channel, object_number)

    # - Distance

    def distance_to_object(self, object_number: int = 0, object_height: float = 0) -> Optional[float]:
        """
        Returns the distance to an object in the field of view, or `None` if the
        object is not found.

        - `object_height`: The height of the object in question in mm. This should
        be a known value based on the real-world measurement of the object
        for accurate results.
        """
        if self.number_of_objects() <= object_number:
            return None

        object_bbox = self.object_bbox(object_number)
        if object_bbox is None:
            return None

        object_height_px = float(object_bbox.height)

        return self.height * object_height / object_height_px

    # - Confidence

    def confidence_of_object(self, object_number: int = 0) -> Optional[float]:
        """
        Returns the confidence that the object is in the field of view, or
        `None` if the object is not found at all.
        """

        if self.number_of_objects() <= object_number:
            return None

        return wallaby.get_object_confidence(
            self.camera_channel,
            object_number
        )

    # - Trackability

    def object_is_trackable(self, object_number: int = 0) -> Optional[bool]:
        """
        Returns whether an object is considered to be close enough to the camera
        to be trackable, or `None` if the object is not found.
        """

        if self.number_of_objects() <= object_number:
            return None

        confidence = self.confidence_of_object(object_number)
        if confidence is None:
            return None

        return confidence > self.object_confidence_threshold
