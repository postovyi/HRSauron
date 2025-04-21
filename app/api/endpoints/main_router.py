from fastapi import APIRouter

from app.api.endpoints.review import router as review_router

main_router = APIRouter(prefix='/api')
main_router.include_router(review_router)
