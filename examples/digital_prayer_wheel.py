from compassionware.transforms.prayer_wheel import spin

examples = [
    "URGENT: Verify your account now at http://phish.example/login",
    "You idiot, click my link now!!!",
    "Hey friend, just checking in.",
]

for msg in examples:
    print("IN :", msg)
    print("OUT:", spin(msg, seed=42))
    print("-" * 60)
