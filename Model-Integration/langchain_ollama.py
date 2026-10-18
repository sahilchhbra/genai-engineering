from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(
        model="qwen2.5:3b",
        temperature=0.3
    )


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful learning assistant."
            "Help students understand technical topics."
            "USe short examples when helpful"
        ),
        (
            "human",
            # "Explain the following {topic} in four sentences and explain in funny way"
            "which team won the cricket world cup 2023"
        )
    ]
)


chain = prompt | model

topic = input("Enter topic to learn: ")

if not topic:
    print("Please enter a valid topic to learn")
else:
    response = chain.invoke({
        "topic": topic
    })

    print("Generated Answer:")
    print("-" * 30)
    print(response.content)