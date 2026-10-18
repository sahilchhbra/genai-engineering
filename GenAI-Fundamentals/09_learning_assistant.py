from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda


# Create a prompt template

learning_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful learning assistant."
            "Help students understand technical topics."
        ),
        (
            "human",
            "Explain {topic} for a {level} student."
            "Include a definition, two key points, "
            "and one practical example."
        )
    ]
)

# Create a simulated model response

def generate_mock_response(messages):

    messages = messages.to_messages()
    user_message = messages[-1].content

    result = {
        "response_type": "simulated",
        "content": (
            "This is a simulated response. \n \n"
            f"Your prepared prompt was: \n {user_message}"
        )
    }

    return result



# Convert the function into a runnable
mock_model = RunnableLambda(
    generate_mock_response
)


# Create the pipeline
learning_assistant = learning_prompt | mock_model



# Get input from the student

topic = input("Enter topic to learn: ")
level = input("Enter level to level (Beginner/intermediate): ")


# Execute the pipleine
result = learning_assistant.invoke({
    "topic": topic,
    "level": level
})

# Dispalying our result
print("\n------Learning Assistant------")
print("Response type:", result["response_type"])
print(result["content"])