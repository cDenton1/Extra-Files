#!/bin/bash

PASS="gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8"

for i in {0000..3333}
do
        echo $PASS $i
done | nc -w 10 localhost 30002

printf "end phase 1\n"

for i in {3334..6666}
do
        echo $PASS $i
done | nc -w 10 localhost 30002

printf "end phase 2\n"

for i in {6667..9999}
do
        echo $PASS $i
done | nc -w 10 localhost 30002

printf "end phase 3\n"
