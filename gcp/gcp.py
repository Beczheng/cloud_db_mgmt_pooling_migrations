from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()

# Load credentials

DB_HOST_GCP = os.getenv("DB_HOST_GCP")
DB_DATABASE_GCP = os.getenv("DB_DATABASE_GCP")
DB_USERNAME_GCP = os.getenv("DB_USERNAME_GCP")
DB_PASSWORD_GCP = os.getenv("DB_PASSWORD_GCP")
#DB_PORT_GCP = int(os.getenv("DB_PORT_GCP", 3306))
#DB_CHARSET_GCP = os.getenv("DB_CHARSET_GCP", "utf8mb4")

# Create a connection string

connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = f'mysql+pymysql://{DB_USERNAME_GCP}:{DB_PASSWORD_GCP}@{DB_HOST_GCP}/{DB_DATABASE_GCP}'

# Create an engine 

engine = create_engine(
        connection_string,
        connect_args=connect_args,
)

# Create tables

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    address = Column(String(50), nullable=False)

    primary_doctors = relationship('Doctors', back_populates='patient')
    
class Doctors(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True)  
    patient_id = Column(Integer, ForeignKey('patients.id'))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    specialization = Column(String(50), nullable=False)

    patient = relationship('Patient', back_populates='primary_doctors')

# Test connection

inspector = inspect(engine)
inspector.get_table_names()

Base.metadata.create_all(engine)
