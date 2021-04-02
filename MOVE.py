import SAY
def out(zoom,x,y,a0,a1,a2,a3,a4,a5,b0,b1,b2,b3,b4,b5,c0,c1,c2,c3,c4,c5,d0,d1,d2,d3,d4,d5,e0,e1,e2,e3,e4,e5,f0,f1,f2,f3,f4,f5,g0,g1,g2,g3,g4,g5,h0,h1,h2,h3,h4,h5,i0,i1,i2,i3,i4,i5,j0,j1,j2,j3,j4,j5,name,n0,n1,n2,n3,n4,k,bn0,bn1,bn2,bn3,bn4,hp,sen,exp):
  if hp==5:
    n2=16
  if hp==4:
    n2=15
  if hp==3:
    n2=14  
  if hp==2:
    n2=13      
  if hp==1:
    n2=12
  if hp==0:
    n2=0            
  if sen>=5:
    n3=16
  if sen==4:
    n3=15
  if sen==3:
    n3=14      
  if sen==2:
    n3=13      
  if sen==1:
    n3=12
  if sen==0:
    n3=0             
  say0=SAY.say(n0)    
  say1=SAY.say(n1)    
  say2=SAY.say(n2)    
  say3=SAY.say(n3)    
  say4=SAY.say(n4)    
  if y in[0,6,-6,12,-12,-18]:
    if x in[0,10,-10,-20]:
      a0="*"
    if x in[1,11,-9,-19]:
      b0="*"
    if x in[2,12,-8,-18]:
      c0="*"
    if x in[3,13,-7,-17]:
      d0="*"
    if x in[4,14,-6,-16]:
      e0="*"
    if x in[5,15,-5,-15]:
      f0="*"
    if x in[6,16,-4,-14]:
      g0="*"
    if x in[7,17,-3,-13]:
      h0="*"
    if x in[8,18,-2,-12]:
      i0="*"
    if x in[9,19,-1,-11]:
      j0="*"  
  if y in[1,7,-5,13,-11,-17]:
    if x in[0,10,-10,-20]:
      a1="*"
    if x in[1,11,-9,-19]:
      b1="*"
    if x in[2,12,-8,-18]:
      c1="*"
    if x in[3,13,-7,-17]:
      d1="*"
    if x in[4,14,-6,-16]:
      e1="*"
    if x in[5,15,-5,-15]:
      f1="*"
    if x in[6,16,-4,-14]:
      g1="*"
    if x in[7,17,-3,-13]:
      h1="*"
    if x in[8,18,-2,-12]:
      i1="*"
    if x in[9,19,-1,-11]:
      j1="*"  
  if y in[2,8,-4,14,-10,-16]:
    if x in[0,10,-10,-20]:
      a2="*"
    if x in[1,11,-9,-19]:
      b2="*"
    if x in[2,12,-8,-18]:
      c2="*"
    if x in[3,13,-7,-17]:
      d2="*"
    if x in[4,14,-6,-16]:
      e2="*"
    if x in[5,15,-5,-15]:
      f2="*"
    if x in[6,16,-4,-14]:
      g2="*"
    if x in[7,17,-3,-13]:
      h2="*"
    if x in[8,18,-2,-12]:
      i2="*"
    if x in[9,19,-1,-11]:
      j2="*"  
  if y in[3,9,-3,15,-9,-15]:
    if x in[0,10,-10,-20]:
      a3="*"
    if x in[1,11,-9,-19]:
      b3="*"
    if x in[2,12,-8,-18]:
      c3="*"
    if x in[3,13,-7,-17]:
      d3="*"
    if x in[4,14,-6,-16]:
      e3="*"
    if x in[5,15,-5,-15]:
      f3="*"
    if x in[6,16,-4,-14]:
      g3="*"
    if x in[7,17,-3,-13]:
      h3="*"
    if x in[8,18,-2,-12]:
      i3="*"
    if x in[9,19,-1,-11]:
      j3="*"  
  if y in[4,10,-2,16,-8,-14]:
    if x in[0,10,-10,-20]:
      a4="*"
    if x in[1,11,-9,-19]:
      b4="*"
    if x in[2,12,-8,-18]:
      c4="*"
    if x in[3,13,-7,-17]:
      d4="*"
    if x in[4,14,-6,-16]:
      e4="*"
    if x in[5,15,-5,-15]:
      f4="*"
    if x in[6,16,-4,-14]:
      g4="*"
    if x in[7,17,-3,-13]:
      h4="*"
    if x in[8,18,-2,-12]:
      i4="*"
    if x in[9,19,-1,-11]:
      j4="*" 
  if y in[5,11,-1,17,-7,-13]:
    if x in[0,10,-10,-20]:
      a5="*"
    if x in[1,11,-9,-19]:
      b5="*"
    if x in[2,12,-8,-18]:
      c5="*"
    if x in[3,13,-7,-17]:
      d5="*"
    if x in[4,14,-6,-16]:
      e5="*"
    if x in[5,15,-5,-15]:
      f5="*"
    if x in[6,16,-4,-14]:
      g5="*"
    if x in[7,17,-3,-13]:
      h5="*"
    if x in[8,18,-2,-12]:
      i5="*"
    if x in[9,19,-1,-11]:
      j5="*"  
  print(a5,end="")
  print(b5,end="")
  print(c5,end="")
  print(d5,end="")
  print(e5,end="")
  print(f5,end="")
  print(g5,end="")
  print(h5,end="")
  print(i5,end="")
  print(j5,"X=",end="")
  print(x,"Y=",end="")
  print(y)
  print(a4,end="")
  print(b4,end="")
  print(c4,end="")
  print(d4,end="")
  print(e4,end="")
  print(f4,end="")
  print(g4,end="")
  print(h4,end="")
  print(i4,end="")
  print(j4,say0,end="")
  print("Z=",end="")
  print(zoom,"BUG",end="")
  print(bn0)
  print(a3,end="")
  print(b3,end="")
  print(c3,end="")
  print(d3,end="")
  print(e3,end="")
  print(f3,end="")
  print(g3,end="")
  print(h3,end="")
  print(i3,end="")
  print(j3,name,say1)
  print(a2,end="")
  print(b2,end="")
  print(c2,end="")
  print(d2,end="")
  print(e2,end="")
  print(f2,end="")
  print(g2,end="")
  print(h2,end="")
  print(i2,end="")
  print(j2,"HP: ",end="")
  print(say2)
  print(a1,end="")
  print(b1,end="")
  print(c1,end="")
  print(d1,end="")
  print(e1,end="")
  print(f1,end="")
  print(g1,end="")
  print(h1,end="")
  print(i1,end="")
  print(j1,"SEN:",end="")
  print(say3)
  print(a0,end="")
  print(b0,end="")
  print(c0,end="")
  print(d0,end="")
  print(e0,end="")
  print(f0,end="")
  print(g0,end="")
  print(h0,end="")
  print(i0,end="")
  print(j0,"EXP:",end="")
  print(exp,say4)
  if k==1:
    print("Base memory")
    print("data:",bn4,end="")
    print("kb")
    print("bug: ",bn0)
    print("key: ",bn1)
    print("EXE: ",bn2)
    print("file:",bn3,end="")
    print("/10")
  if k==2:
    print("Map",end="")
    print("       15|11|09|12")
    print("Now=Z     16|05|01|06")
    print("          17|03|00|04")
    print("          18|07|02|08")
    print("          19|19|10|14")
    print("          20|21|22|23")
  return hp  