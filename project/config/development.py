from dataclasses import dataclass
import os
from dotenv import load_dotenv
load_dotenv()
@dataclass
class Development:
 SQLALCHEMY_DATABASE_URI= os.getenv("DATABASE_URI")
 API_KEY=os.getenv("API_KEY")