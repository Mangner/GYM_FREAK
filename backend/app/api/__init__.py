from fastapi import APIRouter

from .routers import organizations_router, parties_router, people_router

router = APIRouter()
router.include_router(people_router)
router.include_router(organizations_router)
router.include_router(parties_router)

__all__ = ["router"]
