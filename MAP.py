import MOVE
def out(x,y,name,n0,n1,n2,n3,n4,k,bn0,bn1,bn2,bn3,bn4,hp,sen,exp):
  if x in[0,1,2,3,4,5,6,7,8,9]:
    if y in[0,1,2,3,4,5]:#0
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      f3=i5="I"
      h2="S"
      d4="?"
      zoom=0
  if x in[0,1,2,3,4,5,6,7,8,9]:
    if y in[6,7,8,9,10,11]:#1
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      a3="?"
      zoom=1
  if x in[0,1,2,3,4,5,6,7,8,9]:
    if y in[-1,-2,-3,-4,-5,-6]:#2
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      f2="?"
      zoom=2    
  if x in[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]:
    if y in[0,1,2,3,4,5]:#3
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      g4="?"
      zoom=3
  if x in[10,11,12,13,14,15,16,17,18,19]:
    if y in[0,1,2,3,4,5]:#4
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      b4="?"
      zoom=4        
  if x in[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]:
    if y in[6,7,8,9,10,11]:#5
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      e1="?"
      zoom=5
  if x in[10,11,12,13,14,15,16,17,18,19]:
    if y in[6,7,8,9,10,11]:#6
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      d3="?"
      zoom=6    
  if x in[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]:
    if y in[-1,-2,-3,-4,-5,-6]:#7
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      a3="?"
      zoom=7
  if x in[10,11,12,13,14,15,16,17,18,19]:
    if y in[-1,-2,-3,-4,-5,-6]:#8
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      i2="?"
      zoom=8    
  if x in[0,1,2,3,4,5,6,7,8,9]:
    if y in[12,13,14,15,16,17]:#9
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      g3="?"
      zoom=9
  if x in[0,1,2,3,4,5,6,7,8,9]:
    if y in[-7,-8,-9,-10,-11,-12]:#10
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      b4="?"
      zoom=10
  if x in[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]:
    if y in[12,13,14,15,16,17]:#11
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      b1="?"
      zoom=11
  if x in[10,11,12,13,14,15,16,17,18,19]:
    if y in[12,13,14,15,16,17]:#12
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      h1="?"
      d4="I"
      zoom=12
  if x in[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]:
    if y in[-7,-8,-9,-10,-11,-12]:#13
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      f3="?"
      zoom=13
  if x in[10,11,12,13,14,15,16,17,18,19]:
    if y in[-7,-8,-9,-10,-11,-12]:#14
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      e3="?"
      zoom=14
  if x in[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]:
    if y in[12,13,14,15,16,17]:#15
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      a5="?"
      c2="I"
      zoom=15
  if x in[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]:
    if y in[6,7,8,9,10,11]:#16
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      f4="?"
      zoom=16
  if x in[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]:
    if y in[0,1,2,3,4,5]:#17
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      g2="?"
      zoom=17
  if x in[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]:
    if y in[-1,-2,-3,-4,-5,-6]:#18
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      c2="?"
      zoom=18
  if x in[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]:
    if y in[-7,-8,-9,-10,-11,-12]:#19
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      j2="?"
      zoom=19
  if x in[-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]:
    if y in[-13,-14,-15,-16,-17,-18]:#20
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      e4="?"
      a3="I"
      zoom=20
  if x in[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]:
    if y in[-13,-14,-15,-16,-17,-18]:#21
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      i4="?"
      zoom=21
  if x in[0,1,2,3,4,5,6,7,8,9]:
    if y in[-13,-14,-15,-16,-17,-18]:#22
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      g4="?"
      zoom=22
  if x in[10,11,12,13,14,15,16,17,18,19]:
    if y in[-13,-14,-15,-16,-17,-18]:#23
      a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6="O"
      g2="?"
      b4="I"
      zoom=23   
  if bn0==11:
    a0=a1=a2=a3=a4=a5=a6=b0=b1=b2=b3=b4=b5=b6=c0=c1=c2=c3=c4=c5=c6=d0=d1=d2=d3=d4=d5=d6=e0=e1=e2=e3=e4=e5=e6=f0=f1=f2=f3=f4=f5=f6=g0=g1=g2=g3=g4=g5=g6=h0=h1=h2=h3=h4=h5=h6=i0=i1=i2=i3=i4=i5=i6=j0=j1=j2=j3=j4=j5=j6=k0=k1=k2=k3=k4=k5=k6=" "
    b3="Y"
    c3="o"
    d3="u"
    f3="a"
    g3="r"
    h3="e"
    d1="w"
    e1="i"
    f1="n"
    g1="!"
    zoom=24
  z=MOVE.out(zoom,x,y,a0,a1,a2,a3,a4,a5,b0,b1,b2,b3,b4,b5,c0,c1,c2,c3,c4,c5,d0,d1,d2,d3,d4,d5,e0,e1,e2,e3,e4,e5,f0,f1,f2,f3,f4,f5,g0,g1,g2,g3,g4,g5,h0,h1,h2,h3,h4,h5,i0,i1,i2,i3,i4,i5,j0,j1,j2,j3,j4,j5,name,n0,n1,n2,n3,n4,k,bn0,bn1,bn2,bn3,bn4,hp,sen,exp)
  return z