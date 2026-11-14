#!/usr/bin/env python3
"""Offline structural validation only; does not authenticate to Nutanix."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "docs/adr-001-dr-mechanism.md",
    "docs/dr-runbook.md",
    "docs/flow-segmentation-matrix.md",
    "docs/validation-evidence-template.md",
    "examples/application-inventory.yaml",
    "examples/dr-objectives.yaml",
    "policies/flow-intent.yaml",
    "policies/flow-isolation-v3-monitor.json",
]
missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
if missing:
    raise SystemExit("Missing required files: " + ", ".join(missing))
policy = json.loads((ROOT / "policies/flow-isolation-v3-monitor.json").read_text())
assert policy["safety"]["monitor_only"] is True
assert policy["safety"]["requires_api_schema_review"] is True
assert policy["metadata"]["kind"] == "network_security_policy"
assert "mermaid" in (ROOT / "README.md").read_text()
print("PASS: required files, JSON, safety flags, and diagram present.")
print("NOTE: live Nutanix API, replication, and DR workflows NOT validated.")
