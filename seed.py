from app import db, Pet

def seed_pets():
    # Clear existing data
    Pet.query.delete()

    # Sample data for pets
    pet1 = Pet(
        name="Buddy",
        species="Dog",
        image_url="https://example.com/dog1.jpg",
        age=3,
        notes="Friendly and loves to play.",
        available=True
    )

    pet2 = Pet(
        name="Mittens",
        species="Cat",
        image_url="https://example.com/cat1.jpg",
        age=2,
        notes="Shy but affectionate.",
        available=False
    )

    pet3 = Pet(
        name="Goldie",
        species="Fish",
        image_url="https://example.com/fish1.jpg",
        age=1,
        notes="Loves to swim around the tank.",
        available=True
    )

    pet4 = Pet(
        name="Bubbles",
        species="Parrot",
        image_url="https://example.com/parrot1.jpg",
        age=4,
        notes="Talks a lot and mimics sounds.",
        available=True
    )

    # Add pets to the session
    db.session.add_all([pet1, pet2, pet3, pet4])

    # Commit the changes to the database
    db.session.commit()

    print("Seed data added successfully!")

if __name__ == "__main__":
    # Ensure the database connection is setup before seeding
    from app import app
    with app.app_context():
        seed_pets()
