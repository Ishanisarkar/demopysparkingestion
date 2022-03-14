import array
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import JSON, DateTime, String, Integer, Float
from sqlalchemy.orm import relationship

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
Base = declarative_base()

##### ----------------------------
##### User table information

class UsersOrm(Base):

  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  age = Column(Integer)
  birthdate = Column(String)
  city = Column(String)
  created_at = Column(DateTime, default=datetime.utcnow)
  sex = Column(String)
  lat = Column(Float)
  long = Column(Float)
  password = Column(String)
  utm_source = Column(String)
  utm_medium = Column(String)
  utm_campaign = Column(String)
  firstname = Column(String)
  lastname = Column(String)
  useragent = Column(String)
  misc = Column(String)

 # adds = relationship("AdsOrm", backref='users')
  user_referrer = relationship("ReferralsOrm")
 # ads_transaction = relationship("AdsTransactions", backref='ads_transactions')

class AdsOrm(Base):

  __tablename__ = "ads"
  index = Column(Integer, primary_key=True)
  owner_id = Column(Integer, ForeignKey('users.id'))
  title = Column(String)
  category = Column(String)
  price = Column(Float)
  city = Column(String)
  created_at = Column(DateTime, default=datetime.utcnow)
  deleted_at = Column(DateTime, default=datetime.utcnow)
  id = Column(Integer, primary_key=True)

  ##ads_transaction = relationship("AdsTransactions", backref='ads_transactions')


class ReferralsOrm(Base):
  __tablename__ = "referrals"

  id = Column(Integer, primary_key=True)
  referrer_user_id = Column(Integer, ForeignKey('users.id'))
  referree_user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default=datetime.utcnow)
  deleted_at = Column(DateTime, default=datetime.utcnow)

class AdsTransactions(Base):
  __tablename__ = "ads_transactions"

  id = Column(Integer, primary_key=True)
  ad_owner_id = Column(Integer, ForeignKey('users.id'))
  buyer_user_id = Column(Integer, ForeignKey('users.id'))
  ad_id = Column(Integer)
  sold_price = Column(Float)
  created_at = Column(DateTime, default=datetime.utcnow)



