from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(
        model="qwen2.5:3b",
        temperature=0.3
    )


prompts = {

    "Weak Prompt": ChatPromptTemplate.from_messages([

        ("human", "Explain databases.")
    ]),

    "Improved Prompt": ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a programming teacher exaplaining concepts to beginners"
        ),
        (
            "human",
            """
            Explain relational databases to a beginner learning backend development.
            
            Requirements:
            1. start with a simple definition.
            2. Explain tables, rows, and columns.
            3. give one practical example. using an online shopping application.
            4. Use simple language while explanation
            5. keep the answer under 150 words.
            """
        ),
    ])
}


for prompt_name, prompt_template in prompts.items():
    print ("\n" + "=" * 20)

    print(prompt_name)
    print("=" * 20)
    chain = prompt_template | model

    try:
        response = chain.invoke({})
        print(response.content)

    except Exception as error:
        print("An error occured:", type(error).__name__)