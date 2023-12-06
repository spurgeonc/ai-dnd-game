# Initialize variables to store the numbers
token_numbers = None
token = "token"

# Open the text file for reading
with open("detection.txt", "r") as file:
    # Iterate through each line in the file
    for line in file:
        # Check if the line contains token
        if token in line:
            # Extract the four numbers from the line
            numbers = [int(num) for num in line.split("[")[1].split("]")[0].split(", ")]
            
            # Store the numbers in the variables
            token_numbers = numbers

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

# Check if the word "token" was found in the file
if token_numbers is not None:
    # Print the numbers and store them in variables
    # print("Token Numbers:", token_numbers)

    x1, y1, x2, y2 = token_numbers
    # print("x1:", x1) # test line, keeping in case further tests needed
    # print("y1:", y1) # test line, keeping in case further tests needed
    # print("x2:", x2) # test line, keeping in case further tests needed
    # print("y2:", y2) # test line, keeping in case further tests needed

    xcent = (x1 + x2) / 2
    ycent = (y1 + y2) / 2

    # print("xcent:", xcent) # test line, keeping in case further tests needed
    # print("ycent:", ycent) # test line, keeping in case further tests needed

    print(find_room(xcent, ycent))
else:
    print(f"No line containing the word {token} found in the file.")
