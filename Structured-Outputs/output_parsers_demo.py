from langchain_core.messages import AIMessage
from langchain_core.output_parsers import (StrOutputParser, JsonOutputParser, PydanticOutputParser )
from langchain_classic.output_parsers import (ResponseSchema, StructuredOutputParser)
from pydantic import BaseModel, Field

from structured_output_basics import json_response

# model_response = AIMessage(
#
#     content="Python is a programming language.",
# )
#
# parser = StrOutputParser()
#
# result = parser.invoke(model_response)
#
# print("Parsed result: ", result)
# print("Output Type: ", type(result))


# json_response = """ {
#     "name": "Rahul Sharma",
#     "email": "rahul@mail.com",
#     "skills": ["JAVA", "python"],
#     "experience": 3
# }
# """
#
# json_parser = JsonOutputParser()
#
#
# parsed_data = json_parser.invoke(json_response)
#
# print("\n Parsed JSON: ", parsed_data)
# print("Output Type: ", type(parsed_data))
# print("Candidate name: ", parsed_data["name"])
# print("Candidate email: " , parsed_data["email"])


# response_schemas = [
#
#     ResponseSchema(
#         name="name",
#         description="The candidate's full name"
#     ),
#     ResponseSchema(
#         name="experience",
#         description="The candidate's experience in years as number"
#     ),
# ]
#
# structured_parser = StructuredOutputParser.from_response_schemas(response_schemas)
#
#
# format_instructions = structured_parser.get_format_instructions()
#
#
# print("\n Format instructions:")
# print(format_instructions)
#
#
# sample_response = """
# {
#     "name": "Rahul sharma",
#     "experience": "3"
# }
# """
#
# structured_data = structured_parser.parse(sample_response)
#
# print("\n Structured Data", structured_data)
# print("Candidate: ", structured_data["name"])
# print("Experience: ", structured_data["experience"])










class CandidateInfo(BaseModel):
    name: str = Field(description="The full name of the candidate")
    experience: int = Field(description="The experience of the candidate in years")
    skills: list[str] = Field(description="The technical skills of the candidate")


pydanctic_parser = PydanticOutputParser(
    pydantic_object=CandidateInfo
)

print("\n Pydantic format instrctions")

print(pydanctic_parser.get_format_instructions())

sample_candidate_response = """"{
    "name": "Rahul Sharma",
    "experience": "3",
    "skills": ["JAVA", "python"]
}"""


candidate_result = pydanctic_parser.parse(sample_candidate_response)

print("\n candidate_result")
print(candidate_result)

print("Candidate: ", candidate_result.name)
print("Experience: ", candidate_result.experience)
print("Skills ", candidate_result.skills)
print("Object type ", type(candidate_result))

