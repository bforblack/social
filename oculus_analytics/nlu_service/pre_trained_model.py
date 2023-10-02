#from io import BytesIO

import pandas as pd
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification, AutoModelForTokenClassification
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
from minio import Minio
# minio=Minio(endpoint='192.168.0.123:31306',secure=False,
#                   access_key='minioadmin',
#                  secret_key='minioadmin')
MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
#MODEL1=minio.get_object(bucket_name='social',object_name='cardiffnlp/twitter-roberta-base-sentiment-latest/pytorch_model.bin').data
tokenizer = AutoTokenizer.from_pretrained(MODEL)
#con=minio.get_object(bucket_name='social',object_name='cardiffnlp/twitter-roberta-base-sentiment-latest/config.json').json()
config = AutoConfig.from_pretrained(MODEL)
#model = TFAutoModelForSequenceClassification.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
#model.save_pretrained(MODEL)

tokenizer2 = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model2 = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
#model2.save_pretrained(model2)


from transformers import pipeline


def processedData(text)->pd.DataFrame:
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    # encoded_input = tokenizer(text, return_tensors='tf')
    # output = model(encoded_input)
    # scores = output[0][0].numpy()
    # scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    for i in range(scores.shape[0]):
        l = config.id2label[ranking[i]]
        s = scores[ranking[i]]
        # print(f"{i + 1}) {l} {np.round(float(s), 4)}")
        return {i:np.round(float(s), 4)}

def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

def getPipeline():
    sentiment_task = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    nlp = pipeline("ner", model=model2, tokenizer=tokenizer2)
    g= {"sentiment":sentiment_task,"ner":nlp}
    return g


if __name__ == '__main__':
    mk=getPipeline()