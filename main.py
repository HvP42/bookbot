from vispy.util.svg import length
from dask import sizeof
from xlrd.formatting import date_char_dict

def main():
    book_path = "books/frankenstein.txt"
    contents = read_book(book_path)
    words = contents.split()
    print(len(words))
    print(num_chars(contents))
    

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


