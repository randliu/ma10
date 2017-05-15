#!/bin/sh
for i in `ps -el|grep runserver|awk '{ print $2}'` ; do kill -9 $i ;  done
