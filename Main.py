#Main Module

import Student as s
import Admin as a
import sqlite3
 
conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
 
cursor = conn.cursor()

def main():
	print()
	print("=======================================================================")
	
	print('WELLCOME TO BLOOMINGTON LIBRARY')
	print('========================================')
	print('')
	print('1 - LOGIN')
	print('2 - REGISTER')
	print('3 - ADMIN')
	print('0 - EXIT')
	print()
	
	opt = input("Please enter your option : ")
	
	
	#login
	if opt == '1':
		name = ""
		num = input("Please Enter your Student Number : ")
		if a.Login(num)==True:			
			cursor.execute("SELECT name FROM record WHERE s_nuber = ?",(num,))
			data = cursor.fetchall()
			for row in data:
				name = row[0]
			s.SMenu(name)
		else:
			print()
			print('PLEASE REGISTER FIRST!!!')
			print()
			main()
		
		
	 #regigister	
	elif opt == '2':
		print()
		name = input("Please Enter Your Name : ")
		s_name = input("Please Enter Your Surname : ")
		num = input("Please Enter your Student number : ")
		a.AddUser(name,s_name,num)
		print('You can now Login')
		print()
		main()
	
	
	
		
	#admin		
	elif opt == '3':
		name = input("Please enter your Admin username : ")
		print()
		if name == 'Craig' or name == 'craig':
			a.AMenu()
		else:
			print('Please Login as a Student ')
			print()
			main()
	
	elif opt == '0': #exit
		Bye()
	else:
		main()
		
def Bye():
	print('--------------------------------------------')
	print("THANK YOU FOR VISITING US!!")
	print('--------------------------------------------')
		
main()
