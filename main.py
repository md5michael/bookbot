import sys
from stats import get_book_text
from stats import get_letter_number
from stats import sort_letters

if len(sys.argv) < 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

book_name = sys.argv[1]





def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    get_book_text(book_name)
    print("--------- Character Count -------")
    get_letter_number(book_name)
    sort_letters()
    print("============= END ===============")

main()
