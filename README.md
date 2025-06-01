# 🎟️ Event Management API

A Django RESTful backend for managing events and user registrations. Authenticated users can create, list, filter, and register for events with email confirmations via Mailtrap.

---

## 📌 Table of Contents

* [🌐 Overview](#-overview)
* [✨ Features](#-features)
* [🛠 Tech Stack](#-tech-stack)
* [🧹 System Requirements](#-system-requirements)
* [⚙️ Installation](#-installation)

  * [Poetry Setup](#poetry-setup)
  * [Environment Configuration](#environment-configuration)
  * [Docker Setup](#docker-setup)
  * [Running Commands](#running-commands)
* [📬 Email Configuration](#-email-configuration)
* [📚 API Documentation](#-api-documentation)
* [🤪 Testing](#-testing)
* [📬 Test Email Sending](#-email-testing-guide)
* [📝 API Endpoints](#-api-endpoints)

---

## 🌐 Overview

This backend allows users to register for events, receive email confirmations, and browse available events. Admins can manage events via a customized admin interface powered by Jazzmin.

## ✨ Features

* JWT authentication (`djangorestframework-simplejwt`)
* Event creation and registration system
* Role-based access control
* Filtering by date and location
* Custom admin UI with Jazzmin
* API schema with drf-spectacular (Swagger/OpenAPI)
* Email confirmation via Mailtrap
* Dockerized for dev/prod

## 🛠 Tech Stack

* Python 3.12
* Django 5.2
* Django REST Framework
* PostgreSQL
* Docker & Docker Compose
* Mailtrap
* Poetry (dependency management)
* Jazzmin (admin customization)

## 🧹 System Requirements

* Python >= 3.12
* Poetry
* Docker & Docker Compose

## ⚙️ Installation

### Poetry Setup

```bash
    python -m venv .venv
    .venv\Scripts\activate  # Windows
    source .venv/bin/activate  # macOS/Linux
    pip install poetry
    poetry install
```

### Environment Configuration

Create a `.env` file using the provided `.env.sample` as a template:

```bash
    copy .env.sample .env  # Windows
    cp .env.sample .env    # macOS/Linux
```

### Docker Setup

> 🪟 Windows:

```bash
    .\make build
    .\make up
```

> 🍎 macOS/Linux:

```bash
    make build
    make up
```

### Running Commands

> 🪟 Windows:

```bash
    .\make migrate
    .\make createsuperuser
    .\make up
    .\make down
    .\make logs
    .\make restart
    .\make shell
```

> 🍎 macOS/Linux:

```bash
    make migrate
    make createsuperuser
    make up
    make down
    make logs
    make restart
    make shell
```

## 📬 Email Configuration

Emails are sent via Mailtrap. Configure credentials in `.env`:

* `EMAIL_HOST`
* `EMAIL_HOST_USER`
* `EMAIL_HOST_PASSWORD`

You can test that the email service works by registering for an event (see endpoint `/api/events/events/{id}/register/`). The email will appear in your Mailtrap inbox.

## 📚 API Documentation

* Swagger UI: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
* Django Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## 🤪 Testing

Run tests and view coverage **locally**:

```bash
    poetry run pytest
    poetry run coverage run -m pytest
    poetry run coverage report
    poetry run coverage html && start htmlcov\index.html  # Windows
    poetry run coverage html && open htmlcov/index.html   # macOS/Linux
```

## 📬 Email Testing Guide

This project uses [Mailtrap](https://mailtrap.io/) for safe email testing in development. A confirmation email is automatically sent to the user after successful event registration.

### 🧪 How to Test Email Sending

> These steps simulate real email sending using a sandboxed SMTP server provided by Mailtrap.

1. **Create a Mailtrap account:**
   Sign up at [mailtrap.io](https://mailtrap.io/) and create an inbox.

2. **Configure credentials:**
   In the Mailtrap dashboard, navigate to your inbox > "SMTP Settings" > select "Django" and copy the credentials to your `.env` file:

   ```env
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=sandbox.smtp.mailtrap.io
   EMAIL_PORT=587
   EMAIL_HOST_USER=your_mailtrap_username
   EMAIL_HOST_PASSWORD=your_mailtrap_password
   EMAIL_USE_TLS=True
   DEFAULT_FROM_EMAIL=noreply@example.com
   ```

3. **Restart the server:**

   ```bash
   .\make down
   .\make up
   ```

4. **Register for an event:**

   * Log in via the `/api/token/` endpoint.
   * Send a POST request to `/api/events/events/{id}/register/` with your JWT token.

5. **Verify email:**

   * Go to your Mailtrap inbox.
   * You should see a message with subject "Registration Confirmation".

---

🛠 If you want to change email content or logic, see `events/views.py` where the `send_mail(...)` function is called after registration.


## 📝 API Endpoints

* `POST /api/token/` — obtain JWT
* `POST /api/token/refresh/` — refresh JWT
* `GET /api/events/events/` — list events
* `POST /api/events/events/` — create event
* `POST /api/events/events/{id}/register/` — register for an event

---

📦 Uses Poetry for dependency management. Jazzmin enhances admin interface. See `.env.sample` for required configs.
