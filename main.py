from fastapi import FastAPI
from pydantic import BaseModel

# ----------------------------------------------------
# CREATE THE APP
# ----------------------------------------------------
app = FastAPI()

# ----------------------------------------------------
# ENABLE CORS SO FRONTEND (localhost:3000 or 3001) CAN CALL BACKEND
# ----------------------------------------------------
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # allow all origins (React frontend)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------
# DATA MODEL
# ----------------------------------------------------
class PipelineData(BaseModel):
    nodes: list
    edges: list

# ----------------------------------------------------
# ROUTES
# ----------------------------------------------------
@app.get("/")
def read_root():
    return {"message": "Backend is running"}

@app.post("/pipelines/parse")
def parse_pipeline(data: PipelineData):
    # simple response for now
    return {
        "num_nodes": len(data.nodes),
        "num_edges": len(data.edges),
        "is_dag": True
    }
