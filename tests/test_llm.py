from app.generation.llm import AiModel

def test_create_rag_messages_structure():
    # Create a mock version of AiModel so we don't trigger the 
    # heavy model download or Hugging Face authentication during tests
    class MockAiModel(AiModel):
        def __init__(self):
            pass # Skip the real __init__
            
    model = MockAiModel()
    
    context = "The company made 1 billion dollars in Q1."
    question = "How much money did the company make?"
    
    messages = model.create_rag_messages(
        relevent_sections=context,
        question_prompt=question
    )
    
    # 1. Verify structure
    assert isinstance(messages, list)
    assert len(messages) == 2
    
    # 2. Verify roles
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    
    # 3. Verify content injection
    assert context in messages[0]["content"]
    assert question in messages[1]["content"]
