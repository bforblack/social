from pydantic import BaseModel
from typing import Any, Optional

#update variables as per need

class Instagram(BaseModel):
    access_token: Any
    app_id: Any
    Object: Optional[Any]