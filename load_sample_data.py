import os
import django
from datetime import date
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from home.models import Author, Category, Book, Customer

# Create Authors
authors = [
    Author.objects.create(name="Jane Austen", bio="English novelist."),
    Author.objects.create(name="George Orwell", bio="English novelist and essayist."),
    Author.objects.create(name="J.K. Rowling", bio="British author, best known for Harry Potter."),
    Author.objects.create(name="Mark Twain", bio="American writer and humorist."),
    Author.objects.create(name="Agatha Christie", bio="English writer known for detective novels."),
]

# Create Categories
categories = [
    Category.objects.create(title="Fiction"),
    Category.objects.create(title="Mystery"),
    Category.objects.create(title="Fantasy"),
    Category.objects.create(title="Classic"),
    Category.objects.create(title="Science Fiction"),
]

# Create Customers
customers = [
    Customer.objects.create(name="Alice Smith", email="alice@example.com"),
    Customer.objects.create(name="Bob Johnson", email="bob@example.com"),
    Customer.objects.create(name="Charlie Lee", email="charlie@example.com"),
    Customer.objects.create(name="Diana King", email="diana@example.com"),
    Customer.objects.create(name="Ethan Brown", email="ethan@example.com"),
]

# Create Books
books = [
    Book.objects.create(
        title="Pride and Prejudice",
        author=authors[0],
        price=Decimal("19.99"),
        published_date=date(1813, 1, 28),
        stock=10
    ),
    Book.objects.create(
        title="1984",
        author=authors[1],
        price=Decimal("15.99"),
        published_date=date(1949, 6, 8),
        stock=8
    ),
    Book.objects.create(
        title="Harry Potter and the Sorcerer's Stone",
        author=authors[2],
        price=Decimal("25.00"),
        published_date=date(1997, 6, 26),
        stock=12
    ),
    Book.objects.create(
        title="The Adventures of Tom Sawyer",
        author=authors[3],
        price=Decimal("12.50"),
        published_date=date(1876, 6, 1),
        stock=7
    ),
    Book.objects.create(
        title="Murder on the Orient Express",
        author=authors[4],
        price=Decimal("18.75"),
        published_date=date(1934, 1, 1),
        stock=9
    ),
]

# Assign categories to books
books[0].categories.set([categories[0], categories[3]])
books[1].categories.set([categories[0], categories[4]])
books[2].categories.set([categories[0], categories[2]])
books[3].categories.set([categories[0], categories[3]])
books[4].categories.set([categories[0], categories[1]])

print("Sample data loaded successfully.")
