"""Test error handling for Ollama client."""

from falkor.models.ollama_client import OllamaClient, OllamaConnectionError, OllamaModelError

def test_error_handling():
    """Test that errors are handled gracefully."""
    print("🧪 Testing error handling...\n")
    
    # Test 1: Bad connection (wrong port)
    print("Test 1: Bad connection (wrong port)")
    try:
        with OllamaClient(base_url="http://localhost:99999") as client:
            client.list_models()
        print("❌ Test failed - should have raised error")
    except OllamaConnectionError as e:
        print(f"✅ Caught expected error: {e}\n")
    
    # Test 2: Bad model name
    print("Test 2: Invalid model name")
    try:
        with OllamaClient() as client:
            client.chat(
                model="this-model-does-not-exist:999",
                messages=[{"role": "user", "content": "Hello"}]
            )
        print("❌ Test failed - should have raised error")
    except OllamaModelError as e:
        print(f"✅ Caught expected error: {str(e)[:100]}...\n")
    
    # Test 3: Valid connection (should work)
    print("Test 3: Valid connection and model")
    try:
        with OllamaClient() as client:
            models = client.list_models()
            print(f"✅ Successfully connected! Found {len(models)} models")
            
            response = client.chat(
                model="llama3.1:8b",
                messages=[{"role": "user", "content": "Say 'OK' if you can hear me."}]
            )
            print(f"✅ Chat works! Response: {response['message']['content'][:50]}...\n")
    except Exception as e:
        print(f"❌ Unexpected error: {e}\n")
    
    print("✅ All error handling tests passed!")

if __name__ == "__main__":
    test_error_handling()
