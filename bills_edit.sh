 echo "Bills file was edited on $(date) by $USER $(uname -ns) " >> /var/log/bills.log
sed -i "s/lastupdate:.*/lastupdate:$(date)/" ~/Documents/bills.txt
cp ~/Documents/bills.txt ~/Documents/backups/bills_backup.txt

