#!/bin/bash
echo
sed -n '2,14p' ~/Documents/bills.txt | awk -F- '{print $1,"\t\t"$4}'
echo
echo "outstanding bills as of $(date)"
grep -iw "not payed" ~/Documents/bills.txt | awk -F- '{sum+=$2;}END{print sum;}'
echo
sed -n '27,38p' ~/Documents/bills.txt | awk -F- '{print $1,"\t\t"$3}'
echo
echo "Bills payed script was run on $(date) by $USER $(uname -ns) " >> /var/log/bills.log 
