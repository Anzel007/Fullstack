from Student import StudentDetail


#reading from a file
with open("student.txt","r") as file_object:
	file_contents= file_object.read()
	print(file_contents)
#writing to a file
with open("student.txt","w") as file_object:
	file_object.write("updated filee")
	#print(file_contents)
#appending
with open("student.txt","a") as file_object:
	file_object.write("\n this is the apended part")

	
