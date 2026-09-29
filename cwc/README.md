# City Without Crime (CWC)

City Without Crime (CWC) is a Django-based crime reporting and public safety platform built to help citizens, police stations, and administrators manage complaints, emergencies, and criminal records more efficiently.

The project enables:
- citizens to register and lodge complaints,
- police stations to manage assigned complaints,
- administrators to oversee police stations and case activity,
- emergency updates to be published and viewed by users.

## Features

### User Module
- User registration and login
- Complaint submission
- Complaint tracking and status viewing

### Police Station Module
- Police dashboard for assigned complaints
- Criminal record management
- Emergency news creation and updates

### Admin Module
- View all complaints and police stations
- Add or remove police stations
- Oversee platform activity

### Emergency Updates
- Publish emergency notifications
- View recent emergency alerts on the home page

## Tech Stack
- Python
- Django 5.1.5
- SQLite database
- HTML, CSS, Bootstrap
- Pillow for image uploads

## Project Structure

```text
city-without-crime/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── media/
├── static/
├── cwc/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── main/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
└── README.md
```

## Prerequisites

- Python 3.10 or newer recommended
- pip
- Virtual environment support

## Installation

1. Clone the repository:

```bash
git clone https://github.com/tejvir21/city-without-crime.git
cd city-without-crime
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install django pillow
```

If a requirements file is available in the project, you can also use:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open the application in a browser:

```text
http://127.0.0.1:8000/
```

## Default Access

- Home page: `/`
- User registration: `/register/`
- Login: `/login/`
- User dashboard: `/dashboard/`
- Police dashboard: `/police_dashboard/`
- Admin dashboard: `/admin_dashboard/`

## Admin Access

Create a superuser to access the admin dashboard:

```bash
python manage.py createsuperuser
```

Then log in from the Django admin panel or use the app's admin flow as needed.

## Notes

- Media files are stored in the `media/` directory.
- Static files are served from the `static/` directory.
- This project is intended for local development and learning purposes unless extended for production deployment.

## License

This project is licensed under the MIT License.

## Contact

For project-related questions or updates, visit the portfolio:
https://tejvir-portfolio.vercel.app/
