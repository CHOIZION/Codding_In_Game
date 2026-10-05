  mov x0 acc
  teq acc -999
- mov x0 x1
- mov x0 p0
- mov acc p1
- slx x1
- teq x1 0
- mov p0 p1
  slp 1

  slx x1
  mov x1 p1
  nop
  mov x0 acc
  teq acc 999
+ mov 0 x1
- slp acc
- mov 1 x1
- mov p1 p1