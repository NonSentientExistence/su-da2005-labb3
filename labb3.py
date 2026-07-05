
# Inserts an int into an already sorted list of numbers
def insert_in_sorted(x, sorted_list):
    # Iterates through the sorted list. i in range is used to get the correct index for inserting number when x < number in list
    for i in range(len(sorted_list)):
        if x < sorted_list[i]:
            # insert into list at i index, if x <  sorted_list[i]
            sorted_list.insert(i, x)
            return sorted_list
    # If no x < list[i] is found, then x is the largest number in the list. Append to list, then return list
    sorted_list.append(x)
    return sorted_list

# Sorts a list of numbers by calling insert in sorted function
def insertion_sort(my_list):
    
    out = [] 
    # Iterates through all numbers in list
    for n in my_list:
        # calls insert in sorted, that func mutates the out list when inserting number at correct index
        insert_in_sorted(n, out)
    
    return out

# Opens an existing text file, reads all lines 
# Then adds line number and a whitespace to each line in the file.
# Writes this line per line to a new file named numbered_{filename}
def number_lines(filename):
    # Opens submitted file
    with open(filename, 'r', encoding="UTF-8") as fp:
        # Reads all lines in file and adds each line as list element
        lines = fp.readlines()
        # Creates or opens file numbered_{filename}, owerwrites numbered_{filename} if it exists
        with open("numbered_" + filename, "w", encoding="UTF-8") as f:
            # Iterates through lines. I to get index number for numeration of lines in output file
            for i in range(len(lines)):
                # Writes each line to numbered_{filename} with added {index number} and whitespace
                f.write(f"{i} {lines[i]}")

# Opens files and reads, returns a dict with key = word and value = [row number, row number] without duplicate rows
def index_text(filename):

    index_dict = {}
    #Open file with UTF-8 encoding
    with open(filename, 'r', encoding="UTF-8") as fp:
        # assign all lines in file to variable
        lines = fp.readlines()

        # Iterate through each line. Run for range up to length of lines variable, this to get i as index for line number
        for i in range(len(lines)):
            # assign the current line in var line
            line = lines[i]

            # Split line into separate words
            words = line.split() 

            # Iterate through each word
            for w in words:
                # set word to lower case
                lower_word = w.lower()
                # if the word is in the dict, check if it already has that line index as value. If line number  exists, skip that word
                # else, add that word to the dict with the line row as value
                if lower_word in index_dict:
                    if i in index_dict[lower_word]:
                        continue
                    else:
                        index_dict[lower_word].append(i)
                else:
                    index_dict[lower_word] = [i]

    return index_dict

def important_words(an_index, stop_words):
    
    # Assign dict to variable to ensure original dict remains unmutated
    index_words = dict(an_index)

    

    # Iterates through list of stop words. 
    for w in stop_words:
        # Removes each stopword from copied dict, returns none if no match to avoid crash
        index_words.pop(w, None)

    out_list = []

    # loop through dict five times
    for _ in range(5):
        # if the dict is empty, stop loop
        if not index_words:
            break
        freq_word = None
        high_count = 0
        
        # Iterates through each word in the dict
        for w in index_words:
            # Get amount of line rows the word has
            count = len(index_words[w])
            # Check if current count is higher than any previous counts of line rows. If true, set current word line count as highest 
            if count > high_count:
                high_count = count
                freq_word = w

        # Add the highest line count word to list, then remove the word from copy of input dict. 
        out_list.append(freq_word)
        index_words.pop(freq_word)

    return out_list

# Program to ask user for input file, then attempts to process input file in index_text func. Except handles file not found
while True:
    user_file = input("En textfil: ")
    #Attempts to read file in index_text() then submits generated dict to important_words function
    try:
        # Pre generated list of stop words has 'foer' added to it, this to ensure that the file with removed å,ä,ö also works correctly
        user_high_count = important_words(index_text(user_file), ['och', 'jag', 'som', 'det', 'för', 'foer'])
        print("De viktigaste orden är:")
        # Iterate through result list and print each, then break while loop to exit program
        for w in user_high_count:
            print(w)
        break
    # Handles File not found error. If index_text can't open the file, the except will execute
    except FileNotFoundError:
        print("Filen finns inte eller är oläsbar")
        user_option = input("Försöka igen? (j): ")
        # Check if user wanted to enter a new file name. Else stop while (quit)
        if user_option.lower() == "j":
            continue
        else:
            break