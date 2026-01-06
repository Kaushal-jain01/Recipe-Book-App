from faker import Faker
import random
fake = Faker()

from .models import *

def seed_db(n=10) -> None:
    try:
        for i in range(0, n):

            department_objs = Department.objects.all()
            random_idx = random.randint(0, len(department_objs)-1)
            department = department_objs[random_idx]

            student_id = f'STU-{random.randint(100,999)}'
            student_id_obj = StudentID.objects.create(student_id=student_id)
            
            student_name = fake.name()
            student_email = fake.unique.email()
            student_age = fake.random_int(min=18, max=30)
            student_address = fake.address()

            student_obj = Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address
            )

            print(f"Created Student: {student_obj.student_name}, ID: {student_obj.student_id.student_id}")

    except Exception as e:
        print(f"Error seeding database: {e}")