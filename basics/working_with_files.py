import os
# you will not see demo.txt , as it is getting deleted at very end of the script
# r = read , w = write , a = append , x = create
# open file in write mode
file = open("demo.txt", "w")
for range_item in list(range(0,7)):
    print("input something to write in file : ")
    value_to_write = input()
    file.write(value_to_write+"\n")
file.close()

# open file in read mode , we can pass r as second argument which is a default mode here.
file = open("demo.txt")
# read whole file in a shot
print(file.read())
file.close()

# read few character
file = open("demo.txt")
print("Reading first 10 characters : ")
print(file.read(10))
file.close()

# read line by line
file = open("demo.txt")
print("Reading first two lines: ")
print(file.readline())
print(file.readline())
file.close()

# read entire file line by line
file = open("demo.txt")
print("Reading all lines: ")

for line in file:
    print(line)

file.close()

# recommended approach using with where resource management handle by python
print(" file content using with construct")
with open("demo.txt", "r") as file:
    for line in file:
        print(line)

# delete the file, for this we have to import os module in top of the file
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
