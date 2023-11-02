# AI DnD Group

## Members:

Chance Spurgeon-Couraud
Morgan Ray Altmann
Erik Harden
Jared Milligan


 
## Current goals: 

Train AI to recognize rooms/borders/grid squares, token recognition, create classes for GPT personalities, image upload, image reading, file storage




## How we envision this working:

        A camera will overlook a play area
        The play area will consist of a dnd dry erase mat and a dungeon drawn on the mat
        There will be white markers on the mat with a number and letter combination on it
        If they have a number and letter these are npcs for the GMpt to describe
        There will be areas on the mat with numbers
        These will be dungeon rooms
        They will be labeled only with numbers
        A room can be a hall way, a room with doors, a room without doors, etc
        Before moving or starting play the camera will take a picture of the play area
        This will then(in a perfect word) be able to have the numbers and number letters be able to be recorded and recognized as a room npc have vision to detect the boundaries of spaces(dungeon rooms)
        The numbers will be ripped and a gpt personality will be given to each one
        The personality will describe the traits of the room or npc and then store those descriptions in text files titled the number or number letter combo[a]
        Then the pc markers or minis will be placed by the players depending on however they want
        Another screen shot is taken
        The pcs can ask about anything they see(it would be nice to have feature where gpt with the vision would be able to tell where the minis could even see thus able to reject ridiculous requests such as if you had no vision abilities on room 2 but you ask for a description GMpt can tell you to get bent)[b]
        The pcs can then move there characters and after they have moved they take another screen shot and can ask GMpt about their surroundings
        Rinse and repeat until dead or cool stuff


## Features:
        Multiple gpt bots to for every personality
        A gpt bot to create prompts to train new gpt bots(bots of bots kinda like the office space that microsoft has done)
        A vision to gpt ability so that gpt can see and then actually make sense when he talks
        The ability to use dalle 3 to create an image based on dm gpts description of a room
        Plus more i think this should be enough description for now though
        
        
        


























## Image upload and scan



1. Upload image 
   1. Image file types to read
2. Read image
   1. Read numbers in grid
   2. Read rooms in grid
3. Store Room descriptions
4. Chatgpt personality classes
   1. Rules of what it can do
   2. Setting
   3. 




## Notes
     API: read image
     ChatGPT:
     what libraries can I use to recognize grid like maps and store the data in a file?
     ChatGPT
     Recognizing grid-like maps and storing the data in a file is a task that involves image processing and data extraction. You can achieve this using various libraries and tools, depending on your programming language and requirements. Here's a general overview of the libraries and technologies you can use for this purpose:

### Python:

    a. OpenCV: OpenCV is a popular computer vision library in Python. You can use it for image processing tasks, such as detecting grid lines and extracting data.
    b. NumPy: NumPy is useful for numerical operations and can be handy for data manipulation once you've extracted the grid data.
    c. Pytesseract: If your grid-like maps contain text, you can use Pytesseract to perform OCR (Optical Character Recognition) to extract text data.
    d. Matplotlib: Matplotlib can be used for visualization if you need to display or save the processed images.

### Image Processing Libraries:
    a. PIL (Python Imaging Library): PIL is another Python library for image processing and manipulation.
    b. Scikit-Image: Scikit-Image is an image processing library that is built on top of SciPy.
    * Machine Learning and Deep Learning:
    a. TensorFlow and Keras: You can use deep learning frameworks like TensorFlow and Keras for more advanced tasks like detecting and recognizing grid patterns. Convolutional Neural Networks (CNNs) can be helpful for this.
    b. PyTorch: PyTorch is another popular deep learning framework that can be used for image processing and object recognition.

### Grid Detection Algorithms:

    a. Hough Transform: The Hough Line Transform is a technique for detecting straight lines in an image. You can implement this using OpenCV or similar libraries.
    b. RANSAC (Random Sample Consensus): RANSAC can be used to robustly estimate grid parameters in the presence of outliers.
    * File Storage and Data Serialization:
    a. CSV: If the grid data is tabular, you can save it in CSV (Comma-Separated Values) format using Python's built-in CSV module.
    b. JSON: JSON is a lightweight data-interchange format and can be used to store structured data.
    c. SQLite: If you need a relational database, you can use SQLite to store the grid data.
    * Geospatial Libraries:
    a. If your grid-like maps have geospatial information (e.g., latitude and longitude), you might want to use geospatial libraries like GDAL, Fiona, or Shapely for working with geospatial data.
    
    p


## tl;dr
    memory token - separate memory for each room
    Different instances of chatgpt - different characters, different personalities, different rooms, different jobs
    Json or pickle to save data
    Using Pytorch
    Settings file, text files for repeated info
    Room bot feeds descriptions to DM bot,
    Personality class, also fed to DM bot?
    Recognize hallways vs rooms based on shape






  
### comments
    [a]I am excited about the prospect of different GPT personalities, especially if there's more than 1 in a single room, and figuring out how that'll work
    [b]Using the characters/rooms closest to the player tokens will probably be the most difficult part of the project, but I'm excited to see how it plays out
