from enum import StrEnum


class Prompt(StrEnum):
    CODE_REVIEW_TEMPLATE = """
        ### Instructions ###\n
        You are given the initial assignment, github repo contents and candidate level.
        You must write a review on the task, estimate it with a mark (1 being the worst result, 
        5 being the best result)according to the given candidate level and write overall 
        conclusion about the task.
        Pay attention to project structure, code quality and code readability.
        
        Candidate level:
        {candidate_level}
        
        Assignment:
        {assignment}
        
        Repo contents:
        {repo_contents}
    """

    CODE_REVIEW_ASSISTANT = """
        ### Formatting Instructions ###\n
        Return review result as a Python dict with keys being 'review', 'mark' and 'conclusion' 
        with their values as generated values for these keys.
    """
