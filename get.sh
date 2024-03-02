#!/bin/sh
while :; do
  wget $IP:$PORT -O- > /dev/null 
  sleep $SLEEP
done
