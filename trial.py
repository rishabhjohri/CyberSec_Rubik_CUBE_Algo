import numpy
def upshift(a,index,n):#upshift(r, i, Kc[i])
 col = []
 for j in range(len(a)):
  col.append(a[j][index])
 shiftCol = numpy.roll(col,-n)
 for i in range(len(a)):
  for j in range(len(a[0])):
   if(j==index):
    a[i][j] = shiftCol[i]
  print(a)

a=[[1,2,3],[4,5,6],[7,8,9]]
upshift(a,0,-1)

def rotate180(n):
 bits = "{0:b}".format(n)
 return((bits[::-1], 2))
x=[]
k=[12,2,3]
x.append(rotate180(k[0]))
x.append(rotate180(k[1]))
x.append(rotate180(k[2]))
print(x)