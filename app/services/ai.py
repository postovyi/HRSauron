from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI

from app.schemas.ai import ReviewInputSchema, ReviewOutputSchema
from app.config import settings
from app.enums.prompt import Prompt
from app.services.github import gh_service


class AIReview:
    @staticmethod
    async def review(data: ReviewInputSchema) -> ReviewOutputSchema:
        client = ChatOpenAI(
            openai_api_key=data.openai_token,
            model=settings.ai.MODEL_NAME,
            temperature=settings.ai.TEMPERATURE,
        )
        client = client.with_structured_output(schema=ReviewOutputSchema)
        prompt = ChatPromptTemplate.from_messages([
            ("system", settings.ai.SYSTEM_ROLE),
            ("human", Prompt.CODE_REVIEW_TEMPLATE),
            ("assistant", Prompt.CODE_REVIEW_ASSISTANT),
        ])
        files_with_content = await gh_service.get_repo_files(repo_full_name=data.repo_url)
        chain = prompt | client
        return await chain.ainvoke({
            "candidate_level": data.candidate_level,
            "assignment": data.assignment,
            "repo_contents": files_with_content
        })

ai_review = AIReview()