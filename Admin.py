#Admin Module
import Student as s
import sqlite3
conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
 
cursor = conn.cursor()

def AMenu():
	print()
	print("=======================================================================")
	print('Hello Aministrator, Welcome to SE Library')
	print('1 - View Books by Catagory')
	print('2 - View Borrowed Books')
	print('3 - View Avialable Books')	
	print('4 - View All Books')
	print('5 - View Book Names')
	print('6 - View Book Catagories')
	print('7 - View Registered Students')
	print('8 - Add Book')
	print('9 - Add User')
	print('10 - Delete Book')
	print('11 - Delete User')
	print('Print any other key to exit ')
	print()
	
	opt = input("Enter your Option : ")
	
	BMenu(opt)
	
def BMenu(opt):
	if opt =='1':
		print()
		name = input("Please Enter Book Catagory : ")
		s.ViewByCat(cat)
		AMenu()
		
	elif opt =='2':
		ViewBorrowed()
		AMenu()
		
	elif opt =='3':
		ViewAvailable()
		AMenu()
		
	elif opt =='4':
		s.ViewAll()
		AMenu()
		
	elif opt =='5':
		s.ViewNames()
		AMenu()
		
	elif opt =='6':
		s.ViewCat()
		AMenu()
		
	elif opt =='7':
		ViewRegStudents()
		AMenu()
		
	elif opt =='8':
		print()
		name = input("Please Enter Book Name : ")
		author = input("Please Enter Author : ")
		catagory = input("Please Enter Catagory : ")
		AddBook(name, author, catagory)
		AMenu()
		
	elif opt =='9':
		print()
		name = input("Please Enter Your Name : ")
		s_name = input("Please Enter Your Surname : ")
		num = input("Please Enter your Student number : ")
		AddUser(name,s_name,num)
		AMenu()
		
	elif opt =='10':
		print()
		name = input("Please Enter Book Name : ")
		DeleteBook(name)
		AMenu()
		
	elif opt =='11':
		print()
		name = input("Please Enter Name of the User to delete : ")
		DeleteUser(name)
		AMenu()
	
	#m.main()
	
	


def ViewBorrowed():
	cursor.execute("SELECT * FROM books WHERE avilability = 'no'")
	print('BOOK NAME'+'\t'+'| AUTHOR'+'\t'+'| CATAGORY'+'\t'+'| LENDER')
	print('----------------------------------------------------------------------')
	data = cursor.fetchall()
	for row in data:
		print(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3])

def ViewAvailable():
	cursor.execute("SELECT * FROM books WHERE avilability = 'yes'")
	print(('BOOK NAME'+'\t'+'| AUTHOR'+'\t'+'| CATAGORY'))
	print('-----------------------------------------------------------------------')
	data = cursor.fetchall()
	for row in data:
		print(row[0]+'\t'+row[1]+'\t'+row[2])
		
		
def ViewRegStudents():
	cursor.execute("SELECT * FROM record")
	data = cursor.fetchall()
	print('NAME'+'\t'+'| Surname'+'\t'+'| Student Number')
	print('-----------------------------------------------------------------------')
	for row in data:
		print(row[0]+'\t'+row[1]+'\t'+row[2])
		
def AddUser(name,surname,s_number):
	cursor.execute("INSERT INTO record VALUES (?,?,?)",(name,surname,s_number))
	conn.commit()
	print("User "+name+" "+surname+" added Succesfuly")
		
		
		
def Login(s_number):
	cursor.execute("SELECT s_nuber FROM record WHERE s_nuber = ?", (s_number,))
	data = cursor.fetchall()
	if len(data)==0:
		return False
		print('not found')
	else:
		return True
		
def AddBook(name, author, catagory):
	cursor.execute("INSERT INTO books VALUES (?,?,?,?,?)",(name,author,catagory,'','yes'))
	conn.commit()
	print()
	print("Book ",name," added succesfuly" )
	
def DeleteBook(name):
	cursor.execute("DELETE FROM books WHERE name = ?",(name,))
	conn.commit()
	print()
	print("Book ",name," Deleted Succesfuly")
	
def DeleteUser(name):
	cursor.execute("DELETE FROM record WHERE name = ?",(name,))
	conn.commit()
	print()
	print("User ",name," Deleted Succesfuly")
