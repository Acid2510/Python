def say_name(name):
    print name
say_name('Acid')


def say_name(name):
    print "hello",format(name)
say_name('Acid')


def say_name_age(name, age):
    print "hello my name is {}, I am {} years old".format(name,age)
say_name_age('Acid',11)


def say_name_age_haha(name,age):
    print "hello my name is {}, I am {} years old".format(name,age)
    if age >16:
        print "Your to old"
    else:
        print "your still a little kid"
say_name_age_haha("Gassa",15)

  
