import nltk
from nltk.tokenize import word_tokenize
from gensim import corpora
from gensim.models import LdaModel

# دانلود منابع nltk
nltk.download('punkt')
nltk.download('stopwords')

# ساخت لیست کلمات بی‌اهمیت (stopwords) برای فارسی
farsi_stopwords = set(["و", "در", "به", "از", "که", "این", "است", "را", "با", "تا", "برای", "بر", "هم", "اگر", "من", "تو", "ما", "شما", "او"])

# تابع برای پردازش متن فارسی
def preprocess_text_farsi(text):
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha()] # فقط کلمات را نگه‌داریم
    tokens = [word for word in tokens if word not in farsi_stopwords] # حذف کلمات بی‌اهمیت
    return tokens

# دریافت مکالمات از کاربر (به زبان فارسی)
conversations = []
while True:
    sentence = input("benivis or enter ro bezan : ")
    
    if sentence == "":
        break
    
    conversations.append(sentence)

# پردازش مکالمات
processed_conversations = [preprocess_text_farsi(conv) for conv in conversations]

# ساخت دیکشنری و کیسه کلمات
dictionary = corpora.Dictionary(processed_conversations)
corpus = [dictionary.doc2bow(conv) for conv in processed_conversations]

# ساخت مدل LDA
lda_model = LdaModel(corpus, num_topics=2, id2word=dictionary, passes=15)

# نمایش موضوعات
topics = lda_model.print_topics(num_words=4)
print("\nnatije")
for topic in topics:
    print(topic)