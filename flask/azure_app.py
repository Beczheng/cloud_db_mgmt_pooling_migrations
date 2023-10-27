import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables from .env file

load_dotenv()  

# Load credentials

DB_HOST_AZURE = os.getenv("DB_HOST_AZURE")
DB_DATABASE_AZURE = os.getenv("DB_DATABASE_AZURE")
DB_USERNAME_AZURE = os.getenv("DB_USERNAME_AZURE")
DB_PASSWORD_AZURE = os.getenv("DB_PASSWORD_AZURE")
#DB_PORT_AZURE = int(os.getenv("DB_PORT_AZURE", 3306))
#DB_CHARSET_AZURE = os.getenv("DB_CHARSET_AZURE", "utf8mb4")

# Create a connection string

connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = f'mysql+pymysql://{DB_USERNAME_AZURE}:{DB_PASSWORD_AZURE}@{DB_HOST_AZURE}/{DB_DATABASE_AZURE}'

# Create an engine

engine = create_engine(
        connection_string,
        connect_args=connect_args,
)

# Create a flask application

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

@app.route('/doctors')
def doctors():
    with engine.connect() as connection:
        query1 = text('SELECT * FROM doctors')
        result1 = connection.execute(query1)
        db_data1 = result1.fetchall()
    return render_template('doctors.html', data1=db_data1)

@app.route('/patients')
def patients():
    with engine.connect() as connection:
        query2 = text('SELECT * FROM patients')
        result2 = connection.execute(query2)
        db_data2 = result2.fetchall()
    return render_template('patients.html', data2=db_data2)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )