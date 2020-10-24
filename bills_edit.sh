#echo bills log with edit info 
echo "Bills file was edited on $(date) by $USER $(uname -ns) " >> /var/log/bills.log
#changes the last update: string in file
sed -i "s/lastupdate:.*/lastupdate:$(date)/" ~/Documents/bills.txt
#saves a backup of file
cp ~/Documents/bills.txt ~/Documents/backups/bills_backup.txt

