S:teq p0 0
+ slp 1
+ jmp S
  slp 3
  mov 0 acc
  teq p1 0
- dst 0 1
  slp 1
  teq p1 0
- dst 1 1
  slp 1
  teq p1 0
- dst 2 1
  mov acc x2

S:teq p0 0
+ slp 1
+ jmp S
  mov 0 acc
  teq p1 0
- dst 0 1
  slp 1
  teq p1 0
- dst 1 1
  slp 1
  teq p1 0
- dst 2 1
  slp 3
  mov acc x3