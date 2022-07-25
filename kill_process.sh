#!/bin/bash
pgrep -af routes.py | while read -r pid cmd ; do
    kill -9 $pid
    echo "pid: $pid killed"
done