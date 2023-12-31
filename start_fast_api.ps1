# Set environment variables
$env:ADMIN_SECRET = 'YourSecret'
$env:DATABASE_URL = 'sqlite:///blog_website.db'
$env:RECAPTCHA_SITE_KEY = "YourSiteKey"
$env:RECAPTCHA_SECRET_KEY = "YourSecretKey"
$env:GMAIL_PASSWORD = "YourGmailPassword"
$env:GMAIL_USERNAME = "YourGmailUsername"

# Run the application with Poetry
poetry run tailwindcss -i app.css -o .\blog_website\static\css\tailwind.css --minify
poetry run uvicorn blog_website.main:app --reload
