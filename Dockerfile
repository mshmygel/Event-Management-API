FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --upgrade pip \
    && pip install poetry

# Copy pyproject.toml, lock file and README
COPY pyproject.toml poetry.lock* README.md /app/

# Install dependencies (without installing current project as package)
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copy project files
COPY . /app/

# Debug: List files to confirm structure (can be removed later)
RUN ls -la /app && ls -la /app/event_managment_api || true

# Expose port
EXPOSE 8000

# Run the application (development server)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

