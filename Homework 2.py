print("String methods-capitalize()")
text = "python 3.8.0, documentåtion released on 14/10/2019"
word1 = "python"
word2 = "3.8.0"
word3 = "doctumentation"
word4 = "released"
word5 = "on"
word6= "14/10/2019"
print(word1.capitalize() + word2.capitalize() + word3.capitalize() + word4.capitalize() + word5.capitalize() + word6.capitalize())

print("String methods-center(width[,fillchar])")
print(text.center(60, "-"))

print("String methods-count(sub[,start[,end]])")
substring = "o"
result = text.count(substring)
print(result)
substring = "t"
count = text.count(substring, 3, 23)
print(count)



