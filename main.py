import RUNX
import RUNY
import MPT
hp=5
sen=5
s=z=1
exp=o0=o1=o2=o3=o4=o5=o6=o7=o8=o9=o10=o11=o12=o13=o14=o15=o16=o17=o18=o19=o20=o21=o22=o23=bn0=bn1=bn2=bn3=bn4=f=n=x=y=c=0
while z!=0:
  name=""
  n5=n6=n7=n8=n9=k=f=0
  c=input("$:")             
  if sen<0:
    z=hp=z-1
  if c=="*":
    if s==1:
      s=2
    elif s==2:
      s=1    
  if c=="+":
    if bn1>0:
      if bn2>0:
        if sen<25:
          sen=sen+2
          bn1=bn1-1
          bn2=bn2-1
  x=RUNX.out(c,s,x)
  y=RUNY.out(c,s,y)    
  if x==7:
    if y==2:
      name="SHOP"
      if c=="5":
        v=input("20kb=>1EXE y/n:")
        if v=="y":
          if bn4>=20:
            bn4=bn4-20
            bn2=bn2+1     
  if x==13:
    if y==9:
      if c=="5":
        name="BUG"
        n5=6
        f=1
        if o1==0:
          sen=sen-1
          exp=exp+5
          bn0=bn0+1
          bn4=bn4+5
          o1=1
  if x==3:
    if y==4:
      if c=="5":
        name="BUG"
        n5=6
        f=1
        if o0==0:
          sen=sen-1
          exp=exp+5
          bn0=bn0+1
          bn4=bn4+5
          o0=1
  if x==17:
    if y==13:
      if c=="5":
        name="BUG"
        n5=6
        f=1
        if o5==0:
          sen=sen-1
          exp=exp+5
          bn0=bn0+1
          bn4=bn4+5
          o5=1
  if x==-6:
    if y==7:
      if c=="5":
        name="BUG"
        n5=6
        f=1
        if o6==0:
          sen=sen-1
          exp=exp+5
          bn0=bn0+1
          bn4=bn4+5
          o6=1        
  if x==11:
    if y==4:
      if c=="5":
        name="BUG"
        n5=6
        f=1
        if o9==0:
          sen=sen-1
          exp=exp+5
          bn0=bn0+1
          bn4=bn4+5
          o9=1
  if x==-5:
    if y==-9:
      if c=="5":
        name="BUG"
        n5=6
        f=1
        if o12==0:
          sen=sen-1
          exp=exp+5
          bn0=bn0+1
          bn4=bn4+5
          o12=1
  if x==1:
    if y==-8:
      if c=="5":
        name="BUG"
        n5=6
        f=1
        if o13==0:
          sen=sen-1
          exp=exp+5
          bn0=bn0+1
          bn4=bn4+5
          o13=1
  if x==14:
    if y==-9:
      if c=="5":
        name="BUG"
        n5=6
        f=1
        if o14==0:
          sen=sen-1
          exp=exp+5
          bn0=bn0+1
          bn4=bn4+5
          o14=1
  if x==-15:
    if y==10:
      if c=="5":
        name="BUG"
        n5=6
        f=1
        if o19==0:
          sen=sen-1
          exp=exp+5
          bn0=bn0+1
          bn4=bn4+5
          o19=1
  if x==-14:
    if y==2:
      if c=="5":
        name="BUG"
        n5=6
        f=1
        if o20==0:
          sen=sen-1
          exp=exp+5
          bn0=bn0+1
          bn4=bn4+5
          o20=1
  if x==-11:
    if y==-10:
      if c=="5":
        name="BUG"
        n5=6
        f=1
        if o22==0:
          sen=sen-1
          exp=exp+5
          bn0=bn0+1
          bn4=bn4+5
          o22=1
  if x==5:
    if y==-4:
      if c=="5":
        name="EXE"
        n5=7
        f=1
        if o2==0:
          exp=exp+10
          bn2=bn2+1
          bn4=bn4+5
          o2=1
  if x==0:
    if y==9:
      if c=="5":
        name="EXE"
        n5=7
        f=1
        if o7==0:
          exp=exp+10
          bn2=bn2+1
          bn4=bn4+5
          o7=1          
  if x==-10:
    if y==-3:
      if c=="5":
        name="EXE"
        n5=7
        f=1
        if o10==0:
          exp=exp+10
          bn2=bn2+1
          bn4=bn4+5
          o10=1
  if x==18:
    if y==-4:
      if c=="5":
        name="EXE"
        n5=7
        f=1
        if o11==0:
          exp=exp+10
          bn2=bn2+1
          bn4=bn4+5
          o11=1
  if x==-18:
    if y==-4:
      if c=="5":
        name="EXE"
        n5=7
        f=1
        if o21==0:
          exp=exp+10
          bn2=bn2+1
          bn4=bn4+5
          o21=1
  if x==-9:
    if y==13:
      name="KEY"
      if c=="5":
        n5=9
        f=1
        if o3==0:
          bn1=bn1+1
          o3=1        
  if x==6:
    if y==15:
      name="KEY"
      if c=="5":
        n5=9
        f=1
        if o4==0:
          bn1=bn1+1
          o4=1        
  if x==-4:
    if y==4:
      name="KEY"
      if c=="5":
        n5=9
        f=1
        if o8==0:
          bn1=bn1+1
          o8=1        
  if x==-2:
    if y==-14:
      name="KEY"
      if c=="5":
        n5=9
        f=1
        if o15==0:
          bn1=bn1+1
          o15=1        
  if x==6:
    if y==-14:
      name="KEY"
      if c=="5":
        n5=9
        f=1
        if o16==0:
          bn1=bn1+1
          o16=1        
  if x==16:
    if y==-16:
      name="KEY"
      if c=="5":
        n5=9
        f=1
        if o17==0:
          bn1=bn1+1
          o17=1        
  if x==-20:
    if y==17:
      name="KEY"
      if c=="5":
        n5=9
        f=1
        if o18==0:
          bn1=bn1+1
          o18=1        
  if x==-16:
    if y==-14:
      name="KEY"
      if c=="5":
        n5=9
        f=1
        if o23==0:
          bn1=bn1+1
          o23=1        
  bn3=bn2+bn1
  z=MPT.out(c,x,y,f,name,n5,n6,n7,n8,n9,k,bn0,bn1,bn2,bn3,bn4,hp,sen,exp)
print("You are lost!")