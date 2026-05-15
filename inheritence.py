# Single Inheritance
class Parent:
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")

obj1 = Child()
obj1.show_parent()
obj1.show_child()


# Multilevel Inheritance
class Grandparent:
    def grandparent_method(self):
        print("This is Grandparent class")

class Parent2(Grandparent):
    def parent_method(self):
        print("This is Parent2 class")

class Child2(Parent2):
    def child_method(self):
        print("This is Child2 class")

obj2 = Child2()
obj2.grandparent_method()
obj2.parent_method()
obj2.child_method()


# Multiple Inheritance
class Father:
    def father_method(self):
        print("This is Father class")

class Mother:
    def mother_method(self):
        print("This is Mother class")

class Son(Father, Mother):
    def son_method(self):
        print("This is Son class")

obj3 = Son()
obj3.father_method()
obj3.mother_method()
obj3.son_method()


# Hierarchical Inheritance
class Animal:
    def animal_method(self):
        print("This is Animal class")

class Dog(Animal):
    def dog_method(self):
        print("This is Dog class")

class Cat(Animal):
    def cat_method(self):
        print("This is Cat class")

obj4 = Dog()
obj5 = Cat()

obj4.animal_method()
obj4.dog_method()

obj5.animal_method()
obj5.cat_method()


# Hybrid Inheritance
class A:
    def method_a(self):
        print("Class A")

class B(A):
    def method_b(self):
        print("Class B")

class C(A):
    def method_c(self):
        print("Class C")

class D(B, C):
    def method_d(self):
        print("Class D")

obj6 = D()
obj6.method_a()
obj6.method_b()
obj6.method_c()
obj6.method_d()