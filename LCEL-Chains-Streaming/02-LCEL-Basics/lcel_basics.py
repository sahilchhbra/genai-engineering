from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(
        model="qwen2.5:3b",
        temperature=0.3
    )


# Create the prompt_template

prompt = ChatPromptTemplate.from_template(

    "Explain {topic} in simple words with one practical example"
)

parser = StrOutputParser()

chain = prompt | model | parser


response = chain.invoke({
    "topic": "Artifical Intelligence",
})


print("Response: ")
print(response)

print("\n Output type: ")
print(type(response))