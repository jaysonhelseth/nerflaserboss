#!/bin/bash

while true
do
	aplay laser.wav
	irsend SEND_ONCE NERFBLUE KEY_2
	sleep 1
done
