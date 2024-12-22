#Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern:"))
#Use a while loop to iterate through each row
row = 0
while row < size:
    #use a for loop to print asterisks in the row
    for _ in range(size):
        print("*" * size) # Print asterisks side by side without a new line
        print()  # Move to the next line after printing a row
        row +=1 # Increment the row counter