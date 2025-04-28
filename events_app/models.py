"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
from enum import Enum

class EventType(Enum):
    PARTY = 'Party'
    STUDY = 'Study'
    NETWORKING = 'Networking'
    OTHER = 'Other'

guest_event_table = db.Table('guest_event_table',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'), primary_key=True)
)

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20))
    events_attending = db.relationship(
        'Event', 
        secondary=guest_event_table,
        back_populates='guests'
    )
    
    def __repr__(self):
        return f'<Guest: {self.name}>'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    date_and_time = db.Column(db.DateTime, nullable=False)
    event_type = db.Column(db.Enum(EventType), default=EventType.OTHER)
    guests = db.relationship(
        'Guest', 
        secondary=guest_event_table,
        back_populates='events_attending'
    )
    
    def __repr__(self):
        return f'<Event: {self.title}>'