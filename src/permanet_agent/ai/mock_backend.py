class MockAIBackend:
    """Deterministic local backend for tests and development."""

    def answer(self, prompt: str) -> str:
        text = " ".join(prompt.strip().split())
        if not text:
            return "Ask a short field question after @permanet ask."
        return "Mock answer: " + text[:120]
