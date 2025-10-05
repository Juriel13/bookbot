import sys
from stats import get_num_words, get_chars_dict, sort_characters

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
  book_filepath = f"{sys.argv[1]}"
  print(f"============ BOOKBOT ============\n Analyzing book found at {book_filepath}...")

  book_text = get_book_text(book_filepath)
  word_count = get_num_words(book_text)
  print(f"----------- Word Count ----------\n Found {word_count} total words")

  book_character_count = get_chars_dict(book_text)
  print("--------- Character Count -------")
  
  sorted_character_count = sort_characters(book_character_count)
  for i in sorted_character_count:
    if i["char"].isalpha() == True:
      print(f"{i["char"]}: {i["num"]}")
  print("============= END ===============")

main ()