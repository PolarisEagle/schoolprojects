# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def two_words(password):
  global two_words_list, guesses, words
  two_words_list = []
  words = get_dictionary()
  guesses = 0
  index = 0
  # get each word from the dictionary file
  for i in words:
    exit = False
    try:
      index += 1
    except IndexError:
      break
    tempindex = 0
    while exit == False:
      tempword = ''
      try:
        tempword = i + words[tempindex]
      except IndexError:
        exit = True
      # matchwords(tempword)
      guesses += 1
      # print(tempword)
      if (tempword == password):
        return True, guesses
      try:
        tempindex += 1
      except IndexError:
        exit = True
  return False, guesses

def two_words_num(password):
  global two_words_list, guesses, words
  two_words_list = []
  words = get_dictionary()
  guesses = 0
  index = 0
  # get each word from the dictionary file
  for i in words:
    exit = False
    try:
      index += 1
    except IndexError:
      break
    tempindex = 0
    while exit == False:
      tempword = ''
      number = 0
      while number != 10:
        try:
          tempword = i + words[tempindex] + str(number)
          if (tempword == password):
            return True, guesses
        except IndexError:
          exit = True
        number += 1
        guesses += 1
      try:
        tempindex += 1
      except IndexError:
        exit = True
  return False, guesses
# def matchwords(i):
#   for x in words:
#     if x == i:
#       return i
#     else:
#       two_words_list.append(x)
#   return False
