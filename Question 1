def check(s,t):
  order = {}
  order2 = {}
  new_string = ""
  misc = ""
  p = 0

  for i,c in enumerate(t):
    order[c] = i

  # iterate through order
  
  for char in s:
      if char in order2:
          order2[char] +=1
      else:
          order2[char] = 1
          if char not in order:
              misc += char
              
  order = sorted(order.items(), key=lambda x: x[1])
          
  while p < len(order):
      if order[p][0] in order2:
          new_string += order[p][0] * order2[order[p][0]]
          p += 1
  
    
  return new_string + misc




check("swtgsarsu","rats")
