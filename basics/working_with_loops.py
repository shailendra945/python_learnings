holdings = ["axis bank", "icici bank", " bajaj finance", "adani power", "hpcl", "cummins", "jio finance",
            "reliance power", "tata power", "asian energy", "sulzon energy", "jws energy", "adani port"]
print(len(holdings))

for stock in holdings:
    print(stock)

# print the largest stock name & length
largest_stock_name_len = 0
largest_stock_name = ""
for stock in holdings:
    if len(stock) > largest_stock_name_len:
        largest_stock_name_len = len(stock)
        largest_stock_name = stock
    else:
        print("smaller name stock {}".format(stock)
              + " ," + "It has {} letters".format(len(stock)))

print("largest name stock {}".format(largest_stock_name)
      + " ," + "It has {} letters".format(largest_stock_name_len))


# return the even numbers from the given list
def find_even_number(list_obj):
    even_numbers = []
    for num in list_obj:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


print(find_even_number([2, 3, 5, 6, 1, 7, 8, 9, 10, 1]))

#print 1 to 10 using while loop
i = 0
while True:
    i = i + 1
    print(i)
    if i == 10:
        break

# taking user input and terminate when end is entered
while True:
    print("Say something : ")
    input_value = input()
    if input_value == "end":
        break
    else:
        print(input_value)

# skip first five number and print others
numbers = [10, 20,30,40,50,60,70,80,90,100]
count = 0
for num in numbers:
    if count < 5:
        count = count + 1
        continue
    else:
        print(num)

