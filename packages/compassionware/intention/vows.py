from dataclasses import dataclass

@dataclass(frozen=True)
class Vows:
    """
    Core non-negotiables. These are intentionally simple so they can be tested
    and enforced by transforms.
    """
    non_harming: bool = True
    non_escalation: bool = True
    truthfulness: bool = True
    dignity_preservation: bool = True
    no_impersonation: bool = True
    no_personal_data: bool = True


DEFAULT_VOWS = Vows()
