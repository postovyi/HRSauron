from fastapi import APIRouter

from app.schemas.ai import ReviewInputSchema, ReviewOutputSchema
from app.services.ai import ai_review

router = APIRouter(prefix='/code-review', tags=['Review'])


@router.post('/review', response_model=ReviewOutputSchema)
async def review(data: ReviewInputSchema) -> ReviewOutputSchema:
    return await ai_review.review(data)
