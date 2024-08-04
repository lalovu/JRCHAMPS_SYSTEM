from . import db
from flask_login import UserMixin
from flask_migrate import Migrate
import enum

class Role(enum.Enum):
    student = "student"
    admin = "admin"
    teacher = "teacher"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)  # Ensure email is not null
    password = db.Column(db.String(150), nullable=False)  # Ensure password is not null
    role = db.Column(db.String(50), nullable=False)  # Ensure role is not null

    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return f'<User {self.email}>'

class StudentInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('student_info', lazy=True))
    student_name = db.Column(db.String(150), nullable=False)
    date_of_birth = db.Column(db.String, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    parent_guardian_name = db.Column(db.String(150), nullable=False)
    email_gp = db.Column(db.String(150), nullable=False)
    relationship_to_student = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    emergency_contact_name = db.Column(db.String(150), nullable=False)
    emergency_relationship = db.Column(db.String(100), nullable=False)
    emergency_contact_number = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<StudentInfo {self.id}: {self.student_name}>"

class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Announcement {self.title}>'
    
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade_level = db.Column(db.String(50), nullable=False)
    schedule_from = db.Column(db.String(50), nullable=False)
    schedule_to = db.Column(db.String(50), nullable=False)

    students = db.relationship('Student', secondary='subject_student', back_populates='subjects')

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Many-to-many relationship with subjects
    subjects = db.relationship('Subject', secondary='subject_student', back_populates='students')

# Define the association table for the many-to-many relationship
subject_student = db.Table('subject_student',
    db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'), primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True)
)