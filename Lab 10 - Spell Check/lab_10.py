import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("dictionary.txt")

    # Create an empty list to store our names
    dict_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        dict_list.append(line)

    my_file.close()

    print("---Linear Search---")

    chapter_1 = open("AliceInWonderLand200.txt")
    chapter_list = []
    line_number = 0
    for line in chapter_1:
        line = line.strip()
        line_number += 1
        for word in split_line(line):
            found = False
            for dict_word in dict_list:
                if word.upper() == dict_word:
                    found = True
                    break
            if not found:
                print("Line", line_number,"possible misspelled word:",word)

    chapter_1.close()

    print("---Binary Search---")

    key = dict_list
    book_1 = open("AliceInWonderLand200.txt")
    book_list = []
    line_number1 = 0
    dict_list1 = len(dict_list)-1
    found = False

    # Loop until we find the item, or our upper/lower bounds meet
    while line_number1 <= dict_list1 and not found:

        # Find the middle position
        middle_pos = (line_number1 + dict_list1) // 2

        # Figure out if we:
        # move up the lower bound, or
        # move down the upper bound, or
        # we found what we are looking for
        if dict_list[middle_pos] < key:
            line_number1 = middle_pos + 1
        elif dict_list[middle_pos] > key:
            dict_list1 = middle_pos - 1
        else:
            found = True

    book_1.close()



main()