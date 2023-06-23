import json
import sys
import io

import dill
from transformers import pipelines

from  oculus_source import source_connector as sc
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
from dotenv import load_dotenv
load_dotenv()


def dump_model(model_name):

    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)
    model = TFAutoModelForSequenceClassification.from_pretrained(MODEL)
    modelInfo={'sentiments':{'modle':model,'tokenizer':tokenizer,'config':config}}
    sc._minio_connector().\
        put_object(bucket_name='social', object_name=model_name, data=io.BytesIO(dill.dumps(modelInfo)),length=sys.getsizeof(modelInfo))



def get_sentiment_model():

    # Preprocess text (username and link placeholders)
    def preprocess(text):
        new_text = []
        for t in text.split(" "):
            t = '@user' if t.startswith('@') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            new_text.append(t)
        return " ".join(new_text)

    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)
    # PT
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    # model.save_pretrained(MODEL)
    text = "Covid cases are increasing fast!"
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    # # TF
    model = TFAutoModelForSequenceClassification.from_pretrained(MODEL)
    model.save_pretrained(MODEL)
    #text = "Covid cases are increasing fast!"
    # encoded_input = tokenizer(text, return_tensors='tf')
    # output = model(encoded_input)
    # scores = output[0][0].numpy()
    # scores = softmax(scores)
    # # Print labels and scores
    # ranking = np.argsort(scores)
    # ranking = ranking[::-1]
    # for i in range(scores.shape[0]):
    #     l = config.id2label[ranking[i]]
    #     s = scores[ranking[i]]
    #     print(f"{i + 1}) {l} {np.round(float(s), 4)}")
    #
    # sentiment:{"model":model,'tokenizer':tokenizer}

    #dump_model('sentiment',sentiment)

if __name__ == '__main__':
    dump_model("sentiment")
