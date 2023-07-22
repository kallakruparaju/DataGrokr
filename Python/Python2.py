from abc import ABC ,abstractmethod

class Person(ABC):

    @abstractmethod
    def get_gender(self):
        print("person is:")

class Male(Person):

    def get_gender(self):
        super().get_gender()
        print("Male")

class Female(Person):

    def get_gender(self):
        super().get_gender()
        print("Female")

f = Female()
m = Male()
f.get_gender()
m.get_gender()