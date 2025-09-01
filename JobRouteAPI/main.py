from routes.roadmap import roadmap_router
from fastapi import FastAPI
from routes.auth import auth_router
from routes.users import user_router
from routes.skills import skill_router

app = FastAPI()

# Including Routers with Correct Prefixes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(skill_router, prefix="/skills", tags=["Skills"])
app.include_router(roadmap_router, prefix="/roadmap", tags=["Roadmap"])


@app.get("/")
def root():
    return {"message": "Welcome to JobRoute API"}

# Health Check API
@app.get("/health")
def health_check():
    return {"status": "Server is Running"}
