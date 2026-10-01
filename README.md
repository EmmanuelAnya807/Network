# Django Social Network 🌐

A social networking platform I built with **Python**, **Django**, and **JavaScript** as part of Harvard's **CS50 Web Programming with Python and JavaScript** course.

This project brought together many of the Django and JavaScript concepts I had been learning. I built features for creating posts, following users, editing content, liking posts, viewing profiles, and navigating through paginated feeds.

It was also a good opportunity to think more carefully about **user relationships, permissions, database design, and frontend-backend communication**.

---

## Features

* User registration, login, and authentication
* Create new posts
* View all posts
* View individual user profiles
* Follower and following counts
* Follow and unfollow users
* Following feed
* Edit personal posts
* Like and unlike posts
* Dynamic like count updates
* Pagination for posts
* User-specific permissions
* Responsive interface built with Bootstrap

---

## Tech Stack

### Languages

* Python
* HTML5
* CSS3
* JavaScript
* SQL

### Frameworks & Libraries

* Django
* Bootstrap

### Database

* SQLite

### Tools

* Git
* GitHub
* Visual Studio Code

---

## Project Structure

```text
network/
│
├── network/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/EmmanuelAnya807/<Network-Project>.git
```

### Navigate into the project

```bash
cd <Network-Project>
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply migrations

```bash
python manage.py migrate
```

### Run the development server

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000/
```

---

## Usage

After launching the application, users can:

1. Register for an account.
2. Log in.
3. Create posts.
4. Browse posts from other users.
5. Visit user profiles.
6. Follow or unfollow users.
7. View posts from users they follow.
8. Edit their own posts.
9. Like or unlike posts.
10. Navigate through posts using pagination.

---

## What I Learned

Network helped me take several concepts I already knew and use them together in a larger application.

While building it, I became more comfortable with:

* Django models and ORM
* Many-to-many relationships
* Foreign key relationships
* Authentication and authorization
* CRUD operations
* Django URL routing
* Querying and filtering data
* Django's `Paginator`
* JavaScript event handling
* DOM manipulation
* Asynchronous requests with `fetch()`
* Working with JSON responses
* Connecting frontend interactions to backend logic
* Database design
* Responsive web design with Bootstrap

One part I especially enjoyed was working with relationships between users. Features such as following and liking look simple from the user's perspective, but implementing them made me think about how those relationships should actually be represented in the database.

---

## Challenges

Some of the parts that required the most problem-solving were:

* Designing the relationships between users, posts, followers, and likes.
* Making sure users could only edit their own posts.
* Implementing follow and unfollow functionality correctly.
* Updating likes and like counts without reloading the page.
* Adding pagination while keeping the interface easy to use.
* Making sure authenticated actions were properly protected on the backend.

These challenges helped me improve at tracing how a feature moves through the application, from the user interface to the JavaScript, Django view, database, and back again.

---

## Future Improvements

Some features I would like to explore in the future include:

* Profile pictures
* Post image uploads
* Comments and replies
* Search functionality
* Notifications
* Direct messaging
* REST API with Django REST Framework
* More automated testing
* Production deployment
* Docker support
* Improved mobile responsiveness

---

## Screenshots

Examples:

* Home Page
  <img width="1920" height="1048" alt="image" src="https://github.com/user-attachments/assets/86888000-b783-487b-b721-5511cd3a9c1f" />

* User Profile
  <img width="1920" height="1048" alt="image" src="https://github.com/user-attachments/assets/970039f3-0003-4223-b75d-2a7195100975" />

* Create Post
  <img width="1920" height="1048" alt="image" src="https://github.com/user-attachments/assets/cd81eef4-a377-4d31-bf24-674372d39a21" />

* Following Page
  <img width="1920" height="1048" alt="image" src="https://github.com/user-attachments/assets/d06e64ec-d7bf-4f67-b51e-06f4d4bb1bd0" />

* Edit Post
  <img width="1920" height="1048" alt="image" src="https://github.com/user-attachments/assets/e224d6fc-010d-46e7-b63e-46b866aff3f0" />

* Pagination
  <img width="1920" height="1048" alt="image" src="https://github.com/user-attachments/assets/186eabe9-6eb5-4bfa-8d99-08ed48c8cc32" />


---

## Live Demo

Coming Soon

---

## Author

**Anya Emmanuel Chidiebube**

Computer Science Student
University of Nigeria, Nsukka

* GitHub: https://github.com/EmmanuelAnya807
* LinkedIn: https://linkedin.com/in/anya-emmanuel

---

## License

This project was developed for educational purposes as part of Harvard University's **CS50 Web Programming with Python and JavaScript** course.
