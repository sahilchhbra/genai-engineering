from pydantic import BaseModel, ValidationError


class Candidate(BaseModel):
    name: str
    email: str
    skills: list[str]
    experience: int


candidate_data = {
    "name": "Rahul Sharma",
    "email": "rahul@mail.com",
    "skills": ["JAVA", "python"],
    "experience": 3,
}

try:
    candidate = Candidate.model_validate(candidate_data)
    print("VALID CANDIDATE:")
    print(candidate)
    print("NAME:", candidate.name)
    print("EMAIL:", candidate.email)
    print("EXPERIENCE:", candidate.experience)

except ValidationError as error:
    print("Validation failed")
    print(error)



invalid_candidate_data = {
    "name": "Rahul Sharma",
    "email": "rahul@mail.com",
    "skills": ["JAVA", "python"],
    "experience": "three",
}


try:
    candidate = Candidate.model_validate(invalid_candidate_data)
    print("INVALID CANDIDATE:")
    print(candidate)
except ValidationError as error:
    print("Validation failed")
    print(error)
