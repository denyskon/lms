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
