import ollama

modal_name = "qwen2.5:3b"

prompts = [

    "Explain python",
    (

        "Explain python to a a beginner in exactly three sentences"
        "Include one simple example"
    ),
]


for index, prompt_text in enumerate(prompts, start=1):
    print(f"\n{'=' * 15} Prompt {index} {'=' * 15}\n")
    print("Prompt: " + prompt_text)

    response = ollama.chat(
        model=modal_name,
        messages=[
            {
                "role": "user",
                "content": prompt_text,
            }
        ]
    )
    print("\n Model response")
    print(response["message"]["content"])