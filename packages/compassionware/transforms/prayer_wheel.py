from __future__ import annotations

import random
from dataclasses import dataclass

from compassionware.intention.vows import Vows, DEFAULT_VOWS
from compassionware.policies.core import Policy, DEFAULT_POLICY, apply_policy
from compassionware.signals.basic import detect_signals

DEFAULT_BLESSINGS = [
    "May you be safe. May you be well. May you be at peace.",
    "May your burdens be eased, and may kindness find you today.",
    "May wisdom guide your steps, and may harm fall away.",
    "May you and all beings be free from fear and suffering.",
    "May your heart know rest, and may your life be filled with gentle light.",
    "Shalom. Peace to you, and peace to all who are touched by this moment.",
]

@dataclass(frozen=True)
class WheelResult:
    response: str
    blessing: str
    notes: tuple[str, ...]


def spin(
    incoming: str,
    *,
    vows: Vows = DEFAULT_VOWS,
    policy: Policy = DEFAULT_POLICY,
    blessings: list[str] | None = None,
    seed: int | None = None,
) -> str:
    """
    Digital Prayer Wheel:
    Transform an incoming message (spam/hostility) into a calm, blessing-forward response.

    Philosophy:
    - Do not retaliate.
    - Do not engage malicious content.
    - Offer a short blessing and exit.

    This is deliberately minimal and safe-by-default.
    """
    _ = vows  # vows are carried for future enforcement expansion

    if seed is not None:
        random.seed(seed)

    b = random.choice(blessings or DEFAULT_BLESSINGS)

    sig = detect_signals(incoming or "")
    notes = []
    if sig.link_present:
        notes.append("link_present")
    if sig.coercion:
        notes.append("coercion")
    if sig.urgency:
        notes.append("urgency")
    if sig.insult_present:
        notes.append("insult")

    # We do not echo back hostile text, links, or instructions.
    response = b

    return apply_policy(response, policy)
