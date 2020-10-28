#!/bin/bash
filetool ()
{
echo
clear
printf "
File path: $(stat --format %n $1)
File permissions: $(stat --format %a $1)
Last accessed on: $(stat --format %x $1)
Last modified on: $(stat --format %z $1)\n"
printf "
a. Change file name
b. Change file permissions
c. Copy file to new directory
d. Move file to new directory
e. Delete file
f. Exit script with no changes
________________________________\n\n"
read -p "What would you like to do? " choice
if [ $choice = "a" ]
then
        read -p "Please enter new file name (ex: textfile.txt): " newname
        read -p "please enter directory of file (ex: ~/home/nicholas/Documents/): " newdir
        cp $1 $newdir$newname
        echo "File name changed, Thank you."
elif [ $choice = "b" ]
then
        read -p "Please enter new permissions (ex: 644): " newperm
        chmod $newperm $1
        echo "File permissions changed to $newperm, Thank you."
elif [ $choice = "c" ]
then
        read -p "please enter name for the file in directory (ex: text.txt): " copyname
        read -p "Please enter new directory for file (/home/nicholas/Documents/): " copylocation
        cp $1 $copylocation$copyname
        echo "file was copied to $copyfile, Thank you." 
elif [ $choice = "d" ]
then
        read -p "please enter name for file in the new directory (ex: text.txt): " movename
        read -p "Please enter new directory for file (/home/nicholas/Documents/): " movelocation
        mv $1 $movelocation$movename
        echo "file was moved to $copyfile, Thank you."  
elif [ $choice = "e" ]
then
        rm $1
        echo "File deleted, Thank you."
else
echo "script has ended with no changes the the file"
fi
}
i
