import json
import jsonschema
from llm.openai_client import call_llm
from schemas.plan_schema import PLAN_SCHEMA

PLANNER_PROMPT = """
You are a Planner Agent.
Break the user task into steps.
Each step must include: step_number, action, tool.
Available tools: weather, github.
Return ONLY valid JSON.
"""

def plan(user_input: str):
    response = call_llm(PLANNER_PROMPT + "\nUser task: " + user_input)
    plan_json = json.loads(response)
    jsonschema.validate(instance=plan_json, schema=PLAN_SCHEMA)
    return plan_json
