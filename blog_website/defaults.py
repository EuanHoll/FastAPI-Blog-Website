import os
from datetime import datetime

from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from blog_website.models import CommonBase

engine = create_engine(os.environ["DATABASE_URL"])
CommonBase.metadata.create_all(engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


default_jinja_config = {
    "site_name": "My Blog",
    "current_year": datetime.now().year,
    "recaptcha_site_key": os.environ["RECAPTCHA_SITE_KEY"],
}

recaptcha_secret_key = os.environ["RECAPTCHA_SECRET_KEY"]
is_a_bot_threshold = 0.5

site_mapping = {
    "blog_posts": "/blog_posts",
    "view_blog_post": "/blog_posts/{id}",
    "about": "/about",
    "contact": "/contact",
    "home": "/",
    "admin": "/best_admin",
}

templates = Jinja2Templates(
    directory=os.path.join(os.path.dirname(__file__), "templates")
)

gmail_username = os.environ["GMAIL_USERNAME"]
gmail_password = os.environ["GMAIL_PASSWORD"]
