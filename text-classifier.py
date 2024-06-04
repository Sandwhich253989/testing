from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob import Word

train = [
    ("I love this sandwich.", "pos"),
    ("this is an amazing place!", "pos"),
    ("I feel very good about these beers.", "pos"),
    ("this is my best work.", "pos"),
    ("what an awesome view", "pos"),
    ("I do not like this restaurant", "neg"),
    ("I am tired of this stuff.", "neg"),
    ("I can't deal with this", "neg"),
    ("he is my sworn enemy!", "neg"),
    ("my boss is horrible.", "neg"),
    ("I am excited to try out this new place", "pos")
]

test = [
    ("the beer was good.", "pos"),
    ("I do not enjoy my job", "neg"),
    ("I ain't feeling dandy today.", "neg"),
    ("I feel amazing!", "pos"),
    ("Gary is a friend of mine.", "pos"),
    ("I can't believe I'm doing this.", "neg"),
]

model = NaiveBayesClassifier(train)
prob = model.prob_classify("Iam not feeling bad today")
print("Iam not feeling bad today :")
print(model.classify("Iam not feeling bad today"), "\n")

print("probability of being positive : ", prob.prob("pos"))
print("probability of being negative : ", prob.prob("neg"))

print("test data accuracy : ", model.accuracy(test))

print(model.show_informative_features())

blob = TextBlob("""
He enjoys practicing his ballet in the bathroom.
I'm excited to try my new classifier.
""", classifier=model)

for s in blob.sentences:
    print(s)
    print(s.classify())


word = Word("funniest")
print(word.lemmatize("a"))
