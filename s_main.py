import random
import warnings

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances

warnings.filterwarnings("ignore")


data = pd.read_pickle(r'16k_apperal_data_preprocessed')

def generate_random_products():
    n = data.shape[0]
    p_nums = random.sample(range(0, n), 6)
    urls = []
    for i in p_nums:
        res = data.iloc[[i]].values[0]
        urls.append([res[3],str(str(res[1]) + " " + str(res[2]) + " " + str(res[4])),str(res[5]),str(res[6]),i])
    return urls

tfidf_title_vectorizer = TfidfVectorizer(min_df=0)
tfidf_title_features = tfidf_title_vectorizer.fit_transform(data['title'])


def get_recomendattions(doc_id):
    num_results = 7
    urls = []
    pairwise_dist = pairwise_distances(tfidf_title_features, tfidf_title_features[doc_id])
    indices = np.argsort(pairwise_dist.flatten())[0:num_results]
    for i in range(1, len(indices)):
        res = data.iloc[[indices[i]]].values[0]
        urls.append([res[3], str(str(res[1]) + " " + str(res[2]) + " " + str(res[4])), str(res[5]), str(res[6]), indices[i]])
    return urls
