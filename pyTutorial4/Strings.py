# Here we will be learning about Strings

print("Python Tutorial by BibekG")
print("Python Tutorial \n by BibekG")
print("Python Tutorial \" by BibekG")

phrase = "Python Tutorial by BibekG"
print(phrase)

# Concatination
phrase = "Python Tutorial by BibekG"
print(phrase + "is great")

# Lower Case
phrase = "Python Tutorial by BibekG"
print(phrase.lower())

# Upper Case
phrase = "Python Tutorial by BibekG"
print(phrase.upper())

# True or False
phrase = "Python Tutorial by BibekG"
print(phrase.isupper())
print(phrase.islower())

phrase = "Python Tutorial by BibekG"
print(phrase.upper().isupper())

# length of a string
phrase = "Python Tutorial by BibekG"
print(len(phrase))

# individual character i want to grab
# Python Tutorial by BibekG
# 0123456789
phrase = "Python Tutorial by BibekG"
print(phrase[0])

# index function
# where a specific character is located inside a string
phrase = "Python Tutorial by BibekG"
print(phrase.index("P"))
print(phrase.index("y"))
print(phrase.index("BibekG"))

# replace
phrase = "Python Tutorial by BibekG"
print(phrase.replace("Tutorial", "Learning"))

