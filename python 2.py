from textblob import TextBlob

# متن ورودی
text = str(input("ye chizi bego?"))

# ایجاد یک نمونه از TextBlob
blob = TextBlob(text)

# تحلیل احساسات
sentiment = blob.sentiment

# نمایش نتایج
print(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")

# بررسی مثبت یا منفی بودن احساسات
if sentiment.polarity > 0:
    print("Positive sentiment.")
elif sentiment.polarity < 0:
    print("Negative sentiment.")
else:
    print("Neutral sentiment.")