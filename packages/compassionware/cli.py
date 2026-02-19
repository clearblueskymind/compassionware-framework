import argparse
from compassionware.transforms.prayer_wheel import spin

def main() -> None:
    p = argparse.ArgumentParser(prog="compassionware", description="CompassionWare CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    w = sub.add_parser("wheel", help="Digital Prayer Wheel: transform message into a blessing-forward response")
    w.add_argument("text", help="Incoming message text")

    args = p.parse_args()

    if args.cmd == "wheel":
        print(spin(args.text))
