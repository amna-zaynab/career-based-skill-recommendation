from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

class Career(BaseModel):
    career_name: str
    skills: list[str]

class Skill(BaseModel):
    skill_name: str
    career_id: str