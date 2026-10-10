  slx x1
  mov x1 dat
  mov x0 acc
  mov x3 null
  mov x3 null
L:teq dat 1
- mov x3 null
  mov x3 x2
+ mov x3 null
  teq x0 acc
- jmp L

  mov p1 x2
  mov p0 x2
  teq x3 x1
+ mov x3 x0
  slp 1