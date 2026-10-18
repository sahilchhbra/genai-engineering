import ollama
from openai import OpenAI

import os
import time

LOCAL_MODEL = "qwen2.5:3b"
api_key = os.getenv("NVIDIA_API_KEY")

if not api_key:
    raise ValueError("NVIDIA_API_KEY is missing")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key,
)


prompt_text = """
    Explain REST APIs to a beginner.
    Requirements:
    1. Explain the concept in simple language.
    2.give one practical example.
    3. Give answer exactly in 3 bullet points
"""


print("\n========================== LOCAL MODEL ===========================\n")

try:
    start_time = time.perf_counter()
    local_response = ollama.chat(
        model=LOCAL_MODEL,
        messages=[
            {"role":"user", "content":prompt_text},
        ],
    )
    local_duration = time.perf_counter() - start_time
    local_answer = local_response["message"]["content"]
    print(local_answer)
    print(f"\n Response time: {local_duration:.2f} seconds")

except Exception as error:
    local_response = None
    print(error)
    print("Local Model failed: ", type(error).__name__)




print("\n========================== HOSTED MODEL ===========================\n")

try:
    start_time = time.perf_counter()

    hosted_response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user", "content": prompt_text
            }
        ],
        max_tokens=500,
        temperature=0.3,
    )

    hosted_duration = time.perf_counter() - start_time
    hosted_answer = hosted_response.choices[0].message.content

    if hosted_answer:
        print(hosted_answer)
    else:
        print("Hosted Model returned no text")

    print(f"\n Response time: {hosted_duration:.2f} seconds")

except Exception as error:
    hosted_response = None
    print("Hosted Model failed: ", type(error).__name__)



print("\n========================== COMPARISON SUMMARY ===========================\n")

print("Local response received: ", bool(local_response))
print("Hosted response received: ", bool(hosted_response))