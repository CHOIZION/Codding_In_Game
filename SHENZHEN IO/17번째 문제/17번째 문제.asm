@ mov 50 p1
  slx x1
  mov x1 dat
L:tcp dat acc
+ add 1
- sub 1
+ gen p1 1 0
- gen p1 0 1
  mov 50 p1
+ slp 1
- slp 1
+ jmp L
- jmp L
  mov 0 x1

S:slp 1
  mov x0 acc
  tlt acc 0
+ jmp S
  mov acc x1
  mov x0 acc
  mov x0 dat
  slx x1
  mov x1 null
  gen p1 acc 0
  gen p0 dat 0