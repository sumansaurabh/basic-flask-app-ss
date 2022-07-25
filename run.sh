#!/bin/sh
i=5000
while [ $i -ne 5003 ]
do
        i=$(($i+1))
        # nohup python routes.py "$i" &
        nohup python tornado_server.py --port="$i" &

done