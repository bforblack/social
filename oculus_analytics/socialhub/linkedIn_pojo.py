from pydantic import BaseModel
from typing import Any, Optional

#update variables as per need

class LinkedIn(BaseModel):
    access_token: Any
    app_id: Any
    Object: Optional[Any]
