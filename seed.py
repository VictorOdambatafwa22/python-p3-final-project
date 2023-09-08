from faker import Faker
import random
from datetime import datetime
from sqlalchemy import create_engine,desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
#from models import Borrowing, Book, Student, student_books
from models import Borrowing,Returning, Book, Student,Staff,Books_in_student_custody
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
        print("Student successfully added to the database") 


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
        print("Staff successfully added to the database") 

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
        print("Book successfully added to the database")  

    elif chosen_option=="4":
        borrowings = []
        borrowing = Borrowing(
                book_id=input("Enter book ID: "),
                student_id=input("Enter student ID: "),
                borrow_date=datetime.now(),   
                staff_id=input("Enter staff ID: ") 
            )
        session.add(borrowing)
        borrowings.append(borrowing)
        session.commit()  


        session.query(Book).update({
        Book.quantity: Book.quantity - 1
    })
        session.commit()
        print("Book successfully borrowed")   


    elif chosen_option=="5":
        returnings = []
        returning = Returning(
                book_id=input("Enter book ID: "),
                student_id=input("Enter student ID: "),
                return_date=datetime.now(),   
                staff_id=input("Enter staff ID: ") 
            )
        session.add(returning)
        returnings.append(returning)
        session.commit()  

        session.query(Book).update({
        Book.quantity: Book.quantity + 1
    })
        session.commit()  
        print("Book successfully returned") 
     
    elif chosen_option=="6": 
        id=input("Enter student id: ")
        first_name=input("Enter new first name : ")
        student=session.query(Student).filter(Student.id==int(id)).first()
        student.first_name = first_name
        session.commit()
        print("Student successfully updated") 

    elif chosen_option=="7": 
        id=input("Enter staff id: ")
        first_name=input("Enter new first name : ")
        staff=session.query(Staff).filter(Staff.id==int(id)).first()
        staff.first_name = first_name
        session.commit()
        print("Staff successfully updated")    
         
    elif chosen_option=="8": 
        id=input("Enter book id: ")
        title=input("Enter new title : ")
        book=session.query(Book).filter(Book.id==int(id)).first()
        book.title = title
        session.commit()
        print("Book successfully updated")  

    elif chosen_option=="9": 
        books=session.query(Book).all()
        print("-"*70)
        for book in books:          
            print(f' {book.id} {book.ISBN} {book.title} {book.author} {book.category} {book.quantity}') 
            print("-"*70)

    elif chosen_option=="10": 
        students=session.query(Student).all()
        print("-"*70)
        for student in students:          
            print(f' {student.id} {student.first_name} {student.last_name} {student.grade_form}') 
            print("-"*70)    


    elif chosen_option=="11": 
        staffs=session.query(Staff).all()
        print("-"*70)
        for staff in staffs:          
            print(f' {staff.id} {staff.first_name} {staff.last_name} {staff.title}') 
            print("-"*70)   
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