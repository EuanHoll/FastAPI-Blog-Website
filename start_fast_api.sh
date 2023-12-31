#!/bin/bash

# Set environment variables
export ADMIN_SECRET='YourSecret'
export DATABASE_URL='sqlite:///website.db'
export RECAPTCHA_SITE_KEY='YourSiteKey'
export RECAPTCHA_SECRET_KEY='YourSecretKey'
export GMAIL_PASSWORD='YourGmailPassword'
export GMAIL_USERNAME='YourGmailUsername'

# Run the application with Poetry
poetry run tailwindcss -i app.css -o .\blog_website\static\css\tailwind.css --minify
poetry run uvicorn blog_website.main:app --reload
