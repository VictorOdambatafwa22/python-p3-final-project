import os
import sys
sys.path.append(os.getcwd)
from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer, ForeignKey, Table, UniqueConstraint)
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

# ....................students class....................
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    grade_form = Column(Integer())

    borrowings = relationship("Borrowing", backref=backref ("student"))
    books = relationship("Book",secondary="student_books", back_populates="students")
    


# ...............................class Book...................

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    category = Column(String())
    quantity = Column(Integer())

    borrowings = relationship("Borrowing", backref=backref ("book"))
    students = relationship("Student", secondary="student_books", back_populates="books")
   
# ...............................class Borrowing...................

class Borrowing(Base):
    __tablename__ = 'borrowings'
    id = Column(Integer(), primary_key=True)
    book_id = Column(Integer(), ForeignKey('books.id'))
    student_id = Column(Integer(), ForeignKey('students.id'))
