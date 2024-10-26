from pydantic import BaseModel
import datetime


class EventPayload(BaseModel):
    title: str
    organizer: str
    opentime: datetime.datetime
    duration: datetime.datetime
    location: str


class EventJoinPayload(BaseModel):
    event_id: str
    user_name: str
    join: bool


class EventDeletePayload(BaseModel):
    event_id: str
