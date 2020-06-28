class Person(object):
    def __init__(self, name):
        self.name = name

    def get_identity(self):
        print("My name is {}".format(self.name))


class Spy(Person):
    def __init__(self, name, alias):
        super(Spy, self).__init__(name)
        self.alias = alias

    def get_identity(self):
        super(Spy, self).get_identity()
        print("...And I am {}".format(self.alias))
        

a = Person("Aitor")
b = Spy("James Bond", "007")

a.get_identity()
b.get_identity()
