

def radiation (start,stop,step):

    def f(x):
        import math
        return 10*math.e**(math.log(0.5)/5.27 * x)
       
    count=start
    total=0
    while count<stop:

        total+=f(count)*step
        count+=step
        #print count
        #print f(count)
    return total
