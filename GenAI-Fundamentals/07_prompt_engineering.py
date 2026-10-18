from langchain_core.prompts import PromptTemplate


# Example 1
review_template = PromptTemplate.from_template(

    """
    Classify this review as positive or negative
    
    Review: "{review}"
    
    Return only the classification
    """
)


formatted_prompt = review_template.format(
    review="the application is easy to use and works perfectly"
)

print("Geneated Prompt:")
print(formatted_prompt)







# The topic is python. The difficultly level is beginner here are towo questions What is a list  what is a dictionary











