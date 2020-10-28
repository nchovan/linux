#!/bin/bash
echo	
#obtain specified strings with sed and print specied columns with awk 
sed -n '2,14p' ~/Documents/bills.txt | awk -F- '{print $1,"\t\t"$4}'
echo
#print text with the current date
echo "outstanding bills as of $(date)"
#obtain specified strings with sed and sum second column with awk
grep -iw "not payed" ~/Documents/bills.txt | awk -F- '{sum+=$2;}END{print sum;}'
echo
sed -n '27,38p' ~/Documents/bills.txt | awk -F- '{print $1,"\t\t"$3}'
echo
#sends an echo with the current date, user, nodename and system to my bills log
echo "Bills payed script was run on $(date) by $USER $(uname -ns) " >> /var/log/bills.log 
