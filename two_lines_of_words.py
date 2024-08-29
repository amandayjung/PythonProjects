'''
File: two_lines_of_words.py
Name: Amanda Jung
Course: CSC 120, Summer 2024
Purpose: Read two lines from user, prints their words, 
concatenates them, sort them, and prints pairs of words.
'''

line1 = input()
line2 = input()
# Split each line into words
words1 = line1.split()
words2 = line2.split()
print("The first line was:", words1)
print("The second line was:", words2)
# Blank line
print() 
combined_words = words1 + words2
print("The combination of both lines had", len(combined_words), "words.")
print("The combined set of words was:", combined_words)
print() 

# Sort
sorted_combined_words = []
while combined_words:
    min_word = combined_words[0]
    for word in combined_words:
        if word < min_word:
            min_word = word
    sorted_combined_words.append(min_word)
    combined_words.remove(min_word)

print("After sorting, the words were:", sorted_combined_words)
print() 
print("Pairs:")
for i in range(min(len(words1), len(words2))):
    print(i, ":", words1[i] + ",", words2[i])
