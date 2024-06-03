# Aspireit Assignment
## Name : Ankit Srivastava
## email : ankitsrivastava637as@gmail.com
## Project Structure
- `app/`: Contains the Flask application.
- `app/auth/`: Authentication-related routes and models.
- `app/main/`: Main application routes and models.
- `app/ml/`: Machine learning model integration.
- `app/templates/`: HTML templates.
- `app/static/`: Static files such as CSS.
- `tests/`: Test cases.
- `run.py`: Entry point to start the Flask application.

## API Endpoints

- **/auth/register (POST):** Register a new user.
- **/auth/login (POST):** User login.
- **/main/profile (GET, PUT):** Retrieve and update the user profile.
- **/main/buffer (POST):** Upload a buffer object.
- **/main/buffer/<buffer_id> (GET):** Retrieve a buffer object.
- **/main/analyze (POST):** Analyze text data.

## Setup Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Create and activate a virtual environment:

```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## Install the dependencies:

```bash
pip install -r requirements.txt   

```

## Start the Flask application:
```bash
python run.py
```

## Running the Backend unit Tests
You can run the tests by executing the following command in your terminal:
```bash
python -m unittest discover tests
```

## Frontend (React):

## Install dependencies:

```bash
npm install
```

## Start the React development server:

```bash
npm start
```




