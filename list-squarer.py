# Define a function named 'square' that takes a list as an argument
def square(list):
    # Create an empty list to store the squared values
    listsquared = []

    # Loop through each element in the input list using its index
    for i in range(len(list)):
        # Append the square of the current element to the 'listasquared' list
        listsquared.append(list[i]**2)
    
    # Return the list of squared values
    return listsquared
