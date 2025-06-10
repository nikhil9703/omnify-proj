# Omnify Fitness Class Booking API

A Django-based backend API for managing fitness class schedules and bookings. This project allows users to view available fitness classes, book slots, and manage scheduling efficiently.

## 🚀 Features

- View a list of upcoming fitness classes
- Book a slot for a specific class
- Ensure slots are not overbooked
- Admin interface to manage classes and bookings
- Input validation and clean error handling

## 🛠️ Tech Stack

- **Backend:** Django
- **Database:** SQLite (default), easily switchable to PostgreSQL/MySQL
- **Tools:** Django Admin, Django REST Framework (optional)

## 📁 Project Structure

omnify-proj/
├── manage.py
├── omnify_proj/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└── fitness/
├── init.py
├── admin.py
├── apps.py
├── models.py
├── views.py
└── urls.py


🧪 Sample API Endpoints
Note: These endpoints assume a REST implementation. You can expand these based on your views.py.

GET /classes/ — List all fitness classes

POST /book/ — Book a slot for a class

GET /bookings/ — List all bookings (admin only)

✅ Booking Logic
A class has a limited number of slots.

Bookings are only successful if slots are available.

Once slots reach zero, no further bookings are allowed.
🙌 Acknowledgements
Thanks to the Omnify team for the inspiration. This is a self-built backend API simulation of real-world booking systems.
