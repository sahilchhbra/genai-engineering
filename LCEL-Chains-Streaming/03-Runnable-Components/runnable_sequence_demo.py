from langchain_core.runnables import RunnableLambda, RunnableSequence

def convert_to_uppercase(text):
    return text.upper()

def add_prefix(text):
    return f"Processed Result: {text}"


uppercase_runnable = RunnableLambda(convert_to_uppercase)

prefixed_runnable = RunnableLambda(add_prefix)


sequence = RunnableSequence(first = uppercase_runnable, last = prefixed_runnable)

result = sequence.invoke("Hello Langchain")

print("Result: ")
print(result)