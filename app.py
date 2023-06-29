from flask import Flask
from models import db,Product

app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Jennicson1@localhost:5432/kissanmart'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

@app.route('/register')
def register():
    return 'Okay'



# Create the database tables (run this once)
with app.app_context():
    db.create_all()

# Rest of your Flask app code...

# Run the Flask app
if __name__ == '__main__':
    app.run()
