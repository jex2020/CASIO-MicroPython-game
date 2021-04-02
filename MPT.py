import SAY
import MAP
import SPEAK
def out(c,x,y,f,name,n5,n6,n7,n8,n9,k,bn0,bn1,bn2,bn3,bn4,hp,sen,exp):
  n0=n1=n2=n3=n4=0
  if c=="b":
    k=1
  if c=="m":
    k=2
  if x in [10,11,12]:
    if y in [-13,-14,-15]:
      if c=="5":
        f=2
        n5=17
        n6=18
        n7=20
        n9=19
      name="Ven"
  if x in [12,13,14]:
    if y in [15,16,17]:
      if c=="5":
        f=1
        n5=17
        n6=18
      name="Gai"
  if x in [-20,-19]:
    if y in [-14,-15,-16]:
      if c=="5":
        f=1
        n5=17
        n6=18
      name="Jen"
  if x in [-19,-18,-17]:
    if y in [13,14,15]:
      if c=="5":
        f=1
        n5=17
        n6=18
      name="Kive"
  if x in [4,5,6]:
    if y in [2,3,4]:
      if c=="5":
        n5=f=1
        n6=10
        n9=11
      name="Lun"  
  if x in [7,8,9]:
    if y in [4,5]:
      if c=="5":
        n5=3
        n6=8
        n7=4
        n8=5
        f=2
      name="Mode      "
  say5=SAY.say(n5)
  say6=SAY.say(n6)
  say7=SAY.say(n7)
  say8=SAY.say(n8)
  say9=SAY.say(n9)
  z=MAP.out(x,y,name,n0,n1,n2,n3,n4,k,bn0,bn1,bn2,bn3,bn4,hp,sen,exp)
  SPEAK.out(f,say5,say6,say7,say8,say9)
  return z