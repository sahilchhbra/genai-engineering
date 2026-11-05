import ollama
from sklearn.metrics.pairwise import cosine_similarity

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


# between sentence 1 and 2
similarity_1 = cosine_similarity(
    [embedding[0]],
    [embedding[1]],
)[0][0]

# between sentence 1 and 3
similarity_2 = cosine_similarity(
    [embedding[0]],
    [embedding[2]],
)[0][0]

print("Sentence 1: ")
print(sentences[0])

print("\nSentence 2: ")
print(sentences[1])

print("\nSentence 3: ")
print(sentences[2])

print("\nSIMILARITY RESULT: ")

print("Similarity between sentence 1 VS sentence 2: ")
print(round(float(similarity_1), 4))

print("Similarity between sentence 1 VS sentence 3: ")
print(round(float(similarity_2), 4))