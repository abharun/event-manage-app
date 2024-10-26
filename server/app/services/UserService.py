from app.db.dbconnect import SessionLocal
from app.db.schemas import UserSchema
from app.models.user import UserModel

dbHandler = SessionLocal()


async def get_single_user(id: int):
    return dbHandler.query(UserSchema).filter(UserSchema.id == id).first()


async def auth_user(username: str):
    try:
        exist_user = (
            dbHandler.query(UserSchema).filter(UserSchema.username == username).first()
        )
        return exist_user if exist_user else False
    except Exception:
        return False


async def get_multi_users(page: int, perpage: int):
    offset = (page - 1) * perpage
    return dbHandler.query(UserSchema).offset(offset).limit(perpage).all()


async def insert_user(user_info: UserModel):
    try:
        new_user = UserSchema(
            username=user_info.username,
        )
        dbHandler.add(new_user)
        dbHandler.commit()
        return True
    except Exception:
        return False


async def delete_user(id: int):
    try:
        user = dbHandler.query(UserSchema).filter(UserSchema.id == id).first()
        if user:
            dbHandler.delete(user)
            dbHandler.commit()
            return True
        else:
            return False
    except Exception:
        return False
