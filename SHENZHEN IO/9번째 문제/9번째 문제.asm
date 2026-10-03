  tcp  x0 -2
- jmp E
  mov p0 x1
  mov p1 x1
  tgt x3 9
- mov x3 x1
+ mov x3 acc
+ sub 8
+ mov acc x1
  slp 3
E: slp 1