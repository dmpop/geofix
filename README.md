#Geofix

[SL4A](https://code.google.com/p/android-scripting/) Python script to obtain and store geographical coordinates. The script acquires geographical coordinates using either the network or GPS. The obtained data is saved in a tab-separated text file and an SQLite database.

Geofix comes with a simple Python Bottle-based web app that can display entries from the SQLite database.

## Requirements

- SL4A
- Python for Android
- Python Bottle (required for Geofix Web)
- Git (optional)

## Installation

Copy the *geofix.py* script to the *sl4a/scripts* directory on the Android device.

## Geofix Web Installation

- Install the Python Package Manager (pip). On Debian and Ubuntu, this can be done by running the `apt-get install python-pip` command as root.
- Install pip. To do this on Debian and Ubuntu, run the `pip install bottle` as root.
- Clone the project's GitHub repository using the `git clone https://github.com/dmpop/geofix.git` command.
- Copy the *geofix.sqlite* database from the Android device to the *geofix-web* directory.
- Switch to the *geofix-web* directory and run `./geofix-web.py` to start the app. Point the browser to http://127.0.0.1.8080/geofix to access it.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
