from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import get_settings

data_secret = get_settings()
DB_URL = (
    f"postgresql://{data_secret.db_user}:{data_secret.db_password}"
    f"@{data_secret.db_host}:{data_secret.db_port}/{data_secret.db_name}"
)

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
