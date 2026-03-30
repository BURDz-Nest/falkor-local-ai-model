"""Ollama API client for chat completions."""

import httpx
from typing import List, Dict, Any, Optional


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
        self.client = httpx.Client(timeout=60.0)

    def chat(
        self,
        model: str,
        messages: List[Dict[str, str]],
        stream: bool = False
    ) -> Dict[str, Any]:
        """Send chat completion request to Ollama.
        
        Args:
            model: Model name (e.g., 'llama3.1:8b')
            messages: List of message dicts with 'role' and 'content'
            stream: Whether to stream the response
            
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
            "stream": stream
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
