cp ~/Documents/password.txt ~/Documents/backups/password_backup.txt
sort -k1 -n ~/Documents/password.txt > ~/Documents/password.temp
mv ~/Documents/password.temp ~/Documents/password.txt
chmod 600 ~/Documents/password.txt
chmod 600 ~/Documents/backups/password_backup.txt
echo "password file was edited on $(date) by $USER $(uname -ns) " >> /var/log/password.log
