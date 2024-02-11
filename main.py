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

    print("===separator===")
    print("Calling 'get_letter_count()' with the frankenstein text. Expected result: Something along the lines of '{'p': 6121, 'r': 20818, 'o': 25225, ...'")
    letter_count = get_letter_count(text)
    print(letter_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_letter_count(text):
    lower_text = text.lower()
    letter_count = {}
    for letter in lower_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
        
main()
