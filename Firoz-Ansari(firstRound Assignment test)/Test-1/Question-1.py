# Step 1: Create an empty list to store the numbers-------------------------
numbers = []

# Step 2: Read numbers from the user and add them to the list---------------
n = int(input("Enter the number of elements: "))
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

# Step 3: Using Bubble Sort for ascending order ----------------------------------
def ListAscending(numbers):
 for i in range(n - 1):      # Repeat for round--
    for j in range(0, n - i - 1):   # compare each round
        if numbers[j] > numbers[j + 1]:
            # Swap the elements if they are in the wrong order
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


# Step 4: Bubble Sort for descending order (reverse sorting logic)
def listDscending(numbers):
 for i in range(n - 1):
    for j in range(0, n - i - 1):
        if numbers[j] < numbers[j + 1]:
            # Swap the elements if they are in the wrong order
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


# function call-------
ListAscending(numbers) 
# Print the sorted lists-------------
print("Ascending Order:", numbers)


# function call-------
listDscending(numbers)
# Print the sorted lists---------
print("Descending Order:", numbers)  
