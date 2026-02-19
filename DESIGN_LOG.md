# DESIGN_LOG

## 2026-02-19 — Initial framework scaffolding

**Flagship:** Digital Prayer Wheel (spam / hostility → blessing-forward response)

### Design commitments (“you set the vows”)
- We do not retaliate.
- We do not shame.
- We do not impersonate.
- We do not include personal data.
- We keep responses short, calm, and non-engaging with malicious content.

### Architectural choices
- `intention/` contains explicit vows & defaults.
- `policies/` contains rules enforced by transforms (and tested).
- `signals/` contains lightweight detectors (no claims of “truth detection”).
- `transforms/` is pure, testable logic.
- `adapters/` is optional and separated from core ethics logic.

### Next steps
- Add adapter examples (Discord webhook, SMS provider stubs)
- Add richer blessings sources (user-provided, multilingual packs)
- Add sincerity-signal module for “human vs. coercion patterns”
