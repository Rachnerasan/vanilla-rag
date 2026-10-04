import math

class VectorIndex:
    def __init__(self, distance_metric="cosine", embedding_fn=None):
        """
        A simple, from-scratch vector index for educational purposes.
        """
        self.distance_metric = distance_metric
        self.embedding_fn = embedding_fn
        self.vectors = []
        self.metadata = []

    def add_vector(self, vector, metadata):
        """
        Store a vector and its associated metadata.
        """
        self.vectors.append(vector)
        self.metadata.append(metadata)

    def _cosine_distance(self, v1, v2):
        """
        Calculate cosine distance between two vectors.
        distance = 1 - cosine_similarity
        """
        dot_product = sum(a * b for a, b in zip(v1, v2))
        magnitude1 = math.sqrt(sum(a * a for a in v1))
        magnitude2 = math.sqrt(sum(b * b for b in v2))
        
        if magnitude1 == 0 or magnitude2 == 0:
            return 1.0
            
        return 1 - (dot_product / (magnitude1 * magnitude2))

    def search(self, query_text, k=3):
        """
        Embed the query and find the k nearest vectors.
        """
        if not self.embedding_fn:
            raise ValueError("No embedding function provided to VectorIndex.")
            
        query_vector = self.embedding_fn(query_text)
        
        results = []
        for i, vector in enumerate(self.vectors):
            if self.distance_metric == "cosine":
                distance = self._cosine_distance(query_vector, vector)
            else:
                # Fallback to euclidean or raise error
                raise NotImplementedError(f"Metric {self.distance_metric} not implemented.")
                
            results.append((self.metadata[i], distance))
            
        # Sort by distance (lowest is best)
        results.sort(key=lambda x: x[1])
        return results[:k]
