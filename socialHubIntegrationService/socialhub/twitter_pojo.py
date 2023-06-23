from pydantic import BaseModel
from typing import Any, Optional

class Twitter(BaseModel):
    access_token: Any
    app_id: Any
    Object: Optional[Any]
