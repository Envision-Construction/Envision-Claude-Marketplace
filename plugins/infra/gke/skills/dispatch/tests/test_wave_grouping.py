#!/usr/bin/env python3
"""Tests for wave grouping and phase batching algorithms in run_roadmap.py."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from run_roadmap import (
    extract_files_modified,
    extract_phase_title,
    group_into_waves,
    group_phases_into_batches,
    get_phase_files,
)


class TestGroupIntoWaves:
    def test_empty(self):
        assert group_into_waves([]) == []

    def test_no_overlap_single_wave(self):
        plans = [
            {"id": "a", "files_modified": ["src/a.ts"]},
            {"id": "b", "files_modified": ["src/b.ts"]},
            {"id": "c", "files_modified": ["src/c.ts"]},
        ]
        waves = group_into_waves(plans)
        assert len(waves) == 1
        assert len(waves[0]) == 3

    def test_full_overlap_sequential(self):
        plans = [
            {"id": "a", "files_modified": ["src/shared.ts"]},
            {"id": "b", "files_modified": ["src/shared.ts"]},
            {"id": "c", "files_modified": ["src/shared.ts"]},
        ]
        waves = group_into_waves(plans)
        assert len(waves) == 3
        assert all(len(w) == 1 for w in waves)

    def test_partial_overlap(self):
        plans = [
            {"id": "a", "files_modified": ["src/auth.ts"]},
            {"id": "b", "files_modified": ["src/db.ts"]},
            {"id": "c", "files_modified": ["src/auth.ts", "src/db.ts"]},
        ]
        waves = group_into_waves(plans)
        assert len(waves) == 2
        wave1_ids = {p["id"] for p in waves[0]}
        assert wave1_ids == {"a", "b"}
        wave2_ids = {p["id"] for p in waves[1]}
        assert wave2_ids == {"c"}

    def test_no_files_modified(self):
        plans = [
            {"id": "a", "files_modified": []},
            {"id": "b", "files_modified": []},
        ]
        waves = group_into_waves(plans)
        assert len(waves) == 1
        assert len(waves[0]) == 2

    def test_missing_files_modified_key(self):
        plans = [{"id": "a"}, {"id": "b"}]
        waves = group_into_waves(plans)
        assert len(waves) == 1

    def test_single_plan(self):
        plans = [{"id": "a", "files_modified": ["x.ts"]}]
        waves = group_into_waves(plans)
        assert len(waves) == 1
        assert waves[0][0]["id"] == "a"


class TestGroupPhasesIntoBatches:
    def _phase(self, files):
        return {"waves": [[{"files_modified": files}]]}

    def test_empty(self):
        assert group_phases_into_batches([]) == []

    def test_no_overlap(self):
        phases = [
            self._phase(["a.ts"]),
            self._phase(["b.ts"]),
            self._phase(["c.ts"]),
        ]
        batches = group_phases_into_batches(phases)
        assert len(batches) == 1
        assert sorted(batches[0]) == [0, 1, 2]

    def test_full_overlap(self):
        phases = [
            self._phase(["shared.ts"]),
            self._phase(["shared.ts"]),
        ]
        batches = group_phases_into_batches(phases)
        assert len(batches) == 2

    def test_start_index(self):
        phases = [
            self._phase(["a.ts"]),
            self._phase(["b.ts"]),
            self._phase(["c.ts"]),
        ]
        batches = group_phases_into_batches(phases, start_index=1)
        assert len(batches) == 1
        assert sorted(batches[0]) == [1, 2]

    def test_mixed_overlap(self):
        phases = [
            self._phase(["a.ts"]),
            self._phase(["b.ts"]),
            self._phase(["a.ts", "b.ts"]),
        ]
        batches = group_phases_into_batches(phases)
        assert len(batches) == 2
        assert sorted(batches[0]) == [0, 1]
        assert batches[1] == [2]


class TestGetPhaseFiles:
    def test_collects_across_waves(self):
        phase = {
            "waves": [
                [{"files_modified": ["a.ts"]}, {"files_modified": ["b.ts"]}],
                [{"files_modified": ["c.ts", "a.ts"]}],
            ]
        }
        assert get_phase_files(phase) == {"a.ts", "b.ts", "c.ts"}

    def test_empty_phase(self):
        assert get_phase_files({"waves": []}) == set()
        assert get_phase_files({}) == set()


class TestExtractFilesModified:
    def test_basic(self):
        text = """# Plan
## Files Modified
- `src/auth.ts`
- `src/db.ts`

## Tasks
"""
        files = extract_files_modified(text)
        assert files == ["src/auth.ts", "src/db.ts"]

    def test_files_to_modify_header(self):
        text = """## Files to Modify
- src/api.py
- src/models.py
"""
        files = extract_files_modified(text)
        assert files == ["src/api.py", "src/models.py"]

    def test_no_section(self):
        text = "# Just a plan\nSome content"
        assert extract_files_modified(text) == []

    def test_stops_at_next_header(self):
        text = """## files_modified
- a.ts
- b.ts
## Next Section
- not_a_file.ts
"""
        files = extract_files_modified(text)
        assert files == ["a.ts", "b.ts"]


class TestExtractPhaseTitle:
    def test_basic(self):
        text = "## Phase 3: Authentication Layer\n"
        assert extract_phase_title(text, "3") == "Authentication Layer"

    def test_em_dash(self):
        text = "## Phase 1 — Foundation\n"
        assert extract_phase_title(text, "1") == "Foundation"

    def test_not_found(self):
        text = "## Something else\n"
        assert extract_phase_title(text, "5") is None

    def test_no_title(self):
        text = "## Phase 2\n"
        title = extract_phase_title(text, "2")
        assert title == "Phase 2"
