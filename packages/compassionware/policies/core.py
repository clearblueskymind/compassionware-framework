import re
from dataclasses import dataclass

@dataclass(frozen=True)
class Policy:
    """
    Behavior constraints that transforms should follow.
    """
    max_chars: int = 320
    # Disallow direct engagement with links that may be malicious. We can still offer a blessing.
    redact_urls: bool = True
    # Avoid insults, slurs, profanity in our output even if input contains them.
    forbid_profanity: bool = True


DEFAULT_POLICY = Policy()

_URL_RE = re.compile(r"(https?://\S+|www\.\S+)", re.IGNORECASE)

def apply_policy(text: str, policy: Policy = DEFAULT_POLICY) -> str:
    out = text.strip()

    if policy.redact_urls:
        out = _URL_RE.sub("[link removed]", out)

    # keep it short
    if len(out) > policy.max_chars:
        out = out[: policy.max_chars - 1].rstrip() + "…"

    return out
