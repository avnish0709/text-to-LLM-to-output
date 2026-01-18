Text-to-LLM-to-Output (AI Pipeline Backend)

This is my first backend project where I connected a visual drag-and-drop AI pipeline builder (ReactFlow frontend) with a FastAPI backend.
The backend receives nodes and edges from the UI and returns:
1.)   Total number of nodes
2.)   Total number of edges
3.)   Whether the pipeline forms a valid DAG
The frontend can be completely changed or redesigned — the backend works independently as long as it receives the JSON structure.


Features

FastAPI backend
CORS enabled (so any UI can connect)
Receives pipeline data (nodes + edges)
Performs simple DAG validation
Returns results as JSON


How it Works
1.)  The user builds a pipeline on the frontend (Input → LLM → Output).
2.)  The frontend sends the pipeline to /pipelines/parse.
3.)  The backend receives the pipeline and analyzes it.
4.)  The backend responds with counts + DAG status.

This project helped me learn:
a)  API creation
b) Frontend → Backend communication

JSON handling

Basic AI pipeline structure
