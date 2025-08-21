from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)


df = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})


X = df['message']
y = df['label']
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)
model = MultinomialNB()
model.fit(X_vec, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    msg = request.form['message']
    msg_vec = vectorizer.transform([msg])
    pred = model.predict(msg_vec)[0]
    return render_template('index.html', prediction='Spam' if pred == 1 else 'Not Spam')

if __name__ == '__main__':
    app.run(debug=True)
