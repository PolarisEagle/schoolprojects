# a213_pw_analyzer.py
import time
import pwalgorithms as pwa
oneortwo = input("One or Two words or Two words and a number (1/2/3)")

password = input("Enter password:")

if oneortwo == "1":
  print("Analyzing a one-word password ...")
  time_start = time.time()
  found, num_guesses = pwa.one_word(password)
  time_end = time.time()
elif oneortwo == "2":
  print("Analyzing a two-word password ...")
  time_start = time.time()
  found, num_guesses = pwa.two_words(password)
  time_end = time.time()
elif oneortwo == "3":
  print("Analyzing a two-word & number password ...")
  time_start = time.time()
  found, num_guesses = pwa.two_words_num(password)
  time_end = time.time()
else:
  print("Invalid Response for one or two passwords. Please try again.")


# attempt to find password

# report results
if (found):
  print(password, "found in", num_guesses, "guesses")
else: 
  print(password, "NOT found in", num_guesses, "guesses!")
print("Time:", format((time_end-time_start), ".8f"))