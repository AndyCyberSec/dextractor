#/usr/local/bin/python3

from cmd import Cmd
import dextractor
from ppadb.client import Client as AdbClient
import subprocess
import os
import dumper

 
class Dextractor(Cmd):
    prompt = 'dextractor % '
    intro = "\n64 65 78 74 72 61 63 74 6F 72"
    intro += "\nAndyCyberSec 2020 - www.andreabruschi.net"
    intro += "\nType ? or help to list commands"
    client = AdbClient(host="127.0.0.1", port=5037)
    device = None

    # DOs
    # arg is the APK
    def do_dextract(self, arg):
        dextractor.dextract(arg)
    
    # arg is always none
    def do_devices(self, arg=None):
        devices = self.client.devices()

        i = len(devices)
        print("[+] Found %s devices: \n" % (i))
        for device in devices:
            print('[*] %s' % device.serial)

    # arg is package and destination folder
    def do_dump(self, arg=None):

        try:
            package, dest = parse_arg(arg)
        except ValueError:
            package = None

        if package:
            if dest:
                if self.device:
                    try:
                        # Directory pull to be implemented in ppadb, using standalone binary
                        # output = self.device.pull("/data/data/%s %s" % (package, dest))
                        try:
                            cmd = ['adb', 'pull', "/data/data/%s" % package, dest]
                            adb = subprocess.Popen(cmd)
                            adb.wait()
                        except:
                            print("[-] Error while dumping app data.")

                        filelist = dumper.fast_scandir(dest)
                        dumper.dump(filelist,'xml',dest)
                        dumper.dump(filelist,'sqlite',dest)

                    except FileNotFoundError as e:
                        print(e)

                else:
                    print("[-] Connect to a device first.") 
            else:
                print("[-] Type the path where to save the data.")
        else:
            print("[-] Package name is needed.")     
        

    def do_connect(self, device=None):
        if device:
            self.device = self.client.device(device)
            print("[+] Connected to %s" % self.device.serial)
        else:
            n_devices = len(self.client.devices())
            if n_devices == 1:
                device = self.client.devices()
                self.device = self.client.device(device[0].serial)
                print("[+] Connected to %s" % self.device.serial) 

    def do_packages(self, filter=None):
        grep = ""
        if filter:
            grep = "|grep %s" % filter
        if self.device:
            output = self.device.shell("pm list packages %s" % grep)
            print(output)
        else:
            print("[-] Connect to a device first.")

    def do_exit(self, arg):
        print("See you soon!")
        return True



    # HELPs
    def help_dextract(self):
        print("Type: dextract file.apk")

    def help_devices(self):
        print("List all devices.")

    def help_dump(self):
        print("Dump app data.")
        print("Usage: dump package destination")
    
    def help_connect(self):
        print("Connect to an android device. If only one device is connected, just type connect.")
        print("Usage: connect <devices output>.")

    def help_packages(self):
        print("List all the installed apps.")
        print("Usage: packages <name filter>.")
    
    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')
 
    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print("Type ? or help to list commands.")
 


def parse_arg(arg):
    return tuple(arg.split())

def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders
    
 
if __name__ == '__main__':
    Dextractor().cmdloop()
