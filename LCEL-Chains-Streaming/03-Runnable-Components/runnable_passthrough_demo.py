from langchain_core.runnables import (RunnableLambda, RunnablePassthrough, RunnableParallel)

def count_words(text):
    return len(text)


workflow = RunnableParallel(

    original_text = RunnablePassthrough(),
    word_count = RunnableLambda(count_words)
)

result = workflow.invoke(
    "Langchain makes AI developement easy"
)

print("result: ", result)

print("Original Text: ")
print(result["original_text"])

print("\n Word Count: ")
print(result["word_count"])