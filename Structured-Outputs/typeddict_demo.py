from typing import TypedDict


class Candidate(TypedDict):
    name: str
    email: str
    skills: list[str]
    experience: int


candidate = Candidate = {
    "name": "Rahul Sharma",
    "email": "rahul@mail.com",
    "skills": ["JAVA", "python"],
    "experience": 3,
}

print("Candidate: ", candidate)
print("NAME:", candidate["name"])
print("EMAIL:", candidate["email"])
print("SKILLS:", candidate["skills"])
print("EXPERIENCE:", candidate["experience"])
