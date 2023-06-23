from pydantic import BaseModel
from typing import Any, Optional

#update variables as per need

class Instagram(BaseModel):
    accessToken: Any
    appId: Any
    Object: Optional[Any]