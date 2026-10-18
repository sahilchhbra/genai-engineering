import json

# Create structured data
response  = {

    "topic": "Python",
    "difficulty": "Beginner",
    "questions": [
        "What is a list?",
        "What does a dictionary?"
    ]
}

# convert the dictionary into JSON text
json_response = json.dumps(response, indent=4)
print(json_response)


# Validate the required fields

required_fields = ["topic", "difficulty", "questions"]


if all(field in response for field in required_fields):
    print ("\n Validation successful!")
else:
    print ("\n Validation failed!")


print("\n Topic: ", response["topic"])
print("\n Difficulty: ", response["difficulty"])
print("\n No. of questions: ", len(response["questions"]))