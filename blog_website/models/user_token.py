from datetime import datetime, timedelta, timezone

from blog_website.models.base import CommonBase
from blog_website.models.user import User
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class UserToken(CommonBase):
    __tablename__ = "user_tokens"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    token = Column(String(255), nullable=False)
    expires_at = Column(
        DateTime, nullable=False, default=datetime.now(timezone.utc) + timedelta(days=7)
    )

    user = relationship("User", back_populates="tokens")
