from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(
        model="qwen2.5:3b",
        temperature=0.3
    )

prompt_styles = {
    "1": "Explain the topic clearly to a beginner",

    "2": (
        "Explain the topic clearly to a beginner"
        "Include one practical example"
    ),

    "3": (
        "Explain the topic clearly to a beginner"
        "Include one practical example and three key takeaways"
        "Keep the response concise"
    )
}


print("======================== PROMPT ENGINEERING PLAYGROUND ======================")


topic = input("Enter topic to learn: ").strip()

print("\n prompt styles")
print("1. Basic explanation")
print("2. Explanation with a example")
print("3. Explanation with a example and key takeaways")


choice = input("\nEnter your choice (1-3): ").strip()


if not topic:
    print("\n Please enter a topic to learn")

elif choice not in prompt_styles:
    print("\n Please enter a valid choice between 1, 2 and 3")

else:

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful programming teacher."
                "Use simple and accurate language"
            ),
            (
                "human",
                "Explain the following topic: {topic} \n\n"
                "Instructions: {instructions}"

            )
        ])


    chain = prompt | model

    try:
        response = chain.invoke({
            "topic": topic,
            "instructions": prompt_styles[choice]
        })

        print("\n" + "=" * 15 + "AI response " + "=" * 15)
        print(response.content)

    except Exception as error:
        print("An error occured:", type(error).__name__, error)