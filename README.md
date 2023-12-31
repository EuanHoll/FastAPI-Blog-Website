# FastAPI Blog Website

Welcome to the FastAPI Blog Website, a high-performance blog platform built using [FastAPI](https://fastapi.tiangolo.com/), styled with [Tailwind CSS](https://tailwindcss.com/), powered by [Jinja](https://jinja.palletsprojects.com/en/3.1.x/), and enhanced with a touch of [HTMX](https://htmx.org/).

## Key Features

Experience the power of FastAPI and enjoy these remarkable features:

- **Blazing Fast**: Boasting remarkable speed, FastAPI rivals the performance of NodeJS and Go.
- **User-Friendly**: Designed with simplicity in mind, it's easy to use and learn, making it accessible for developers of all levels.
- **Server Side Rendering**: We've leveraged server-side rendering to ensure top-notch performance and user experience.
- **All-In-One Solution**: With the exception of a Gmail and reCAPTCHA account, everything you need is contained within this project.
- **Admin Panel**: Easily manage your blog posts, contact requests, and admin users with the integrated Markdown editor.

## Installation

Get your FastAPI Blog Website up and running with these simple steps:

### 1. Clone the Repository

Begin by cloning this repository to your local machine. You can do this by executing the following command:

```shell
git clone https://github.com/EuanHoll/FastAPI-Blog-Website.git fastapi_blog_website
```

### 2. Navigate to the Project Folder

Move to the project's root folder using your terminal or command prompt:

```shell
cd fastapi_blog_website
```

### 3. Install Dependencies

We recommend using Poetry for dependency management. If you don't have Poetry installed, please follow the [official Poetry installation guide](https://python-poetry.org/docs/) to set it up on your system.

Once you have Poetry ready, install the project dependencies with a single command:

```shell
poetry install
```

Alternatively, you can choose to install dependencies using the `requirements.txt` file. However, please note that this approach may not always keep your dependencies up to date.

### 4. Set Environment Variables

Ensure that your project functions correctly by setting the necessary environment variables. You can do this by exporting the following variables in your terminal:

```shell
export ADMIN_SECRET='YourSecret'
export DATABASE_URL='sqlite:///website.db'
export RECAPTCHA_SITE_KEY='YourSiteKey'
export RECAPTCHA_SECRET_KEY='YourSecretKey'
export GMAIL_PASSWORD='YourGmailPassword'
export GMAIL_USERNAME='YourGmailUsername'
```

Please be cautious when setting these variables, as there are default values provided in each of the startup scripts. Make sure to replace them with your specific configurations.


### 5. Provide Icons
The following files are missing from the FastAPI Blog Website project and need to be provided:

1. `blog_website\static\images\logo.webp`
2. `blog_website\static\android-chrome-192x192.webp`
3. `blog_website\static\android-chrome-512x512.webp`
4. `blog_website\static\apple-touch-icon.png`
5. `blog_website\static\favicon-16x16.png`
6. `blog_website\static\favicon-32x32.png`
7. `blog_website\static\favicon.ico`

These files are essential for the proper functioning and appearance of the website. These are not included with this project, the site will run without them, however you will see issues. These should be the logo of your site.

## Usage

Running the FastAPI server and managing your FastAPI Blog Website is a breeze. Here's a simple guide to get you started:

### Starting the FastAPI Server

Choose the appropriate command for your operating system:

- **Unix-based Systems**:
  
  Open your terminal and execute the following command:

  ```shell
  sh start_fast_api.sh
  ```

- **Windows Systems**:

  Use PowerShell and run this command:

  ```powershell
  ./start_fast_api.ps1
  ```

Once the server is up and running, you're ready to explore your website.

### Accessing Your Website

Open your web browser and enter the following URL:

```
http://localhost:8000
```

You'll be greeted by your FastAPI Blog Website, ready for exploration.

### Live Tailwind CSS Compilation (Development)

During development, you can enable live Tailwind CSS compilation for a smoother experience. To do this:

- **Unix-based Systems**:

  Run the following command in your terminal:

  ```shell
  sh start_tailwind.sh
  ```

- **Windows Systems**:

  In PowerShell, execute this command:

  ```powershell
  ./start_tailwind.ps1
  ```

Please note that enabling live Tailwind CSS compilation is not necessary for simply running the site but can significantly enhance your development workflow.

## First Time Setup

To make the most of your admin panel and secure your FastAPI Blog Website, follow these initial steps:

### Admin Panel URL Customization

By default, the admin panel is accessible at `/best_admin`. If you wish to customize the URL, navigate to the `defaults.py` file and make the desired changes.

### Accessing the Admin Panel

To get started, use the default admin account with the following credentials:

- **Username**: admin
- **Password**: admin

For security reasons, we strongly recommend creating a custom admin account and deleting the default one.

Enjoy managing your FastAPI Blog Website effortlessly and securely!


## License

This project is licensed under the [MIT License with Attribution](LICENSE).

Copyright (c) [2023] [EuanHoll]
