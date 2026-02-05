from llm.openai_client import call_llm

VERIFIER_PROMPT = """
You are a Verifier Agent.
Check results for missing or failed steps.
Then produce a clean final answer.
"""

def verify(user_task, results):
    return call_llm(
        VERIFIER_PROMPT +
        f"\nTask: {user_task}\nResults: {results}"
    )
