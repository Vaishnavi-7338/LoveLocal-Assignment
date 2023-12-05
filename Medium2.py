# Define a function 'numofdig' that takes a list as input and returns a dictionary
def numofdig(lis):
    # Initialize an empty dictionary 'd' to store the count of each element in the list
    d = {}
    
    # Iterate through the elements of the list
    for i in lis:
        # Check if the element is already in the dictionary
        if i not in d:
            # If not, add it to the dictionary with a count of 1
            d[i] = 1
        else:
            # If already in the dictionary, increment its count
            d[i] = d[i] + 1
    
    # Return the dictionary with counts
    return d

# Initialize an empty list 'inputs' to store user inputs
inputs = []

# Prompt the user to enter the number of elements
print('Enter the number of elements:')
n = int(input())

# Prompt the user to enter the elements and add them to the 'inputs' list
print('Enter the elements:')
for i in range(n):
    k = int(input())
    inputs.append(k)

# Get the length of the 'inputs' list
n = len(inputs)

# Create an empty list 'lis' to store elements occurring more than n/3 times
lis = []

# Call the 'numofdig' function to get a dictionary of element counts
d = numofdig(inputs)

# Iterate through the elements in the dictionary
for i in d:
    # Check if the count of the element is greater than n/3
    if d[i] > n/3:
        # If true, add the element to the 'lis' list
        lis.append(i)

# Print the final list 'lis'
print(lis)
