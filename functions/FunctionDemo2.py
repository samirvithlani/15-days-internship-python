def myFun(*argv):
    print("argv",argv)

myFun('samir','raj',12,25)

def data(**kwargs):
    print("kwargs",kwargs)

data(ok ="hello",second="gm")    