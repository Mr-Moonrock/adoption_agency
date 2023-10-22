from app import app, db
from models import Pet

# Create an application context
with app.app_context():
    # Drop the existing tables if they exist
    db.drop_all()
    # Create the tables
    db.create_all()

    # Create some sample data
    sample_pets = [
        Pet(name='Whiskers', species='Cat', photo_url='https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_640.jpg', age=3, notes='Playful and friendly', available=True),
        Pet(name='Fluffy', species='Cat', photo_url='https://images.unsplash.com/photo-1615789591457-74a63395c990?auto=format&fit=crop&q=80&w=1000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZG9tZXN0aWMlMjBjYXR8ZW58MHx8MHx8fDA%3D', age=5, notes='Loves cuddling', available=False),
        Pet(name='Buddy', species='Dog', photo_url='https://images.unsplash.com/photo-1611003228941-98852ba62227?auto=format&fit=crop&q=80&w=1000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YmFieSUyMGRvZ3xlbnwwfHwwfHx8MA%3D%3D', age=2, notes='Great with kids', available=True),
        Pet(name='Max', species='Dog', photo_url='https://dogtime.com/wp-content/uploads/sites/12/2011/01/GettyImages-1294547052.jpg?resize=1200,630', age=4, notes='Loyal companion', available=False),
        Pet(name='Spike', species='Porcupine', photo_url='https://t3.ftcdn.net/jpg/03/40/69/38/360_F_340693892_PZ6UIBKlo91d5a09Nt3WNPSaCytuFO9U.jpg', age=1, notes='Handle with care', available=True),
        Pet(name='Prickles', species='Porcupine', photo_url='https://upload.wikimedia.org/wikipedia/commons/8/88/Porcupine_%285670622729%29.jpg', age=2, notes='Adorable but spiky', available=False),
    ]

    # Add the sample data to the database
    for pet in sample_pets:
        db.session.add(pet)

    # Commit the changes
    db.session.commit()

print('Sample data added to the database.')