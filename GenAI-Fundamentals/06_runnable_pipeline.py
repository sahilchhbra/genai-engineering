from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda


# Step 1 create a chat prompt template
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful python tutor."),
    ("human", "Explain {topic} with a simple practical example.")
    ])


# Step 2: Create a simulated model function
def simulate_model_response(prompt_value):
    messages = prompt_value.to_messages()
    user_message = messages[-1].content
    return f"Simulated AI response for: {user_message}"


# Step3: Convert the function into a runnable
fake_model = RunnableLambda(simulate_model_response)


# Step 4 Connect the components in a pipeline
chain = chat_prompt | fake_model

result = chain.invoke({
    "topic": "Python Decorators"
})

print("Final Result")
print(result)
