import uuid
from datetime import datetime

from pydantic import BaseModel, Field


# Events

class EventCreate(BaseModel):
    event_type: str = Field(..., min_length=1, max_length=255, examples=["order.placed"])
    payload: dict = Field(..., examples=[{"order_id": "123", "amount": 99.99}])
    source: str | None = Field(None, max_length=100, examples=["order-service"])


class EventResponse(BaseModel):
    event_id: uuid.UUID
    status: str = "accepted"


class EventDetail(BaseModel):
    id: uuid.UUID
    event_type: str
    payload: dict
    source: str | None
    created_at: datetime

    model_config = {"from_attributes": True}


# Notifications

class NotificationOut(BaseModel):
    id: uuid.UUID
    event_id: uuid.UUID
    title: str
    body: str | None
    is_read: bool
    read_at: datetime | None
    created_at: datetime

    model_config = {"from_attributes": True}


class NotificationList(BaseModel):
    items: list[NotificationOut]
    total: int


class UnreadCount(BaseModel):
    count: int


# Subscriptions

class SubscriptionCreate(BaseModel):
    pattern: str = Field(..., min_length=1, max_length=255, examples=["order.*"])


class SubscriptionOut(BaseModel):
    id: uuid.UUID
    pattern: str
    created_at: datetime

    model_config = {"from_attributes": True}


# WebSocket messages

class WSMessage(BaseModel):
    type: str
    pattern: str | None = None
    data: dict | None = None
