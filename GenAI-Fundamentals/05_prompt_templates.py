# from langchain_core.prompts import PromptTemplate
from pydoc_data.topics import topics

# Example 1
# prompt_template = PromptTemplate.from_template(
#     "Explain {topic} in simple language."
#     "Give one practical example"
# )
#
#
# formatted_prompt = prompt_template.format(
#     topic="Genrative AI",
# )
#
# print(formatted_prompt)


# Example 2

from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful python tutor."),
    ("human", "Explain {topic} with a simple practical example.")
    ])

messages = chat_prompt.format_messages(
    topic = "Python Decortors"
)

for message in messages:
    print(f"Role: {message.type}")
    print(f"Content: {message.content}")
    print()
