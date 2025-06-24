# Function to remove common letters and return the count of remaining letters
def remove_common_letters(name1, name2):
    # Convert both names to lowercase
    name1 = name1.lower()
    name2 = name2.lower()
    
    # Convert names to lists of characters
    name1_list = list(name1)
    name2_list = list(name2)
    
    # Cancel out common letters
    for letter in name1:
        if letter in name2_list:
            name1_list.remove(letter)
            name2_list.remove(letter)
    
    # Return the total count of remaining letters
    return len(name1_list) + len(name2_list)

# Function to determine the relationship based on the FLAMES game
def flames_game(name1, name2):
    # Count remaining letters after removing common ones
    remaining_count = remove_common_letters(name1, name2)
    
    # Define the FLAMES list
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    
    # Use the count to remove letters in a cyclic manner
    while len(flames) > 1:
        index = (remaining_count % len(flames)) - 1
        
        # If index is -1, remove the last element
        if index >= 0:
            right = flames[index + 1:]  # Elements to the right of the index
            left = flames[:index]       # Elements to the left of the index
            flames = right + left       # Join both sides to get new list
        else:
            flames.pop()  # If index is -1, just pop the last element
    
    # Mapping the result to relationship
    result = flames[0]
    if result == 'F':
        return "Friends"
    elif result == 'L':
        return "Love"
    elif result == 'A':
        return "Affection"
    elif result == 'M':
        return "Marriage"
    elif result == 'E':
        return "Enemies"
    elif result == 'S':
        return "Siblings"

# Example usage
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

relationship = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {relationship}")
