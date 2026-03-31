"""Test streaming responses from Ollama."""

from falkor.models.ollama_client import OllamaClient, OllamaConnectionError
from falkor.cli.renderer import FalkorRenderer

print("\n" + "="*60)
print("Testing Streaming Responses")
print("="*60)

renderer = FalkorRenderer()

try:
    client = OllamaClient()
    
    # Check if Ollama is running
    print("\nChecking Ollama connection...")
    models = client.list_models()
    print(f"✅ Connected! Found {len(models)} models.\n")
    
    if not models:
        print("❌ No models available. Install one with: ~/bin/ollama pull llama3.1:8b")
    else:
        # Use first available model
        model = models[0]
        print(f"Using model: {model}")
        print("\nAsking: 'What is 2+2?'\n")
        print("Watch the response stream token-by-token!")
        print("-" * 60)
        
        # Create a simple message
        messages = [
            {"role": "user", "content": "What is 2+2? Give a short answer."}
        ]
        
        # Get streaming response
        stream = client.chat_stream(model=model, messages=messages)
        
        # Render with typewriter effect
        response = renderer.render_streaming_response(stream)
        
        print("-" * 60)
        print(f"\n✅ Streaming complete! Received {len(response)} characters.")
        print("\nFull response:")
        print(response)
        
except OllamaConnectionError as e:
    print(f"\n❌ {e}")
    print("\nMake sure Ollama is running!")
    print("Try: ~/bin/ollama list")
except Exception as e:
    print(f"\n❌ Error: {e}")
finally:
    if 'client' in locals():
        client.close()

print("\n" + "="*60)
print("✅ Test complete!")
print("\nNow run 'python main.py' to see streaming in Falkor!")
print("="*60 + "\n")
