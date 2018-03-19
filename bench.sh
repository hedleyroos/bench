#!/bin/sh

ulimit -n 10000
ab -c 5000 -n 20000 -s 90 -k http://localhost:81/
