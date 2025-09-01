from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from utils import predict_career
from database import skills_collection

roadmap_router = APIRouter()

class SkillSelection(BaseModel):
    skills: list[str]
    career: str

career_skills = {
    "Data Scientist": ["Python", "Machine Learning", "SQL", "Deep Learning", "Pandas"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Node.js"],
    "Frontend Developer": ["HTML", "CSS", "React", "JavaScript"],
    "Backend Developer": ["Node.js", "Express.js", "MongoDB", "API Development"],
    "AI Engineer": ["Python", "TensorFlow", "Deep Learning", "Computer Vision"],
    "Machine Learning Engineer": ["Python", "Scikit-Learn", "TensorFlow", "Data Preprocessing"],
    "Cyber Security Specialist": ["Ethical Hacking", "Network Security", "Python", "Linux"],
    "Full Stack Developer": ["HTML", "CSS", "JavaScript", "MongoDB", "Node.js"],
    "Cloud Engineer": ["AWS", "Azure", "Cloud Security", "Linux"]
}

@roadmap_router.post("/generate")
async def generate_roadmap(skill_selection: SkillSelection):
    if skill_selection.career not in career_skills:
        raise HTTPException(status_code=404, detail="Career not found")

    all_skills = career_skills[skill_selection.career]
    missing_skills = list(set(all_skills) - set(skill_selection.skills))

    return {"missing_skills": missing_skills}
