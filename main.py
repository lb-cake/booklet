

def word_counter_num(string: str) -> int:
    return len(string.split())

def find_duplicates(string: str) -> dict[str, int]:
    # TODO - find duplicates and print the number of occurences it shows up
    lower_case_book = string.lower()
    words = lower_case_book.split()
    word_counter = {}
    for word in words:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    return word_counter



word_counter_dict = {}
words = 0
book = "books/frankenstein"
with open("./books/frankenstein.txt") as f:
    text = f.read()
    words = word_counter_num(text)
    word_counter_dict = find_duplicates(text)


word_counter_res = dict(sorted(word_counter_dict.items(), key=lambda item: item[1], reverse=True))
print(f"--- Begin report of {book} ---")
print(f"{words} words found in the document\n")

for word in word_counter_res:
    print(f"The '{word}' was found {word_counter_res[word]} times")
