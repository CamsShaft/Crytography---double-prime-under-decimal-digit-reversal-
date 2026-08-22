#!/usr/bin/env python3
import argparse
import subprocess
import signal
import sys
from sympy import isprime

def run(cmd: list[str]) -> str:
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"Command failed ({p.returncode}): {' '.join(cmd)}\nSTDERR:\n{p.stderr}")
    return p.stdout.strip()

def generate_prime(bits: int) -> int:
    # relies on your working openssl command
    out = run(["openssl", "prime", "-generate", "-bits", str(bits)])
    return int(out, 10)

def reverse_decimal_digits(n: int) -> int:
    s = str(n)
    rs = s[::-1].lstrip('0')
    return int(rs) if rs else 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, default=1024)
    ap.add_argument("-n", "--iterations", type=int, default=0,
                    help="Number of iterations. Use 0 for infinite until you quit.")
    args = ap.parse_args()

    stop = False
    def on_sigint(sig, frame):
        nonlocal stop
        stop = True
        print("\n[!] Ctrl+C: stopping...", file=sys.stderr)

    signal.signal(signal.SIGINT, on_sigint)

    i = 0
    while True:
        if stop:
            break
        i += 1
        if args.iterations and i > args.iterations:
            break

        p = generate_prime(args.bits)
        r = reverse_decimal_digits(p)

        # only print when "prime in reverse" succeeds
        if isprime(r):
            print(f"\n[+] Found prime whose decimal reverse is also prime")
            print(f"p  ({p.bit_length()} bits, {len(str(p))} digits) = {p}")
            print(f"rev({len(str(p))} digits) = {r}")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
