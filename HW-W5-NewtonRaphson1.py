sum_number = 0
average_number = 0
minimum_numnber = 0
maximum_number = 0
list_number = []
for i in range(20):
    number = float(input("enter a number: "))
    list_number.append(number)

print("Array: ", list_number)

minimum_index = (list_number.index(min(list_number))) # findes minimum number index
maximum_index = (list_number.index(max(list_number))) # findes maximum number index

print("minimum: ", list_number[minimum_index])
print("maximum: ", list_number[maximum_index])

print("sum: ", sum(list_number)) # sum of all numbers
print("average: ", sum(list_number) / len(list_number)) # average number
