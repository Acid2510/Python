from random import randint

def guess_number():
    rand=randint(1,5)
    answer=input('Hello there,can you guess what number that im thinking of?(hint:1-5):')
    if answer==rand:
        print 'you are correct, GOOD JOB'
    else:
        print'you are incorrect, better luck next time'
        print '\n'
        guess_number()
guess_number()
