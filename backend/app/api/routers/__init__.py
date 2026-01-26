from .organizations import router as organizations_router
from .parties import router as parties_router
from .people import router as people_router

__all__ = [
    "organizations_router",
    "parties_router",
    "people_router",
]
