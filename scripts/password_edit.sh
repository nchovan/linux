#creats a backup initially
cp ~/Documents/password.txt ~/Documents/backups/password_backup.txt
#sorts the file alphabetically by the first column saves output in a temp file
sort -k1 -n ~/Documents/password.txt > ~/Documents/password.temp
#renames the temp file to be the new file
mv ~/Documents/password.temp ~/Documents/password.txt
#automatically change the permission of the files
chmod 600 ~/Documents/password.txt
chmod 600 ~/Documents/backups/password_backup.txt
#echo my password log the file was edited
echo "password file was edited on $(date) by $USER $(uname -ns) " >> /var/log/password.log
