# CI/CD Workshop Sample Project

This project is a boilerplate for a workshop on CI/CD using Django (Backend), React (Frontend), and GitHub Actions.

## Project Structure

- `backend/`: Django project with server-side rendering (Templates).
- `.github/workflows/`: CI/CD pipeline definitions.

## Key Features for the Workshop

1.  **Automated Testing**: The CI pipeline (`main.yml`) automatically runs Django tests on every push or pull request to the `main` branch.
2.  **Cross-Origin Support**: Backend is configured with CORS to allow the frontend to communicate easily.

## Local Development

### Running the Project
1. `cd backend`
2. `python -m venv venv`
3. `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. `pip install -r requirements.txt`
5. `python manage.py runserver`
6. Open `http://127.0.0.1:8000/` in your browser.


## Test Cases Demo
In `backend/api/tests.py`, we have:
- `HealthCheckTests`: Validates the API is alive.
- `DataTests`: Validates the data structure.
- `HomeTemplateTests`: Ensures the Django home page renders correctly.

Try changing the data in `backend/api/views.py` without updating tests to see the CI pipeline fail!
