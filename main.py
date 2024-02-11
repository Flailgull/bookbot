FRANKENSTEIN = "books/frankenstein.txt"
def main():
    text = get_book_text(FRANKENSTEIN)
    print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
main()
