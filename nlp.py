from textblob import TextBlob as tb



p = """
    In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of 
    a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the 
    final copy is available. It is also used to temporarily replace text in a process called greeking, which allows 
    designers to consider the form of a webpage or publication, without the meaning of the text influencing the design.
    """

blob = tb(p)

print(blob.tags)
print(blob.noun_phrases)

print(blob.word_counts)

print("Sentiment analysis")
for i in blob.sentences:
    print(i.sentiment.polarity)


print(blob.sentiment)

