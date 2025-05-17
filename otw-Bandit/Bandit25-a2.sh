!/bin/bash

for i in {0000..3333}
do
        echo gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 %i >> /tmp/dentontest/poss1.txt
done

for i in {3334..6666}
do
        echo gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 %i >> /tmp/dentontest/poss2.txt
done

for i in {6667..9999}
do
        echo gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 %i >> /tmp/dentontest/poss3.txt
done

cat poss1.txt | nc localhost 30002 | grep -v "Wrong" > res1.txt

then

cat poss2.txt | nc localhost 30002 | grep -v "Wrong" > res2.txt

then

cat poss3.txt | nc localhost 30002 | grep -v "Wrong" > res3.txt
