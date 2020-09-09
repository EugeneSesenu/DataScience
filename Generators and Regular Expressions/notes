Patterns: represents a set of strings which can be potentially infinite. 
backslashes cause problems in handling
$ matches the end of the string
* matches zero or more previous RE 
+ Matches one or more previous RE
{m,n} Matches m to n occurences of previous RE
? Matches zero or one occurences of previous RE

"GET ON" or "GET READY" .......We can use parentheses to create gorupings inside a pattern: r"(ab)+"
'\d same as '[0-9]', matches a digit 
'D' same as '{0-9] matches anything but a digit etc
'\s' matches a whitespace character


MATCH and SEARH FUNCTIONS
present participle words have an ending of "ing" 

CODE: Import re
s = "Doing things going home, staying awake, sleeping later"
re.findall(r'\w+ing\b',s)

OUTPUT :     ['Doing', 'going', 'staying','sleeping']

Note: \b ----> represents the end of the word



CODE:  re.findall (r'[+-]?\d+', "23 + - 24 = -1")

OUTPUT : ['23','-24','-1']


CODE: s = ("If I'm not in a hurry, then I should stay." + "On the other hand, If I leave, then I can sleep")
re.findall(r'[li]f (.*), then', s)

OUTPUT :  ['I'm not in a hurry", 'I leave']. (a condition from both sentences)






FUNCTIONS IN THE "RE" MODULE
* re.match(pattern, str)
* re.search(pattern, str)
* re.findall(pattern, str)
* re.finditer(pattern, str) 
* re.sub(pattern, replacement,str, count = 0)


THE FOLLOWING PROGRAM WILL RETURN ALL "she" words with "he"

import re
str = "she goes where she wants to, she's a sheriff."
newstr = re.sub(r'\b[Ss]he\b', 'he', str)

OUTPUT: This will print ===== he goes where he wants to, he's a sheriff








MATCH OBJECT
the functions (MATCH, SEARCH, and FINDITER) use MATCH objects to describe the found occurence.


the -----> compile(pattern, flags = 0) : precompiles the pattern, mainly for efficiency reasons.


#untoward ---> Simple python Manipulation ----> adjusting strings

[Built in functions]
fox.upper() ---makes it an upper case letter
fox.lower() ---makes it a lower case letter
fox.ljust(20) ----adjust the statement "fox" to the left
fox.Rjust(20) -----adjust the statement "fox" to the right
fox.partition() ---- returns the substring before the first slop point


FORMAT STRINGS--> extracting values from themselves and manipulating them into the desired format.




