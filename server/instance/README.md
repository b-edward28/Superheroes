# Superheroes Flask API
A Flask API for managing superheroes and their superpowers. This application demonstrates model relationships, validation logic, serialization, and CRUD functionality using SQLAlchemy and Flask-Migrate.

---

## Description
This API enables users to:
- View heroes and their superpowers
- Assign powers to heroes with a strength level.
- Update power descriptions.
- Create new hero-power associations.

The database includes three models:
- `Hero`
- `Power`
- `HeroPower` (join table)

Each hero can have many powers, and each power can be used by many heroes, connected via the `HeroPower` join model with a specified strength (e.g., "Strong", "Average", "Weak").

---

## Author
**Brendah Edward**  
Email: edwardbrendah28@gmail.com  
GitHub: https://github.com/b-edward28

---

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/b-edward28/Superheroes
cd Superheroes

---

### 2. Create and activate a virtual environment
pipenv install && pipenv shell


### 3. Navigate to the server
cd server

### 4. Run migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

### 5. Seed the database
python seed.py

### 6. Run the server
flask run or python server/app.py

### 7. License
MIT License

Copyright (c) 2025 Brendah Edward

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
THE SOFTWARE.






