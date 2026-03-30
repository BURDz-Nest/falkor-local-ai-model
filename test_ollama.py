"""Test script for Ollama client."""

from falkor.models.ollama_client import OllamaClient

def test_ollama():
    """Test basic Ollama connection."""
    print("🧪 Testing Ollama connection...\n")
    
    with OllamaClient() as client:
        # List available models
        print("📋 Available models:")
        models = client.list_models()
        for model in models:
            print(f"  - {model}")
        print()
        
        # Test chat with llama3.1:8b
        print("💬 Testing chat with llama3.1:8b...")
        print("Sending: 'Hello!'\n")
        
        response = client.chat(
            model="llama3.1:8b",
            messages=[{"role": "user", "content": "Hello!"}]
        )
        
        assistant_message = response["message"]["content"]
        print(f"🤖 Falkor: {assistant_message}\n")
        print("✅ Test successful!")

if __name__ == "__main__":
    test_ollama()
