from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(
        model="qwen2.5:3b",
        temperature=0.3
    )

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful programming teacher."
            "You are a programming teacher."
            "Exaplin concepts in simple language"
        ),
        (
            "human",
            "Explain the following {topic} with one practical python example"
        )
    ]
)

parser = StrOutputParser()


chain = prompt | model | parser

response = chain.invoke({

})


print("AI Learning assistant: ")
print("---------------------------")
print(response)


print("\n Output type: ")
print(type(response))