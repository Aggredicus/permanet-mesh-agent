from __future__ import annotations

import importlib.util
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "scripts" / "generate_review_packet.py"
    spec = importlib.util.spec_from_file_location("generate_review_packet", path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_build_packet_contains_review_sections(monkeypatch):
    module = load_module()

    def fake_git_text(*args: str, fallback: str = "Unavailable") -> str:
        command = " ".join(args)
        values = {
            "branch --show-current": "quality/6-code-review-pipeline",
            "rev-parse --short HEAD": "abc1234",
            "status --short": "None",
            "diff --name-only main...": "docs/sops/code-review-process.md",
            "diff --stat main...": "1 file changed",
            "log --oneline main..HEAD": "abc1234 Add review process",
        }
        return values.get(command, fallback)

    monkeypatch.setattr(module, "git_text", fake_git_text)

    packet = module.build_packet("main")

    assert "# Pull Request Review Packet" in packet
    assert "quality/6-code-review-pipeline" in packet
    assert "docs/sops/code-review-process.md" in packet
    assert "## Validation checklist" in packet
    assert "## Review checklist" in packet
    assert "Ready for maintainer review" in packet
