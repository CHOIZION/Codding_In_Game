@ add x0
@ add x1
@ mov acc dat
@ add x3
  teq p0 100
+ mov 0 x3
+ jmp E
  mov x0 x2
  mov dat x2
  mov acc x2
E:slp 1

@ mov x3 x1
  slx x1
  mov x1 x2

  teq p0 100
+ mov 0 acc
+ jmp B
  tlt acc x0
+ mov 100 x3
+ mov x0 null
+ jmp A
  tlt acc x0
+ mov 10 x3
- mov 1 x3
A:add 1
  teq acc x0
+ mov 0 acc
B:slp 1