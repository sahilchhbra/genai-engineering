import ollama

sentences = [
    "I love learning python programming",
    "Python coding something i really love",
    "The weather is very cold today"
]

response = ollama.embed(
    model="nomic-embed-text",
    input=sentences,
)

embedding = response["embeddings"]


for index, sentence in enumerate(sentences):
    print(f"\nSentence {index + 1}:")
    print(sentence)

    print("\n First 5 embeddings Values")
    print(embedding[index][:5])

    print("\nVector Dimensions: ")
    print(len(embedding[index]))

    print("-" * 50)
