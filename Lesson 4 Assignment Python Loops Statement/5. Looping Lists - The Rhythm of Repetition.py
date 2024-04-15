# Objective:
# Dive into the heart of Python loops with a musical twist. Your task is to explore different ways of looping through lists, each with its unique style and purpose. By the end of this assignment, you will be able to control your loops like a DJ controls the tracks, ensuring each element gets its time to shine.

# Task 1: The for Loop DJ Set
# Using the provided genres list, write a for loop that prints out each genre with a custom message. Extend this task by adding a counter that displays the number of the track before the genre.

# # Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
track_number=0
for genre in genres:
    track_number+=1
    print(f"Track #{track_number}. Currently Playing {genre}")

# Task 2: The Remix Artist with while
# Convert the for loop from Task 1 into a while loop. Ensure it performs the same function but also includes a condition to stop the loop if a certain genre is played for instance Hip-hop.

index=0
while index<len(genres) and genres[index]!="Hip-hop":
    print(f"Track #{index+1}. Currently Playing {genres[index]}")
    index +=1


# Task 3: Light Show Technician Loop
# Using the range() function, loop through the genres list by index. For each genre, print out the track number and a message that the light show is ready. Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre.

for i in range(len(genres)):
    if genres[i] == "Classical":
        continue
    
    print(f"Track #{i+1}. Light Show is ready for {genres[i]}")