#opens txt file saved in the repository
source = open('The Oxford Book of Latin Verse.txt')
text = source.read()
# imports regular expression
import re
#function raises a TypeError is the argument is not a string
#function creates a list of all the words that end with "at"
def test(book):
    if type(book) != str:
        raise TypeError("Not a string")
    result = re.findall(r"\b[A-Za-z]*at\b", book)

     long_words = []
     for element in result:
        if len(element)> 3:
            long_words.append(element)
    return long_words

test(text)
