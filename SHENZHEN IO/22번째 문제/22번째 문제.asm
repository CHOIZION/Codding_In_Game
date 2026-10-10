  mov x1 acc
  mov acc x0
  tgt acc -1
- jmp E
  mov acc x2
L:mov x1 x2
  teq x3 8
- jmp L
E:slp 1

  teq x0 -1
+ mov 0 x2
+ mov acc x3
+ mov 0 acc
S:teq x1 0
+ jmp E
  teq x1 1
+ add 20
  teq x1 10
+ add 50
  teq x1 100
+ add 100
E:slp 1

  slx x1
  mov x1 acc
  mov 0 x3
L:mov x0 x2
  teq x3 8
- jmp L
  mov acc x2