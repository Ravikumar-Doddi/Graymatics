def is_valid(string):
  stack = []
  for char in string:
    stack_length = len(stack)
    if char in ['(', '{', '[']:
      stack.append(char)
    elif char in [')', '}', ']']:
      if stack_length == 0:
        return False
      if char == ')' and stack[-1] == '(':
        stack.pop()
      elif char == '}' and stack[-1] == '{':
        stack.pop()
      elif char == ']' and stack[-1] == '[':
        stack.pop()
      else:
        return False
  
  if stack_length != 0:
        return True

print(is_valid("( ) [ ] { }"))  
print(is_valid("] ( ) ["))  
print(is_valid("{ { [] ( } } )"))  
print(is_valid("{ [ ( ) ] }")) 

