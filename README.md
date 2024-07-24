# Job Portal

A comprehensive job portal application developed using Django, providing a platform for job seekers and employers to connect.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- User authentication and authorization.
- Job listing and search functionality.
- Application management for job seekers.
- Job posting and management for employers.

## Tech Stack
- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default), PostgreSQL (optional)
- **Version Control:** Git
- **Deployment:** Docker, Heroku/AWS (optional)

## Installation

### Prerequisites
- Python 3.x
- Django
- Git

### Steps
1. **Clone the repository**
    ```bash
    git clone https://github.com/DityaChawla/School-Management-System.git
    cd jobportal
    ```

2. **Create and activate a virtual environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**
    ```bash
    python manage.py runserver
    ```

## Usage
- Navigate to `http://127.0.0.1:8000/` in your web browser.
- Register as a new user, and explore the functionalities based on your user role (job seeker or employer).

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code follows the project's style and passes all tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
