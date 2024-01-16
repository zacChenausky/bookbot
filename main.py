def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = number_of_words(text)
  letter_count = count_letters(text)
  print_report(book_path, num_words, letter_count)
  #print(text)
  #print(num_words)
  #print(letter_count)

def print_report(path, num_words, letter_count):
  print(f"--- Begin report of {path} ---")
  print(f" {num_words} words found in the document")
  print('\n')
  result_list = list(letter_count.items())
  result_list.sort()
  for result in result_list:
    if result[0].isalpha():
      print(f"The {result[0]} character was found {result[1]} times")
  print("--- End Report --- ")

def number_of_words(text):
  words = text.split()
  return len(words)

def count_letters(text):
  letters = {}
  for i in text:
    lower = i.lower()
    if lower in letters:
      letters[lower] += 1
    else:
      letters[lower] = 1
  return letters

def get_book_text(path):
  with open(path) as f:
    return f.read()

main()