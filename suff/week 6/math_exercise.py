def program():
    print '\n'
    print 'math program' 
    print '1.Addition'
    print '2.Subtraction' 
    print '3.Multiplication'
    print '4.Division'
    print '5.Exit'
    choce=input('What is your choice(Numbers only):')
    if choce==1:
        print'addition'
        a=first()
        b=second()
        add (a,b)
        program()
    elif choce==2:
        print'Subtraction'
        a=first()
        b=second()
        subtract(a,b)
        program()
    elif choce==3:
        print'multiplication'
        a=first()
        b=second()
        multiply(a,b)
        program()
    elif choce==4:
        print'Division'
        a=first()
        b=second()
        divide(a,b)
        program()
    elif choce==5:
        exit()
        


def add (a,b):
        print 'Adding {} + {} = {}'.format(a,b,a+b)
def subtract(a,b):
        print 'subtracting {} - {} = {}'.format(a,b,a-b)
def multiply (a,b):
        print 'Multiplying {} x {} = {}'.format(a,b,a*b)
def divide (a,b):
        print 'Deviding {} / {} = {}'.format(a,b,a/b)
def first():
    inp=input('input the first number:')
    return inp
def second():
    inp=input('input the second number:')
    return inp
program()
