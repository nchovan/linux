#!/bin/bash
checkfile ()
{
if [[ $1 =~ [.txt]+$ ]] #if statement does file end with .txt
then		
	read -p ".txt file,  would you like to change the file type?" ftype #get user input
	if [ $ftype == "no" ] #if statement using user input
		then
		echo 'file not changed, thank you'	
	else
		read -p "please enter new file type format (ex .tx)t :" newtype
		newpath=$(echo $1 | sed "s/.txt$/$newtype/") #set variable newpath to output
		mv $1 $newpath 
		fi
elif
	read -p ".sh file,  would you like to change the file type?" ftype #get user input
	if [ $ftype == "no" ] #if statement using user input
		then
		echo 'file not changed, thank you'	
	elif
		read -p "please enter new file type format (ex .tx)t :" newtype
		newpath=$(echo $1 | sed "s/.sh$/$newtype/") #set variable newpath to output
		mv $1 $newpath 
		fi
else
	read -p "file is not .txt or .sh,  would you like to change the file type?" ftype #get user input
	if [ $ftype == "no" ] #if statement using user input
		then
		echo 'file not changed, thank you'	
	elif
		read -p "please enter new file type format (ex .tx)t :" newtype
		newpath=$(echo $1 | sed "s/.sh$/$newtype/") #set variable newpath to output
		mv $1 $newpath 
		fi
echo "script complete"
fi
}
