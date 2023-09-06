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
    session.query(Student).delete()
    fake = Faker()


    students = []
    for _ in range(20):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name()
           

        )
        session.add(student)
        students.append(student)


    books = []
    for _ in range(20):
        book = Book(
            ISBN=fake.ISBN(),
            title=fake.title(),
            category=fake.category(),
            quantity=fake.quantity()

        )
        session.add(book)
        books.append(book)


    existing_combinations = set()

    for _ in range(50):
        student_id = random.randint(1, 20)
        book_id = random.randint(1, 20)
        if (student_id, book_id) in existing_combinations:
            continue
        existing_combinations.add((student_id, book_id))
        student_book_data = {"student_id": student_id, "book_id": book_id}
        stmt = insert(student_books).values(student_book_data)
        session.execute(stmt)

    for _ in range(50):
        borrowing = Borrowing(
            student_id=random.randint(1, 20),
            book_id=random.randint(1, 20)
        )
        session.add(borrowing)
    session.commit()
    session.close()