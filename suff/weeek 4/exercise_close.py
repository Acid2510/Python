print('welcome to my program')
close="yes"
while close !='no':
    print('menu:')
    print('1.calculate area of triangle')
    print('2.calculate area of rectangle')
    print('3.calculate area of square')
    number=input('Your choice(1-3):')
    if number==1:
        print('calculating the are of triangle')
        base=input('what is the length of the base?:')
        height=input('what is the length of the height?:')
        print('the area of the triagle is:{0}'.format(base*height/2))
    if number==2:
        print('calculating the are of rectangle')
        lenght=input('what is the length of the rectangle:')
        width=input('what is the width of the rectangle:')
        print ('the area of the square is:{0}'.format(lenght*width))
    if number==3:
        print('calculating the are of square')
        side=input('what is the side of the square:')
        print ('the area of the square is:{0}'.format(side*side))
    close=raw_input('want to find another area?(yes/no):')
