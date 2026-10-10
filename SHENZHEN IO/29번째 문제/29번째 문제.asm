  teq p1 0
- mov p0 acc
- dgt 1
- mov acc dat
- mov dat x3
- mov x2 acc
- add 1
- mov dat x3
- mov acc x2
- jmp 9
  tgt dat 0
+ mov 2 x1
+ mov 0 dat
9: slp 1

  slx x2
  mov 0 x0
0: teq x0 9
- mov 0 x1
- jmp 0

  slx x3
  mov x3 x1
  mov x0 acc
  add x0
0:mov x1 dat
  tgt x0 acc
+ mov 0 x1
+ mov dat x0
+ mov dat x1
+ mov x0 acc
  teq x1 9
- jmp 0
  mov 0 x1
  mov x0 x2

@ mov 50 p0
@ mov 50 p1
  slx x2
  mov x2 acc
  teq acc 0
+ add 2
  mul 2
  mov acc x1
  mov x0 p1
  mov x0 p0