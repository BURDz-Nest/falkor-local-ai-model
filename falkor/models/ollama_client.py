"""Ollama API client for chat completions."""

import json
import httpx
from typing import List, Dict, Any, Optional, Iterator


class OllamaError(Exception):
    """Base exception for Ollama client errors."""
    pass


class OllamaConnectionError(OllamaError):
    """Raised when cannot connect to Ollama server."""
    pass


class OllamaModelError(OllamaError):
    """Raised when model is not available."""
    pass


class OllamaClient:
    """Simple client for Ollama API."""

    def __init__(self, base_url: str = "http://localhost:11434"):
        """Initialize Ollama client.
        
        Args:
            base_url: Ollama server URL (default: http://localhost:11434)
        """
        self.base_url = base_url
        # Longer timeout for streaming
        self.client = httpx.Client(timeout=httpx.Timeout(60.0, read=300.0))

    def chat(
        self,
        model: str,
        messages: List[Dict[str, str]],
        stream: bool = False
    ) -> Dict[str, Any]:
        """Send chat completion request to Ollama (non-streaming).
        
        Args:
            model: Model name (e.g., 'llama3.1:8b')
            messages: List of message dicts with 'role' and 'content'
            stream: Should be False for this method (use chat_stream for streaming)
            
        Returns:
            Response dict from Ollama API
            
        Raises:
            OllamaConnectionError: If cannot connect to Ollama server
            OllamaModelError: If model is not available
            
        Example:
            >>> client = OllamaClient()
            >>> response = client.chat(
            ...     model="llama3.1:8b",
            ...     messages=[{"role": "user", "content": "Hello!"}]
            ... )
        """
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": model,
            "messages": messages,
            "stream": False  # Force non-streaming for this method
        }
        
        try:
            response = self.client.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.ConnectError:
            raise OllamaConnectionError(
                f"Cannot connect to Ollama at {self.base_url}. "
                "Is Ollama running? Try: ~/bin/ollama list"
            )
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise OllamaModelError(
                    f"Model '{model}' not found. Available models: {self.list_models()}"
                )
            raise OllamaError(f"Ollama API error: {e}")

    def chat_stream(
        self,
        model: str,
        messages: List[Dict[str, str]]
    ) -> Iterator[str]:
        """Send chat completion request with streaming (yields tokens as they arrive).
        
        Args:
            model: Model name (e.g., 'llama3.1:8b')
            messages: List of message dicts with 'role' and 'content'
            
        Yields:
            Content chunks (tokens) as they arrive from the model
            
        Raises:
            OllamaConnectionError: If cannot connect to Ollama server
            OllamaModelError: If model is not available
            
        Example:
            >>> client = OllamaClient()
            >>> for chunk in client.chat_stream(
            ...     model="llama3.1:8b",
            ...     messages=[{"role": "user", "content": "Hello!"}]
            ... ):
            ...     print(chunk, end="", flush=True)
        """
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": model,
            "messages": messages,
            "stream": True
        }
        
        try:
            with self.client.stream("POST", url, json=payload) as response:
                response.raise_for_status()
                
                # Ollama streams NDJSON (newline-delimited JSON)
                for line in response.iter_lines():
                    if line.strip():
                        try:
                            data = json.loads(line)
                            # Extract the content chunk
                            if "message" in data and "content" in data["message"]:
                                yield data["message"]["content"]
                        except json.JSONDecodeError:
                            # Skip malformed lines
                            continue
                            
        except httpx.ConnectError:
            raise OllamaConnectionError(
                f"Cannot connect to Ollama at {self.base_url}. "
                "Is Ollama running? Try: ~/bin/ollama list"
            )
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise OllamaModelError(
                    f"Model '{model}' not found. Available models: {self.list_models()}"
                )
            raise OllamaError(f"Ollama API error: {e}")

    def list_models(self) -> List[str]:
        """List available models.
        
        Returns:
            List of model names
            
        Raises:
            OllamaConnectionError: If cannot connect to Ollama server
        """
        url = f"{self.base_url}/api/tags"
        try:
            response = self.client.get(url)
            response.raise_for_status()
            data = response.json()
            return [model["name"] for model in data.get("models", [])]
        except httpx.ConnectError:
            raise OllamaConnectionError(
                f"Cannot connect to Ollama at {self.base_url}. "
                "Is Ollama running? Try: ~/bin/ollama list"
            )

    def close(self):
        """Close the HTTP client."""
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
