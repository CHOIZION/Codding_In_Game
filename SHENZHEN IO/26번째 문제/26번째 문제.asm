  slx x0
  teq p0 100
+ jmp E
  mov 0 x3
  mov 0 acc
L:mov x0 dat
  teq dat 9
- dst 0 1
  teq dat x2
- dst 1 1
  teq x3 10
- jmp L
E:mov acc x1
  slp 1

S:slx x0
  teq p0 100
+ mov null x1
  mov x0 acc
+ jmp S
  teq acc 11
- gen p1 6 0

  slx x2
  mov x2 null
  mov 0 x1
L:mov x3 x0
  teq x1 10
- jmp L