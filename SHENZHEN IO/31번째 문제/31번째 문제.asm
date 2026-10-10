  teq p0 0
- mov p1 acc
- mov p0 dat
  teq x2 1
- jmp E
  tgt dat 79
+ mov 100 x3
+ jmp E
  mov acc x1
  tlt dat 51
- mov x0 null
  mov x0 x3
E:slp 1

@ mov 50 p1
  teq x3 1
+ mov x3 acc
L:+mov x3 p1
+ mov 0 x1
+ sub 1
+ slp 1
+ tgt acc 0
+ jmp L
  mov 50 p1
- teq x3 x2
- mov 0 x1
+ mov 1 x1
  slp 1