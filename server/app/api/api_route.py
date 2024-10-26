from fastapi import APIRouter
from app.api.domain.user_api import user_api as user_router
from app.api.domain.event_api import event_api as event_router

api_router = APIRouter()


@api_router.get("/health_check")
def health_check():
    return {"Message": "Server is Running"}


api_router.include_router(user_router, prefix="/user")
api_router.include_router(event_router, prefix="/event")
