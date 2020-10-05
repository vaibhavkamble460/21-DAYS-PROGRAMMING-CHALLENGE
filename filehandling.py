#to open a file placed in same location as that of python file
f = open("datafile.txt", "r")
print(f.read())
f.close()
#to open a file placed in different directory
'''f = open("D:\\demofile.txt", "r")
print(f.read())
f.close()'''
#to read only specific part from the text file
f = open("datafile.txt", "r")
print(f.read(5))
#you can return one line by using the readline() method:
print(f.readline())
#By looping through the lines of the file, you can read the whole file, line by line:
f = open("datafile.txt", "r")
for x in f:
  print(x)

#To write to an existing file
f = open("datafile.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("datafile.txt", "r")
print(f.read())
#to overite the content we must open file in w mode
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
#
f = open("myfile.txt", "x")
#to delete a file
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  