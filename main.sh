#!/bin/bash

#Function to login the user i.e; to check the password 
login() {
	#Checking whether the user is Registered or not
	#If registered ask for password or else Ask if the user want to register
         if grep -q "$1\	" users.tsv; then
                echo "Enter your password";
                 read password;
                 checkpassword "$1" "$password"

        else
		echo -e "Username doesnot exist\nDo you wish to Register as a new user?[y/n]"
		 read opinion;
        	if [ "$opinion" == y ]; then
			Register
		else
			exit;
		fi
        fi
}


#Function for hashing a given string

Hash_string() {
	echo -n "$1" | sha256sum | awk '{print $1}'

}

#Function to compare the entered password with password stored
checkpassword() {

	#Obtaining the hashvalue of the password set by user at registration
        org_pass=$(grep "$1" users.tsv | awk '{print $2}')

	#Comparing the stored hash value with the hash value of password entered
        if [ "$org_pass" == $(Hash_string "$2") ]; then
                echo "Login successful!";
        else
                echo -e "Password is incorrect!\nRetry";
                read password;
                checkpassword "$1" "$password"
        fi
}


#Function for login of second user
player-2_login() {
	#Checking that 1st username is not same as 2nd username
	if [ "$1" != "$username1" ]; then 
		
		login "$1"
	else 
		echo -e "Player-2 cannot be same as Player-1\nPlease try again"
		read username2again;
		player-2_login "$username2again"

	fi
}

#Function to register new users
Register() {
	
                echo "Please re-enter your Username";
                read username;
		if grep -q "$username\	" users.tsv; then
			echo "Username already exist"
			Register
		else	
               		echo "Enter your password";
                	read password;
                	echo -e "$username\t$(Hash_string "$password" )" >> users.tsv
        	fi

}

	
#Authentication for Player-1
echo "Player-1 : Enter your username"
read username1;
login "$username1";


#Authentication for player-2
echo "Player-2 : Enter your username"
read username2;
player-2_login "$username2"

python3 game.py "$username1" "$username2"
