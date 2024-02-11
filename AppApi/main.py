import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from AppApi.routers import app
app = FastAPI()

app.include_router(app.GeminiRouter.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run(app)