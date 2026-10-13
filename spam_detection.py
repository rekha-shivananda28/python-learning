from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score,classification_report

messages=[
    "win a free prize now",
    "are you coming to college",
    "claim your cash reward",
    "hello how are you",
    "you won a free gift",
    "please call me later",
    "free entry in a contest",
    "let us meet tomorrow",
    "claim your prize today",
    "see you in class",
    "urgent win cash now",
    "can we meet after class",
    "congratulations you won a free prize",
    "please send me te notes",
    "free gift waiting fo you ",
    "I will call you tomorrow",
    "claim your free reward",
    "what time is the meeting",
    "win money with this offer",
    "thank you for your help",
]

labels=[
    "spam","ham","spam","ham","spam",
    "ham","spam","ham","spam","ham",
    "spam","ham","spam","ham","spam",
    "ham","spam","ham","spam","ham",
]
print("Message:",len(messages))
print("Labels:",len(labels))
X_train,X_test,y_train,y_test=train_test_split(
    messages,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels
)
model=make_pipeline(
    CountVectorizer(),
    MultinomialNB()

)
model.fit(X_train,y_train)
test_predictions=model.predict(X_test)
accuracy=accuracy_score(y_test,test_predictions)
print("=====SPAM MESSAGE DETECTION=====")
print("Training message:",len(X_train))
print("Model accuracy:",round(accuracy*100,2),"%")
print("\nClassification Report:")
print(classification_report(
    y_test,
    test_predictions,
    labels=["ham","spam"],
    zero_division=0

))
new_messages=[
    "congratulations you won a free prize",
    "Hello,can we meet after class?",
    "claim your free cash reward now"
]
new_predictions=model.predict(new_messages)
print("\n=====NEW MESSAGE PREDICTIONS=====")

for message,prediction in zip(new_messages,
new_predictions):
    print("Message:",message)
    print("prediction:",prediction.upper())
    print()