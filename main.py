


def main():
    file_path = "books/frankenstein.txt"
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    #print(file_contents)
    num_words = count_words(file_contents)
    #print(num_words)
    chars_dict = count_characters(file_contents)
    #print(chars_dict)
    chars_sorted = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {file_path} ---")
   #print(f"{num_words} words found in the document")

    for i in chars_sorted:
        if not i["char"].isalpha():
            continue
        print(f"The {i['char']} character was found {i['num']} times")
    
    print("--- End report ---")
    

def sort_on(d):
    return d["num"]


def count_words(file):
    words = file.split()
    return len(words)

def count_characters(file):
    chars_in_text = {}
    file_lowered = file.lower()
    for char in file_lowered:
        if char in chars_in_text:
            chars_in_text[char] +=1
        else:
            chars_in_text[char] = 1
    return chars_in_text


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num":chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

main()