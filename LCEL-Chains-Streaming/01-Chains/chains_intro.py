def generate_article(topic):

    article = f"""

    {topic} """

    return article


def genrate_summary(article):

    summary = article[:100]
    return summary


def generate_title(article):

    title = "Understanding the importance of AI"
    return title


topic = "Artificial Intelligence"

article = generate_article(topic)

summary = genrate_summary(article)

title = generate_title(article)


print("Article:")
print(article)

print("\nSummary:")
print(summary)

print("\nTitle:")
print(title)
