# ReviewSystem

**By Antonio Martin**

This project is a complete application for a business review system. It allows users to explore businesses, view details, and leave ratings and comments. 
The main goal is notify to Bussiness's owner when it has a bad review.
The implementation includes a Django backend and a Next.js frontend, with a Docker configuration for deploying the backend.

## Demo

https://github.com/user-attachments/assets/236cf297-bc0e-4815-8dbc-7b371e6c9885

## Technologies

- **Backend**: Django, Django REST Framework, Celery, Redis (for background task processing)
- **Frontend**: Next.js (React)
- **Database**: SQLite for development (recommended PostgreSQL for production)
- **Containers**: Docker for backend deployment
- **Authentication and Permissions**: Basic user management in Django
  
## Features

- **Business Exploration**: A list of businesses with details and average ratings.
- **Ratings and Reviews**: Users can rate and comment on businesses.
- **Automated Notifications**: Sends alerts (using Celery and Redis) when a business receives a low rating.
- **User-Friendly Interface**: The frontend in Next.js provides a UI with star ratings and business search.
- **Docker Deployment (Backend)**: Docker configuration isolates the backend and its dependencies.


## Installation & Setup

### Backend (Django)

1. Clone the repository and navigate to the backend folder:

   ```bash
   git clone https://github.com/antoniomd-fi/ReviewSystem
   cd review_system_backend

2. Set Up Environment Variables
   - In the review_system_backend folder, create a .env file with the following configuration:
    ```env
      DEBUG=1
      CELERY_BROKER_URL=redis://redis:6379/0
      CELERY_RESULT_BACKEND=redis://redis:6379/0

      # Twilio Credentials
      TWILIO_ACCOUNT_SID=<Your Twilio Account SID>
      TWILIO_AUTH_TOKEN=<Your Twilio Auth Token>
      TWILIO_PHONE_NUMBER=<Your Twilio Phone Number>

      # SMTP Credentials for Email Notifications
      EMAIL_HOST=<Your SMTP Host>
      EMAIL_PORT=<Your SMTP Port>
      EMAIL_HOST_USER=<Your Email Username>
      EMAIL_HOST_PASSWORD=<Your Email Password>
      EMAIL_USE_TLS=True  # Set to False if your SMTP provider does not use TLS
    ```
   - Replace **Your Twilio Account SID**, **Your Twilio Auth Token**, **Your Twilio Phone Number**, and SMTP credentials with your actual credentials.
3. Step 3: Backend Setup (Docker)
    - Run the Docker container for the backend:
       ```bash
        docker-compose up --build
     This will set up and start the Django server along with Redis for task management. 
    - Once the server is running, apply migrations and create a superuser:
       ```bash
        docker-compose exec django_app python manage.py migrate
        docker-compose exec django_app python manage.py createsuperuser

4.  Frontend Setup (Manual)
    - Open a new terminal, navigate to the frontend folder, and install dependencies:
        ```bash
        cd review_system_frontend/review_system
        npm install
    - Start the frontend development server:
       ```bash
      npm run dev

## Usage

- Access the frontend at http://localhost:3000 to view and interact with businesses.
- Navigate to the backend admin panel at http://localhost:8000/admin to manage businesses, reviews, and users, also you can use postman or insomnia with the endpoints.
- Whenever a business receives a low rating, an automated notification (via SMS and email) will be sent to the business owner.

## Possible Improvements

- Full Dockerization: Integrate the frontend into Docker alongside the backend for a complete deployment setup.
- Enhanced Notifications: Implement WebSocket-based notifications for real-time alerts to the frontend.
- Authentication and Authorization: Introduce OAuth for third-party authentication and add a role-based permissions system.
- Production Database: Use PostgreSQL for production environments.
- Caching Optimization: Use caching to improve performance for frequently requested endpoints, such as the business list.
