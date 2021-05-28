#APP NAME: Darklane Password Locker v1.0
#Script Coded by : Ayan Upadhaya
#contact: ayanu881@gamil.com

import sqlite3
from hashlib import sha256

ADMIN_PASS='123456'
DATABASE='passwd.db'

conn=sqlite3.connect(DATABASE)

def store_password(service_name_s,service_user_name,service_password,mail):
	params=(service_name_s,service_user_name,service_password,mail)
	conn.execute("INSERT INTO PASSWORDS VALUES(?,?,?,?);",params)
	conn.commit()

def show_passwords():
	c=conn.cursor()
	cursor=c.execute("SELECT *FROM PASSWORDS;")
	print('site name |'+'user name |'+'password |'+'email')
	print('-----------------------------------------------')
	entry_number=0
	for row in cursor:
		
		print(row[0]+   '\t|'+row[1]+   '\t|'+row[2]+  '\t|'+row[3]+'\n')
		entry_number+=1

	print(f"Total number of entries :{entry_number}")

print("Welcome to Darklane Password Manager")
print("****************************************")

print("Enter The Master Password")
access=input('>')

if access==ADMIN_PASS:
	try:
		conn.execute("""CREATE TABLE PASSWORDS(site_name TEXT NOT NULL,user_name TEXT NOT NULL,passwords TEXT NOT NULL,email TEXT NOT NULL);""")
		print("Your safe has been created!\nWhat would you like to store in it today?")
	except:
		print("What would you like to do today?")
	
	option=''
	while True:
		print()
		print("--------COMMANDS----------")
		print("Press i to store passowrd")
		print("Press c to create a password")
		print("Press s to show passwords")
		print("Press q to quit")
		option=input(">")
		if option == 'i':
			service_name_s=input("Enter the service name:")
			service_user_name=input("Enter the user name:")
			service_password=input("Enter your password:")
			service_mail=input("Enter your mail:")

			store_password(service_name_s,service_user_name,service_password,service_mail)
			print()
			print( "Your credentials has been safe successfully\n")

		elif option=='c':
			service_name=input("Enter the service name:")
			service_user_name=input("Enter the user name:")
			new_password=sha256(service_name.encode('utf-8')+service_user_name.encode('utf-8')).hexdigest()[:18]
			print(f"Your New Password For {service_name} = {new_password}")

			user_choice=input("Do you want to store this password?(y/n)")
			if user_choice.lower()=='y':
				store_password(service_name,service_user_name,new_password)
			else:
				continue

		elif option=='s':
			show_passwords()
		elif option=='q':
			break
		else:
			print("Wrong input")
			continue

else:
	print("Wrong Password Entered")
