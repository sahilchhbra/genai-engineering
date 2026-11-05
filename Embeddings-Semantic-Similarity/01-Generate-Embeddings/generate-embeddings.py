import ollama

text = "I love learning python programming"

response = ollama.embed(
    model="nomic-embed-text",
    input=text,
)

embedding = response["embeddings"][0]


print("INPUT text: ")
print(text)

print("\nEmbedding Vector: ")
print(embedding)

print("\nVector Dimensions: ")
print(len(embedding))

print("\n First 5 Values")
print(embedding[:5])

print("\n OUTPUT type")
print(type(embedding))