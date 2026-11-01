from langchain_core.runnables import (RunnableLambda, RunnableParallel)

def count_words(text):
    return len(text.split())


def convert_to_uppercase(text):
    return text.upper()


def count_characters(text):
    return len(text)



parallel_workflow = RunnableParallel(

    word_count=RunnableLambda(count_words),
    upper_text=RunnableLambda(convert_to_uppercase),
    character_count=RunnableLambda(count_characters),
)


result = parallel_workflow.invoke(
    "LangChain is useful"
)


print("Parallel Execution Result: ")
print(result)

print("\nWord Count: ")
print(result["word_count"])

print("\nUppeCase Text: ")
print(result["upper_text"])

print("\nCharacter Count: ")
print(result["character_count"])