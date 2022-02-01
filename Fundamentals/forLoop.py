# exp = [1440,2500,3156,1295,4700]
# total = 0
# for item in exp:
#     total = total + item
#
# print("$"+str(total))

# range() function
# syntax range(start_index, end+1_index)
# for i in range(1, 11):
#     print(i)

# exp = [1440,2500,3156,1295,4700]
# total = 0
# for i in range(len(exp)):
#     print("Month:",(i+1),"Expense:",exp[i])
#     total += exp[i]
#
# print("Total expense: $" + str(total))

# searching
# key_location = "sofa"
# locations = ["living room", "chair", "garage", "sofa", "closet"]
# for i in locations:
#     if i==key_location:
#         print("Key found in",i)
#         break
#     else:
#         print("Key not found in",i)

for i in range(1,11,1):
    if i%2==0:
        continue
    print("Square of",i,"is",(i**2))

# while-statement
i = 1
while i<=5:
    print(i)
    i = i + 1
