import numpy as np 
from Search.Cosine_Similarity import Similarity

class VectorStore:
    def __init__(self):
        self.chunks = []
        self.embeddings = []

    def add(self,chunk,embedding):
        self.chunks.append(chunk)
        self.embeddings.append(embedding)

    def search(self,query,top_k = 3):
        relevent = {}

        c = Similarity()

        for i , embedding in enumerate(self.embeddings):
            s = c.cosine_similarity(query,embedding)
            relevent[i] = s

        # Sort by Similarity Score 
        sorted_results = sorted(relevent.items(),key=lambda x : x[1], reverse=True)

        # Take only top K results
        top_results = sorted_results[:3]

        result = []

        for index , score in top_results:
            result.append((self.chunks[index],score))
        return result