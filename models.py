from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (Integer,
                        Numeric,
                        Float,
                        ForeignKey,
                        String,
                        Text,
                        Column,
                        Date,
                        Boolean,
                        DateTime,
                        BigInteger,
                        SmallInteger,
                        ARRAY,
                        UniqueConstraint)


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    birth_date = Column(Date)
    path_to_photo = Column(String)
    email = Column(String)
    name = Column(String)
    surname = Column(String)
    sex = Column(Boolean)
    phone_number = Column(String)
    is_activated = Column(Boolean)
    activation_uuid = Column(String)
    activation_uuid_date = Column(DateTime)
    restore_uuid = Column(String)
    restore_uuid_date = Column(DateTime)
    vk_id = Column(Integer)
    google_id = Column(Numeric(21, 0))
    new_email = Column(String)
    email_update_uuid = Column(String)
    email_update_uuid_date = Column(DateTime)
    registration_date = Column(DateTime)
    active = Column(Boolean)
