from pydantic import BaseModel, Field

from app.enums import CandidateLevel


class ReviewInputSchema(BaseModel):
    assignment: str
    openai_token: str
    repo_url: str
    candidate_level: CandidateLevel


class ReviewOutputSchema(BaseModel):
    mark: int = Field(..., ge=0, le=5)
    review: str
    conclusion: str
