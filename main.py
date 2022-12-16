picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for pix_row in picture:
  for pixel in pix_row:
    if (pixel == 1):
      print("*", end=' ' )
    else:
      print(' ',end=' ')
  print('')