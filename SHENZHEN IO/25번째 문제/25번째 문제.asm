  slx x0
  mov x0 acc
  sub 1
  mul 7
  mov acc x1
  gen p0 7 0

  slx x2
  mov x2 acc
  teq acc 14
+ mov 11 x3
+ slp 7
+ jmp E
  mov acc x1
  mov 7 acc
L:mov x0 x3
  slp 1
  sub 1
  teq acc 0
- jmp L
E: mov 0 x3