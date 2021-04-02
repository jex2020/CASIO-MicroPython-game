def out(c,s,x):        
  if c=="7":
    x=x-s
  if c=="9":
    x=x+s
  if c=="1":
    x=x-s
  if c=="3":
    x=x+s
  if c=="4":
    x=x-s
  if c=="6":
    x=x+s
  if x>19:
    x=x-s 
  if x<-20:
    x=x+s
  return x