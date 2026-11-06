# CampusConnect

**Name:** John Michael Arcenal
**Section:** G1

A small Django web app for students and administrators. Students sign up with their name, email, and course, then log in to a personalized dashboard and edit their profile. Users with the Admin role can open an admin panel.

## Features

- Sign up with username, email, name, and course, with a success message
- Log in and log out
- Dashboard showing the user's name, role, course, total member count, and last login
- Profile page to edit name, email, and course (`UpdateView`, login required)
- Admin-only panel, with a 403 Forbidden page for students
- Django admin with custom Role and Course fields
- Bootstrap 5 styling via CDN

## Tech Stack

- Python 3.13
- Django 6.1
- SQLite (default database)
- Bootstrap 5

## Setup

Run these from the folder that contains `manage.py` (`campusconnect/campusconnect`).

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open http://127.0.0.1:8000/.

## Pages and URLs

| URL | Description | Access |
|---|---|---|
| `/` | Dashboard | Logged-in users |
| `/accounts/signup/` | Create an account | Anyone |
| `/accounts/login/` | Log in | Anyone |
| `/accounts/logout/` | Log out (POST) | Logged-in users |
| `/accounts/profile/` | Edit own profile | Logged-in users |
| `/admin-panel/` | Admin panel | Admin role only |
| `/admin/` | Django admin | Staff accounts |

## Roles

Each user has a role: **Student** (default) or **Admin**. Admins can be set in the Django admin under **Users** by editing the **Role** field. Sign-up does not let users choose their own role.

## Project Structure

```
campusconnect/
├── accounts/        # Custom user model, signup, login, profile
├── dashboard/       # Dashboard and admin panel
├── campusconnect/   # Project settings and root URLs
└── templates/       # Base layout and page templates
```
