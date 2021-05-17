# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''

Homework:

Task 1

Method overloading.

Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, and make their own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter.  

 '''
class Animal:
    def talk(self):
        print('animal cant talk')
class Dog(Animal):
    def talk(self):
        print('wouf')
class Cat(Animal):
    def talk(self):
        print('meow')
c=Animal()
c.talk()

    
'''

Task 2

Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books

```

class Library:

    pass

 

class Book:

    pass

 

class Author:

    pass

'''


class Library:
    def __init__(self,name, books = [], authors = []):
        self.name=name
        self.books =books
        self.authors=authors

    def new_book(self,name: str, year: int, author):
        a=Book(name,year,author)
        self.books.append(a)
        if not author in self.authors.name:
            self.authors.append(input('put name'),input('put country'),input('put birthday'))



    def group_by_author(self,author):
        for aut in self.authors:
            if aut.name==author:
                return self.aut.books


    def group_by_year(self,year: int):
        return [book for book in self.books if book.year==year]


class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year=year
        self.author=author



class Author:
    def __init__(self, name, country, birthday, books = []):
        self.name = name
        self.country=country
        self.birthday=birthday
        self.books=books


'''

Task 3

Fraction

Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) with appropriate checking and error handling

```

class Fraction:

pass

x = Fraction(1/2)

y = Fraction(1/4)

x + y == Fraction(3/4)

'''