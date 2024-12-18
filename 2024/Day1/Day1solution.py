# Read the file and flatten the contents into a list
file_path = '2024/Day1/input.txt'
dist = 0

# Initialize lists to store the two sets of numbers
leftlist = []
rightlist = []

with open(file_path, 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split()) #split nums on whitespace and convert to integers
        #append nums to separate lists
        leftlist.append(num1)
        rightlist.append(num2)

#sort lists (ascending is default)
leftlist.sort()
rightlist.sort()


for item1, item2 in zip(leftlist, rightlist): #pair elements from separate lists into tuples
    sum = abs(item1-item2) #uses absolute difference
    dist += sum


print(dist)


