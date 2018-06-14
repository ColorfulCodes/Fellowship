def decode(s):
    hold = []
    count = []
    n = 0
    new_string = ''
    # place value s in between new brackets
    s = '1[{0}]'.format(s)
    for char in s:
      if char.isdigit():
        n = n*10 + ord(char)-ord('0')
      elif '[' == char:
        count.append(n)
        n = 0
        hold.append(new_string)
        new_string = ''
      elif ']' == char:
        new_string = hold.pop() + new_string*count.pop()
      else:
        new_string += char
    return new_string
    
decode("4[ab]")
