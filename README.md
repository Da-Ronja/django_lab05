# Lab: User Management and Display

In this lab, I will apply what we learned about setting up Models, Templates, and Views in Django.

## Objectives

- Set up a new Django project and app.
- Create a User model with basic fields.
- Populate the database with fake user data.
- Display a list of users on a web page.

---

## Steps

### 1. Start a New Django Project

Create a new Django project for this lab. Run the following command:

```cmd
django-admin startproject userportal
```

### 2. Create a New App

Inside my project, create a new Django app to manage user data:

```cmd
python manage.py startapp users
```

### 3. Create the User Model

In the `models.py` file of my `users` app, define a new model called `User` with the following fields:

- `first_name`: CharField (e.g., `max_length=50`)
- `last_name`: CharField (e.g., `max_length=50`)
- `email`: EmailField (e.g., `unique=True`)

### 4.a Make Migrations and Migrate

After defining the model, make the migrations to create the `User` table in my database:

```cmd
python manage.py makemigrations
python manage.py migrate
```

### 4.b Creating an admin user

```cmd
python manage.py createsuperuser
```

### 5. Populate the Database with Fake Users

1. Install the Faker library (as I already have) to generate fake data:

   ```cmd
   pip install faker
   ```

2. Create a script in my project root (e.g., `populate_users.py`) to populate the database with fake users using Faker.

3. Run the script to generate and add user data to my database.

### 6. Register the User Model in the Admin Interface

In the `admin.py` file of my `users` app, register the `User` model so I can view and manage users in Django’s admin panel.

```python
from django.contrib import admin
from .models import User

admin.site.register(User)
```

### 7. Create a View for the `/users` Page

Define a view that retrieves all `User` instances from the database and passes them to a template for rendering. This view should correspond to the `/users` URL path.

### 8. Create a Template to Display the User List

1. In the `templates` directory of my `users` app, create a template (e.g., `user_list.html`) to display an HTML list of users' names and emails.

2. Use Django template tags to loop through the users and display their details.

### 9. Update `urls.py` to Add the `/users` Route

In my app’s `urls.py`, add a URL pattern for `/users` that points to the new view I've created. Be sure to include this URL configuration in the project's main `urls.py`.

---

## Summary

By completing this lab, I will have set up a simple user management feature that includes:
- Creating a custom model and populating it with fake data.
- Registering the model in the admin interface.
- Displaying a list of users on a webpage using Django templates and views.
