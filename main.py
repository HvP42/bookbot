from vispy.util.svg import length
from dask import sizeof
from xlrd.formatting import date_char_dict

def main():
    book_path = "books/frankenstein.txt"
    contents = read_book(book_path)
    words = contents.split()
    print_report(book_path)
    
def print_report(book_path):
    print("--- Begin report of " + book_path + " ---")
    contents = read_book(book_path)
    words = contents.split()
    print(f"{len(words)} found in the document")
    chars = num_chars(contents)
    l = list_of_dict(chars)
    l.sort(reverse=True, key=sort_on)
    for d in l:
        buchstabe = d["name"]
        nummer = d["num"]
        print(f"The {buchstabe} character was found {nummer} times")
    
    
def list_of_dict(char_dict):
    result = []
    for key in char_dict:
        val = char_dict[key]
        x = {}
        x["name"] = key
        x["num"] = char_dict[key]
        result.append(x)
    return result 
    
def sort_on(dict):
    return dict["num"]

def read_book(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

        
def num_chars(text):
    lowertext = text.lower()
    char_Dict = {}
    for c in lowertext:
        try:
            i = char_Dict[c]
            char_Dict[c] = i+1
        except:
            char_Dict[c] = 0
            
    return char_Dict
   
main()


