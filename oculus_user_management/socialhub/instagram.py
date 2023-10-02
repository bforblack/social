from pydantic import BaseModel
from typing import Any, Optional


class Instagram(BaseModel):
    accessToken: Optional[str]
    appId: Optional[str]
    Object: Optional[str]
