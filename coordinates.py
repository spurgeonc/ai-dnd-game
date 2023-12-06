global coordinates 
coordinates = []

def find_token_coords():
    global coordinates
    # Open the text file for reading
    with open('detection.txt', 'r') as file:
        # Initialize a variable to keep track of the line number
        line_number = 0

        # Initialize variables to store the four numbers
        token_line = None
        numbers = None
        
        # Iterate through each line in the file
        for line in file:
            # Increment the line number
            line_number += 1
            
            # Check if the line contains the word "token"
            if "token" in line:
                print(f"Found 'token' on line {line_number}: {line.strip()}")
                token_line = line.strip()  # Remove leading/trailing whitespace
                # Split the line by spaces and convert the numbers to integers
                numbers = [int(num) for num in token_line.split() if num.isdigit()]

                if len(numbers) == 4:
                    coordinates = numbers  # Store the coordinates in the global variable
                    return  # Exit the function after finding the coordinates



def find_room(x, y):
    if (515 <= x <= 590 and 175 <= y <= 220) or (543 <= x <= 573 and 321 <= y <= 336):
        return "Room 7"
    elif 445 <= x <= 515 and 175 <= y <= 220:
        return "Room 2"
    elif 372 <= x <= 415 and 145 <= y <= 175:
        return "Room 3"
    elif 290 <= x <= 330 and 145 <= y <= 175:
        return "Room 4"
    elif (190 <= x <= 260 and 170 <= y <= 215) or (262 <= x <= 333 and 173 <= y <= 215):
        return "Room 15"
    elif (120 <= x <= 190 and 165 <= y <= 215) or (110 <= x <= 142 and 355 <= y <= 400):
        return "Room 6"
    elif (528 <= x <= 590 and 333 <= y <= 590) or (515 <= x <= 528 and 220 <= y <= 340):
        return "Room 12"
    elif 200 <= x <= 255 and 356 <= y <= 405:
        return "Room 8"
    elif 142 <= x <= 200 and 355 <= y <= 400:
        return "Room 9"
    elif 110 <= x <= 142 and 355 <= y <= 400:
        return "Room 10"
    elif 422 <= x <= 527 and 335 <= y <= 410:
        return "Room 11"
    elif (515 <= x <= 590 and 220 <= y <= 318) or (380 <= x <= 515 and 225 <= y <= 255) or (401 <= x <= 515 and 259 <= y <= 335):
        return "Room 13"
    elif (372 <= x <= 443 and 175 <= y <= 218) or (417 <= x <= 443 and 145 <= y <= 218):
        return "Room 14"
    elif 355 <= x <= 440 and 105 <= y <= 145:
        return "Room 16"
    elif 270 <= x <= 355 and 105 <= y <= 145:
        return "Room 17"
    elif 333 <= x <= 375 and 87 <= y <= 105:
        return "Room 18"
    elif 333 <= x <= 373 and 144 <= y <= 222:
        return "Room 19"
    elif (210 <= x <= 300 and 215 <= y <= 355) or (210 <= x <= 320 and 215 <= y <= 255):
        return "Room 20"
    elif 115 <= x <= 210 and 212 <= y <= 355:
        return "Room 21"
    elif (333 <= x <= 373 and 222 <= y <= 350) or (295 <= x <= 407 and 260 <= y <= 350):
        return "Room 22"
    elif 260 <= x <= 422 and 350 <= y <= 405:
        return "Room 23"
    else:
        return "No room found for these coordinates"

# Example usage:
x = 400  # test for now
y = 250  # test for now
find_token_coords()  # Call the function to find the token coordinates
# Check if the "token" line was found
if len(coordinates) == 4:
    # Now you can access the individual numbers
    num1, num2, num3, num4 = coordinates  # Use coordinates instead of numbers
    print(f"Numbers from 'token' line: {num1}, {num2}, {num3}, {num4}")
else:
    print("The word 'token' was not found in the file.")

room = find_room(x, y)
print(f"Coordinates ({x}, {y}) are in {room}")
