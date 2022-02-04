#!/Users/benjaminsteele/miniconda3/bin/python3
import sys

# Fetches dictionary from file and parses it into a useable list.
def getDictionary():
  try:
    dictionaryFile = open('./words_alpha.txt', 'r')
  except:
      print("Error: Could not open dictionary.")
      sys.exit(1)
  # Create list from dictionary file
  dictionary = list(map(str.strip, dictionaryFile.readlines()))
  dictionary = list(map(str.upper, dictionary))
  dictionaryFile.close()
  return dictionary
  
def main():
  # Get and validate required letter input (1 letter)
  required = None
  while True:    
    required = input("Enter required letter: ")
    if required.isalpha() and len(required) == 1:
      break
    else:
      print("Invalid letter, please try again.")
  
  # Get and validate optional letters input (6 letters)
  optional = None
  while True:
    invalid_letter = False
    optional = input("Enter the remaining 6 letters (i.e abcdef): ")
    for i in range(6):
      if not optional[i].isalpha():
        invalid_letter = True
        print("Invalid symbol in entered letters, please try again.")   
        break
    if not invalid_letter:
      break

  # Format letters into capitalized list
  required = required.upper()
  optional = optional.upper()
  optional = list(optional)
  optional.append(required)

  # Load dictionary
  dictionary = getDictionary()

  words = []
  biggest_word_length = -1
  biggest_word = ''
  # For each word in the dictionary
  for e in dictionary:
    # If the word is less than 4 characters, skip.
    if len(e) < 4:
      continue
    # If the word does not contain the required character, skip.
    if required not in e:
      continue
    # If all of the characters in word exist in optional, add to word list.
    if all(c in optional for c in e):
      words.append(e)
      # Check and update biggest word.
      if len(e) > biggest_word_length:
        biggest_word_length = len(e)
        biggest_word = e

  # Display results
  print("---BIGEST WORD---")
  print(biggest_word + '\n')
  print("---ALL WORDS---")
  print(words)

if __name__ == '__main__':
  main()