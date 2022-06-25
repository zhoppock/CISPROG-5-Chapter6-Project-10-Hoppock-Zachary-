def myRange(param1, param2=None, param3=None):
  myList = []
  if param2 == None and param3 == None:
    start = 0
    end = param1
    step = 1
  elif param3 == None:
    start = param1
    end = param2
    step = 1
  else:
    start = param1
    end = param2
    step = param3

  if step > 0:
    temp = start;
    while temp < end:
      myList.append(temp)
      temp += step
  else:
    temp = end;
    while temp > start:
      myList.append(temp)
      temp += step
  return myList

def main():
  print(myRange(4))
  print(myRange(4, 16))
  print(myRange(4,16,4))
  print(myRange(4,16,-4))