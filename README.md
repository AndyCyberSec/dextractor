# dextractor
Android pentesting with ease.

### Prerequisites
* dex2jar
* adb

## Installation

```
pip3 install -r requirements.txt 
```

## Note
The tool will use pure-python-adb but actually it doesn't support pull of directories. For this functionality the script now uses adb binary.

## Commands
```
Documented commands (type help <topic>):
========================================
connect  devices  dextract  dump  exit  help  packages
```

## Description
The tools allows to connect through adb to an Android device. Once connected, use the **packages** command to list the installed apps, use **dump** command to save locally the app data files (/data/data/app_package) and dump all xml and sqlite3 content into txt files for further inspection.

## Authors

* **Andrea Bruschi** - *Initial work* - [AndyCyberSec](https://github.com/AndyCyberSec)
