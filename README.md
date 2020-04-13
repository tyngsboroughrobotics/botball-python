# NEW LOCATION: See https://github.com/tyngsboroughrobotics/game2020/tree/master/botball

# Botball for Python

Botball for Python provides Python wrappers for several useful Botball components (including motors, servos, sensors and wheels), as well as access to the entire `libwallaby` C library so it can interoperate with existing projects. Botball for Python is designed for Python 3.6 and is fully typed and documented.

Botball for Python is really two things:

 - A set of wrappers for `libwallaby` functions useful in Botball competitions
 - An interface for describing how your robot should behave during a match

## Links

The source code is available at https://github.com/tyngsboroughrobotics/botball.

The documentation is available at https://tyngsboroughrobotics.github.io/botball.

## Installation and usage

Please read the [Setting up a project](#setting-up-a-project) section for details on how to install Botball for Python on your robot.

## Contributing

Botball for Python is provided by the Tyngsborough Robotics team for use by all Botball participants! If you find a bug or want to request new functionality, please [create an issue](https://github.com/tyngsboroughrobotics/botball/issues/new) or submit a pull request. We'll try our best to be responsive and provide updated documentation when things change.

Botball for Python is actively developed and maintained by:

 - Wilson Gramer ([GitHub](https://github.com/Wilsonator5000), [Twitter](https://twitter.com/wgramer03))

---

# Setting up a project
 
## Prerequisites
 
Make sure you have the following software on your computer:
 
### macOS

 - PyCharm CE 2019.2 or later (https://www.jetbrains.com/pycharm/)
 - Homebrew (https://brew.sh/)
 - Latest Git version (`brew install git`)
 - Python 3.7 or later (`brew install python`)
  
### Windows

 - PyCharm CE 2019.2 or later (https://www.jetbrains.com/pycharm/)
 - Latest Git version (https://git-scm.com/download/win)
 - Python 3.7 or later (https://www.python.org/downloads/windows/)

### Chrome OS/Linux

 - Unfortunately Chrome OS/Linux isn't supported at the moment, but feel free to make a pull request!

Some knowledge of Python is required; some knowledge of the terminal would be useful.

## Creating your project

Because Botball for Python's wrappers have already been written by us, all you need to do is create a Python project with the code you want to run during matches. We've provided a template project for you to get started, available [here](https://github.com/tyngsboroughrobotics/game2020/tree/template). Get in touch if you have any questions — happy hacking!
