from stats import report
import sys

def main():
    print("Usage: python3 main.py <path_to_book>")


    if sys.argv[1] == None:
        sys.exit(1)
    
    return report(sys.argv[1])
     #return get_book_text("books/frankenstein.txt")

main()


    