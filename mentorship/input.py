# Inputs in python
print("Enter Values")
# inputs in variables

word = input("enter a word")
sentence = input("enter a sentence")
character = input("enter a character")
integer = int(input("enter an integer"))
dnum = float(input("enter a float"))

# Array input
first, second, third = input("enter three integers").split()
# Template
# varName = list( map( <dataType>, <iterable/list/tuple>))
arr = list(map(int, input("enter space seperated integers").split()))

print("Word: ", word)
print("Sentence ", sentence)
print("Character ", character)
print("Integer ", integer)
print("Float ", dnum)
print("Array: ", arr)


 