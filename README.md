# Cosmos private key from seed phrase / mnemonic

## Using Python to Convert a Seed Phrase to a Private Key

We can achieve this with the `mnemonic`, `bip32utils`, and `bip39` libraries. Additionally, the `cosmospy` library simplifies Cosmos private key derivation.

## Install Required Libraries

Run the following command to install the necessary libraries:

```bash
pip install cosmospy mnemonic
```

## How It Works

**Seed Phrase**: The seed phrase is provided as input.

**Derivation Path**: The default path for Cosmos (m/44'/118'/0'/0/0) is used.

**Private Key Generation**: cosmospy's seed_to_privkey function converts the mnemonic to a private key.

**Output**: The private key is printed as a hex string.

argparse is used to define two arguments:

* --seed: The seed phrase (required).
* --path: Optional argument to specify a custom derivation path (default is m/44'/118'/0'/0/0).
The script reads the --seed value from the command line.
It passes the seed phrase and derivation path to the derive_cosmos_private_key function.
The private key is derived and displayed.

---

## Running the Script

Save the script as derive_cosmos_key.py and run it from the terminal:

```bash
python derive_cosmos_key.py --seed "mimic orphan adjust happy book cave divert grocery cricket brain diesel duck"
```

Optional: Specify a Different Derivation Path

```bash
python derive_cosmos_key.py --seed "mimic orphan adjust happy book cave divert grocery cricket brain diesel duck" --path "m/44'/118'/0'/0/1"
```

---

## Output

The output will look like this:

**Cosmos Private Key (hex)**: 4f4f5a8e2f0f55b96a3c22b1a17bc5b3e7e8ecdb2adf... (truncated)

---

## Key Notes

* Always securely store your seed phrase and derived private keys.
* The private key allows full control over your funds.
* The script follows the Cosmos chain standard derivation path.
* The --seed argument is required; the script will fail if it’s missing.
* Enclose the seed phrase in quotes if it contains spaces.
* The --path argument allows you to specify a custom derivation path for flexibility.
