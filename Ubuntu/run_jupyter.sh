#!/bin/bash

args_run=$1
PID_num=$(pgrep -f jupyter-noteboo )
PID_print=$(ps -eaf|grep jupyter-note|grep -v grep|awk '{print $2, $5}')

if [ "$args_run" = "run" ]; then
        echo "running jupyter notebook"
        nohup jupyter notebook &
elif [ "$args_run" = "stop" ]; then
        if [ $(echo $PID_num | wc -l) -eq 1 ]; then
                kill -9 $PID_num
                exit
        else
                echo "Which note book you want to kill? (0: all, others from 1)"
                echo "$PID_print"
                read num
                if [ $num = 0 ]; then
                        echo "all notebooks shutdown"
                        kill -9 $PID_num
                        exit
                else
                        kill_PID=$(echo $PID_num | cut -d ' ' -f $num)
                        echo $kill_PID "killed"
                        kill -9 $kill_PID
                fi
        fi
else
        echo "insert argument"
fi