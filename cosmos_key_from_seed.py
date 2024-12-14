#!/usr/bin/env python

import argparse
from cosmospy import generate_wallet, seed_to_privkey
from mnemonic import Mnemonic

def derive_cosmos_private_key(mnemonic_phrase, derivation_path="m/44'/118'/0'/0/0"):
    """
    Derives the Cosmos private key from a seed phrase using a given derivation path.
    """
    try:
        # Convert mnemonic to private key
        private_key = seed_to_privkey(mnemonic_phrase, path=derivation_path)
        return private_key.hex()  # Return as hex string
    except Exception as e:
        print(f"Error deriving private key: {e}")
        return None

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Derive Cosmos Private Key from Seed Phrase")
    parser.add_argument(
        "--seed",
        type=str,
        required=True,
        help="Your 12 or 24-word seed phrase enclosed in quotes"
    )
    parser.add_argument(
        "--path",
        type=str,
        default="m/44'/118'/0'/0/0",
        help="HD wallet derivation path (default: m/44'/118'/0'/0/0)"
    )
    args = parser.parse_args()

    # Derive the private key
    cosmos_private_key = derive_cosmos_private_key(args.seed, args.path)
    if cosmos_private_key:
        print("Cosmos Private Key (hex):", cosmos_private_key)


