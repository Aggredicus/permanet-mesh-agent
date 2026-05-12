from permanet_agent.memory.pagination_cache import PaginationCache


def test_pagination_cache_returns_next_chunk_and_clears_when_done():
    cache = PaginationCache()
    cache.store("!node", 0, ["chunk two", "chunk three"])

    assert cache.has_pending("!node", 0)
    assert cache.pop_next("!node", 0) == "chunk two"
    assert cache.pop_next("!node", 0) == "chunk three"
    assert cache.pop_next("!node", 0) is None
    assert not cache.has_pending("!node", 0)


def test_pagination_cache_is_per_node_and_channel():
    cache = PaginationCache()
    cache.store("!node-a", 0, ["a0"])
    cache.store("!node-a", 1, ["a1"])
    cache.store("!node-b", 0, ["b0"])

    assert cache.pop_next("!node-a", 0) == "a0"
    assert cache.pop_next("!node-a", 1) == "a1"
    assert cache.pop_next("!node-b", 0) == "b0"


def test_pagination_cache_ignores_empty_chunks():
    cache = PaginationCache()
    cache.store("!node", 0, ["", "  "])

    assert cache.pop_next("!node", 0) is None
