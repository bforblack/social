from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
from pydantic import BaseModel,Field
from datetime import datetime
import bson

class Sage(BaseModel):
    _id:Optional[str]

    @abstractmethod
    def getuserData(self):
     pass


    def __generateID(self):
        pass




