from app import db

from app.models import UserModel, RoleModel
from app.constants import app_constants

def create_user(email, password, name) -> UserModel:
    new_user = UserModel(name=name, email=email, password=password)
    role = RoleModel.query.get(app_constants.ROLE_USER)
    new_user.roles.append(role)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user