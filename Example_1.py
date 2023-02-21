import os
# for read file we can use an open() function in this example we also use 'with' for create a file handle in our code it is 'f''
#actually we need to choose the mode our open() function it will be 'r'
# a file handle it is language definition of some object, it has a name 'f'


##with open('data.txt', 'r') as f:
    ##data = f.read()


#if we want to write some data in our file we must to use a write() function 
#actually we need to change the mode our open() function it will be 'w'


##with open('data.txt', 'w') as f:
    ##data = 'some data to be written to the file'
    ##f.write(data)

#for example we can to write the following code 

with open('data.txt_1','w') as f:
	data='hello world'
	f.write(data)
c=open('data.txt_1','r')
print(c.read())