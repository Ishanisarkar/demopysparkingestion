from models.init import create_all
from models.orm import UsersOrm


engine = create_all()

engine.query()