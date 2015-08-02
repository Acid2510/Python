class living_things:
    def __init__(self,name):
        self.name=name
    
    def move(self):
        print'i am moving'
    def breathe(self):
        print'i am breathing'
    def my_name(self):
        print 'my name is {}'.format(self.name)

class human(living_things):
    def thinking(self):
        print "i am thinking"

class cat(living_things):
    def climbing_a_roof(self):
        print "i am climbing a roof"

class Bee(living_things):
    def have_a_stinger(self):
        print "I have a stinger"

Gassa=human("Gassa")
cater=cat("cater")
Beeter=Bee("Beester")

Gassa.move()
cater.move()
Beeter.move()
print ""
Gassa.thinking()
cater.climbing_a_roof()
Beeter.have_a_stinger()
