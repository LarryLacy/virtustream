#!/bin/bash

INP=$1
VAL=0
NUM=0
PREV1=0
PREV2=1

while [ $VAL -lt $INP ]; do
	echo $NUM
	NUM=$(($PREV1+$PREV2))
	PREV2=$PREV1
	PREV1=$NUM
	VAL=$(($VAL+1))
done

