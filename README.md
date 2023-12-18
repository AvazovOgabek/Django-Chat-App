![Project Logo](/statics/img/img.png)

# DjangoChatApp

This is a simple chat application built using Django framework. It allows users to sign up, log in, search for other users, view profiles, and engage in real-time chat conversations.

---

## Features

- **User Authentication**: Users can sign up and log in securely.
- **Profile Management**: Users can view and manage their profiles.
- **Real-time Chat**: Users can engage in real-time chat conversations.

---

## Requirements

- Python (3.x recommended)
- Django (3.x recommended)
- Pillow (for image handling)
- Other dependencies as listed in `requirements.txt`

---

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/AvazovOgabek/DjangoChatApp.git
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

5. **Access the application in your browser at** `http://127.0.0.1:8000/`

---

## Usage

- **Signup**: Create a new account using valid credentials.
- **Login**: Log in with your username and password.
- **Search**: Search for other users by username.
- **Chat**: Engage in real-time conversations with other users.

---

## Folder Structure

- `registrations/`: Contains signup and login views.
- `profiles/`: Manages user profiles.
- `templates/`: HTML templates for different views.
- `static/`: Contains static files like CSS, JavaScript, and images.

---

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

---

## Credits

- This project was created by Avazov Og'abek.

---
