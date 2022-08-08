import random
def find_min_steps( a,  b):
    steps = 0
    if (a == b):
        return a; # if same just return it (c step)
    if (a > b):# making always a smaller than b
        t=a;
        a=b;
        b=t;

    while (1):
        while (a <= b / 2):# double the smaller number to be bigger than half of the bigger number
            a *= 2;
            steps=steps+1;

        if (a == b):
            return steps+a; # if same then just c step a times
        t = b - a; # iterate c step until one number is twice as big as second one
        steps += a - t;
        a = t;
        b = a + t;



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a=10;
    b=21;
    for i in range(10):
        a=random.randint(1, 20)
        b=random.randint(1, 20)
        print("The minimum number of steps required to perform the operation on a: "+str(a)+" & b:"+str(b)+" is:"+str(find_min_steps(a,b)))
