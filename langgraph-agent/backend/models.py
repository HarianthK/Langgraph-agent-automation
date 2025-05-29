from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class BusinessData(Base):
    __tablename__ = "business_data"

    id = Column(Integer, primary_key=True, index=True)
    zip_code = Column(String)
    city = Column(String)
    state = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    census_tract = Column(String)
    population = Column(Integer)
    country = Column(String)
    is_capital = Column(Boolean)
    business_description = Column(String)
    naics = Column(String)


# This is my real password 😬, don't use it.
DATABASE_URL = "postgresql://postgres:admin123@localhost:5432/business_data_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)
