FRANKENSTEIN = "books/frankenstein.txt"
def main():
    with open(FRANKENSTEIN, "r") as f:
        file_contents = f.read()
        print(file_contents)
        
main()
