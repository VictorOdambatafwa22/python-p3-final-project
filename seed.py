from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
#from models import Borrowing, Book, Student, student_books
from models import Borrowing, Book, Student
if __name__ == "__main__":
    engine = create_engine('sqlite:///librarys.db')
    Session = sessionmaker(bind=engine)
    session = Session()
  
    students = []

    student = Student(
            first_name=input("Enter first name: "),
            last_name=input("Enter last name: "),
            grade_form=input("Enter form: ")         
        )
    session.add(student)
    students.append(student)

    session.commit()

    

    books = []

    book = Book(
            ISBN=input("Enter ISBN: "),
            title=input("Enter book title: "),
            author=input("Enter book author: "),
            category=input("Enter book category: "),
            quantity=input("Enter number of copies: ")         
        )
    session.add(book)
    books.append(book)

    session.commit()

    session.close()