  teq x0 0
+ jmp end
  teq x0 1
+ mov 1 x3
  teq x0 10
+ mov 5 x3
  teq x0 100
+ mov 12 x3
end: slp 1

  slx x0
  add x0
  tlt acc x1
- sub x1
- mov acc x3
- mov 0 acc
- gen p1 4 0
  slp 1

end: slx x1
  mov x1 acc
loop: teq acc 0
+ jmp end
  tgt acc 4
+ sub 5
+ mov 10 x3
- sub 1
- mov 1 x3
  slp 1
  mov 0 x3
  slp 1
  jmp loop