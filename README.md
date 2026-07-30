# Automated UAT/PROD Update Notification System

## Overview

The **Automated UAT/PROD Update Notification System** is a Django-based automation tool that sends email notifications to active users whenever the UAT (User Acceptance Testing) or Production (PROD) environment is updated.

Instead of manually composing and sending emails, the application reads user information and email templates from an Excel file, personalizes the email for each active user, and sends HTML emails automatically.

---

## Features

- Read user details from an Excel workbook.
- Separate user lists for UAT and PROD environments.
- Send notifications only to active users.
- Read email subject and HTML body from the Excel template.
- Personalize emails by replacing **[Name]** with the recipient's name.
- Send HTML emails using Django's email framework.
- Trigger notifications using a simple Django management command.
- Supports both Console Email Backend (testing) and SMTP Email Backend (live emails).
- Validates email addresses using Regular Expressions before sending notifications.

---

## Tech Stack

- Python 3
- Django
- Pandas
- OpenPyXL
- SMTP (Gmail)

---

## Project Structure

```
Notifier/
│
├── AutomatedNotification/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── notifier/
│   ├── excel_reader.py
│   ├── email_sender.py
│   ├── services.py
│   ├── management/
│   │   └── commands/
│   │       └── notify.py
│   └── ...
│
├── UseCase__002_.xlsx
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Excel Workbook

The application uses an Excel workbook named:

```
UseCase__002_.xlsx
```

### Sheet 1 : UATUser

| Name | Email | IsActive |
|------|-------|----------|
| John | john@example.com | Yes |

---

### Sheet 2 : ProdUser

| Name | Email | IsActive |
|------|-------|----------|
| Alice | alice@example.com | Yes |

---

### Sheet 3 : Email Format

| Subject | Body |
|----------|------|
| UAT Update | HTML Email Body |
| PROD Update | HTML Email Body |

---

## Installation

Clone or download the project.

Create a virtual environment.

```
python -m venv venv
```

Activate it.

Windows

```
venv\Scripts\activate
```

Install dependencies.

```
pip install -r requirements.txt
```

---

## Email Configuration

Create a `.env` file in the project root.

Example:

```env
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

> Use a Gmail App Password instead of your Gmail account password.

---

## Running the Project

### Send UAT Notifications

```
py manage.py notify UAT
```

### Send PROD Notifications

```
py manage.py notify PROD
```

---

## How It Works

1. Read the Excel workbook.
2. Select the required sheet (UATUser or ProdUser).
3. Filter only active users.
4. Read the corresponding email template.
5. Replace **[Name]** with the recipient's name.
6. Send HTML emails using Django's email backend.
7. Display the notification summary.

---

## Example Workflow

```
py manage.py notify UAT
        │
        ▼
Read UATUser Sheet
        │
        ▼
Filter Active Users
        │
        ▼
Read Email Template
        │
        ▼
Replace [Name]
        │
        ▼
Send HTML Email
        │
        ▼
Recipient Inbox
```

---

## Configuration

For testing:

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

For live emails:

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
```

---

## Future Enhancements

- Scheduled email notifications using Django Commands and Task Scheduler/Cron.
- Logging of sent emails.
- Admin dashboard for managing users.
- Upload Excel files through the web interface.
- Support for multiple notification templates.

---