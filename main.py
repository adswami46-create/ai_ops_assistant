from fastapi import FastAPI
from pydantic import BaseModel
from agents.planner import plan
from agents.executor import execute
from agents.verifier import verify

app = FastAPI()

class TaskRequest(BaseModel):
    task: str

@app.post("/run")
def run_task(req: TaskRequest):
    plan_json = plan(req.task)
    execution_results = execute(plan_json)
    final_output = verify(req.task, execution_results)

    return {
        "plan": plan_json,
        "results": execution_results,
        "final_answer": final_output
    }
