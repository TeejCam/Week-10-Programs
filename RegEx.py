import re

'''
1. Write a program to check that a string contains only a certain set of characters
(A-Z and 0-9)
Test:
"ABCDEFabcdef123450"
"*&%@#!}{"
'''
def containsChar(str):
    str = re.findall('[A-Z0-9]', str)
    if(len(str) > 0):
        return True
    else: return False

print("Problem 1:\n")
print(containsChar("ABCDEFabcdef123450"))
print(containsChar("*&%@#!}{"))

''' 
2. Write code that matches a string that has an a followed by 0 or more b's
Test: 
“ab”
“abc”
“a”
“ab”
“abb”
'''

def matchGreedy(str):
    pattern = r'ab*'
    for char in str:
        if re.search(pattern, char):
            return True
        else: return False

print("Problem 2:\n")
print(matchGreedy("ab"))
print(matchGreedy("abc"))
print(matchGreedy("a"))
print(matchGreedy("ab"))
print(matchGreedy("abb"))

''' 
3. Write code that matches a string that has an a followed by 1 or more b's
Test:
“ab”
“abc”
“a”
“ab”
“abb”
'''

def matchNonGreedy(strings):
    pattern = r'^ab+'
    results = []
    for s in strings:
        if re.search(pattern, s):
            results.append((s, True))
        else:
            results.append((s, False))
    return results

print("Problem 3:\n")
test = ["ab", "abc", "a", "ab", "abb"]
for s, result in matchNonGreedy(test):
    print(s, result)

'''
4. Write code to find sequences of lowercase letters joined by an underscore
Test:
"aab_cbbbc"
"aab_Abbbc"
"Aaab_abbbc"
'''
print("Problem 4:\n")
def findLowercaseUnderscore(str):
    matches = re.findall(r'[a-z]+_[a-z]+', str)
    return matches

print(findLowercaseUnderscore("aab_cbbbc"))
print(findLowercaseUnderscore("aab_Abbbc"))
print(findLowercaseUnderscore("Aaab_abbbc"))

'''
5. Write code that matches a word at the beginning of a string
Test: 
"The quick brown fox jumps over the lazy dog."
" The quick brown fox jumps over the lazy dog."
'''
def matchStart(str):
    # Im assuming that you want us to trim the whitespace on the second one
    str = str.lstrip()
    match = re.findall(r'^\w+', str)
    return match

print("Problem 5:\n")
print(matchStart("The quick brown fox jumps over the lazy dog."))
print(matchStart(" The quick brown fox jumps over the lazy dog."))

'''
6. Write code that matches a word containing 'z'
Test: 
"The quick brown fox jumps over the lazy dog."
"Python Exercises."
'''
def containsZ(str):
    str = re.findall('[z]', str)
    if (len(str) > 0):
        return True
    else:
        return False
print("Problem 6:\n")
print(containsZ("The quick brown fox jumps over the lazy dog."))
print(containsZ("Python Exercises."))
'''
7. Write code to remove leading zeroes from  an IP address
Test:
"216.08.094.196"
'''
def removeLeadingZeros(ip):
    sections = ip.split(".")
    splitSections = [str(int(section)) for section in sections]
    return '.'.join(splitSections)

print("Problem 7:\n")
print(removeLeadingZeros("216.08.094.196"))

'''
8. Write code to search for literal strings within a string.
Sample text: 'The quick brown fox jumps over the lazy dog.'
Searched words: 'fox', 'dog', 'horse'
'''
print("Problem 8:\n")
def searchWords(str):
    words = ['fox', 'dog', 'horse']
    results = []
    for word in words:
        if re.search(rf'\b{word}\b', str):
            results.append((word, True))
        else:
            results.append((word, False))
    return results

for word, result in searchWords('The quick brown fox jumps over the lazy dog.'):
    print(word, result)

'''
9. Write code to search for a literal string and also find the location within 
the original string where the pattern occurs
Sample text: 'The quick brown fox jumps over the lazy dog.'
Searched words: 'fox' 
'''
print("Problem 9:\n")
def searchWordsAndLocation(str):
    match = re.search(r'\bfox\b', str)
    if match:
        return match.start()
    else:
        return -1
print(searchWordsAndLocation('The quick brown fox jumps over the lazy dog.'))

'''
10. Write code to replace whitespaces with an underscore and vice versa
Test: “Regular Expressions” and “Code_Examples”
'''
print("Problem 10:\n")
def replace(str):
    if ' ' in str:
        return re.sub(r'\s', '_', str)
    elif '_' in str:
        return re.sub(r'_', ' ', str)
    else:
        return str
print(replace("Regular Expressions"))
print(replace("Code_Examples"))

'''
11. Write code to extract year, month, and date from a URL
Test: https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/
'''
print("Problem 11:\n")
def extractDate(url):
    date = re.findall(r'/(\d{4})/(\d{2})/(\d{2})/', url)
    if len(date) > 0:
        print(date)
    else:
        print("No date found")
print(extractDate("https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"))

'''
12. Write code to find all words starting with 'a' or 'e' in a given string
Test: "The following example creates an ArrayList with a capacity of 50 elements. 
Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
'''
print("Problem 12:\n")
def findWordsAE(str):
    words = re.findall(r'\b[aAeE]\w*', str)
    return words
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
print(findWordsAE(text))
'''
13. Write code to replace all occurrences of a space, comma, or dot with a colon
Test: 'Python Exercises, PHP exercises.'
'''
print("Problem 13:\n")
def replaceWithColon(str):
    return re.sub(r'[ ,.]', ':', str)

print(replaceWithColon("Python Exercises, PHP exercises."))

'''
14. Write code to remove multiple spaces froma  string
Test: 'Python      Exercises'
'''

print("Problem 14:\n")
def removeMultipleSpaces(str):
    return re.sub(r'\s+', ' ', str)

print(removeMultipleSpaces('Python      Exercises'))