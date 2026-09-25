s = "Instagram"

print("The length of string s:",len(s))
print(type(s))
print(dir(s))   # used to show all function of that str

s1 = "welcome to the python"
s2 = s1.capitalize()
print("The capitalized :",s2) # convert 1st character of 1st word into upperCase

s3 = "welcome to the python"
s4 = s1.upper()
print("The UpperCase :",s4)  # converted Into uppercase

s5 = "WELCOME TO THE PYTHON"
print("The Lowercase of string s5:",s5.lower()) # converted into lowercase

s3 = "welcome to the python"
print(s3.title()) # used to make 1st letter of word into upperCase

s3 = "    welcome to the python          "
print(s3.strip())  # remove space from both sides
print(s3.rstrip()) # remove trailing spaces
print(s3.lstrip())  # remove leading spaces

name = "Python"
print(name.replace("Python","Sanjana"))  # replace whole word
print(name.replace("P","J")) # replace 1st letter of string

# Replaces all occurrences of a with i.
n1 = "Sanjana"
a = "a"
b = "i"
print(n1.replace(a,b))

s0 = "Sanjana"
print(len(s0))

s8 = "welcome to python"
print(s8.split())  # seperate each word

s9 = ["welcome", "to", "python"]
print(" ".join(s9))  # combine all word together

s10 = "Welcome to python"
print(s10.find("python")) # return 1st index of that starting word

s11 = "Welcome to python"
print(s11.index("to")) # return index of that words 1st letter

s12 = "Welcome to the python lecture"
print("Total count of o:",s12.count("o"))
print("Total count of l:",s12.count("l"))
print("Total count of e:",s12.count("e"))

s13 = "Welcome to python"
print(s13.startswith("Welcome")) # True
print(s13.startswith("to"))  # false

s14 = "welcome to python"
print(s14.endswith("python")) #True

s15 = "Python"
print(s15.isalpha())  # if all letter of string is alpha return true

s16 = "123456"
s17 = "pyth12981"
print(s16.isdigit())  # True
print(s17.isdigit())  # False

s18 = "Python123"  # combination of alpha-numeric 
print(s18.isalnum())  # true

s19 = "python1244$"
print(s19.isalnum())  # false

s20 = "Sanjana"
print(s20.count("a"))  #3

s21 = "Python"
print(s21.zfill(10)) # 0000Python 
