import subprocess


def debug(pid):

    cmd = ['adb', "forward", "tcp:1234", "jdwp:{}".format(pid)]
    stream = subprocess.Popen(cmd)
    stream.wait()

    jdb = ["jdb", "-attach", "localhost:1234"]
    stream = subprocess.Popen(jdb)
    stream.wait()
