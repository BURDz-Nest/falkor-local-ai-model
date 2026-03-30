# 🐛 Known Issues & Future Improvements

## Known Issues

### 1. Banner Resize Issue 🎨
**Priority**: Low  
**Status**: Documented, not blocking  

The ASCII banner doesn't resize perfectly when you change terminal width mid-session. The responsive logic works on startup but doesn't handle live resizing.

**Workaround**: Restart Falkor after resizing terminal  
**Fix**: Would need terminal resize event handling (SIGWINCH signal)  
**Complexity**: Medium - requires signal handling and live redraw  
**Decision**: Skip for now, focus on core functionality  

---

## Future Improvements

### Phase 1 Enhancements
- [ ] Live resize handling for banner
- [ ] Streaming responses (typewriter effect)
- [ ] Better loading indicators
- [ ] Command autocomplete
- [ ] Session history persistence

### Phase 2 (RAG)
- [ ] Document ingestion
- [ ] Vector database setup
- [ ] Embedding generation
- [ ] Context retrieval

### Phase 3 (Multi-Agent)
- [ ] Agent switching
- [ ] Per-agent knowledge bases
- [ ] Agent personalities

---

## Quick Wins (Easy Improvements)
- [ ] Add `/version` command
- [ ] Add `/models` alias for `/model`
- [ ] Show token count in responses
- [ ] Add `/save` to export conversation
- [ ] Color themes

---

**Updated**: 2026-03-17  
**Last Review**: Phase 1 - Step 4
