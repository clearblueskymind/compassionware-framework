# CompassionWare (Framework)

A contemplative-first toolkit for transforming digital interactions toward kindness.

This repository is intentionally structured so **ethics are not an add-on**:
they live in the architecture (vows, policies, signals) and are enforced by tests.

## Seed journal → Cathedral

- **Legacy repo**: the original living journal (notes, transmissions, experiments).
- **This repo**: the clean, installable framework others can adopt and extend.

See: [`LINEAGE.md`](LINEAGE.md) and [`DESIGN_LOG.md`](DESIGN_LOG.md).

## Quick start

```bash
pip install -e ".[dev]"
python -m compassionware.cli --help
```

### Digital Prayer Wheel (flagship)

Transform a hostile or spammy message into a calm, blessing-forward response:

```bash
compassionware wheel "You idiot, click my link now!!!"
```

Or from Python:

```python
from compassionware.transforms.prayer_wheel import spin

print(spin("You idiot, click my link now!!!"))
```

## Modules (high level)

- `intention/` — vows & intention objects (“why”)
- `policies/` — safety & non-escalation rules (“how we behave”)
- `signals/` — lightweight cues (tone, coercion, manipulation) (“what we notice”)
- `transforms/` — conversions (spam → blessing, escalation → de-escalation) (“what we do”)
- `adapters/` — optional connectors (SMS, email, chat) (“where it runs”)

## Contributing

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md). We welcome both
technical improvements and contemplative clarity.
