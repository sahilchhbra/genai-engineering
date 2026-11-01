import json

normal_resposne = {
    "Rahul Sharma has 2 yrs of exp"
    "and knows JAVA and python"
}

print("NORMAL RESPONSE")
print(normal_resposne)


structured_response = {
    "name": "Rahul Sharma",
    "experince": 3,
    "skills": ["JAVA", "python"]
}

print("Structured Response")
print(structured_response)


print("Name: ", structured_response["name"])
print("Experince: ", structured_response["experince"])
print("Skills: ", structured_response["skills"])


json_response = json.dumps(structured_response, indent=4)

print("JSON Response")
print(json_response)
