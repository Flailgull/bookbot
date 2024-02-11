FRANKENSTEIN = "books/frankenstein.txt"
LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def main():
    print("Bookreport for books/frankenstein.txt")
    print("")
    report = get_report(FRANKENSTEIN)

    print(report)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_letter_count(text):
    #lowercase text to avoid duplicates for say 'a' and 'A'
    lower_text = text.lower()
    #make a dictionary with 'p' : 6121 and so on
    letter_count = {}
    for letter in lower_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    #convert the dictionary into a list of dictionaries, only take letters 'a' to 'z'
    letter_list = []
    for letter in LETTERS:
        letter_list.append({"name": letter, "num": letter_count[letter]})
    
    letter_list.sort(reverse=True, key=sort_on)

    return letter_list

def get_report(path):
    text = get_book_text(path)
    word_count = get_word_count(text)
    letter_list = get_letter_count(text)

    report = f"--- Begin report of {path} ---\n"
    report += f"{word_count} words found in the document\n\n"

    for letter in letter_list:
        report += f"The '{letter["name"]}' character was found {letter["num"]} times\n"
    
    report += "--- End report ---"

    return report

def sort_on(dict):
    return dict["num"]
        
main()
