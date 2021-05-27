
loop= []
def addToLoop(x):
    if loop[0] == x:
        return True    
    loop.append(x)
    return False
def makeStep(a,pos):
    temp = []
    for i in a:
        if pos[1] == i[0]:
            temp.append(i)
    return temp

def loopFinder(a,pos):
    step = makeStep(a,pos)
    for k in step:
        x = addToLoop(k)
        if(x):
            return True
        else:
            if loopFinder(a,k):
                return True
            else:
                loop.pop()
    return False

def thereIsLoop(a):
    flag = False
    for i in a:
        loop.append(i)
        if loopFinder(a,i):
            flag = True
            break    
        loop.pop()
    return flag


