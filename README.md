# ClosedSooq – Online garage sale
![ClosedSooqHome](https://github.com/user-attachments/assets/8fc756a1-ec28-41de-9994-a81f196ec940)
![ClosedSooqItemList](https://github.com/user-attachments/assets/f83bc53b-ea46-444f-859a-6f80193f749f)
![ClosedSooqCreate](https://github.com/user-attachments/assets/c15ea93b-0dbe-4fd8-b026-80a4929dbc60)







## Idea
Garage sale website where users can post items they want to sell, and view the items others have posted.

---

## Overview
ClosedSooq is a website for listing used or otherwise unwanted items for sale online, by logging in as a registered user, creating an item that gets added to the items list, and viewing the items listed for sale by other users.

---



## User Stories
### Viewer = unregistered user
### User = registered


- 1) As a viewer, I want to be able to sign up and log in.
- 2) As a viewer of the website, I want to be able to see which items other users posted in the items list.
- 3) As a viewer of the website, I want to be able to see a list of item categories.
- 4) As a user, I want to be able to post items.
- 5) As a user, I want to be able to see which items I posted in my page. 
- 6) As a user, I want to be able to update and delete an item I posted.


### As an Admin user
- As an admin, I can create an instance of Category, and I can create, read, update, and delete any item.


---
## Future Features

- **Adding a pictures field in the form for creating an item** – Users will be able to upload pictures of their items.
- **User Profiles** – Let users manage and see each other's profiles that include the items they've posted. 
- **Item Categories Filter** – Filter items by categories and display them.
- **Search function** – Users can search for specific item names and categories.  

---

## Technologies

**Language**  Python 3.12+ 
**Backend**  Django 5.x 
**Frontend**  HTML5, CSS3, Django Templates 
**Database**  PostgreSQL 
**Auth System**  Django Authentication 


---

## ERD Overview

**Original ERD in the design phase**
![souq1-ERD](https://github.com/user-attachments/assets/831cff42-b878-4052-93e0-02ea1da9986a)





**Entities:**
- **User** (Django default user model)
- **Item**
  - item ID
  - item name 
  - is used
  - price in JOD
  - categories
  - item description
  - creator = User

- **Category**
  - category ID
  - category name

**Relationships:**
- One **User** can create many **Items**.
- Many **Items** can contain many **Categories**.
- One **Admin** can create many **Categories**.

---

## Installation

### 1 - Clone the Repository
```bash
git clone https://git.generalassemb.ly/jumanadodin/Capstone-Jumana
cd Capstone-Jumana
```

### 2 - Create Virtual Environment
```bash
python -m venv capstone-venv
source capstone-venv\scripts\activate # (Mac: capstone-venv/bin/activate )
```

### 3 - Install Dependencies
```bash
pip install -r requirements.txt
```

### 4 - Configure PostgreSQL
Create a database in **pgAdmin 4** (e.g., `ClosedSooqDB`),  
then update `settings.py` → `DATABASES` section with your credentials.

### 5 - Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6 - Create Superuser
```bash
python manage.py createsuperuser
```

### 7 - Run the Server
```bash
python manage.py runserver
```

Access the app at: **http://127.0.0.1:8000/**

---

## Folder Structure

```
CapstoneJumana/
│
├── ClosedSooq/              
│   ├── asgi.py
│   ├── settings.py 
│   ├── urls.py
│   └── wsgi.py
│
├── main_app/ 
│   ├── media/                 
│   │    └── images/               
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── templates/
│   │   └── categories/
│   │   └── items/
|   |   └── registration/
│   └── static/css/
│       └── base.css
│
├── manage.py
└── README.md
└── requirements.txt
```


---

