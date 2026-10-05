@ mov 10 x1
@ nop
  tgt x1 10
+ mov x0 acc
  teq p1 100
+ tgt acc 0
+ sub 1
+ mov 1 x1
  slp 1