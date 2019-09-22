import csv
import re

# FILENAME=input("Enter a CSV filename to check the format")

rows=[]
b=set()
unique=[]
error_mails=list()
dup_email=[]
row3=[]
TOTAL_LINE=0

# line_no=0
## READ FILE
def read_file(filename):
	#####  ==> to prevent appending when refresh
	global TOTAL_LINE
	dup_email.clear()   
	error_mails.clear()
	rows.clear()
	unique.clear()
	b.clear()
	#####  ==> to prevent appending when refresh  ====> finish 
	with open(filename, 'r') as csvfile: 
		csvreader = csv.reader(csvfile) 
		for row in csvreader: 
			rows.append(row)
		TOTAL_LINE=csvreader.line_num 
		# print(TOTAL_LINE)
		print("Total no. of rows: %d"%(csvreader.line_num))
		# print(rows)

## CHECK UNIQUE
def find_unique(check_field):
	if check_field not in b:
		unique.append(check_field)
		b.add(check_field)
		return 1
	else:
		return 0


## CHECK FORMAT
def check_format():
	for row in rows:
		field=str(row)
		field=field[1:-1]
		x=re.search("\w+@\w+.\w+",field)
		if(x.string[1:-1]==x.group()):
			valid=x.group()
			# print()
			is_unique=find_unique(valid)
			if is_unique==0:
				# print(valid, "   >>>  remove this duplicate email")
				dup_email.append(field)
				# print(rows.index(valid))
				# print(rows.index(valid)
		else:
			# print(field,"    >>>>    this email has an error")
			error_mails.append(field)
			# return 0

def printall():
	for row1 in rows:
		row2=str(row1)
		row2=row2[2:-2]
		# print(row2)
		row3.append(row2)
		# print(rows.index(row1[2:-2]))
		# if row2 in dup_email:
			# print(row2)
		# else:
		# 	print("a")
	print("==== LIST OF DUPLICATE EMAILS ====")
	for x in dup_email:
		if x[1:-1] in row3:
			set1=set()
			# print(set1)
			if x[1:-1] not in set1:
				set1.add(x[1:-1])
				line_no=row3.index(x[1:-1])
				print(x)
	print("==== LIST OF INVALID EMAILS WITH INDEX ====")
	for x in error_mails:
		if x[1:-1] in row3:
			line_no=row3.index(x[1:-1])
			print(line_no+1,'	',x)

def exec_csv(FILENAME):
	read_file(FILENAME) #2sldkfj@dlkjs.com
	check_format()
	# printall()	
	# return dup_email,error_mails
	# print()
	# print("List of Duplicate Emails")
	# print(dup_email)
	# print()
	# print("List of Emails which contains error")
	# print(error_mails)
	# print()
	# print(TOTAL_LINE)
# exec_csv('CRM_test.csv')

# print(TOTAL_LINE)