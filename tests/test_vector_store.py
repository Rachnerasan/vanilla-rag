import math
from app.retrieval.vector_store import VectorIndex

def test_cosine_distance():
    index = VectorIndex(distance_metric="cosine")
    
    v1 = [1.0, 0.0]
    v2 = [1.0, 0.0]
    # Cosine similarity of identical vectors is 1.0 -> distance is 0.0
    dist = index._cosine_distance(v1, v2)
    assert math.isclose(dist, 0.0, abs_tol=1e-5)
    
    v3 = [0.0, 1.0]
    # Orthogonal vectors -> similarity 0.0 -> distance 1.0
    dist_ortho = index._cosine_distance(v1, v3)
    assert math.isclose(dist_ortho, 1.0, abs_tol=1e-5)
    
    v4 = [-1.0, 0.0]
    # Opposite vectors -> similarity -1.0 -> distance 2.0
    dist_opp = index._cosine_distance(v1, v4)
    assert math.isclose(dist_opp, 2.0, abs_tol=1e-5)

def test_vector_search():
    # Mock embedding function that simply passes the query vector through
    mock_embed = lambda x: x
    
    index = VectorIndex(distance_metric="cosine", embedding_fn=mock_embed)
    
    # Store some fake vectors
    index.add_vector([1.0, 0.0], {"text": "horizontal line"})
    index.add_vector([0.0, 1.0], {"text": "vertical line"})
    index.add_vector([0.707, 0.707], {"text": "diagonal line"})
    
    # Search for a vector very close to horizontal [1.0, 0.0]
    results = index.search([0.9, 0.1], k=2)
    
    assert len(results) == 2
    # The closest match should be the horizontal line
    assert results[0][0]["text"] == "horizontal line"
    
    # The second closest match should be the diagonal line
    assert results[1][0]["text"] == "diagonal line"
    
    # Verify the distances are sorted properly (lowest distance first)
    assert results[0][1] < results[1][1]
