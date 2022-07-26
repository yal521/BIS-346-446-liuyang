alphabet='abcdefghijklmnopqrstuvwxyz'

#a :First half of the string using starting and ending indices
firsthalf=int(len(alphabet)//2)
print(alphabet[0:firsthalf])

#b: First half of the string using only the ending indices
print(alphabet[:len(alphabet) // 2])

#c: The second half of the string using starting and ending indices
lastitem=len(alphabet)
print(alphabet[firsthalf:lastitem])

#d: The second half of the string using only the starting indices
print(alphabet[firsthalf:])

#e: Every second letter of the string starting with 'a'
print(alphabet[::2])

#f:The entire string in reverse
print(alphabet[::-1])

#g Every third letter of the string in reverse starting with 'z'
reverse=alphabet[::-1]
print(reverse[::3])

