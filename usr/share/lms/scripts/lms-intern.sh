#!/bin/bash
echo $3 $4

case $1 in

  rename)
     echo "rename"
     echo "dir=$2"
     ;;
  move)
     echo "move"
     ;;
  *)
     echo "use rename or move"
     ;;
esac
if [ "$3" == "" ];then
    $3="%Y_%m_%d-%H_%M_%S"
fi
if [ "$3" == "-" ];then
    $3="%Y_%m_%d-%H_%M_%S"
fi

if [ $1 == "rename" ];then
    exiftool '-filename<FileModifyDate' -d $3%%-c.%%le -r $2
    echo "rename ready"
fi

if [ $1 == "move" ];then
    exiftool '-filename<FileModifyDate' -d $3%%-c.%%le -r $2
    exiftool '-Directory<FileModifyDate' -d $2/$4 -r $2
    echo "move ready"
fi
exit 0
#%Y_%m_%d-%H_%M_%S
#%Y/%Y_%m
