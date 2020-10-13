def downshift(a,index,n):
 col = []
 for j in range(len(a)):
  col.append(a[j][index])
 shiftCol = numpy.roll(col,n)
 for i in range(len(a)):
  for j in range(len(a[0])):
   if(j==index):
    a[i][j] = shiftCol[i]