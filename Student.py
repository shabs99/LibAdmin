#Students Module
import sqlite3
conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
 
cursor = conn.cursor()


def SMenu(sname):
	print()
	print("=======================================================================")
	print('Hello ',sname,', Welcome to SE Library')
	print('1 - View Books by Catagory')
	print('2 - Lend a Book')
	print('3 - Return a Book')	
	print('4 - View All Books')
	print('5 - View Book Names')
	print('6 - View Book Catagories')
	print('Print any other key to exit ')
	print()
	
	##ADD MENU
	opt = input("Enter your Option : ")
	
	BMenu(opt, sname)
	
def BMenu(opt,sname):
	if opt =='1':
		print()
		cat = input("Please Enter Book Catagory : ")
		ViewByCat(cat)
		print()
		SMenu(sname)
		
	elif opt =='2':
		print()
		bname = input("Please Enter Book Book Name : ")
		Lend(bname, sname)
		SMenu(sname)
		
	elif opt =='3':
		print()
		name = input("Please Enter Book Name : ")
		Return(name)
		SMenu(sname)
		
	elif opt =='4':
		ViewAll()
		SMenu(sname)
		
	elif opt =='5':
		ViewNames()
		SMenu(sname)
		
	elif opt =='6':
		ViewCat()
		SMenu(sname)
	#m.Main()


def Lend(name, person):
	if Find(name)==True:
		#cursor.execute("SELECT * INTO report FROM books WHERE b_name = ?",(name,)) 
		#conn.commit()
		cursor.execute("""UPDATE books SET avilability = 'no' WHERE b_name = ?""",(name,))
		conn.commit()
		cursor.execute("""UPDATE books SET b_code = ? WHERE b_name = ?""",(person,name,))
		conn.commit()
		print('You can collect your book from the shelf')
	else:
		print('Book not found')

def Find(name):
	cursor.execute("SELECT b_name FROM books WHERE b_name = ?", (name,))
	data = cursor.fetchall()
	if len(data)==0:
		return False
	else:
		return True
		
def Return(name):
	cursor.execute("""UPDATE books SET avilability = 'yes' WHERE b_name = ?""",(name,))
	conn.commit()
	cursor.execute("""UPDATE books SET b_code = '' WHERE b_name = ?""",(name,))
	conn.commit()
	print('Book succesfuly returned')


def ViewByCat(cat):
	cursor.execute("SELECT * FROM books WHERE catagory = ?", (cat,))
	print('BOOK NAME'+'\t'+'| AUTHOR'+'\t'+'| CATAGORY'+'\t'+'| AVAILABILITY')
	print('-----------------------------------------------------------------------------------')
	data = cursor.fetchall()
	for row in data:
		print(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[4])

def ViewAll():
	cursor.execute("SELECT * FROM books")
	lst = cursor.fetchall()
	print(('BOOK NAME'+'\t'+'| AUTHOR'+'\t'+'| CATAGORY'+'\t'+'| AVAILABILITY'))
	print('-----------------------------------------------------------------------------------')
	for row in lst:
		print(row[0]+'\t'+ row[1]+'\t'+ row[2]+'\t'+ row[4])
		
		
def ViewNames():
	cursor.execute("SELECT b_name FROM books")
	data = cursor.fetchall()
	for row in data:
		print(row[0])
	
def ViewCat():
	cursor.execute("SELECT catagory FROM books")
	data = cursor.fetchall()
	for row in data:
		print(row[0])		


	
