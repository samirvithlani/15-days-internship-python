'''
            and
    no1 > 20 and no1 %2 ==0
     
      t   t true
      f   - false
      t  f  false

          or

     t  - true
     f  t  true
     f f - false     



'''

no = int(input("enter no"))

if no>=20 or no %2==0:
    print("true")
else:
    print("false")    
