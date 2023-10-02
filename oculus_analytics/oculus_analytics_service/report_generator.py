import os

import numpy as np
import matplotlib.pyplot as plt
import base64
from base64 import b64decode, b64encode
import base64
import gridfs
from database import mongo_connector
from pymongo import MongoClient
def createSentimentChart(data1):
    data=[checkValue(data1,'neutral'),checkValue(data1,'negative'),checkValue(data1,'positive')]
    sentiments = ['neutral', 'negative', 'positive']
    explode = (0.1, 0.0, 0.2)
    colors = ("blue", "red", "green")
    wp = {'linewidth': 1, 'edgecolor': "orange"}
    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(data,
                                      autopct=lambda pct: func(pct, data),
                                      explode=explode,
                                      labels=sentiments,
                                      shadow=True,
                                      colors=colors,
                                      startangle=90,
                                      wedgeprops=wp,
                                      textprops=dict(color="black"))
    ax.legend(wedges, sentiments,
              title="Sentiments",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title("Post Analytics")
    # show plot
    #
    #f = plt.figure()
    fig.savefig("foo.pdf", bbox_inches='tight')
    plt.close()
    with open("foo.pdf", "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read())
        return encoded_string


def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)

def checkValue(data,key):
    if key in data['label'].values:
        return data['label'].value_counts()[key]
    else :
        return 0
def entityPlots(data1):
    entityMapping={'O':'Outside of a named entity',
                   'B-MIS':'Beginning of a miscellaneous entity right after another miscellaneous entity',
                   'I-MIS':'Miscellaneous entity',
                   'B-PER':'Beginning of a person’s name right after another person’s name',
                  'I-PER':'Person’s name',
                  'B-ORG':'Beginning of an organization right after another organization',
                          'I-ORG':'organization','B-LOC':'Beginning of a location right after another location',
                   'I-LOC':'Location'}

    data=[]
    for i in entityMapping:
        data.append(checkValue(data1, i))

    #data = [checkValue(data1, 'neutral'), checkValue(data1, 'negative'), checkValue(data1, 'positive')]
    sentiments = list(entityMapping.keys())
    explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.0,0.0,0.0)
    colors = ("orange", "cyan", "brown",
              "grey", "indigo", "beige",'blue','green','red')
    wp = {'linewidth': 1, 'edgecolor': "orange"}
    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(data,
                                      autopct=lambda pct: func(pct, data),
                                      explode=explode,
                                      labels=sentiments,
                                      shadow=True,
                                      colors=colors,
                                      startangle=90,
                                      wedgeprops=wp,
                                      textprops=dict(color="black"))
    ax.legend(wedges, sentiments,
              title="Entity Description",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title("Post Analytics")
    #data = [checkValue(data1, 'neutral'), checkValue(data1, 'negative'), checkValue(data1, 'positive')]




def write_new_pdf(path):
    db = MongoClient(os.environ.get('DATA_SOURCE_CONNECTION_STRING')).get_database('social').get_collection('post')
    fs = gridfs.GridFS(db)
    # Note, open with the "rb" flag for "read bytes"
    with open(path, "rb") as f:
        encoded_string = base64.b64encode(f.read())
    with fs.new_file(
        chunkSize=800000,
        filename=path) as fp:
        fp.write(encoded_string)
