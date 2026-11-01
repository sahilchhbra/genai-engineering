from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (RunnableLambda, RunnablePassthrough)

model = ChatOllama(
        model="qwen2.5:3b",
        temperature=0.3
    )

parser = StrOutputParser()


article_prompt = ChatPromptTemplate.from_template(
    """
    Write a short article around 120 words about {topic}.
    Use simple language.
    """
)

article_chain = article_prompt | model | parser


summary_prompt = ChatPromptTemplate.from_template(

    """
    Summarize the following article in 2-3 sentences.
    {article}
    """
)


summary_chain = summary_prompt | model | parser


title_prompt = ChatPromptTemplate.from_template(
    """
    Generate a short and attractive title
    for the following summary:
    {summary}
    """
)

title_chain = title_prompt | model | parser


workflow = (

    RunnablePassthrough.assign(
        article = article_chain
    )

    |

    RunnablePassthrough.assign(
        summary=(
            RunnableLambda(
                lambda data: {"article": data["article"]}
            )
            |summary_chain
        )
    )

    |

    RunnablePassthrough.assign(
        title=(
            RunnableLambda(
                lambda data: {"summary": data["summary"]}
            )
            | title_chain
        )
    )
)

result = workflow.invoke({
    "topic": "Benefits of learning python"
})


print("\nGenerated Article\n")
print(result["article"])

print("\nGenerated Summary\n")
print(result["summary"])

print("\nGenerated Title\n")
print(result["title"])