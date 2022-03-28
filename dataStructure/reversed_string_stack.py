# As a part of this class reverse a string using stack
import stack

string = "imhsar ssim olleh"
reversed_string_stack = ""
s = stack.Stack()
# your code goes here
for char in string:
    s.push(char)

while not s.is_empty():
    reversed_string_stack += s.pop(char)

print(reversed_string_stack)
