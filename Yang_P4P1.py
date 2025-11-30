#Yang_P4P1
#Jay Yang
#Sunday November 23, 2025

import string

def main():
#Ask the user to enter the filename
    filename = input("Enter the name of the text file: ")

    try:
#Try to open and read the file line by line
        with open(filename, "r") as file:
            lines = file.readlines()
#Check if the file is empty
        if not lines:
            print("Error: The file is empty.")
            return
#Dictionary for storing word frequncies
        word_freq = {}
        total_length = 0
        word_count = 0

#Punctuation to remove
        punct = string.punctuation

        for line in lines:
#Remove punctuation, lowercase everything
            clean_line = line.lower().translate(str.maketrans("", "", punct))
            words = clean_line.split()

#Process words line
            for word in words:
#Skip short words
                if len(word) < 3:      
                    continue
#Add word length to total(used for average word length)
               total_length += len(word)
#Count this word
                word_count += 1
#Dictionary for starting word frequencies
                word_freq[word] = word_freq.get(word, 0) + 1
#update frequency dicitionary
        if word_count == 0:
            print("Error: No valid words (3+ letters) found.")
            return

#Calculate average word length
        avg_length = round(total_length / word_count, 2)

#Prepare formatted output
        result_text = "\n\n--- ANALYSIS RESULTS ---\n"
        result_text += "Word Frequency:\n"
        for word, count in sorted(word_freq.items()):
            result_text += f"{word}: {count}\n"
        result_text += f"\nAverage Word Length: {avg_length} characters\n"

#Append results to the same file
        with open(filename, "a") as file:
            file.write(result_text)
        print(result_text)
        print("Results have been appended to Random.txt")

    except FileNotFoundError:
#Error if the file doesn't exist
        print("The file contains no data") 
        

#Run the program
main()



