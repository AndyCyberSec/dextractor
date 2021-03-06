# dextractor
Android pentesting with ease.

## Description
The tools allows to connect through adb to an Android device. Once connected, use the **packages** command to list the installed apps, use **dump** command to save locally the app data files (/data/data/app_package) and dump all xml and sqlite3 content into txt files for further inspection.
It allows to connect quickly through jdb and test if anti-debug is in place.
It also checks for dangerous permissions in AndroidManifest.xml

```
andrea@MBP-di-Andrea dextractor % dextractor

64 65 78 74 72 61 63 74 6F 72
AndyCyberSec 2020 - www.andreabruschi.net
Type ? or help to list commands
dextractor % perm ./AndroidManifest.xml

[+] Requesting https://developer.android.com/reference/android/Manifest.permission...

[+] Found 4 dangerous permissions in AndroidManifest.xml

Dangerous:      android.permission.RECORD_AUDIO

Dangerous:      android.permission.CAMERA

Dangerous:      android.permission.WRITE_EXTERNAL_STORAGE

Dangerous:      android.permission.ACCESS_FINE_LOCATION
```

### Prerequisites
* dex2jar
* adb

## Installation

```
pip3 install -r requirements.txt 
```

### Note
The tool will use pure-python-adb but actually it doesn't support pull of directories. For this functionality the script now uses adb binary.

## Commands
```
Documented commands (type help <topic>):
========================================
connect  cwd  debug  devices  dextract  dump  exit  help  packages  perm
```

## Usage
You can create a symlink into your /usr/local/bin

```
ln -s /path/dextractor/main.py /usr/local/bin/dextractor
```

```
$ dextractor

64 65 78 74 72 61 63 74 6F 72
AndyCyberSec 2020 - www.andreabruschi.net
Type ? or help to list commands
dextractor % help

Documented commands (type help <topic>):
========================================
connect  cwd  debug  devices  dextract  dump  exit  help  packages  perm

dextractor % 
```

## Authors

* **Andrea Bruschi** - *Initial work* - [AndyCyberSec](https://github.com/AndyCyberSec)
