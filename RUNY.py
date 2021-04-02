def out(c,s,y):      
  if c=="7":
    y=y+s
  if c=="9":
    y=y+s
  if c=="1":
    y=y-s
  if c=="3":
    y=y-s      
  if c=="8":
    y=y+s
  if c=="2":
    y=y-s
  if y>17:
    y=y-s
  if y<-18:
    y=y+s
  return y  