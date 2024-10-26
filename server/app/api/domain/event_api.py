from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.api.payloads.event import EventPayload, EventJoinPayload
from app.services import EventService

event_api = APIRouter()


@event_api.get("/")
async def get_events():
    result = await EventService.get_event_list()
    return result if result else []


@event_api.post("/new")
async def create_event(new_event: EventPayload):
    result = await EventService.create_new_event(new_event=new_event)
    if result:
        return JSONResponse(status_code=200, content=new_event)
    else:
        return JSONResponse(status_code=500, content={"status": "failed"})


@event_api.put("/attend")
async def attend_event(payload: EventJoinPayload):
    result = await EventService.attend_to_event(
        username=payload.user_name, event_id=payload.event_id, join=payload.join
    )
    if result:
        return JSONResponse(status_code=200, content={"status": "success"})
    else:
        return JSONResponse(status_code=500, content={"status": "failed"})


@event_api.delete("/")
async def delete_event(event_id: str):
    result = await EventService.delete_event(event_id)
    if result:
        return JSONResponse(status_code=200, content={"status": "success"})
    else:
        return JSONResponse(status_code=500, content={"status": "failed"})
