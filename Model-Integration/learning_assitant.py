import os
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate

from openai import (
    APIConnectionError,
    RateLimitError,
    APITimeoutError,
    AuthenticationError,
    APIConnectionError
)

api_key = os.getenv("NVIDIA_API_KEY")

if not api_key:
    raise ValueError("NVIDIA_API_KEY is missing")

model = ChatNVIDIA(
        model="openai/gpt-oss-20b",
        api_key=api_key,
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
            "Explain the following {topic}"
        )
    ]
)

chain = prompt | model

topic = input("Enter topic to learn: ")

try:
    response = chain.invoke({
            "topic": topic
    })

    if not response.content:
        print("No response from Nvidia API")
    else:
        print("Generated Answer:")
        print("-" * 30)
        print(response.content)

except AuthenticationError:
    print("Authentication falied. Check your api_key")

except RateLimitError:
    print("Rate limit exceeded. Try again later")

except APITimeoutError:
    print("Timeout exceeded. Try again later")

except APIConnectionError:
    print("Connection error. Try again later")

except Exception as e:
    print("An unexpected error occured. Try again later")
