from config import make_settings
from sqlalchemy import create_engine
from app import write

def main():
  settings = make_settings()
  settings.init()
  write.insert_data()
  




if __name__ == "__main__":
    main()