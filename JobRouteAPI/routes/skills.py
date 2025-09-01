from fastapi import APIRouter, HTTPException
from models import Skill
from database import skills_collection
from utils import predict_career
from pydantic import BaseModel

skill_router = APIRouter()

class SkillInput(BaseModel):
    skills: str

@skill_router.post("/recommend")
async def recommend_skills(skill_input: SkillInput):
    try:
        # Ensure the input is a valid string
        if not isinstance(skill_input.skills, str):
            raise HTTPException(status_code=400, detail="Input must be a string.")

        prediction = predict_career(skill_input.skills)
        
        # Check if prediction is None or invalid
        if prediction is None:
            raise HTTPException(status_code=500, detail="Error in prediction.")

        return {"career_prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@skill_router.get("/get")
async def get_skills():
    skills = list(skills_collection.find({}, {"_id": 0}))
    return skills

@skill_router.post("/recommend")
async def recommend_skills(skill_input: SkillInput):
    prediction = predict_career(skill_input.skills)
    return {"career_prediction": prediction}
