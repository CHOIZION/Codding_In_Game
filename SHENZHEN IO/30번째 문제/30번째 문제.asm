  slx x0
  mov x0 acc
  mul 2
  mov acc x3
  mov acc x2

  slx x3
1:  mov x0 x2
  slp x0
  teq x1 6
+ jmp 1
  mov 0 x2

  slx x3
  mov x3 x1
  mov x0 x2
  slp x0
  mov 0 x2