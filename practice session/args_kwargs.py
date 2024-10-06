def use(*args):
    total=0
    for a in args:
        total=total+a
    print(total)
use(1,2,3,4,5,6,7,8)


def show(*args):
    for i in args:
        print(i)
    
show(11,22,33,44,55,66,77,88,99)



def new(**kwargs):
     
    print(kwargs)
new(pranav=100, rgk='gk',yes='no',ss=5)
