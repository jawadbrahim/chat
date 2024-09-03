from dataclasses import dataclass
import uuid
from datetime import datetime
@dataclass
class Create_Qa:
    id:uuid.UUID
    question:str
    answer:str
    created_at:datetime