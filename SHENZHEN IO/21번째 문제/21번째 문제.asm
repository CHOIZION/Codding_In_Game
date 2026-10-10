@ mov -999 dat
  mov p1 acc
  teq p0 100
- jmp A
  teq dat acc
+ mov -999 dat
+ mov -999 x3
- mov p1 dat
A:teq dat -999
- sub dat
- mov acc x3
  slp 1