0: mov x0 dat
  tcp dat -1
- jmp 9
+ dst x0 dat
+ mov acc x1
  mov 0 x3
+ slp 1
+ tgt x2 100
  slp 1
  jmp 0
9: tgt x2 4
+ mov 0 acc
+ mov acc x1
  slp 1