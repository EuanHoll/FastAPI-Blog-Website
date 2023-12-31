from blog_website.models.base import CommonBase
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class BlogPost(CommonBase):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    preview = Column(Text)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"))
    is_published = Column(Boolean, default=False)

    author = relationship("User", back_populates="blog_posts")

    def __repr__(self):
        return f"<BlogPost {self.title}>"

    def __str__(self):
        return self.title

    def get_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "preview": self.preview,
            "content": self.content,
            "author_id": self.author_id,
        }
