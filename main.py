FRANKENSTEIN = "books/frankenstein.txt"
def main():
    print("===separator===")
    print("Reading books/frankenstein.txt and printing it to the console")
    text = get_book_text(FRANKENSTEIN)
    print(text)
    
    print("===separator===")
    print("Calling 'get_word_count()' with the frankenstein text. Expected result: 77986 words.")
    word_count = get_word_count(text)
    print(word_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())
        
main()
