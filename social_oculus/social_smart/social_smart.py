from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import pandas as pd
from scipy.special import softmax
class Smart:
    def __init__(self,comments):
        self.comments=comments

    def process_sentiments(self)->pd.Dataframe:
        MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
        tokenizer = AutoTokenizer.from_pretrained(MODEL)
        config = AutoConfig.from_pretrained(MODEL)
        model = TFAutoModelForSequenceClassification.from_pretrained(MODEL)
        encoded_input = tokenizer(self.comments['comments'], return_tensors='pt')
        output = model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = pd.argsort(scores)
        ranking = ranking[::-1]
        for i in range(scores.shape[0]):
            l = config.id2label[ranking[i]]
            s = scores[ranking[i]]
            self.comments['sentiments']=[i+i]
            self.comments['score']=[pd.round(float(s), 4)]
            #print(f"{i + 1}) {l} {pd.round(float(s), 4)}")
        return self.comments











