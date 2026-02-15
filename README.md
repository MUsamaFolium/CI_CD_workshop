# CI/CD Workshop Sample Project

This project is a boilerplate for a workshop on CI/CD using Django (Backend), React (Frontend), and GitHub Actions.

## Project Structure

- `backend/`: Django project with server-side rendering (Templates).
- `.github/workflows/`: CI/CD pipeline definitions.

## Key Features for the Workshop

1.  **Automated Testing**: The CI pipeline (`main.yml`) automatically runs Django tests on every push or pull request to the `main` branch using Docker.
2.  **Dockerized Deployment**: The project is containerized for consistent development and production environments.
3.  **Cross-Origin Support**: Backend is configured with CORS to allow the frontend to communicate easily.

## Local Development

### Running with Docker (Recommended)

**Prerequisites:**
- Docker and Docker Compose installed on your system
- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

**Steps:**
1. Create a `.env` file in the `backend/` directory (optional, for custom settings):
   ```env
   DJANGO_SECRET_KEY=your-secret-key-here
   DJANGO_DEBUG=True
   ```

2. Build and run the containers:
   ```bash
   docker-compose up --build
   ```

3. The application will be available at `http://127.0.0.1:8000/`

**Useful Docker Commands:**
- `docker-compose up -d` - Run in detached mode (background)
- `docker-compose down` - Stop and remove containers
- `docker-compose logs -f backend` - View logs
- `docker-compose exec backend python manage.py migrate` - Run migrations
- `docker-compose exec backend python manage.py createsuperuser` - Create admin user
- `docker-compose exec backend python manage.py test` - Run tests

**Environment Variables:**
Create a `.env` file in the `backend/` directory with the following variables (optional):
```env
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
AWS_ACCESS_KEY_ID=your-aws-key
AWS_SECRET_ACCESS_KEY=your-aws-secret
AWS_DEFAULT_REGION=ap-south-1
```

**Production Deployment:**
For production, use the production docker-compose file:
```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

### Running with Virtual Environment (Alternative)

If you prefer not to use Docker:
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
