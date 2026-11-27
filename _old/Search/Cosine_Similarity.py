import numpy as np 

class Similarity: 
    def cosine_similarity(self,query,document_chunk):

        distance_from_orgin_of_query = np.linalg.norm(query)
        distance_from_orgin_of_document_chunk = np.linalg.norm(document_chunk)

        dot_product = np.dot(query,document_chunk)

        distance_from_orgin = distance_from_orgin_of_document_chunk * distance_from_orgin_of_query

        angle = dot_product/distance_from_orgin

        print(angle)

        return angle        


s = Similarity()
s.cosine_similarity(-100000000,20)
