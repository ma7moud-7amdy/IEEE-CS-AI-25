import string

myfile = open("simple_text.txt" , "r")
if(myfile.readable()):
    text = myfile.read()
myfile.close()
text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
words = text.split()  # Split into words
charDict = dict()
for word in words:
    if word in charDict:
        charDict[word]+=1
    else:
        charDict[word] = 1
# print the result
for word in charDict:
    print(f"{word} = {charDict[word]}")