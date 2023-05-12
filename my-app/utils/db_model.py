from utils.config import BASE
from sqlalchemy import (
    INTEGER,
    Column,
    DateTime,
    ForeignKey,
    String,
)


class Account(BASE):
    __tablename__ = "ACCOUNT"

    ID = Column(String(200), primary_key=True, nullable=False)
    Email = Column(String(50), nullable=False, unique=True)
    Password = Column(String(500), nullable=False)
    Name = Column(String(50), nullable=False)
    Gender = Column(String(50))
    Create_time = Column(DateTime)
    Last_login_time = Column(DateTime)


class Post(BASE):
    __tablename__ = "POST"

    ID = Column(String(200), primary_key=True, nullable=False)
    Account_id = Column(String(200), ForeignKey("ACCOUNT.ID"))
    Type = Column(String(50), nullable=False)
    Title = Column(String(200), nullable=False)
    Content = Column(String(255))
    Location = Column(String(50))
    Limit_member = Column(INTEGER)
    Create_time = Column(DateTime, nullable=False)  # 文章建立時間
    Start_time = Column(DateTime, nullable=False)  # 活動開始時間
    End_time = Column(DateTime, nullable=False)  # 活動結束時間
    Close_time = Column(DateTime, nullable=False)  # 報名結束時間


class PostParticipant(BASE):
    __tablename__ = "POST_PARTICIPANT"

    Post_id = Column(String(200), ForeignKey("POST.ID"), primary_key=True, nullable=False)
    Account_id = Column(String(200), ForeignKey("ACCOUNT.ID"), primary_key=True, nullable=False)


# 註解：因為這些資料是直接用匯入資料庫的，所以暫時用不到
class Weather(BASE):
    __tablename__ = "WEATHER"

    ID = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    StartTime = Column(DateTime)
    Wx = Column(String(50))
    PoP3h = Column(String(100))
    Temperature = Column(INTEGER)


# class MedicalArticles(BASE):
#     __tablename__ = "MEDICAL_ARTICLES"

#     ID = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
#     Title = Column(String(255))
#     Author = Column(String(50))
#     Article = Column(String(5000))
#     Url = Column(String(255))
