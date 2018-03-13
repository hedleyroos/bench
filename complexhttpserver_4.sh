#!/bin/bash

trap 'kill $PID1 $PID2 $PID3 $PID4; exit' SIGINT
PID1=0
PID2=0
PID3=0
PID4=0
./ve/bin/python -m ComplexHTTPServer 9011 &
PID1=$!
./ve/bin/python -m ComplexHTTPServer 9012 &
PID2=$!
./ve/bin/python -m ComplexHTTPServer 9013 &
PID3=$!
./ve/bin/python -m ComplexHTTPServer 9014
