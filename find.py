import glob
import os
from gluster import gfapi
import datetime


class CommandNotFound(Exception):
    pass

class InvalidCommand(Exception):
    pass


def find_file(path, name, ignore_case=False):
    for entry in volume.scandir(path):
        #dir_path = path+entry.name
        if entry.is_dir():
            find_file(entry.path, name, ignore_case)
        if ignore_case:
            if name.lower() == entry.name.lower():
                print entry.path
        else:
            if name == entry.name:
                print entry.path

def find_atime(days, path):
    for name in os.listdir(path):
        dir_path = path + name
        if os.path.isdir(dir_path):
            find_atime(days, dir_path+"/")
        else:
            curr_time  = datetime.date.today()
            print dir_path
            atime = os.path.getatime(dir_path)
            atime = datetime.datetime.fromtimestamp(atime).date()
            diff = curr_time - atime
            if days <= diff.days:
                print dir_path


def read(path):
    f = volume.fopen(path, 'r')
    find_dir(dir_path, name, ignore_case)
    file_contents = f.read()
    f.close()
    return file_contents

cmd = raw_input()
volume = gfapi.Volume('node5', 'voltest1')
volume.mount()
if cmd.split(" ")[0] == "find":
    if len(cmd.split(" ")) == 4:
        dir_path = cmd.split(" ")[1]
        if dir_path == ".":
            dir_path = volume.getcwd()
        if "-name" in cmd:
            file_name = cmd.split(" ")[3]
            ignore_case = False
            if "-iname" in cmd:
                ignore_case = True
            find_file(dir_path, file_name, ignore_case)
        elif "-atime" in cmd:
            days = cmd.split(" ")[3]
            find_atime(days, dir_path)
        else:
            raise InvalidCommand
    else:
        raise InvalidCommand
else:
    raise CommandNotFound

