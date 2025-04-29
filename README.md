# Event Management API

Event Management API is a Django RESTful backend for managing events and user registrations.  
It allows authenticated users to create, list, filter, and register for events with email confirmations via Mailtrap.

## Features

- JWT authentication (via `djangorestframework-simplejwt`)
- Event creation and registration system
- Role-based access (only authenticated users can register)
- Filtering events by date and location
- Admin panel customization with Jazzmin
- API schema generation with drf-spectacular (Swagger/OpenAPI)
- Email confirmation on event registration (Mailtrap SMTP)
- Dockerized setup for development and production


## Tech Stack

- Python 3.12
- Django 5.2
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Mailtrap (for email testing)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd Event-Management-API
   ```

2. **Configure environment variables**:  
   Create a `.env` file using `.env.sample` as a reference.

3. **Build and run the containers**:
   ```bash
   docker-compose build --no-cache
   docker-compose up -d
   ```

4. **Run migrations and create a superuser**:
   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Access the services**:

   - Swagger docs: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
   - Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## API Endpoints

- `POST /api/token/` — Obtain JWT
- `POST /api/token/refresh/` — Refresh token
- `GET/POST /api/events/events/` — List or create events
- `POST /api/events/events/{id}/register/` — Register for event

## Notes

- Uses Mailtrap for email testing. See `.env.sample` to configure.
- Filter example: add query parameters like `?date=2024-05-01&location=Kyiv` to filter events.
