"""
    This is the practice file for Regex
    The most common uses of regular expressions are:
        Search a string (search and match)
        Finding a string (findall)
        Break string into a sub strings (split)
        Replace part of a string (sub)

    The special sequences consist of "\\" and a character from the following list:
        \d  Matches any decimal digit; equivalent to the set [0-9].
        \D  The complement of \d. It matches any non-digit character; equivalent to the set [^0-9].
        \s  Matches any whitespace character; equivalent to [ \t\n\r\f\v].
        \S  The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
        \w  Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]. With LOCALE, it will match the set [a-zA-Z0-9_] plus characters defined as letters for the current locale.
        \W  Matches the complement of \w.
        \b  Matches the empty string, but only at the start or end of a word.
        \B  Matches the empty string, but not at the start or end of a word.
        \\  Matches a literal backslash.

"""


text = """Regular expressions are extremely useful in extracting information from text such as code, log files, spreadsheets, or even documents. 
And while there is a lot of theory behind formal languages, the following lessons and examples will explore the more practical uses of regular expressions so that you can use them as quickly as possible.
The first thing to recognize when using regular expressions is that everything is essentially a character, and we are writing patterns to match a specific sequence of characters (also known as a string). 
Most patterns use normal ASCII, which includes letters, digits, punctuation and other symbols on your keyboard like %#$@!, but unicode characters can also be used to match any type of international text.
Below are a couple lines of text, notice how the text changes to highlight the matching characters on each line as you type in the input field below. To continue to the next lesson, 
you will need to use the new syntax and concept introduced in each lesson to write a pattern that matches all the lines provided.
Go ahead and try writing a pattern that matches all three rows, it may be as simple as the common letters on each line."""

# import libraries
import re

# search a string

pattern = re.compile("expressions")
res = pattern.findall(text)
print(res)

#1
pattern = re.compile("expressions.*?character")
res = pattern.findall(text)
print(res)

