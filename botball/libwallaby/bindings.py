try:
    from typing import Any
except ImportError:
    pass


def accel_x() -> int:
    """

    - File: analog.h

    - Copyright: KISS Institute for Practical Robotics

    - Defgroup: accel Accelerometer


    - Brief: Gets the sensed x acceleration

    - Description: +/- 2G range,  1024 per G

    - Description: This should be approximately 0 when at rest and flat on a table

    - Returns: The latest signed x acceleration value

    - In group: accel

    """
    ...

def accel_y() -> int:
    """

    - Brief: Gets the sensed y acceleration

    - Description: +/- 2G range,  1024 per G

    - Description: This should be approximately 0 when at rest and flat on a table

    - Returns: The latest signed y acceleration value

    - In group: accel

    """
    ...

def accel_z() -> int:
    """

    - Brief: Gets the sensed z acceleration

    - Description: +/- 2G range,  1024 per G

    - Description: This should be approximately -1024 when at rest and flat on a table

    - Returns: The latest signed z acceleration value

    - In group: accel

    """
    ...

def accel_calibrate() -> int:
    """

    Initiates a calibration of the accelerometer

    - Note: Not Yet Implemented

    - Returns: 1: success 0: failure

    - In group: accel

    """
    ...
def analog(port: int) -> int:
    """

    - File: analog.h

    - Copyright: KISS Institute for Practical Robotics

    - Defgroup: analog Analogs


    Gets the 12-bit analog value of a port.

    - Param:[in] port A value between 0 and 5 specifying the sensor to read from.

    - Returns: The latest 12-bit value of the port (a value in the range 0 to 4095).

    - See: analog12

    - In group: analog

    """
    ...

def analog8(port: int) -> int:
    """

    Gets the 8-bit analog value of a port.

    - Param:[in] port A value between 0 and 5 specifying the sensor to read from.

    - Returns: The latest 8-bit value of the port (a value in the range 0 to 255).

    - See: analog

    - In group: analog

    """
    ...

def analog10(port: int) -> int:
    """

    Gets the 10-bit analog value of a port.

    - Param:[in] port A value between 0 and 5 specifying the sensor to read from.

    - Returns: The latest 10-bit value of the port (a value in the range 0 to 1023).

    - See: analog

    - In group: analog

    """
    ...

def analog12(port: int) -> int:
    """

    Gets the 12-bit analog value of a port.

    - Param:[in] port A value between 0 and 5 specifying the sensor to read from.

    - Returns: The latest 12-bit value of the port (a value in the range 0 to 4095).

    - See: analog

    - In group: sensor

    """
    ...

def analog_et(port: int) -> int:
    """

    Gets the 10-bit analog value of an ET sensor on the given port.

    - Param:[in] port A value between 0 and 7 specifying the ET sensor to read from.

    - Returns: The latest 10-bit value of the port (a value in the range 0 to 1023).

    - See: analog

    - In group: analog

    - Deprecated: defaulting to analog() on the Wallaby

    """
    ...

def set_analog_pullup(port: int, pullup: int):
    """

    Sets analog pullup status for one port.

    - Param:[in] port A value between 0 and 5 specifying the analog sensor to read from.

    - Param:[in] pullup A value of 0 (inactive) or 1 (active).

    - See: analog

    - In group: analog

    - Deprecated: no effect on the Wallaby

    """
    ...

def get_analog_pullup(port: int) -> int:
    """

    Gets the analog pullup status for one portt.

    - Param:[in] port A value between 0 and 7 specifying the analog sensor to read from.

    - Returns: The status of the analog pullup on the specified port

    - See: analog

    - In group: analog

    - Deprecated: no effect on the Wallaby

    """
    ...
def set_dictionary(dicionaryId: int) -> int:
    """

    - File: aruco.h

    - Copyright: KISS Institute for Practical Robotics

    - Defgroup: aruco ArucoMarkers


    - Brief: Sets the dictionary to use for Aruco Markers

    - Description: dictionary id where < 0 is custom dictionary

    - Description: Gets and sets the Dictionary to use for Aruco Markers

    - Returns: signed int

    - In group: aruco

    """
    ...

def set_aruco_marker_size_cm(cm: int):
    """

    - Brief: Sets the Arcuo Marker Size

    - Description: set the aruco marker size in cm

    - Returns: void

    - In group: aruco

    """
    ...

def set_chess_board_square_size_cm(cm: int):
    """

    - Brief: Sets the Chess Board Square Size

    - Description: set the calibration chess board square size in cm

    - Returns: void

    - In group: aruco

    """
    ...

def get_marker_pose(markerId: int) -> int:
    """

    - Brief: Get XYZ RXRYRZ of an Aruco Marker

    - Description: marker of current dictionary

    - Description: Gets the Rotation and Translation vector of an Aruco Marker

    - Returns: double*

    - In group: aruco

    """
    ...

def can_see_marker(marker: int) -> int:
    """

    - Brief: Checks if a marker is in view

    - Description: marker id of current dictionary

    - Description: Checks if an Aruco Marker can be seen in the current view

    - Returns: signed short

    - In group: aruco

    """
    ...

def get_markers_in_view() -> int:
    """

    - Brief: Runs camera calibration

    - Description: Runs a camera calibration TODO

    - Returns: signed short

    - In group: aruco


    - Brief: Gets an array of all markers in view

    - Description: TODO

    - Description:  Gets an array of all Aruco markers in view

    - Returns: int*

    - In group: aruco

    """
    ...
def beep():
    """

    Trigger an audible beep

    - Note: does not seem to work on the Wallaby

    """
    ...
def battery_charging() -> int:
    """

    - File: battery.h

    - Author: Joshua southerland

    - Copyright: KISS Institute for Practical Robotics

    - Defgroup: battery Battery


    Whether or not the battery is charging

    - Returns: 0: not charging  1: charging

    - Deprecated: not applicable for the Wallaby controller

    - In group: battery

    """
    ...

def power_level() -> float:
    """

    The device's power level

    - Returns: The device's current battery capacity 0: 0%   1: 100%

    - Note: defaults to LiFePO4 chemistry

    - In group: battery

    """
    ...

def power_level_nimh() -> float:
    """

    The device's power level (NiMH chemistry)

    - Returns: The device's current battery capacity 0: 0%   1: 100%

    - In group: battery

    """
    ...

def power_level_lipo() -> float:
    """

    The device's power level (LiPo chemistry)

    - Returns: The device's current battery capacity 0: 0%   1: 100%

    - In group: battery

    """
    ...

def power_level_life() -> float:
    """

    The device's power level (LiFePO4 chemistry)

    - Returns: The device's current battery capacity 0: 0%   1: 100%

    - See: power_level()

    - In group: battery

    """
    ...
def shut_down_in(s: int):
    """

    Register an event to stop the user program after s seconds

    - Param:[in] s The number of seconds to wait before the end of program

    """
    ...

def wait_for_light(light_port_: int):
    """

    Initiate a calibration and wait for light sequence

    which is a normal early step in Botball programs

    - Param:[in] light_port_ The analog port and light sensor to use.

    """
    ...
def set_a_button_text(text: str):
    """

    - File: button.h

    - Copyright: KISS Institute for Practical Robotics

    - Defgroup: button Buttons


    Updates the A button's text.

    - Param: text The text to display. Limit of 16 characters.

    - In group: button

    - Deprecated: not planned for the Wallaby

    """
    ...

def set_b_button_text(text: str):
    """

    Updates the B button's text.

    - Param: text The text to display. Limit of 16 characters.

    - In group: button

    - Deprecated: not planned for the Wallaby

    """
    ...

def set_c_button_text(text: str):
    """

    Updates the C button's text.

    - Param: text The text to display. Limit of 16 characters.

    - In group: button

    - Deprecated: not planned for the Wallaby

    """
    ...

def set_x_button_text(text: str):
    """

    Updates the X button's text.

    - Param: text The text to display. Limit of 16 characters.

    - In group: button

    - Deprecated: not planned for the Wallaby

    """
    ...

def set_y_button_text(text: str):
    """

    Updates the Y button's text.

    - Param: text The text to display. Limit of 16 characters.

    - In group: button

    - Deprecated: not planned for the Wallaby

    """
    ...

def set_z_button_text(text: str):
    """

    Updates the Z button's text.

    - Param: text The text to display. Limit of 16 characters.

    - In group: button

    - Deprecated: not planned for the Wallaby

    """
    ...

def a_button() -> int:
    """

    Gets the A button's state (pressed or not pressed.)

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button_clicked

    - In group: button

    - Note: Not yet implemented

    """
    ...

def b_button() -> int:
    """

    Gets the B button's state (pressed or not pressed.)

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button_clicked

    - In group: button

    - Note: Not yet implemented

    """
    ...

def c_button() -> int:
    """

    Gets the C button's state (pressed or not pressed.)

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button_clicked

    - In group: button

    - Note: Not yet implemented

    """
    ...

def x_button() -> int:
    """

    Gets the C button's state (pressed or not pressed.)

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button_clicked

    - In group: button

    - Note: Not yet implemented

    """
    ...

def y_button() -> int:
    """

    Gets the Y button's state (pressed or not pressed.)

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button_clicked

    - In group: button

    - Note: Not yet implemented

    """
    ...

def z_button() -> int:
    """

    Gets the Z button's state (pressed or not pressed.)

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button_clicked

    - In group: button

    - Note: Not yet implemented

    """
    ...

def side_button() -> int:
    """

    Gets the side button's state (pressed or not pressed.)

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button_clicked

    - In group: button

    - Deprecated: Not present on the Wallaby

    """
    ...

def black_button() -> int:
    """

    Gets the black button's state (pressed or not pressed.)

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button_clicked

    - In group: button

    - Deprecated: Not present on the Wallaby

    """
    ...

def left_button() -> int:
    """

    Gets the left button's state (pressed or not pressed.)

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button_clicked

    - In group: button

    """
    ...

def right_button() -> int:
    """

    Gets the right button's state (pressed or not pressed.)

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button_clicked

    - In group: button

    """
    ...

def a_button_clicked() -> int:
    """

    Gets the A button's state (pressed or not pressed.)

    \blocksuntil the button is no longer pressed.

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button

    - In group: button

    - Note: Not yet implemented

    """
    ...

def b_button_clicked() -> int:
    """

    Gets the A button's state (pressed or not pressed.)

    \blocksuntil the button is no longer pressed.

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button

    - In group: button

    - Note: Not yet implemented

    """
    ...

def c_button_clicked() -> int:
    """

    Gets the B button's state (pressed or not pressed.)

    \blocksuntil the button is no longer pressed.

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button

    - In group: button

    - Note: Not yet implemented

    """
    ...

def x_button_clicked() -> int:
    """

    Gets the C button's state (pressed or not pressed.)

    \blocksuntil the button is no longer pressed.

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button

    - In group: button

    - Note: Not yet implemented

    """
    ...

def y_button_clicked() -> int:
    """

    Gets the X button's state (pressed or not pressed.)

    \blocksuntil the button is no longer pressed.

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button

    - In group: button

    - Note: Not yet implemented

    """
    ...

def z_button_clicked() -> int:
    """

    Gets the Y button's state (pressed or not pressed.)

    \blocksuntil the button is no longer pressed.

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button

    - In group: button

    - Note: Not yet implemented

    """
    ...

def side_button_clicked() -> int:
    """

    Gets the Z button's state (pressed or not pressed.)

    \blocksuntil the button is no longer pressed.

    - Returns: 1 for pressed, 0 for not pressed

    - See: a_button

    - In group: button

    - Note: Not yet implemented

    """
    ...

def any_button() -> int:
    """

    Determines whether or not any of the buttons are pressed.

    - Returns: 1 for pressed, 0 for not pressed

    - In group: button

    - Note: Not yet implemented

    """
    ...

def extra_buttons_show():
    """

    Shows the X, Y, and Z buttons.

    - See: set_extra_buttons_visible

    - In group: button

    - Note: Not yet implemented

    """
    ...

def extra_buttons_hide():
    """

    Hides the X, Y, and Z buttons. This is the default.

    - See: set_extra_buttons_visible

    - In group: button

    - Note: Not yet implemented

    """
    ...

def get_extra_buttons_visible() -> int:
    """

    Determines whether or not the X, Y, and Z buttons are visible.

    - See: set_extra_buttons_visible

    - In group: button

    - Note: Not yet implemented

    """
    ...

def set_extra_buttons_visible(visible: int):
    """

    Sets whether or not the X, Y, and Z buttons are visible.

    - See: get_extra_buttons_visible

    - In group: button

    - Note: Not yet implemented

    """
    ...
def camera_open() -> int:
    """

    Opens the default system camera for use at LOW_RES (160x120).

    - Returns: 1 on success, 0 on failure

    - See: camera_open_at_res

    - See: camera_open_device

    - See: camera_close

    - In group: camera

    """
    ...

def camera_open_black() -> int:
    """

    Opens the default system camera for use at LOW_RES (160x120).

    This will improve frame rates for the black Logitech camera

    - Returns: 1 on success, 0 on failure

    - See: camera_open_at_res

    - See: camera_open_device

    - See: camera_close

    - In group: camera

    """
    ...

def camera_open_at_res(res: Any) -> int:
    """

    Opens the default system camera for use at a given resolution.

    - Param: res The resolution the camera should operate at. This can be:

      - LOW_RES (160x120)

      - MED_RES (320x240)

      - HIGH_RES (640x480)

    \warning Only LOW_RES is currently supported. The function will fail for other resolutions.

    - Returns: 1 on success, 0 on failure

    - See: camera_open

    - See: camera_open_device

    - See: camera_close

    - In group: camera

    """
    ...

def camera_open_device(number: int, res: Any) -> int:
    """

    Opens a camera for use.

    - Param: number The camera's id. 0 is the first camera, 1 is the second camera, etc.

    - Param: res The resolution the camera should operate at. This can be:

      - LOW_RES (160x120)

      - MED_RES (320x240)

      - HIGH_RES (640x480)

    \warning Only LOW_RES is currently supported. The function will fail for other resolutions.

    - Returns: 1 on success, 0 on failure

    - See: camera_open

    - See: camera_close

    - In group: camera

    """
    ...

def camera_open_device_model_at_res(number: int, model: Any, res: Any) -> int:
    """

    Opens a camera for use.

    - Param: number The camera's id. 0 is the first camera, 1 is the second camera, etc.

    - Param: res The resolution the camera should operate at. This can be:

      - LOW_RES (160x120)

      - MED_RES (320x240)

      - HIGH_RES (640x480)

    - Param: model The camera model

      - WHITE_2016  The white 2016 Botball camera

      - BLACK_2017  The black 2017 Botball camera

    \warning MED_RES is supported only for the BLACK_2017 camera and HIGH_RES is not supported

    - Returns: 1 on success, 0 on failure

    - See: camera_open

    - See: camera_close

    - In group: camera

    """
    ...

def camera_load_config(name: str) -> int:
    """

    Loads the config file specified by name. The system will look for the config in the base path.

    - Param: name The configuration to load. Configuration file names are case sensitive.

    - Note: Do NOT include the config file extension ".conf" in the name parameter.

    - Returns: 1 on success, 0 on failure.

    - See: set_camera_config_base_path

    - In group: camera

    """
    ...

def set_camera_width(width: int):
    """

    Sets the camera's x resolution.

    \warning Setting the camera width is not currently supported.

    - Param: width The width in pixels

    - In group: camera

    """
    ...

def set_camera_height(height: int):
    """

    Sets the camera's y resolution.

    \warning Setting the camera height is not currently supported.

    - Param: width The height in pixels

    - In group: camera

    """
    ...

def get_camera_width() -> int:
    """

    Gets the camera's x resolution.

    \attention This value might be different than the previously set x resolution. Never assume the x resolution.

    - Returns: The camera's x resolution, in pixels.

    - In group: camera

    """
    ...

def get_camera_height() -> int:
    """

    Gets the camera's y resolution.

    \attention This value might be different than the previously set y resolution. Never assume the y resolution.

    - Returns: The camera's y resolution, in pixels.

    - In group: camera

    """
    ...

def camera_update() -> int:
    """

    Pulls a new image from the camera for processing.

    - Returns: 1 on success, 0 on failure.

    - In group: camera

    """
    ...

def get_camera_pixel(p: Any) -> Any:
    """

    Gets the color of a pixel.

    - Param: p The point at which the pixel lies.

    - Returns: The rgb value of the pixel located at point p.

    - Note: A (r, g, b) value of (-1, -1, -1) will be returned for points that are out of range.

    - In group: camera

    """
    ...

def get_channel_count() -> int:
    """

    - Returns: Number of channels in the current configuration.

    - See: get_object_count

    - In group: camera

    """
    ...

def get_object_count(channel: int) -> int:
    """

    - Param: channel The channel to scan for objects.

    - Note: Objects are sorted by area, largest first.

    - Returns: Number of objects in the given channel, -1 if channel doesn't exist.

    - See: get_channel_count

    - In group: camera

    """
    ...

def get_object_data(channel: int, object: int) -> str:
    """

    - Returns: The string data associated with a given object on a given channel.

    If there is no data associated, 0 is returned.

    - Note: This data is not guaranteed to be null terminated.

    - Note: This string pointer will be invalid after a call to camera_update()

    - See: get_object_data_length

    - In group: camera

    """
    ...

def get_code_num(channel: int, object: int) -> int:
    """

    - Returns: The data associated with the given channel and object as an integer. If the given channel or object doesn't exist, -1 is returned.

    - See: get_object_data

    """
    ...

def get_object_data_length(channel: int, object: int) -> int:
    """

    - Returns: The length of the string data associated with a given object on a given channel.

    If there is no data associated, 0 is returned. If the channel or object is invalid, 0 is returned.

    - See: get_object_data

    - In group: camera

    """
    ...

def get_object_confidence(channel: int, object: int) -> int:
    """

    - Returns: The confidence, between 0.0 and 1.0, that given object on the given channel is significant.

    If the channel or object doesn't exist, 0.0 is returned.

    - In group: camera

    """
    ...

def get_object_area(channel: int, object: int) -> int:
    """

    - Returns: The object's bounding box area. -1 is returned if the channel or object doesn't exist.

    - In group: camera

    """
    ...

def get_object_bbox(channel: int, object: int) -> Any:
    """

    - Returns: The bounding box of the given object on the given channel.

    - In group: camera

    """
    ...

def get_object_bbox_ulx(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def get_object_bbox_uly(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def get_object_bbox_brx(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def get_object_bbox_bry(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def get_object_bbox_width(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def get_object_bbox_height(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def get_object_centroid(channel: int, object: int) -> Any:
    """

    - Returns: The (x, y) centroid of the given object on the given channel.

    - In group: camera

    """
    ...

def get_object_centroid_column(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def get_object_centroid_x(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def get_object_centroid_row(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def get_object_centroid_y(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def get_object_center(channel: int, object: int) -> Any:
    """

    - Returns: The (x, y) center of the given object on the given channel.

    - In group: camera

    """
    ...

def get_object_center_column(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def get_object_center_x(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def get_object_center_row(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def get_object_center_y(channel: int, object: int) -> int:
    """
    (undocumented)
    """
    ...

def camera_close():
    """

    Cleanup the current camera instance.

    - See: camera_open

    - See: camera_open_at_res

    - See: camera_open_device

    - In group: camera

    """
    ...

def set_camera_config_base_path(path: str):
    """

    Sets the path in which to look for camera configurations.

    - Param: path the absolute directory path in which to look for camera configurations.

    - In group: camera

    """
    ...

def get_camera_frame_row(row: int) -> str:
    """

    Retrieves the current camera frame row as a BGR (BGR888) array. The returned

    pointer is invalid after camera_update() is called again.
    *

    - Returns: the current BGR888 camera frame row.

    - In group: camera

    """
    ...

def get_camera_frame() -> str:
    """

    Retrieves the current camera frame as a BGR (BGR888) array. The returned

    pointer is invalid after camera_update() is called again.
    *

    - Returns: the current BGR888 camera frame.

    - In group: camera

    """
    ...

def get_camera_element_size() -> int:
    """
    (undocumented)
    """
    ...
def calibrate_compass():
    """

    - File: compass.h

    - Author: Joshua southerland

    - Copyright: KISS Institute for Practical Robotics

    - Defgroup: compass Com...


    Begin calibrating the compass.
    *

    Will display the calibration parameter results which

    can be used in the future with set_compass_params
    *

    Provided by Dr. Andrew H. Fagg and Twister Robotics

    - In group: com...

    """
    ...

def set_compass_params(meanX: float, meanY: float, meanZ: float, W1: float, W2: float, div_E1: float, div_E2: float):
    """

    Set the compass parameters based on a previous calibration.
    *

    Provided by Dr. Andrew H. Fagg and Twister Robotics
    *

    - Param:[in] meanX a value provided by calibrate_com...

    - Param:[in] meanY a value provided by calibrate_com...

    - Param:[in] meanZ a value provided by calibrate_com...

    - Param:[in] W1 a value provided by calibrate_com...

    - Param:[in] W2 a value provided by calibrate_com...

    - Param:[in] div_E1 a value provided by calibrate_com...

    - Param:[in] div_E2 a value provided by calibrate_com...

    - In group: com...

    """
    ...

def get_compass_angle() -> float:
    """

    Get the current compass heading.
    *

    Provided by Dr. Andrew H. Fagg and Twister Robotics

    - Returns: the compass angle in radians

    - In group: com...

    """
    ...
def console_clear():
    """************************************************************************

     Copyright 2012 KISS Institute for Practical Robotics                  *

                                                                           *

     This file is part of libkovan.                                        *

                                                                           *

     libkovan is free software: you can redistribute it and/or modify      *

     it under the terms of the GNU General Public License as published by  *

     the Free Software Foundation, either version 2 of the License, or     *

     (at your option) any later version.                                   *

                                                                           *

     libkovan is distributed in the hope that it will be useful,           *

     but WITHOUT ANY WARRANTY; without even the implied warranty of        *

     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *

     GNU General Public License for more details.                          *

                                                                           *

     You should have received a copy of the GNU General Public License     *

     along with libkovan. Check the LICENSE file in the project root.      *

     If not, see <http://www.gnu.org/licenses/>.                           *
    *************************************************************************

    - File: console.h

    - Brief: Methods for working with the console screen

    - Author: Braden McDorman

    - Copyright: KISS Insitute for Practical Robotics

    - Defgroup: console Console


    Clears the UI's console.

    - In group: console

    """
    ...
def create_connect() -> int:
    """

    - File: create.h

    - Author: Braden McDorman

    - Copyright: KISS Institute for Practical Robotics

    - Defgroup: create iRobot (R) Create (TM)


    Waits to establish a connection to the create.

    \blocksuntil A connection to a create is established

    - Returns: 0 on success

    - See: create_disconnect

    - In group: create

    """
    ...

def create_connect_once() -> int:
    """

    Attempts to establish a connection to the create.

    - Returns: 1 if connection succeeded, 0 if connection failed

    - See: create_disconnect

    - In group: create

    """
    ...

def create_disconnect():
    """

    Cleans up connection to the create.

    - See: create_connect

    - In group: create

    """
    ...

def create_start():
    """

    - In group: create

    """
    ...

def create_passive():
    """

    - In group: create

    """
    ...

def create_safe():
    """

    - In group: create

    """
    ...

def create_full():
    """

    - In group: create

    """
    ...

def create_spot():
    """

    - In group: create

    """
    ...

def create_cover():
    """

    - In group: create

    """
    ...

def create_demo(d: int):
    """

    - In group: create

    """
    ...

def create_cover_dock():
    """

    - In group: create

    """
    ...

def get_create_mode() -> int:
    """

    - In group: create

    """
    ...

def get_create_lbump() -> int:
    """

    - In group: create

    """
    ...

def get_create_rbump() -> int:
    """

    - In group: create

    """
    ...

def get_create_lwdrop() -> int:
    """

    - In group: create

    """
    ...

def get_create_cwdrop() -> int:
    """

    - In group: create

    """
    ...

def get_create_rwdrop() -> int:
    """

    - In group: create

    """
    ...

def get_create_wall() -> int:
    """

    - In group: create

    """
    ...

def get_create_lcliff() -> int:
    """

    - In group: create

    """
    ...

def get_create_lfcliff() -> int:
    """

    - In group: create

    """
    ...

def get_create_rfcliff() -> int:
    """

    - In group: create

    """
    ...

def get_create_rcliff() -> int:
    """

    - In group: create

    """
    ...

def get_create_llightbump() -> int:
    """

    - In group: create

    """
    ...

def get_create_lflightbump() -> int:
    """

    - In group: create

    """
    ...

def get_create_lclightbump() -> int:
    """

    - In group: create

    """
    ...

def get_create_rclightbump() -> int:
    """

    - In group: create

    """
    ...

def get_create_rflightbump() -> int:
    """

    - In group: create

    """
    ...

def get_create_rlightbump() -> int:
    """

    - In group: create

    """
    ...

def get_create_llightbump_amt() -> int:
    """

    - In group: create

    """
    ...

def get_create_rlightbump_amt() -> int:
    """

    - In group: create

    """
    ...

def get_create_lflightbump_amt() -> int:
    """

    - In group: create

    """
    ...

def get_create_lclightbump_amt() -> int:
    """

    - In group: create

    """
    ...

def get_create_rclightbump_amt() -> int:
    """

    - In group: create

    """
    ...

def get_create_rflightbump_amt() -> int:
    """

    - In group: create

    """
    ...

def get_create_vwall() -> int:
    """

    - In group: create

    """
    ...

def get_create_overcurrents() -> int:
    """

    - In group: create

    """
    ...

def get_create_infrared() -> int:
    """

    - In group: create

    """
    ...

def get_create_advance_button() -> int:
    """

    - In group: create

    """
    ...

def get_create_play_button() -> int:
    """

    - In group: create

    """
    ...

def get_create_normalized_angle() -> int:
    """

    - In group: create

    """
    ...

def set_create_normalized_angle(angle: int):
    """

    - In group: create

    """
    ...

def get_create_total_angle() -> int:
    """

    - In group: create

    """
    ...

def set_create_total_angle(angle: int):
    """

    - In group: create

    """
    ...

def get_create_distance() -> int:
    """

    - In group: create

    """
    ...

def set_create_distance(dist: int):
    """

    - In group: create

    """
    ...

def get_create_battery_charging_state() -> int:
    """

    - In group: create

    """
    ...

def get_create_battery_voltage() -> int:
    """

    - In group: create

    """
    ...

def get_create_battery_current() -> int:
    """

    - In group: create

    """
    ...

def get_create_battery_temp() -> int:
    """

    - In group: create

    """
    ...

def get_create_battery_charge() -> int:
    """

    - In group: create

    """
    ...

def get_create_battery_capacity() -> int:
    """

    - In group: create

    """
    ...

def get_create_wall_amt() -> int:
    """

    - In group: create

    """
    ...

def get_create_lcliff_amt() -> int:
    """

    - In group: create

    """
    ...

def get_create_lfcliff_amt() -> int:
    """

    - In group: create

    """
    ...

def get_create_rfcliff_amt() -> int:
    """

    - In group: create

    """
    ...

def get_create_rcliff_amt() -> int:
    """

    - In group: create

    """
    ...

def get_create_bay_DI() -> int:
    """

    - In group: create

    """
    ...

def get_create_bay_AI() -> int:
    """

    - In group: create

    """
    ...

def get_create_song_number() -> int:
    """

    - In group: create

    """
    ...

def get_create_song_playing() -> int:
    """

    - In group: create

    """
    ...

def get_create_number_of_stream_packets() -> int:
    """

    - In group: create

    """
    ...

def get_create_requested_velocity() -> int:
    """

    - In group: create

    """
    ...

def get_create_requested_radius() -> int:
    """

    - In group: create

    """
    ...

def get_create_requested_right_velocity() -> int:
    """

    - In group: create

    """
    ...

def get_create_requested_left_velocity() -> int:
    """

    - In group: create

    """
    ...

def create_stop():
    """

    - In group: create

    """
    ...

def create_drive(speed: int, radius: int):
    """

    - In group: create

    """
    ...

def create_drive_straight(speed: int):
    """

    - In group: create

    """
    ...

def create_spin_CW(speed: int):
    """

    - In group: create

    """
    ...

def create_spin_CCW(speed: int):
    """

    - In group: create

    """
    ...

def create_drive_direct(l_speed: int, r_speed: int):
    """

    - In group: create

    """
    ...

def create_spin_block(speed: int, angle: int):
    """

    - In group: create

    """
    ...

def _create_get_raw_encoders(lenc: int, renc: int) -> int:
    """

    - In group: create

    """
    ...

def create_advance_led(on: int):
    """

    - In group: create

    """
    ...

def create_play_led(on: int):
    """

    - In group: create

    """
    ...

def create_power_led(color: int, brightness: int):
    """

    - In group: create

    """
    ...

def create_digital_output(bits: int):
    """

    - In group: create

    """
    ...

def create_pwm_low_side_drivers(pwm2: int, pwm1: int, pwm0: int):
    """

    - In group: create

    """
    ...

def create_low_side_drivers(pwm2: int, pwm1: int, pwm0: int):
    """

    - In group: create

    """
    ...

def create_load_song(num: int):
    """

    - In group: create

    """
    ...

def create_play_song(num: int):
    """

    - In group: create

    """
    ...

def create_read_block(data: str, count: int) -> int:
    """

    - In group: create

    """
    ...

def create_write_byte(byte: str):
    """

    - In group: create

    """
    ...

def create_clear_serial_buffer():
    """

    - In group: create

    """
    ...

def get_create_baud_rate() -> Any:
    """

    - In group: create

    """
    ...

def set_create_baud_rate(baudRate: Any):
    """

    - In group: create

    """
    ...
OI_START = 128

OI_BAUD = 129

OI_SAFE = 131

OI_FULL = 132

OI_DEMO = 136

OI_DRIVE = 137

OI_DRIVE_DIRECT = 145

OI_LEDS = 139

OI_DIGITAL_OUTPUTS = 147

OI_LOW_SIDE_DRIVERS = 138

OI_SEND_IR = 151

OI_SONG = 140

OI_PLAY_SONG = 141

OI_SENSORS = 142

OI_QUERY_LIST = 149

OI_STREAM = 148

OI_PAUSE_RESUME_STREAM = 150

OI_SCRIPT = 152

OI_PLAY_SCRIPT = 153

OI_SHOW_SCRIPT = 154

OI_WAIT_TIME = 155

OI_WAIT_DISTANCE = 156

OI_WAIT_ANGLE = 157

OI_WAIT_EVENT = 156

OI_BUMPS_AND_WHEEL_DROPS = 7

OI_WALL = 8

OI_CLIFF_LEFT = 9

OI_CLIFF_FRONT_LEFT = 10

OI_CLIFF_FRONT_RIGHT = 11

OI_CLIFF_RIGHT = 12

OI_VIRTUAL_WALL = 13

OI_LOW_SIDE_DRIVER_AND_WHEEL_OVERCURRENTS = 14

OI_BUTTONS = 18

OI_DISTANCE = 19

OI_ANGLE = 20

OI_CHARGING_STATE = 21

OI_VOLTAGE = 22

OI_CURRENT = 23

OI_CARGO_BAY_DIGITAL_INPUTS = 32
def debug_print_registers():
    """
    (undocumented)
    """
    ...

def register_value(addy: int) -> int:
    """
    (undocumented)
    """
    ...

def debug_dump_data(data: str, size: Any, where: str) -> int:
    """
    (undocumented)
    """
    ...
def digital(port: int) -> int:
    """

    - File: digital.h

    - Copyright: KISS Institute for Practical Robotics

    - Defgroup: digital Digitals


    - See: get_digital_value

    - In group: digital

    """
    ...

def set_digital_value(port: int, value: int):
    """

    Sets the value of the digital port in output mode.

    - See: get_digital_value

    - In group: digital

    """
    ...

def get_digital_value(port: int) -> int:
    """

    Gets the current value of the digital port.

    - Returns: 1 if the switch is closed, 0 if the switch is open

    - See: set_digital_value

    - In group: digital

    """
    ...

def set_digital_output(port: int, out: int):
    """

    Sets the digital mode.

    - Param:[in] port The port to modify.

    - Param:[in] out 1 for output mode, 0 for input mode.

    - In group: digital

    """
    ...

def get_digital_output(port: int) -> int:
    """

    Gets the current digital mode

    - Returns: 1 for output mode, 0 for input mode

    - See: set_digital_value

    - In group: digital

    """
    ...

def get_digital_pullup(port: int) -> int:
    """

    Gets the current digital pullup state

    - Returns: 1 for active, 0 for inactive

    - Deprecated: not applicable on the Wallaby

    - In group: digital

    """
    ...

def set_digital_pullup(port: int, pullup: int):
    """

    Sets the current digital pullup state

    - Param:[in] port The port to modify

    - Param:[in] pullup The pullup state 1: active  0: inactive

    - Deprecated: not applicable on the Wallaby

    - In group: digital

    """
    ...
def display_clear():
    """************************************************************************

     Copyright 2013 KISS Institute for Practical Robotics                  *

                                                                           *

     This file is part of libkovan.                                        *

                                                                           *

     libkovan is free software: you can redistribute it and/or modify      *

     it under the terms of the GNU General Public License as published by  *

     the Free Software Foundation, either version 2 of the License, or     *

     (at your option) any later version.                                   *

                                                                           *

     libkovan is distributed in the hope that it will be useful,           *

     but WITHOUT ANY WARRANTY; without even the implied warranty of        *

     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *

     GNU General Public License for more details.                          *

                                                                           *

     You should have received a copy of the GNU General Public License     *

     along with libkovan. Check the LICENSE file in the project root.      *

     If not, see <http://www.gnu.org/licenses/>.                           *
    *************************************************************************
    """
    ...

def display_printf(col: int, row: int, t: str):
    """
    (undocumented)
    """
    ...
def set_auto_publish(on: int):
    """************************************************************************

     Copyright 2012 KISS Institute for Practical Robotics                  *

                                                                           *

     This file is part of libkovan.                                        *

                                                                           *

     libkovan is free software: you can redistribute it and/or modify      *

     it under the terms of the GNU General Public License as published by  *

     the Free Software Foundation, either version 2 of the License, or     *

     (at your option) any later version.                                   *

                                                                           *

     libkovan is distributed in the hope that it will be useful,           *

     but WITHOUT ANY WARRANTY; without even the implied warranty of        *

     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *

     GNU General Public License for more details.                          *

                                                                           *

     You should have received a copy of the GNU General Public License     *

     along with libkovan. Check the LICENSE file in the project root.      *

     If not, see <http://www.gnu.org/licenses/>.                           *
    *************************************************************************

    - File: general.h

    - Author: Braden McDorman

    - Copyright: KISS Institute for Practical Robotics

    - Defgroup: general General


    - Brief: Sets whether or not hardware output command publishing happens automatically.

    \details publish() is, by default, called on your behalf by libkovan. When you turn automatic

    publishing off, libkovan expects you to publish() changes manually.

    - Param:[in] on 1 for automatic publishing, 0 for manual publishing

    - Note: Any command involving hardware modification, such as motors or servos,

    requires publish() to be called before changes will be written to the system.

    - In group: general

    - Deprecated: This has no effect when using the Wallaby

    """
    ...

def publish():
    """

    - Brief: Explictly publishes new data to the system

    \details All hardware output commands are stored locally before being written to the system.

    This allows for batch execution of commands with automatic publishing turned off.

    - In group: general

    - Deprecated: This has no effect when using the Wallaby

    """
    ...

def halt():
    """
    (undocumented)
    """
    ...

def freeze_halt():
    """
    (undocumented)
    """
    ...
def create_point2(x: int, y: int) -> Any:
    """
    (undocumented)
    """
    ...

def create_point3(x: int, y: int, z: int) -> Any:
    """
    (undocumented)
    """
    ...

def create_rectangle(ulx: int, uly: int, width: int, height: int) -> Any:
    """
    (undocumented)
    """
    ...
def graphics_open(width: int, height: int) -> int:
    """

    - File: graphics.h

    - Brief: Methods for displaying graphics to the screen.

    - Author: Braden McDorman

    - Copyright: KISS Insitute for Practical Robotics

    - Defgroup: graphics Graphics


    Opens a KISS Graphics Window for drawing and input functions.



    - Param: width The width of the graphics window

    - Param: height The height of the graphics window

    - In group: graphics

    """
    ...

def graphics_close():
    """

    Closes the previously opened KISS Graphics Window

    - In group: graphics

    """
    ...

def graphics_update():
    """

    Update must be called after drawing to the window for changes to be visible.

    This function also must be called regularly for input to work.

    - In group: graphics

    """
    ...

def graphics_clear():
    """

    Fills the entire window with the color black

    - In group: graphics

    """
    ...

def graphics_blit(data: str, x: int, y: int, width: int, height: int):
    """

    This function is equivalent to calling graphics_blit_enc() with an encoding of RGB

    - See: graphics_blit_enc

    """
    ...

def graphics_blit_region(data: str, sx: int, sy: int, ex: int, ey: int, width: int, height: int, dx: int, dy: int):
    """

    This function is equivalent to calling graphics_blit_region_enc() with an encoding of RGB

    - See: graphics_blit_region_enc

    """
    ...

def graphics_blit_enc(data: str, enc: Any, x: int, y: int, width: int, height: int):
    """

    Blits a pixel array onto the graphics context



    - Param: data the 1D array of pixel data to blit

    - Param: enc RGB for a Red-Green-Blue encoding or BGR for a Blue-Green-Red encoding

    - Param: x The destination x coordinate of the blit (target)

    - Param: y The destination y coordinate of the blit (target)

    - Param: width The width of the area to blit

    - Param: height The height of the area to blit

    - In group: graphics

    """
    ...

def graphics_blit_region_enc(data: str, enc: Any, sx: int, sy: int, ex: int, ey: int, width: int, height: int, dx: int, dy: int):
    """

    Blits a pixel array region onto the graphics context



    - Param: data the 1D array of pixel data to blit

    - Param: enc RGB for a Red-Green-Blue encoding or BGR for a Blue-Green-Red encoding

    - Param: sx The start x coordinate of the blit (source)

    - Param: sy The start y coordinate of the blit (source)

    - Param: ex The end x coordinate of the blit (source)

    - Param: ey The end y coordinate of the blit (source)

    - Param: width The width of the area to blit

    - Param: height The height of the area to blit

    - Param: dx The destination x coordinate of the blit (target)

    - Param: dy The destination y coordinate of the blit (target)

    - In group: graphics

    """
    ...

def graphics_fill(r: int, g: int, b: int):
    """

    Fill the graphics context with a color.

    - Param: r the red component of the drawing, from 0 to 255

    - Param: g the green component of the drawing, from 0 to 255

    - Param: b the blue component of the drawing, from 0 to 255

    - In group: graphics

    """
    ...

def graphics_pixel(x: int, y: int, r: int, g: int, b: int):
    """

    Draw a pixel at (x, y)

    - Param: r the red component of the drawing, from 0 to 255

    - Param: g the green component of the drawing, from 0 to 255

    - Param: b the blue component of the drawing, from 0 to 255

    - In group: graphics

    """
    ...

def graphics_line(x1: int, y1: int, x2: int, y2: int, r: int, g: int, b: int):
    """

    Draw a line from the point (x1, y1) to (x2, y2)

    - Param: r the red component of the drawing, from 0 to 255

    - Param: g the green component of the drawing, from 0 to 255

    - Param: b the blue component of the drawing, from 0 to 255

    - In group: graphics

    """
    ...

def graphics_circle(cx: int, cy: int, radius: int, r: int, g: int, b: int):
    """

    Draw an unfilled circle to the graphics window at the given coordinates and with the given radius.

    - Param: r the red component of the drawing, from 0 to 255

    - Param: g the green component of the drawing, from 0 to 255

    - Param: b the blue component of the drawing, from 0 to 255

    - In group: graphics

    """
    ...

def graphics_circle_fill(cx: int, cy: int, radius: int, r: int, g: int, b: int):
    """

    Draw a filled circle to the graphics window at the given coordinates and with the given radius.

    - Param: r the red component of the drawing, from 0 to 255

    - Param: g the green component of the drawing, from 0 to 255

    - Param: b the blue component of the drawing, from 0 to 255

    - In group: graphics

    """
    ...

def graphics_rectangle(x1: int, y1: int, x2: int, y2: int, r: int, g: int, b: int):
    """

    Draw an unfilled rectangle to the graphics window at the given coordinates.

    - Param: x1 the X coordinate of the rectangle's top-left corner

    - Param: y1 the Y coordinate of the rectangle's top-left corner

    - Param: x2 the X coordinate of the rectangle's bottom-right corner

    - Param: y2 the Y coordinate of the rectangle's bottom-right corner

    - Param: r the red component of the drawing, from 0 to 255

    - Param: g the green component of the drawing, from 0 to 255

    - Param: b the blue component of the drawing, from 0 to 255

    - In group: graphics

    """
    ...

def graphics_rectangle_fill(x1: int, y1: int, x2: int, y2: int, r: int, g: int, b: int):
    """

    Draw a filled rectangle to the graphics window at the given coordinates.

    - Param: x1 the X coordinate of the rectangle's top-left corner

    - Param: y1 the Y coordinate of the rectangle's top-left corner

    - Param: x2 the X coordinate of the rectangle's bottom-right corner

    - Param: y2 the Y coordinate of the rectangle's bottom-right corner

    - Param: r the red component of the drawing, from 0 to 255

    - Param: g the green component of the drawing, from 0 to 255

    - Param: b the blue component of the drawing, from 0 to 255

    - In group: graphics

    """
    ...

def graphics_triangle(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, r: int, g: int, b: int):
    """

    Draw an unfilled triangle to the graphics window at the given coordinates.

    - Param: r the red component of the drawing, from 0 to 255

    - Param: g the green component of the drawing, from 0 to 255

    - Param: b the blue component of the drawing, from 0 to 255

    - In group: graphics

    """
    ...

def graphics_triangle_fill(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, r: int, g: int, b: int):
    """

    Draw a filled triangle to the graphics window at the given coordinates.

    - Param: r the red component of the drawing, from 0 to 255

    - Param: g the green component of the drawing, from 0 to 255

    - Param: b the blue component of the drawing, from 0 to 255

    - In group: graphics

    """
    ...

def get_key_state(key: Any) -> int:
    """

    Gets the current state of a keyboard key.



    - Note: A KISS Graphics Window must be open for input functions to work.

    - Param: key An ASCII key code or a Key value from the KeyCode enum.

    - Returns: 1 for pressed, 0 for not pressed

    - In group: graphics

    """
    ...

def get_mouse_position(x: int, y: int):
    """

    Returns the mouse's current position relative to the top left corner of the graphics window.

    - In group: graphics

    """
    ...

def get_mouse_middle_button() -> int:
    """

    Returns the state of the mouse's middle button.

    - Returns: 1 for pressed, 0 for not pressed

    - In group: graphics

    """
    ...

def get_mouse_left_button() -> int:
    """

    Returns the state of the mouse's left button.

    - Returns: 1 for pressed, 0 for not pressed

    - In group: graphics

    """
    ...

def get_mouse_right_button() -> int:
    """

    Returns the state of the mouse's right button.

    - Returns: 1 for pressed, 0 for not pressed

    - In group: graphics

    """
    ...
NUMSEG = 30

SEGL = 5

SEGSP = 7

BOLD = 1

NOBOLD = 0

GXWINDOW = 700

GYWINDOW = 500

def graphics_segmentDisplay(s: int, x: int, y: int, r: int, g: int, b: int, size: float):
    """

    Draw a 16 segment character (alphameric - caps only)
    *

    - Param: s The segments to display

    - Param: x The X coordinate of the first segment's top-left corner

    - Param: y The Y coordinate of the first segment's top-left corner

    - Param: r The red component of the drawing, from 0 to 255

    - Param: g The green component of the drawing, from 0 to 255

    - Param: b The blue component of the drawing, from 0 to 255

    - Param: size The segment's size

    - In group: graphics

    """
    ...

def g_segmentDisplay(s: int, x: int, y: int, r: int, g: int, b: int, size: float):
    """
    (undocumented)
    """
    ...

def graphics_printCharacter(n: int, x: int, y: int, r: int, g: int, b: int, size: float):
    """

    Prints out a character in 16 segment characters
    *

    - Param: n The character to display

    - Param: x The X coordinate of the character's top-left corner

    - Param: y The Y coordinate of the character's top-left corner

    - Param: r The red component of the drawing, from 0 to 255

    - Param: g The green component of the drawing, from 0 to 255

    - Param: b The blue component of the drawing, from 0 to 255

    - Param: size The character's size

    - In group: graphics

    """
    ...

def g_printCharacter(n: int, x: int, y: int, r: int, g: int, b: int, size: float):
    """
    (undocumented)
    """
    ...

def graphics_printString(s: str, x: int, y: int, r: int, g: int, b: int, size: float):
    """

    Prints out a text string in 16 segment characters
    *

    - Param: n The string to display

    - Param: x The X coordinate of the first character's top-left corner

    - Param: y The Y coordinate of the first character's top-left corner

    - Param: r The red component of the drawing, from 0 to 255

    - Param: g The green component of the drawing, from 0 to 255

    - Param: b The blue component of the drawing, from 0 to 255

    - Param: size The strings's size

    - In group: graphics

    """
    ...

def g_printString(s: str, x: int, y: int, r: int, g: int, b: int, size: float):
    """
    (undocumented)
    """
    ...

def graphics_printInt(n: int, minNumDigits: int, x: int, y: int, r: int, g: int, b: int, size: float) -> int:
    """

    Prints out an integer in 16 segment characters
    *

    - Param: n The integer to display

    - Param: minNumDigits minNumDigits is normally 0, but can be larger if leading 0's are desired

    - Param: x The X coordinate of the first character's top-left corner

    - Param: y The Y coordinate of the first character's top-left corner

    - Param: r The red component of the drawing, from 0 to 255

    - Param: g The green component of the drawing, from 0 to 255

    - Param: b The blue component of the drawing, from 0 to 255

    - Param: size The strings's size

    - In group: graphics

    """
    ...

def g_printInt(n: int, minNumDigits: int, x: int, y: int, r: int, g: int, b: int, size: float) -> int:
    """
    (undocumented)
    """
    ...

def graphics_printFloat(n: float, numDigits: int, x: int, y: int, r: int, g: int, b: int, size: float):
    """

    Prints out a float in 16 segment characters
    *

    - Param: n The float to display

    - Param: numDigits numDigits is the number of digits to right of decimal to be printed

    - Param: x The X coordinate of the first character's top-left corner

    - Param: y The Y coordinate of the first character's top-left corner

    - Param: r The red component of the drawing, from 0 to 255

    - Param: g The green component of the drawing, from 0 to 255

    - Param: b The blue component of the drawing, from 0 to 255

    - Param: size The strings's size

    - In group: graphics

    """
    ...

def g_printFloat(n: float, numDigits: int, x: int, y: int, r: int, g: int, b: int, size: float):
    """
    (undocumented)
    """
    ...

def gyro_x() -> int:
    """

    - File: gyro.h

    - Copyright: KISS Institute for Practical Robotics

    - Defgroup: gyro Gyrometer


    Gets the sensed x rotation

    - Returns: The latest signed x rotation value

    - In group: gyro

    """
    ...

def gyro_y() -> int:
    """

    Gets the sensed y rotation

    - Returns: The latest signed y rotation value

    - In group: gyro

    """
    ...

def gyro_z() -> int:
    """

    Gets the sensed z rotation

    - Returns: The latest signed z rotation value

    - In group: gyro

    """
    ...

def gyro_calibrate() -> int:
    """

    Initiates a calibration of the gyrometer

    - Note: Not Yet Implemented

    - Returns: 1: success 0: failure

    - In group: gyro

    """
    ...
def ir_read():
    """

    - Deprecated: non present on the Wallaby

    """
    ...

def ir_write():
    """

    Gets the sensed y rotation

    - Deprecated: non present on the Wallaby

    """
    ...
def magneto_x() -> int:
    """

    - File: magneto.h

    - Copyright: KISS Institute for Practical Robotics

    - Defgroup: magneto Magnetometer


    Gets the sensed x magneto value

    - Returns: The latest signed x magneto value

    - In group: magneto

    """
    ...

def magneto_y() -> int:
    """

    Gets the sensed x magneto value

    - Returns: The latest signed y magneto value

    - In group: magneto

    """
    ...

def magneto_z() -> int:
    """

    Gets the sensed x magneto value

    - Returns: The latest signed z magneto value

    - In group: magneto

    """
    ...

def magneto_calibrate() -> int:
    """

    Initiates a calibration of the magnetometer

    - Note: Not Yet Implemented

    - Returns: 1: success 0: failure

    - In group: magneto

    """
    ...
def get_motor_position_counter(motor: int) -> int:
    """

    - File: motors.h

    - Copyright: KISS Institute for Practical Robotics

    - Defgroup: motor Motors


    - Brief: Gets the current motor position

    - Param:[in] motor The motor port.

    - In group: motor

    - See: gmpc

    """
    ...

def gmpc(motor: int) -> int:
    """

    - Brief: Gets the current motor position

    - Param:[in] motor The motor port.

    - In group: motor

    - See: get_motor_position_counter

    """
    ...

def clear_motor_position_counter(motor: int):
    """

    - Brief: Clears the motor position counter

    - Param:[in] motor The motor port.

    - In group: motor

    - See: cmpc

    """
    ...

def cmpc(motor: int):
    """

    - Brief: Clears the motor position counter

    - Param:[in] motor The motor port.

    - In group: motor

    - See: clear_motor_position_counter

    """
    ...

def move_at_velocity(motor: int, velocity: int) -> int:
    """

    - Brief: Set a goal velocity in ticks per second.

    - Detailed: The range is -1500 to 1500, though motor position accuracy may be decreased outside of -1000 to 1000

    - Param:[in] motor The motor port.

    - Param:[in] velocity The goal velocity in -1500 to 1500 ticks / second

    - In group: motor

    - See: mav

    """
    ...

def mav(motor: int, velocity: int) -> int:
    """

    - Brief: Set a goal velocity in ticks per second

    - Param:[in] motor The motor port.

    - Param:[in] velocity The goal velocity in -1500 to 1500 ticks / second

    - In group: motor

    - See: move_at_velocity

    """
    ...

def move_to_position(motor: int, speed: int, goal_pos: int) -> int:
    """

    - Brief: Set a goal position (in ticks) for the motor to move to.

    - Detailed: There are approximately 1500 ticks per motor revolution.

    - Detailed: This function is more accurate if speeds between -1000 and 1000 are used.

    - Param:[in] motor The motor port.

    - Param:[in] speed The speed to move at, between -1500 and 1500 ticks / second

    - Param:[in] goal_pos The position to move to (in ticks)

    - In group: motor

    - See: mtp

    """
    ...

def mtp(motor: int, speed: int, goal_pos: int) -> int:
    """

    - Brief: Set a goal position (in ticks) for the motor to move to

    - Param:[in] motor The motor port.

    - Param:[in] speed The speed to move at, between -1500 and 1500 ticks / second

    - Param:[in] goal_pos The position to move to (in ticks)

    - In group: motor

    - See: move_to_position

    """
    ...

def move_relative_position(motor: int, speed: int, delta_pos: int) -> int:
    """

    - Brief: Set a goal position (in ticks) for the motor to move to, relative to the current position

    - Param:[in] motor The motor port.

    - Param:[in] speed The speed to move at, between -1500 and 1500 ticks / second

    - Param:[in] delta_pos The position to move to (in ticks) given the current position

    - In group: motor

    - See: mrp

    """
    ...

def mrp(motor: int, speed: int, delta_pos: int) -> int:
    """

    - Brief: Set a goal position (in ticks) for the motor to move to, relative to the current position

    - Param:[in] motor The motor port.

    - Param:[in] speed The speed to move at, between -1500 and 1500 ticks / second

    - Param:[in] delta_pos The position to move to (in ticks) given the current position

    - In group: motor

    - See: move_relative_position

    """
    ...

def set_pid_gains(motor: int, p: int, i: int, d: int, pd: int, id: int, dd: int):
    """

    - Brief: Set the motor PID gains, represented as fractions.

    - Param:[in] motor The motor port.

    - Param:[in] p The P (proportional) gain numerator

    - Param:[in] i The I (integral) gain numerator

    - Param:[in] d The D (derivative) gain numerator

    - Param:[in] pd The P (proportional) gain denominator

    - Param:[in] id The I (integral) gain denominator

    - Param:[in] dd The D (derivative) gain denominator

    - In group: motor

    """
    ...

def get_pid_gains(motor: int, p: int, i: int, d: int, pd: int, id: int, dd: int):
    """

    - Brief: Set the motor PID gains, represented as fractions.

    - Param:[out] motor The motor port.

    - Param:[out] p The P (proportional) gain numerator

    - Param:[out] i The I (integral) gain numerator

    - Param:[out] d The D (derivative) gain numerator

    - Param:[out] pd The P (proportional) gain denominator

    - Param:[out] id The I (integral) gain denominator

    - Param:[out] dd The D (derivative) gain denominator

    - In group: motor

    """
    ...

def freeze(motor: int) -> int:
    """

    - Brief: Active braking to stop a motor

    - Param:[in] motor The motor port.

    - In group: motor

    """
    ...

def get_motor_done(motor: int) -> int:
    """

    - Brief: Check if the motor has reached it's goal

    - Param:[in] motor The motor port.

    - In group: motor

    - Returns:s 1: at goal   0: not at goal

    """
    ...

def block_motor_done(motor: int):
    """

    - Brief: Wait until the motor is at it's goal

    - Param:[in] motor The motor port.

    - See: bmd

    - In group: motor

    """
    ...

def bmd(motor: int):
    """

    - Brief: Wait until the motor is at it's goal

    - Param:[in] motor The motor port.

    - See: block_motor_done

    - In group: motor

    """
    ...

def setpwm(motor: int, pwm: int) -> int:
    """

    - Brief: Set the motor pwm (percent power) command

    - Param:[in] motor The motor port.

    - Param:[in] pwm A new motor pwm command between 0 and 100

    - In group: motor

    """
    ...

def getpwm(motor: int) -> int:
    """

    - Brief: Get the current motor pwm command

    - Param:[in] motor The motor port.

    - In group: motor

    """
    ...

def fd(motor: int):
    """

    - Brief: Moves the given motor forward at full power

    - Param: motor the motor's port.

    - In group: motor

    """
    ...

def bk(motor: int):
    """

    - Brief: Moves the given motor backward at full power

    - Param: motor the motor's port.

    - In group: motor

    """
    ...

def motor(motor: int, percent: int):
    """

    - Brief: Moves a motor at a percent velocity.
    *

    - Param:[in] motor The motor port.

    - Param:[in] percent The percent of the motors velocity, between -100 and 100.
    *

    - In group: motor

    """
    ...

def motor_power(motor: int, percent: int):
    """

    - Brief: Moves a motor at a percent power.
    *

    - Param:[in] motor the motor port.

    - Param:[in] percent The power of the motor, between -100 and 100.
    *

    - In group: motor

    """
    ...

def off(motor: int):
    """

    - Brief: Turns the specified motor off.

    - Param: motor the motor's port.

    - In group: motor

    """
    ...

def alloff():
    """

    - Brief: Turns all motors off.

    - In group: motor

    - See: ao

    """
    ...

def ao():
    """

    - Brief: Turns all motors off.

    - In group: motor

    - See: alloff

    """
    ...
def get_robot_states_sequence_num() -> int:
    """
    (undocumented)
    """
    ...

def get_robot_update_count() -> int:
    """
    (undocumented)
    """
    ...

def get_robot_firmware_version() -> int:
    """
    (undocumented)
    """
    ...

def set_robot_update_delay(us_delay: int) -> int:
    """
    (undocumented)
    """
    ...

def get_robot_update_delay() -> int:
    """
    (undocumented)
    """
    ...

def set_low_volt_threshold(volts: float) -> int:
    """
    (undocumented)
    """
    ...

def get_low_volt_threshold() -> float:
    """
    (undocumented)
    """
    ...
def enable_servo(port: int):
    """

    - File: servo.h

    - Copyright: KISS Institute for Practical Robotics

    - Defgroup: servo Servos


    - Brief: Enable a specific servo

    - Param:[in] port The port, between 0 and 3, to enable

    - In group: servo

    """
    ...

def disable_servo(port: int):
    """

    - Brief: Disable a specific servo

    - Param:[in] port The port, between 0 and 3, to disable

    - In group: servo

    """
    ...

def enable_servos():
    """

    - Brief: Enable all four servo channels

    - In group: servo

    """
    ...

def disable_servos():
    """

    - Brief: Disable all four servo channels

    - In group: servo

    """
    ...

def set_servo_enabled(port: int, enabled: int):
    """

    - Brief: Enable or disable a specific servo

    - Param:[in] port The port, between 0 and 3, to enable

    - Param:[in] enabled The new enable setting 0: disabled 1: enabled

    - In group: servo

    """
    ...

def get_servo_enabled(port: int) -> int:
    """

    - Brief: Check if a servo is enabled

    - Param:[in] port The port, between 0 and 3

    - Returns: The servo enable setting 0: disabled 1: enabled

    - In group: servo

    """
    ...

def get_servo_position(port: int) -> int:
    """

    - Brief: Get the most recent commanded servo position

    - Param: servo The port of the servo

    - Returns: The servo's position as an 11 bit integer (which is an integer between 0 and 2047)

    - Note: This method will return the last _sent_ position, not the currently _set_ position.

    - In group: servo

    """
    ...

def set_servo_position(port: int, position: int):
    """

    - Brief: Set a new servo goal position

    - Param: servo The port of the servo

    - Param: position The new servo position, between 0 and 2047
    *

    - Note: Even though the servos have a _theoretical_ range between 0 and 2047,

    the _actual_ range is often less. Setting the servo to a position that it cannot physically

    reach will cause the servo to audibly strain and will consume battery very quickly.

    - In group: servo

    """
    ...
def mutex_create() -> Any:
    """

    - In group: thread

    """
    ...

def mutex_lock(m: Any):
    """

    - In group: thread

    """
    ...

def mutex_trylock(m: Any) -> int:
    """

    - In group: thread

    """
    ...

def mutex_unlock(m: Any):
    """

    - In group: thread

    """
    ...

def mutex_destroy(m: Any):
    """

    - In group: thread

    """
    ...

def thread_create(func: Any) -> Any:
    """

    - In group: thread

    """
    ...

def thread_start(id: Any):
    """

    - In group: thread

    """
    ...

def thread_wait(id: Any):
    """

    - In group: thread

    """
    ...

def thread_destroy(id: Any):
    """

    - In group: thread

    """
    ...
def msleep(msecs: int):
    """
    (undocumented)
    """
    ...

def systime() -> int:
    """
    (undocumented)
    """
    ...

def seconds() -> int:
    """
    (undocumented)
    """
    ...
def wait_for_milliseconds(msecs: int):
    """

    Waits (blocks) for the given number of milliseconds.

    - Param: msecs the number of milliseconds to sleep

    """
    ...

def wait_for_touch(port: int):
    """

    Waits (blocks) until the digital sensor on the given port has been activated.

    - Param: port The port to wait for activation on

    """
    ...

def wait_for_a_button():
    """

    Waits (blocks) until the a button has been pressed.

    """
    ...

def wait_for_b_button():
    """

    Waits (blocks) until the b button has been pressed.

    """
    ...

def wait_for_c_button():
    """

    Waits (blocks) until the c button has been pressed.

    """
    ...

def wait_for_x_button():
    """

    Waits (blocks) until the x button has been pressed.

    """
    ...

def wait_for_y_button():
    """

    Waits (blocks) until the y button has been pressed.

    """
    ...

def wait_for_z_button():
    """

    Waits (blocks) until the z button has been pressed.

    """
    ...

def wait_for_side_button():
    """

    Waits (blocks) until the side button has been pressed.

    """
    ...

def wait_for_any_button():
    """

    Waits (blocks) until any system button has been pressed.

    """
    ...

def wait_for_a_button_clicked():
    """

    Waits (blocks) until the a button has been pressed and then subsequently released.

    """
    ...

def wait_for_b_button_clicked():
    """

    Waits (blocks) until the b button has been pressed and then subsequently released.

    """
    ...

def wait_for_c_button_clicked():
    """

    Waits (blocks) until the c button has been pressed and then subsequently released.

    """
    ...

def wait_for_x_button_clicked():
    """

    Waits (blocks) until the x button has been pressed and then subsequently released.

    """
    ...

def wait_for_y_button_clicked():
    """

    Waits (blocks) until the y button has been pressed and then subsequently released.

    """
    ...

def wait_for_z_button_clicked():
    """

    Waits (blocks) until the z button has been pressed and then subsequently released.

    """
    ...

def wait_for_side_button_clicked():
    """

    Waits (blocks) until the side button has been pressed and then subsequently released.

    """
    ...
