import os
import sys
sys.path.append(os.getcwd)
from datetime import datetime
from sqlalchemy import (create_engine, PrimaryKeyConstraint,desc, Column, String, Integer, ForeignKey, Table, UniqueConstraint)
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///librarys.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
student_book = Table(
    "student_books",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    extend_existing=True,
)

# ....................class Student....................
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    grade_form = Column(Integer())

    #borrowings = relationship("Borrowing", backref=backref ("student"))
    #books = relationship("Book",secondary="student_books", back_populates="students")
    

# ....................class Student....................
class Staff(Base):
    __tablename__ = 'staffs'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    title = Column(String())

    #borrowings = relationship("Borrowing", backref=backref ("staff"))
    #books = relationship("Book",secondary="student_books", back_populates="staffs")

    #returnings = relationship("Returning", backref=backref ("staff"))
    #books = relationship("Book",secondary="student_books", back_populates="staffs")


# ...............................class Book...................

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True)
    ISBN = Column(Integer())
    title = Column(String())
    author= Column(String())
    category = Column(String())
    quantity = Column(Integer())

    #borrowings = relationship("Borrowing", backref=backref ("book"))
    #students = relationship("Student", secondary="student_books", back_populates="books")
   
   
# ...............................class Borrowing...................

class Borrowing(Base):
    __tablename__ = 'borrowings'
    id = Column(Integer(), primary_key=True)
    book_id = Column(Integer(), ForeignKey('books.id'))
    student_id = Column(Integer(), ForeignKey('students.id'))
    borrow_date = Column(String())
    staff_id = Column(Integer(), ForeignKey('staffs.id'))




    # ...............................class Borrowing...................

class Returning(Base):
    __tablename__ = 'returnings'
    id = Column(Integer(), primary_key=True)
    book_id = Column(Integer(), ForeignKey('books.id'))
    student_id = Column(Integer(), ForeignKey('students.id'))
    return_date = Column(String())
    staff_id = Column(Integer(), ForeignKey('staffs.id'))
    

    # ...............................class BBooks_in_student_custody...................

class Books_in_student_custody(Base):
    __tablename__ = 'books_in_student_custodys'
    id = Column(Integer(), primary_key=True)
    book_id = Column(Integer(), ForeignKey('books.id'))
    student_id = Column(Integer(), ForeignKey('students.id'))
