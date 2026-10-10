1:  slx x3
  mov x3 dat
2: tcp x0 dat
- jmp 2
+ jmp 3
  mov x1 acc
  add 6
  mov acc x1
3: teq x0 x2
+ add 50
- mov 0 acc
  mov 0 x1
  mov acc x3	

  teq x2 100
+ sub acc
- mov x1 dat
- teq dat -999
+ jmp 9
  mov dat x0
  slx x0
  add x0 
9:  tgt acc 50
+ mov 50 p1
- mov p0 p1
  slp 1