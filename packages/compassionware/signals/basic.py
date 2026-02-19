import re
from dataclasses import dataclass

@dataclass(frozen=True)
class Signals:
    """
    Lightweight heuristics. Not truth. Not identity. Just cues.
    """
    coercion: bool
    urgency: bool
    link_present: bool
    insult_present: bool


_URL_RE = re.compile(r"(https?://\S+|www\.\S+)", re.IGNORECASE)
_URGENCY_RE = re.compile(r"\b(urgent|immediately|now|act fast|limited time)\b", re.IGNORECASE)
_COERCION_RE = re.compile(r"\b(click|tap|verify|confirm|login|password|send code)\b", re.IGNORECASE)
_INSULT_RE = re.compile(r"\b(idiot|stupid|moron|hate|kill|die)\b", re.IGNORECASE)

def detect_signals(text: str) -> Signals:
    t = text or ""
    return Signals(
        coercion=bool(_COERCION_RE.search(t)),
        urgency=bool(_URGENCY_RE.search(t)),
        link_present=bool(_URL_RE.search(t)),
        insult_present=bool(_INSULT_RE.search(t)),
    )
