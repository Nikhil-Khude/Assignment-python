#for count the vowels
sentence=input("enter sentence:")
#vowels
vowels="aeiou"
count=0
for char in sentence:
    if char in vowels:
        count+=1
print("number of vowels in the sentence:",count)