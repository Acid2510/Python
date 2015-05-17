shape=raw_input('what area are you triying to find(square/triangle):')
if shape=='triangle':
    base=input('what is the length of the base:')
    height=input('what is the length of the height:')
    print ('the area of the traingle is:{0}'.format(base*height/2))
if shape=='square':
    lenght=input('what is the length of the square:')
    width=input('what is the width of the square:')
    print ('the area of the square is:{0}'.format(lenght*width))

