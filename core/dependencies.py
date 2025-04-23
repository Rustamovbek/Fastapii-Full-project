from sqlalchemy.orm import Session
from typing import Annotated
from core.auth import get_current_user
from core.db_conf import get_db
from fastapi import Depends

DBSessionDep = Annotated[Session, Depends(get_db)]
CurrentUserDep = Annotated[dict, Depends(get_current_user)]
db_dependencies = Depends(get_db)