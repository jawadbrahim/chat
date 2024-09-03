from database.postgres import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
import datetime
from dataclasses import dataclass
import pytz

@dataclass
class Qa(db.Model):
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(pytz.timezone('GMT')))
    