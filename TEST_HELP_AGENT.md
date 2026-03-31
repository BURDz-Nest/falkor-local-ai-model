# 🧪 Testing the Help Agent

**Complete guide to testing Falkor's new Help Agent locally**

---

## 🎯 What is the Help Agent?

The Help Agent is a **built-in Falkor assistant** that:
- ✅ Knows how Falkor works
- ✅ Explains Ollama commands
- ✅ Helps users get more models
- ✅ Troubleshoots common issues
- ✅ Auto-activates when it detects Falkor/Ollama questions

---

## 🚀 Quick Test

### Step 1: Start Falkor

```bash
cd ~/Desktop/Dump/Pupclone/dev/falkor
python main.py
```

### Step 2: Try These Test Questions

**Test 1: Auto-Activation (Detects Help Keywords)**
```
You: how do i get more models?

💡 Help Agent activated

Falkor: [Explains ollama pull commands...]
```

**Test 2: Explicit Help Agent Command**
```
You: /help-agent what models should I use?

💡 Help Agent activated

Falkor: [Recommends models based on use case...]
```

**Test 3: Regular Chat (Should NOT Activate)**
```
You: What is Python?

Falkor: [Regular response, no help agent indicator]
```

---

## 📋 Complete Test Scenarios

### Scenario 1: Getting More Models

**Test questions:**
```
- how do i get more models?
- how to install a new model?
- add model
- download model
- pull model
```

**Expected behavior:**
- ✅ Help Agent activates (shows "💡 Help Agent activated")
- ✅ Explains `ollama pull` command
- ✅ Lists popular models
- ✅ Explains how to switch models in Falkor
- ✅ Response is SHORT and ACTIONABLE

---

### Scenario 2: Switching Models

**Test questions:**
```
- how do i switch models?
- change model
- use different model
```

**Expected behavior:**
- ✅ Help Agent activates
- ✅ Explains `/model` command
- ✅ Describes arrow key navigation
- ✅ Shows full workflow

---

### Scenario 3: Troubleshooting

**Test questions:**
```
- ollama not working
- can't connect to ollama
- it's slow
- model not found
- falkor doesn't work
```

**Expected behavior:**
- ✅ Help Agent activates
- ✅ Provides troubleshooting steps
- ✅ Shows relevant commands
- ✅ Offers solutions

---

### Scenario 4: Regular Questions (No Help Agent)

**Test questions:**
```
- What is Python?
- Write me a function
- Explain recursion
- Tell me a joke
```

**Expected behavior:**
- ❌ Help Agent does NOT activate
- ✅ Regular chat response
- ✅ No "💡 Help Agent activated" message
- ✅ Adds to conversation history normally

---

### Scenario 5: Manual Help Agent Command

**Test:**
```
You: /help-agent

(Shows usage examples)

You: /help-agent why is falkor slow?

💡 Help Agent activated

Falkor: [Explains performance tips...]
```

**Expected behavior:**
- ✅ `/help-agent` alone shows usage
- ✅ `/help-agent <question>` activates help mode
- ✅ Works even if question doesn't have help keywords

---

## 🔍 What to Check

### Visual Indicators

**Help Agent Active:**
```
💡 Help Agent activated

Falkor: [response]
```

**Normal Chat:**
```
Falkor: [response]
```

---

### Response Quality

**Help Agent responses should be:**
- ✅ **SHORT** - Get to the point fast
- ✅ **ACTIONABLE** - Give commands to copy/paste
- ✅ **FRIENDLY** - Encouraging tone
- ✅ **ACCURATE** - Correct Ollama/Falkor info
- ✅ **FOCUSED** - Answer the specific question

**Example GOOD response:**
```
Great question! To get more models:

1. Pull a model:
   ollama pull llama3.1:8b

2. Restart Falkor:
   - Type: exit
   - Then: falkor

3. Switch models:
   - Type: /model
   - Use ↑↓ arrows
   - Press Enter

Popular models:
- llama3.1:8b (4.7GB) - Great all-around
- qwen2.5-coder:32b (19GB) - Best for coding

Try pulling llama3.1:8b first! 🎯
```

---

### Conversation History

**Important:** Help Agent responses should NOT pollute conversation history.

**Test:**
```
1. You: What is Python?
   Falkor: [regular response - ADDED to history]

2. You: how do i get models?
   Help Agent: [help response - NOT added to history]

3. You: continue explaining Python
   Falkor: [should continue from step 1, ignoring step 2]
```

**Expected:**
- ✅ Regular chat builds context
- ✅ Help Agent is one-off (doesn't affect context)
- ✅ After help agent, next regular question continues previous context

---

## 🧪 Test Script

Here's a complete test session:

```
[Start Falkor]

# Test 1: Auto-activation
You: how do i get more models?
✓ Check: Help Agent activates
✓ Check: Explains ollama pull
✓ Check: Lists models

# Test 2: Regular chat
You: What is recursion?
✓ Check: No help agent
✓ Check: Normal response

# Test 3: Troubleshooting
You: ollama not working
✓ Check: Help Agent activates
✓ Check: Shows troubleshooting steps

# Test 4: Manual command
You: /help-agent what models are best for coding?
✓ Check: Help Agent activates
✓ Check: Recommends coding models

# Test 5: Check /help menu
You: /help
✓ Check: Shows /help-agent in table
✓ Check: Shows tip about auto-activation

# Test 6: Context preservation
You: Explain Python classes
Falkor: [response 1]

You: how do i install models?
Help Agent: [help response]

You: continue explaining classes
✓ Check: Continues from response 1 (ignores help)

[Exit Falkor]
```

---

## 🐛 Known Issues to Check

### Issue 1: Help Agent Activates Too Often

**Symptom:** Normal questions trigger help agent

**Check:**
```
You: Tell me how to write a function

(Should NOT activate - "how to" is about programming, not Falkor)
```

**Fix if needed:** Adjust keyword detection in `help_agent.py`

---

### Issue 2: Help Agent Doesn't Activate

**Symptom:** "how do i get models?" doesn't activate help

**Check:**
```python
# In falkor/help_agent.py, verify keywords include:
"how do i", "get model", "install model"
```

---

### Issue 3: Response Too Long

**Symptom:** Help agent gives massive responses

**Expected:** Responses should be ~5-10 lines max, focused on the question

**If too long:** The system prompt tells it to be SHORT. Model might ignore. Try different model.

---

## ✅ Success Criteria

Help Agent is working correctly if:

- [x] **Auto-activates** on Falkor/Ollama questions
- [x] **Shows indicator** ("💡 Help Agent activated")
- [x] **Gives helpful responses** (short, actionable)
- [x] **Doesn't pollute history** (one-off responses)
- [x] **Manual command works** (`/help-agent <question>`)
- [x] **Doesn't activate** on regular questions
- [x] **In help menu** (`/help` shows it)
- [x] **Context preserved** (regular chat continues after help)

---

## 📊 Test Results Template

```markdown
## Test Results - [Date]

### Environment
- Falkor version: 0.1.0
- Model tested: llama3.1:8b
- Platform: macOS

### Test 1: Auto-activation
- Input: "how do i get more models?"
- Help Agent activated: ✅ / ❌
- Response quality: ✅ / ❌
- Notes: ___

### Test 2: Regular chat
- Input: "What is Python?"
- Help Agent activated: ❌ (should not)
- Response quality: ✅ / ❌
- Notes: ___

### Test 3: Manual command
- Input: "/help-agent what models for coding?"
- Help Agent activated: ✅ / ❌
- Response quality: ✅ / ❌
- Notes: ___

### Overall
- All tests passed: ✅ / ❌
- Issues found: ___
- Ready to push: ✅ / ❌
```

---

## 🚀 After Testing

### If All Tests Pass:

```bash
cd ~/Desktop/Dump/Pupclone/dev/falkor
git push origin main
```

### If Issues Found:

1. Document the issues
2. Fix in code
3. Re-test
4. Commit fixes
5. Push when ready

---

## 💡 Tips

### Testing Different Models

Some models are better at following the help agent system prompt:

- **llama3.1:8b** - Usually good at being concise
- **qwen2.5-coder:32b** - Excellent at technical help
- **mistral:7b** - Great at following instructions

If help agent is too verbose, try a different model!

### Testing Edge Cases

```
# Edge case 1: Mixed question
You: What is Python and how do I get more models?
(Should activate - detects "how do I get")

# Edge case 2: Typo
You: how do i gt models?
(Should still activate - partial match)

# Edge case 3: Case sensitivity
You: HOW DO I GET MODELS?
(Should activate - case insensitive)
```

---

## 🎯 Ready to Test!

**Start here:**

```bash
cd ~/Desktop/Dump/Pupclone/dev/falkor
python main.py
```

**Ask:**
```
how do i get more models?
```

**Look for:**
```
💡 Help Agent activated
```

**If you see that** → It's working! 🎉

---

**Questions? Issues? Let me know!** 🐶
