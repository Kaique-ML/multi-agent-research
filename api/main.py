"""FastAPI API para o sistema multi-agente."""
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import uuid
import asyncio

app = FastAPI(title="Multi-Agent Research System")

tasks_store: dict = {}


class ResearchRequest(BaseModel):
    topic: str
    depth: str = "standard"


@app.post("/research")
async def start_research(req: ResearchRequest, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    tasks_store[task_id] = {"status": "processing", "result": None}
    background_tasks.add_task(_run_research, task_id, req.topic, req.depth)
    return {"task_id": task_id, "status": "processing", "estimated_time_seconds": 240}


@app.get("/research/{task_id}")
async def get_research(task_id: str):
    if task_id not in tasks_store:
        return {"error": "Task não encontrada"}
    return {"task_id": task_id, **tasks_store[task_id]}


async def _run_research(task_id: str, topic: str, depth: str):
    try:
        from crew.research_crew import ResearchCrew
        crew = ResearchCrew(topic=topic, depth=depth)
        result = crew.run()
        tasks_store[task_id] = {"status": "completed", "result": str(result)}
    except Exception as e:
        tasks_store[task_id] = {"status": "failed", "error": str(e)}
