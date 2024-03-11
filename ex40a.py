import mystuff

mystuff.apple()
print(mystuff.tangerine)

print('-'*10)

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple
print(thing.tangerine)

print('-'*10)

# dict style
# mystuff['apple']

# module style
mystuff.apple()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)

