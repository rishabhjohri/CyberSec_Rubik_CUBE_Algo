def rotate180(n):
 bits = "{0:b}".format(n)
 return int(bits[::-1], 2)
