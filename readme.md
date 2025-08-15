# Smartphone REST API (Python + Flask)

This is a **simple REST API** built using Python and Flask.  
It allows you to manage a list of smartphones with **Create, Read, Update, and Delete (CRUD)** operations.  
Data is stored in memory (Python list) and resets when the server restarts.

## 🖥 Technologies Used

- **Language:** Python 3
- **Framework:** Flask
- **IDE:** Visual Studio Code (VS Code) / Any Python-supported editor
- **Libraries Used:** Flask (install via `pip install flask`)
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Data Storage:** Python list (in-memory)

## ✨ Features

- **Get all smartphones** (GET `/smartphones`)
- **Get smartphone by ID** (GET `/smartphones/<id>`)
- **Add a new smartphone** (POST `/smartphones/create`)
- **Update an existing smartphone** (PUT `/smartphones/update/<id>`)
- **Delete a smartphone** (DELETE `/smartphones/delete/<id>`)
- **Validation for POST data** (brand, price, model required)
- **404 handling** when item not found

## 🛠 What I Did

1. Created a Flask app with multiple routes for CRUD operations.
2. Used `jsonify()` to return JSON responses.
3. Implemented `next()` function to find a smartphone by ID.
4. Added **data validation** for `POST` request.
5. Implemented **update** using `phone.update(data)`.
6. Implemented **delete** by filtering the list.
7. Tested routes using **browser** (for GET) and **Postman** (for POST/PUT/DELETE).

## 🚀 How to Run

1. Save the file as `RestAPI.py`.
2. Install Flask:
   ```bash
   pip install flask
