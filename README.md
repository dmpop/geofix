#Geofix for Android

[SL4A](https://code.google.com/p/android-scripting/) and [QPython](http://qpython.com/) Python script that obtains and stores geographical coordinates as well as provides the option to take an accompanying photo. The script acquires geographical coordinates using either the network or GPS. The obtained data is saved in a tab-separated text file and an SQLite database.

![](geofix-web/geofix-web.png)

Geofix comes with a simple Python Bottle-based web app that displays the geographical data from the SQLite database.

## Requirements

- SL4A and Python for Android for Android 4.x.x (or QPython for devices running Android 5.0 or higher)
- Python Bottle (required for Geofix Web)
- Git (optional)

## Compatibility

Geofix requires SL4A and Python for Android. However, SL4A doesn't work with Android 5.0 and higher. It's possible to run both packages by installing unofficial Android 5.0-compatible build of [SL4A](https://github.com/kuri65536/sl4a) and [Python for Android](https://github.com/kuri65536/python-for-android). Another solution is to install [QPython](http://qpython.com/) and use the *geofix-qpython.py* script.

## Installation

Copy the *geofix.py* script to the *sl4a/scripts* directory on the Android device. In case you use QPython, copy the *geofix-qpython.py* script to the *com.hipipal.qpyplus/scripts* directory.

## Usage

Open the SL4A (or QPython) app, and run the *geofix.py* script. For faster access, add the script to the homescreen. By default, all data is saved in the *Geofix* directory on the internal storage. You can change the destination directory by modifying the default *geofix_dir* path in the script.

## Geofix Web Installation

- Install the Python Package Manager (pip). On Debian and Ubuntu, this can be done by running the `apt-get install python-pip` command as root.
- Install pip. To do this on Debian and Ubuntu, run the `pip install bottle` as root.
- Clone the project's GitHub repository using the `git clone https://github.com/dmpop/geofix.git` command. Alternatively, grab the latest source code from the project's GitHub repository and unpack the downloaded ZIP archive.
- Copy the *Geofix* directory containing the *geofix.sqlite* database and snapshots from the Android device to the *geofix-web/static* directory.
- Switch to the *geofix-web* directory and run `./main.py` to start the app. Point the browser to http://127.0.0.1:8381/geofix to access it.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
