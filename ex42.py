## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    ## Dog has-a __init__ that takes self and name parameters
    def __init__(self,name):
        ## Set variable name as name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    ## Cat has-a __init__ that takes self and name parameters
    def __init__(self,name):
        ## Set variable name as name
        self.name = name

## Person is-a object
class Person(object):

    ## Person has-a __init__ that takes self and name parameters
    def __init__(self,name):
        ## Set variable name as name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self,name,salary):
        ## Call __init__() of the Person class
        super(Employee,self).__init__(name)

        ## set variable salary as salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog named rover
rover = Dog("rover")

## satan is-a Cat named satan
satan = Cat("satan")

## mary is-a Person named Mary
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a Employee and has-a name Frank and a salary 120000
frank = Employee("Frank", 120000)

## frank has a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
