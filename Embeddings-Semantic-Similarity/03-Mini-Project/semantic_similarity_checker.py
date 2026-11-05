import ollama
from sklearn.metrics.pairwise import cosine_similarity


sentence_one = input("Enter first sentence: ")
sentence_two = input("Enter second sentence: ")



response = ollama.embed(
    model="nomic-embed-text",
    input=[sentence_one, sentence_two],
)

embedding_one = response["embeddings"][0]
embedding_two = response["embeddings"][1]


similarity_score = cosine_similarity(
    [embedding_one],
    [embedding_two],
)[0][0]

print("\n==================== RESULT =====================")

print("Sentence 1: ")
print(sentence_one)

print("\nSentence 2: ")
print(sentence_two)


print("\n Similarity score: ", round(float(similarity_score), 4))



if(similarity_score >= 0.75):
    print("\nThese sentences are highly similar.")

elif(similarity_score >= 0.5):
    print("\nThese sentences are moderately similar.")

else:
    print("\nThese sentences have relatively low similarity.")