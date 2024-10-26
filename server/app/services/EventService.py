from app.db.dbconnect import SessionLocal
from app.db.schemas import EventSchema
from app.api.payloads.event import EventPayload

dbHandler = SessionLocal()


async def get_event_list():
    try:
        return dbHandler.query(EventSchema).all()
    except Exception:
        return False


async def create_new_event(new_event: EventPayload):
    try:
        event = EventSchema(
            title=new_event.title,
            organizer=new_event.organizer,
            opentime=new_event.opentime,
            duration=new_event.duration,
            location=new_event.location,
            joiners=[],
        )
        dbHandler.add(event)
        dbHandler.commit()
        return True
    except Exception:
        return False


async def attend_to_event(username: str, event_id: str, join: bool):
    try:
        event = dbHandler.query(EventSchema).filter(EventSchema.id == event_id).first()
        if join:
            event.joiners.append(username)
        else:
            event.joiners.remove(username)
        dbHandler.commit()
        return True
    except Exception:
        return False


async def delete_event(event_id: str):
    try:
        event = dbHandler.query(EventSchema).filter(EventSchema.id == event_id).first()
        dbHandler.delete(event)
        dbHandler.commit()
        return True
    except Exception:
        return False
