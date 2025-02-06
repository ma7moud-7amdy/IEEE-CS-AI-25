#  Write a Python program that checks if a given word is a palindrome. 
# A palindrome is a word that reads the same backward as forward.
# Input: "level"
# Output: "The word 'level' is a palindrome."
# Input: "python"
# Output: "The word 'python' is not a palindrome."

word = input()
reversedWord = word[::-1]
if word == reversedWord:
    print("The word '",word,"' is a palindrome." , sep="")
else:
    print("The word '",word,"' is not a palindrome.", sep="")