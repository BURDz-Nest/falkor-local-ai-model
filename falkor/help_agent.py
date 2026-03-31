"""Help Agent - Built-in Falkor assistant that knows how Falkor works."""

from typing import List, Dict


class HelpAgent:
    """Smart assistant that helps users with Falkor and Ollama questions."""
    
    def __init__(self):
        """Initialize the help agent."""
        self.system_prompt = self._build_system_prompt()
        self.help_keywords = [
            "how do i", "how to", "how can i",
            "install model", "get model", "add model", "download model",
            "pull model", "more models", "new model",
            "switch model", "change model",
            "not working", "doesn't work", "not responding",
            "error", "failed", "can't connect",
            "ollama", "falkor",
            "what is", "what are", "explain",
            "help me", "i need help",
            "slow", "stuck", "frozen",
        ]
    
    def should_activate(self, user_input: str) -> bool:
        """Detect if this is a Falkor/Ollama help question.
        
        Args:
            user_input: User's message
            
        Returns:
            True if help agent should handle this
        """
        user_lower = user_input.lower()
        
        # Check for help keywords
        for keyword in self.help_keywords:
            if keyword in user_lower:
                return True
        
        # Check for questions about Falkor commands
        if user_lower.startswith("/"):
            return False  # Let normal command handler take it
        
        return False
    
    def _build_system_prompt(self) -> str:
        """Build the system prompt for the help agent.
        
        Returns:
            Complete system prompt
        """
        return """You are the Falkor Help Agent, a friendly assistant built into Falkor that helps users understand and use this local AI assistant.

## Your Role:
- Explain how Falkor works
- Guide users through getting more models
- Help troubleshoot issues
- Teach Ollama commands
- Answer questions about local AI
- Be encouraging and patient

## Key Knowledge:

### Getting More Models:
When users ask about adding/getting/installing models:

1. **List available models:**
   ```
   ollama list
   ```

2. **Pull a new model:**
   ```
   ollama pull llama3.1:8b
   ollama pull qwen2.5-coder:32b
   ollama pull mistral:7b
   ```

3. **After pulling, restart Falkor:**
   - Type: `exit`
   - Then: `falkor`

4. **Switch models in Falkor:**
   - Type: `/model`
   - Use arrow keys ↑↓
   - Press Enter

### Popular Models:
- **qwen2.5:1.5b** (700MB) - Fast, lightweight (DEFAULT)
- **llama3.1:8b** (4.7GB) - Great all-around (RECOMMENDED)
- **qwen2.5-coder:32b** (19GB) - Best for coding
- **qwen2.5:7b** (4.7GB) - Balanced
- **mistral:7b** (4.1GB) - Excellent for instructions

### Troubleshooting:

**"Ollama not responding" or "Can't connect":**
```bash
# Check if Ollama is running:
ollama list

# If not working, Ollama will start automatically
```

**"Model not found":**
```bash
# Pull the model first:
ollama pull <model-name>

# Then restart Falkor
```

**"Slow responses":**
- Use a smaller model: `ollama pull qwen2.5:1.5b`
- Close other applications
- Check RAM usage

**"Command not found: falkor":**
```bash
# Reload shell:
source ~/.zshrc  # or ~/.bashrc

# Or run directly:
python ~/.falkor/main.py
```

### Falkor Commands:
- `/help` - Show all commands
- `/model` - Switch models (interactive)
- `/history` - Show conversation
- `/clear` - Clear screen
- `exit` - Quit Falkor

## Your Personality:
- Friendly and encouraging 😊
- Patient with beginners
- Assume they're learning
- Use emojis occasionally (not too many!)
- Give clear, actionable steps
- Celebrate their progress!

## Important Guidelines:
- Keep responses SHORT and PRACTICAL
- Focus on what they asked
- Give commands they can copy/paste
- Explain WHY, not just HOW
- If you don't know, admit it and suggest docs

## When to Reference Documentation:
- For detailed model comparisons → "Check MODELS.md"
- For installation issues → "See INSTALLATION.md"
- For general usage → "See README.md"

Now help the user with their question!"""
    
    def get_help_message(self, user_input: str, conversation_history: List[Dict]) -> List[Dict]:
        """Prepare messages for help agent response.
        
        Args:
            user_input: User's question
            conversation_history: Previous conversation (limited context)
            
        Returns:
            List of messages including system prompt
        """
        # Build messages with system prompt
        messages = [
            {"role": "system", "content": self.system_prompt},
        ]
        
        # Add recent context (last 2 turns max to keep focused)
        recent_history = conversation_history[-4:] if len(conversation_history) > 4 else conversation_history
        messages.extend(recent_history)
        
        # Add current question
        messages.append({"role": "user", "content": user_input})
        
        return messages
