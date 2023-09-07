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

    def option_list():
        print("CHOOSE AN OPTION")
        print("SETUPS")
        print("Add new student",1)
        print("Add new staff", 2)
        print("Add new book", 3)
        print("TRANSACTIONS")
        print("Borrow a book", 4)
        print("Return a book", 5)
        print("EDIT")
        print("Edit a student", 6)
        print("Edit a staff", 7)
        print("Edit a book", 8)
        print("REPORTS")
        print("View catalogue", 9)
        print("View students",10)
        print("View staff",11)
        print("View books in a student custody", 12)
        print("View borowed books",13)
        print("View returned books", 14)
        print("Promote students",15)

    option_list()
    chosen_option=input("CHOOSE AN OPTION: ")
    if chosen_option=="1":
        students = []
        student = Student(
                first_name=input("Enter first name: "),
                last_name=input("Enter last name: "),
                grade_form=input("Enter form: ")         
            )
        session.add(student)
        students.append(student)
        session.commit()


    elif chosen_option=="2":
        staffs = []
        staff = Staff(
                first_name=input("Enter first name of staff: "),
                last_name=input("Enter last name of staff: "),
                title=input("Enter title of staff: ")     
            )
        session.add(staff)
        staffs.append(staff)
        session.commit()  

    elif chosen_option=="3":
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

    elif chosen_option=="4":
        borrowings = []
        borrowing = Borrowing(
                book_id=input("Enter first name of staff: "),
                student_id=input("Enter last name of staff: "),
                borrow_date=input("Enter title of staff: "),   
                staff_id=input("Enter title of staff: ") 
            )
        session.add(borrowing)
        borrowings.append(borrowing)
        session.commit()  


    else:
        returnings = []
        returning = Returning(
                book_id=input("Enter first name of staff: "),
                student_id=input("Enter last name of staff: "),
                return_date=input("Enter title of staff: "),   
                staff_id=input("Enter title of staff: ") 
            )
        session.add(returning)
        returnings.append(returning)
        session.commit() 

    session.close()