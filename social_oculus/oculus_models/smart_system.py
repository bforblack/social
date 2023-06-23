from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
#
# def _sentiments():
#
#     for i in range(scores.shape[0]):
#         l = config.id2label[ranking[i]]
#         s = scores[ranking[i]]
#         print(f"{i + 1}) {l} {np.round(float(s), 4)}")
