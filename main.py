from collections import defaultdict as dd

def main():
    book_path = "books/frankenstein.txt"

    with open(book_path) as f:
        file_contents = f.read()
        
        file_contents = file_contents.lower()

        word_counts = len(file_contents.split())

        char_dict = dd(int)
        charlist = "abcdefghijklmnopqrstuvwxyz"

        for char in file_contents:
            if char not in charlist:
                continue
            char_dict[char] += 1

        sorted_dict = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)


        print(f"--- Begin report of {book_path} ---")
        print(f"{word_counts} words in {book_path}\n")

        for k, v in sorted_dict:
            print(f"The '{k}' character was found {v} times")

        print("--- End report ---")
main()

