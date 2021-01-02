#LXDB MediaSorter - A program to sort media files.
#Copyright (C) 2019-2021 LXDB Team

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

#LXDB MediaSorter,  Copyright (C) 2019-2021  LXDB Team
#This program comes with ABSOLUTELY NO WARRANTY
#This is free software, and you are welcome to redistribute it
#under certain conditions.

import subprocess
import os


def Rename(filename, sourcepath, recursive):
    if recursive:
        r = '-r'
    else:
        r = ''
    rename = subprocess.run(['exiftool', '-filename<FileModifyDate', '-d', filename + '%%-c.%%e', r, sourcepath], check=True)
    return(rename)

def RMove(foldername, filename, sourcepath, recursive):
    if recursive:
        r = '-r'
    else:
        r = ''
    rename = subprocess.run(['exiftool', '-filename<FileModifyDate', '-d', filename + '%%-c.%%e', r, sourcepath], check=True)
    move = subprocess.run(['exiftool', '-Directory<FileModifyDate', '-d', sourcepath + '/' + foldername, r, sourcepath], check=True)
    return(rename, move)

def GetMetadata(filename):
    process = subprocess.run(['exiftool', filename], check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    output = process.stdout
    return(output)
