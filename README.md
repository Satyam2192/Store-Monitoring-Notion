# Store-Monitoring

## Overview
This repository contains the code for a Django-based API that provides various endpoints for managing timezones, store status, business hours, and generating reports.

## Installation

### Prerequisites
- Django
- Django REST framework

### Setup Steps
1. Clone the repository:
   ```
   git clone https://github.com/Satyam2192/Store-Monitoring-Notion.git
   ```

2. Install required dependencies:
   ```
   pip install django djangorestframework
   ```

## Database Setup
1. Create database tables:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Import initial data:
   ```
   python manage.py import_data
   ```

## Usage

### Starting the Development Server
```
python manage.py runserver
```

### API Endpoints
- Timezones: `http://localhost:8000/api/v1/timezones`
- Store Status: `http://localhost:8000/api/v1/store_status`
- Business Hours: `http://localhost:8000/api/v1/business_hours`
- Trigger Report: `http://localhost:8000/api/v1/trigger_report/`
- Get Reports: `http://localhost:8000/api/v1/get-report/`
- Get Report Detail: `http://localhost:8000/api/v1/get-report/{report_id}/`
