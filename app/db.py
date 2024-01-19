from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database connection URL and creating SQLAlchemy Engine.

# DB_URL = "mysql+pymysql://root@127.0.0.1:3306/lms"
DB_URL = "sqlite:///./libraryMS.db" 

engine = create_engine(DB_URL)
Base=declarative_base()

SessionLocal=sessionmaker(autocommit=False,bind=engine)

