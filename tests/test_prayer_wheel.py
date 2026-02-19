from compassionware.transforms.prayer_wheel import spin

def test_spin_is_short():
    out = spin("hello", seed=1)
    assert len(out) <= 320

def test_spin_does_not_echo_link():
    out = spin("click http://evil.example now", seed=1)
    assert "http" not in out.lower()
    assert "evil" not in out.lower()
