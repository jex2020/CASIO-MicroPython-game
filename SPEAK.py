def out(f,say5,say6,say7,say8,say9):
  if f==1:
    print(say5,end="")
    print(say6,end="")
    print(say9)
  elif f==2:
    print(say5,end="")
    print(say6)
    print(say9)
    a=input("$:")
    if a=="1":
      print(say7)
    elif a=="2":
      print(say8)  