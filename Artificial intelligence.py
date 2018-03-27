# -*- coding: cp1256 -*-
import random
print ("  1  |  2  |  3   |   4 ")
print ("  5  |  6  |  7   |   8 ")
print ("  9  | 10  | 11   |  12 ")
print (" 13  | 14  | 15   |  16 ")
print
print
i=1
y1=0
y2=0
temp1=0
temp2=0
temp3=0
temp4=0
temp5=0
temp6=0
temp7=0
temp8=0
temp9=0
temp10=0
temp11=0
temp12=0
temp13=0
temp14=0
temp15=0
#                  
#the first round
x1=int(input(" player 1    :   "))
x2=int(input(" player 1(2) :   "))
if(x1>16 or x1<1 or x2>16 or x2<1 or x1==temp1 or x1==temp2 or x1==temp3 or x1==temp4 or x2==temp1 or x2==temp2 or x2==temp3 or x2==temp4 or x1==x2):
   print ("wrong number , player 1 gotta choose again")
   x1=int(input(" player 1    :   "))
   x2=int(input(" player 1(2) :   "))
   if(x1>16 or x1<1 or x2>16 or x2<1 or x1==temp1 or x1==temp2 or x1==temp3 or x1==temp4 or x2==temp1 or x2==temp2 or x2==temp3 or x2==temp4 or x1==x2):
      print ("wrong number , player 1 gotta choose again")
      x1=int(input(" player 1    :   "))
      x2=int(input(" player 1(2) :   "))
      if(x1>16 or x1<1 or x2>16 or x2 <1 or x1==temp1 or x1==temp2 or x1==temp3 or x1==temp4 or x2==temp1 or x2==temp2 or x2==temp3 or x2==temp4 or x1==x2):
           quit()
else :
   temp1=x1
   temp2=x2
   print
   x3 = random.randint(1,16)
   if (x3>16 or x3<1 or x3==temp1 or x3==temp2):
      x3 = random.randint(1,16)
      if (x3>16 or x3<1 or x3==temp1 or x3==temp2):
         x3 = random.randint(1,16)
   temp3=x3
   x4 = x3+1
   if (x4>16 or x4 <1  or x4==temp1 or x4==temp2 or x4==temp3 or x3==x4):
       x4=x3-4
       if (x4>16 or x4 <1  or x4==temp1 or x4==temp2 or x4==temp3 or x3==x4):
          x4 = x3-1
          if (x4>16 or x4 <1  or x4==temp1 or x4==temp2 or x4==temp3 or x3==x4):
            x4 = x3+4            
   temp4=x4
   print (' computer chooses : ',x3,' , ',x4,' ')
   if (x2==x1+4) or (x2==x1+1)or (x1==x2+1) or (x1==x2+4) :
        if (x1==4 and x2==5) or ( x1==5 and x2 ==4) or (x1==8 and x2==9) or (x1==9 and x2==8) or (x1==12 and x2==13) or (x1==13 and x2==12) :
           y1=y1
        else:
           y1+=1
   if (x4==x3+4) or ( x4==x3+1) or (x3==x4+1) or (x3==x4+4):
        if (x3==4 and x4==5) or ( x3==5 and x4 ==4) or (x3==8 and x4==9) or (x3==9 and x4==8) or (x3==12 and x4==13) or (x3==13 and x4==12) :
            y2=y2
        else :
            y2+=1
#                  
#the 2nd round
x1=int(input(" player 1    :   "))
x2=int(input(" player 1(2) :   "))
if  (x1>16 or x1<1 or x2>16 or x2 <1 or x1==temp1 or x1==temp2 or x1==temp3 or x1==temp4 or x2==temp1 or x2==temp2 or x2==temp3 or x2==temp4 or x1==x2):
   print ("wrong number , player 1 gotta choose again")
   x1=int(input(" player 1    :   "))
   x2=int(input(" player 1(2) :   "))
   if  (x1>16 or x1<1 or x2>16 or x2 <1 or x1==temp1 or x1==temp2 or x1==temp3 or x1==temp4 or x2==temp1 or x2==temp2 or x2==temp3 or x2==temp4 or x1==x2):
      print ("wrong number , player 1 gotta choose again")
      x1=int(input(" player 1    :   "))
      x2=int(input(" player 1(2) :   "))
      if  (x1>16 or x1<1 or x2>16 or x2 <1 or x1==temp1 or x1==temp2 or x1==temp3 or x1==temp4 or x2==temp1 or x2==temp2 or x2==temp3 or x2==temp4 or x1==x2):
           quit()
else :
   temp5=x1
   temp6=x2
   print
   x3 = random.randint(1,16)
   if  (x3>16 or x3<1 or x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6 ):
      x3 = random.randint(1,16)
      if  (x3>16 or x3<1 or x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6 ):
        x3 = random.randint(1,16)
        if  (x3>16 or x3<1 or x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6 ):
           x3 = random.randint(1,16)
           if  (x3>16 or x3<1 or x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6 ):
              x3 = random.randint(1,16)
              if  (x3>16 or x3<1 or x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6 ):
                x3 = random.randint(1,16)
                if  (x3>16 or x3<1 or x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6 ):
                  x3 = random.randint(1,16)
   temp7=x3
   x4 = x3+1
   if (x4>16 or x4 <1  or x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6 or x4==temp7 or x3==x4):
      x4=x3-4
      if (x4>16 or x4 <1  or x4==temp1 or x4==temp2 or x4==temp3 or x3==temp4 or x3==temp5 or x4==temp6 or x4==temp7 or x3==x4):
         x4 = x3-x
         if (x4>16 or x4 <1  or x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6 or x4==temp7 or x3==x4):
            x4 = x3+4    
   temp8=x4
   print (' computer chooses : ',x3,' , ',x4,' ')
   if (x2==x1+4) or (x2==x1+1)or (x1==x2+1) or (x1==x2+4) :
        if (x1==4 and x2==5) or ( x1==5 and x2 ==4) or (x1==8 and x2==9) or (x1==9 and x2==8) or (x1==12 and x2==13) or (x1==13 and x2==12) :
           y1=y1
        else:
           y1+=1
   if (x4==x3+4) or ( x4==x3+1) or (x3==x4+1) or (x3==x4+4):
        if (x3==4 and x4==5) or ( x3==5 and x4 ==4) or (x3==8 and x4==9) or (x3==9 and x4==8) or (x3==12 and x4==13) or (x3==13 and x4==12) :
            y2=y2
        else :
            y2+=1
#                  
#the 3rd round
x1=int(input(" player 1    :   "))
x2=int(input(" player 1(2) :   "))
if  (x1>16 or x1<1 or x2>16 or x2 <1 or x1==temp1 or x1==temp2 or x1==temp3 or x1==temp4 or x1==temp5 or x1==temp6 or x1==temp7 or x1==temp8 or x2==temp1 or x2==temp2 or x2==temp3 or x2==temp4 or x2==temp5 or x2==temp6 or x2==temp7 or x2==temp8 or x1==x2):
   print ("wrong number , player 1 gotta choose again")
   x1=int(input(" player 1    :   "))
   x2=int(input(" player 1(2) :   "))
   if  (x1>16 or x1<1 or x2>16 or x2 <1 or x1==temp1 or x1==temp2 or x1==temp3 or x1==temp4 or x1==temp5 or x1==temp6 or x1==temp7 or x1==temp8 or x2==temp1 or x2==temp2 or x2==temp3 or x2==temp4 or x2==temp5 or x2==temp6 or x2==temp7 or x2==temp8 or x1==x2):
      print ("wrong number , player 1 gotta choose again")
      x1=int(input(" player 1    :   "))
      x2=int(input(" player 1(2) :   "))
      if  (x1>16 or x1<1 or x2>16 or x2 <1 or x1==temp1 or x1==temp2 or x1==temp3 or x1==temp4 or x1==temp5 or x1==temp6 or x1==temp7 or x1==temp8 or x2==temp1 or x2==temp2 or x2==temp3 or x2==temp4 or x2==temp5 or x2==temp6 or x2==temp7 or x2==temp8 or x1==x2):
           quit()
else :
   temp9=x1
   temp10=x2
   print
   x3 = random.randint(1,16)
   if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6 or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10):
      x3 = random.randint(1,16)
      if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10):
       x3 = random.randint(1,16)
       if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10):
          x3 = random.randint(1,16)
          if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10):
            x3 = random.randint(1,16)
            if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10):
               x3 = random.randint(1,16)
               if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10):
                  x3 = random.randint(1,16)
                  if ( x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10):
                    x3 = random.randint(1,16)
                    if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10):
                      x3 = random.randint(1,16)
                      if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10):
                        x3 = random.randint(1,16)
                        if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10):
                           x3 = random.randint(1,16)
   temp11=x3
   x4 = x3+1
   if (x4>16 or x4 <1  or x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6 or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x3==x4):
      x4=x3-4
      if (x4>16 or x4 <1  or x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6 or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x3==x4):
         x4 = x3-1
         if (x4>16 or x4 <1  or x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6 or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x3==x4):
            x4 = x3+4   
   temp12=x4
   print (' computer chooses : ',x3,' , ',x4,' ')
   if (x2==x1+4) or (x2==x1+1)or (x1==x2+1) or (x1==x2+4) :
        if (x1==4 and x2==5) or ( x1==5 and x2 ==4) or (x1==8 and x2==9) or (x1==9 and x2==8) or (x1==12 and x2==13) or (x1==13 and x2==12) :
           y1=y1
        else:
           y1+=1
   if (x4==x3+4) or ( x4==x3+1) or (x3==x4+1) or (x3==x4+4):
        if (x3==4 and x4==5) or ( x3==5 and x4 ==4) or (x3==8 and x4==9) or (x3==9 and x4==8) or (x3==12 and x4==13) or (x3==13 and x4==12) :
            y2=y2
        else :
            y2+=1
#                  
#the fourth round
x1=int(input(" player 1    :   "))
x2=int(input(" player 1(2) :   "))
if(x1>16 or x1<1 or x2>16 or x2 <1 or x1==temp1 or x1==temp2 or x1==temp3 or x1==temp4 or x1==temp5 or x1==temp6 or x1==temp7 or x1==temp8 or x1==temp9 or x1==temp10 or x1==temp11 or x1==temp12 or x2==temp1 or x2==temp2 or x2==temp3 or x2==temp4 or x2==temp5 or x2==temp6 or x2==temp7 or x2==temp8 or x2==temp9 or x2==temp10 or x2==temp11 or x2==temp12 or x1==x2):
   print ("wrong number , player 1 gotta choose again")
   x1=int(input(" player 1    :   "))
   x2=int(input(" player 1(2) :   "))
   if  (x1>16 or x1<1 or x2>16 or x2 <1 or x1==temp1 or x1==temp2 or x1==temp3 or x1==temp4 or x1==temp5 or x1==temp6 or x1==temp7 or x1==temp8 or x1==temp9 or x1==temp10 or x1==temp11 or x1==temp12 or x2==temp1 or x2==temp2 or x2==temp3 or x2==temp4 or x2==temp5 or x2==temp6 or x2==temp7 or x2==temp8 or x2==temp9 or x2==temp10 or x2==temp11 or x2==temp12 or x1==x2):
      print ("wrong number , player 1 gotta choose again")
      x1=int(input(" player 1    :   "))
      x2=int(input(" player 1(2) :   "))
      if  (x1>16 or x1<1 or x2>16 or x2 <1 or x1==temp1 or x1==temp2 or x1==temp3 or x1==temp4 or x1==temp5 or x1==temp6 or x1==temp7 or x1==temp8 or x1==temp9 or x1==temp10 or x1==temp11 or x1==temp12 or x2==temp1 or x2==temp2 or x2==temp3 or x2==temp4 or x2==temp5 or x2==temp6 or x2==temp7 or x2==temp8 or x2==temp9 or x2==temp10 or x2==temp11 or x2==temp12 or x1==x2):
           quit()
else :
   temp13=x1
   temp14=x2
   print
   x3 = random.randint(1,16)
   if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
      x3 = random.randint(1,16)
      if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
       x3 = random.randint(1,16)
       if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
          x3 = random.randint(1,16)
          if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
            x3 = random.randint(1,16)
            if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
               x3 = random.randint(1,16)
               if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
                  x3 = random.randint(1,16)
                  if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
                    x3 = random.randint(1,16)
                    if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
                      x3 = random.randint(1,16)
                      if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
                        x3 = random.randint(1,16)
                        if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
                           x3 = random.randint(1,16)
                           if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
                              x3 = random.randint(1,16)
                              if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
                                 x3 = random.randint(1,16)
                                 if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
                                    x3 = random.randint(1,16)
                                    if  (x3==temp1 or x3==temp2 or x3==temp3 or x3==temp4 or x3==temp5 or x3==temp6  or x3==temp7 or x3==temp8 or x3==temp9 or x3==temp10 or x3==temp11 or x3==temp12 or x3==temp13 or x3==temp14):
                                       x3 = random.randint(1,16)                           
   x4 = x3+1
   if (x4>16 or x4 <1  or x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6 or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
      x4=x3-4
      if (x4>16 or x4 <1  or x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6 or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
         x4 = x3-1
         if (x4>16 or x4 <1  or x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6 or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
            x4 = x3+4
            if (x4>16 or x4 <1  or x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6 or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
               X4 = random.randint(1,16)
               if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6 or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                  x4 = random.randint(1,16)
                  if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                   x4 = random.randint(1,16)
                   if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                      x4 = random.randint(1,16)
                      if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                        x4 = random.randint(1,16)
                        if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                           x4 = random.randint(1,16)
                           if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                              x4 = random.randint(1,16)
                              if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                                x4 = random.randint(1,16)
                                if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                                  x4 = random.randint(1,16)
                                  if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                                    x4 = random.randint(1,16)
                                    if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                                       x4 = random.randint(1,16)
                                       if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                                          x4 = random.randint(1,16)
                                          if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                                             x4 = random.randint(1,16)
                                             if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                                                x4 = random.randint(1,16)
                                                if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                                                   x4 = random.randint(1,16)
                                                   if  (x4==temp1 or x4==temp2 or x4==temp3 or x4==temp4 or x4==temp5 or x4==temp6  or x4==temp7 or x4==temp8 or x4==temp9 or x4==temp10 or x4==temp11 or x4==temp12 or x4==temp13 or x4==temp14 or x3==x4):
                                                      x4 = random.randint(1,16)            
   print (' computer chooses : ',x3,' , ',x4,' ')
   if (x2==x1+4) or (x2==x1+1)or (x1==x2+1) or (x1==x2+4) :
        if (x1==4 and x2==5) or ( x1==5 and x2 ==4) or (x1==8 and x2==9) or (x1==9 and x2==8) or (x1==12 and x2==13) or (x1==13 and x2==12) :
           y1=y1
        else:
           y1+=1
   if (x4==x3+4) or ( x4==x3+1) or (x3==x4+1) or (x3==x4+4):
        if (x3==4 and x4==5) or ( x3==5 and x4 ==4) or (x3==8 and x4==9) or (x3==9 and x4==8) or (x3==12 and x4==13) or (x3==13 and x4==12) :
            y2=y2
        else :
            y2+=1
if(y1>y2):
    print("Congratulations ! player 1 is winner ")
elif ( y2>y1) :
    print("Hard Luck ! computer is winner ")
else :
    print ("DRAW")
