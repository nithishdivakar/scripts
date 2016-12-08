print('''\documentclass{standalone}
\\usepackage{tikz}
\\begin{document}
\\begin{tikzpicture}[xscale=1,yscale=1]
''')


L = 1 # left offset
H = 1 # height offset
l = 28*0.66 # length of ruler
h = 2*0.66 # height of ruler



line = '''\draw  ({:2.2f},{:2.2f}) --  ({:2.2f},{:2.2f});'''


spl = '''\draw  [fill=black,text=white] ({:2.2f},{:2.2f}) rectangle ({:2.2f},{:2.2f}) node[pos=.5] {{BED}};'''
nig = '''\draw  [fill=black,text=white] ({:2.2f},{:2.2f}) rectangle ({:2.2f},{:2.2f}) node[pos=.5] {{NIGHT}};'''
node = '''\\node at ({:2.2f},{:2.2f}) {{{}}};'''
rectangle = '''\draw   ({:2.2f},{:2.2f}) rectangle ({:2.2f},{:2.2f});'''

sleep_offset = 10


sleep = [(0,4),(14,18),(28,32),(42,46),(56,60),(70,74)]


sleep_offset=sleep_offset/2.0

for i in range(len(sleep)):
  r = sleep[i]
  r = (r[0]+sleep_offset,r[1]+sleep_offset)
  sleep[i] = r
  

night = [(0,3),(9,15),(21,27),(33,39),(45,51),(57,63),(69,75),(81,84)]

print(rectangle.format(0,0,l+L+L,h+H+H))
print(rectangle.format(L,H,L+l,H+h))
print("\n")

f = (l)/(7*12)

for i in range(7*12+1):
  if i%12 == 0:
    print(line.format(L+i*f,H+1.0*h,L+i*f,H+0.0*h))
  elif i%6 == 0:
    print("\t"+line.format(L+i*f,H+1.0*h,L+i*f,H+0.7*h))
  else:
    print("\t\t"+line.format(L+i*f,H+1.0*h,L+i*f,H+0.8*h))

print("\n")

for s in sleep:
  print(spl.format(L+s[0]*f,H+0.7*h,L+s[1]*f,H+0.35*h))
  
print("\n")

for n in night:
  print(nig.format(L+n[0]*f,H+0.0*h,L+n[1]*f,H+0.35*h))
  
print("\n")

for s in sleep:
  print(line.format(L+s[0]*f,H+0.75*h,L+s[0]*f,H+1.1*h))
  t = (s[0]*2)%24
  if t>12:
    print(node.format(L+s[0]*f,H+1.25*h,"\small "+str(int(t%12))+"PM"))
  else:
    print(node.format(L+s[0]*f,H+1.25*h,"\small "+str(int(t))+"AM"))
  
  print(line.format(L+s[1]*f,H+0.75*h,L+s[1]*f,H+1.1*h))
  t = (s[1]*2)%24
  if t>12:
    print(node.format(L+s[1]*f,H+1.25*h,"\small "+str(int(t%12))+"PM"))
  else:
    print(node.format(L+s[1]*f,H+1.25*h,"\small "+str(int(t))+"AM"))
  print()
  
print("\n")
for day, day_name in enumerate(['MON', 'TUE', 'WED','THU','FRI','SAT','SUN']):
  print(node.format(L+(day*12+6)*f,H/2,day_name))
  
print('''\end{tikzpicture}
\end{document}''')
