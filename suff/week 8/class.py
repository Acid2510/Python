class living_things:
    def __init__(self,name):
        self.name=name
    
    def move(self):
        print'i am moving'
    def breathe(self):
        print'i am breathing'
    def my_name(self):
        print 'my name is {}'.format(self.name)

cat=living_things('catser')
cat.breathe()
cat.move()
cat.my_name()


