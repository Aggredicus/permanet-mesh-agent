from __future__ import annotations

from dataclasses import dataclass, field

PaginationKey = tuple[str, int]


@dataclass
class PaginationCache:
    """In-memory continuation cache keyed by node and channel.

    The cache intentionally does not persist across process restarts in v0.2.
    Its purpose is only to prevent automatic multi-packet flooding while still
    allowing a user to explicitly request the next chunk with MORE.
    """

    _pending: dict[PaginationKey, list[str]] = field(default_factory=dict)

    def store(self, node_id: str, channel_index: int, chunks: list[str]) -> None:
        """Store continuation chunks for a node/channel pair."""

        key = (node_id, channel_index)
        clean_chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
        if clean_chunks:
            self._pending[key] = clean_chunks
            return
        self._pending.pop(key, None)

    def pop_next(self, node_id: str, channel_index: int) -> str | None:
        """Return the next pending chunk, clearing state when exhausted."""

        key = (node_id, channel_index)
        chunks = self._pending.get(key)
        if not chunks:
            self._pending.pop(key, None)
            return None

        next_chunk = chunks.pop(0)
        if chunks:
            self._pending[key] = chunks
        else:
            self._pending.pop(key, None)
        return next_chunk

    def has_pending(self, node_id: str, channel_index: int) -> bool:
        """Return whether a node/channel pair has pending continuation chunks."""

        return bool(self._pending.get((node_id, channel_index)))

    def clear(self, node_id: str, channel_index: int) -> None:
        """Clear pending continuation state for a node/channel pair."""

        self._pending.pop((node_id, channel_index), None)
