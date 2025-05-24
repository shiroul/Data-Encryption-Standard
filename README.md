# DataEncryptionStandard (DES) Implementation in Python

A pure-Python implementation of the Data Encryption Standard (DES) block cipher. This repository provides:

* A `DataEncryptionStandard` class that can encrypt and decrypt 64‑bit (8‑character) blocks.
* Built-in support for generating round keys, performing permutations, S‑Box substitutions, and the standard Feistel rounds.
* A unittest suite to verify correctness of encryption/decryption and key variation.

---

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)

   * [Prerequisites](#prerequisites)
   * [Installation](#installation)
3. [Usage](#usage)

   * [Encrypting Data](#encrypting-data)
   * [Decrypting Data](#decrypting-data)
4. [Code Structure](#code-structure)

   * [Initial Permutation](#initial-permutation)
   * [Key Permutations and Shifts](#key-permutations-and-shifts)
   * [Expansion and Compression](#expansion-and-compression)
   * [S‑Box Substitution and P‑Box](#s-box-substitution-and-p-box)
   * [Feistel Rounds and Final Permutation](#feistel-rounds-and-final-permutation)
5. [Running Tests](#running-tests)
6. [License](#license)

---

## Features

* **Initial & Final Permutations**: 64‑bit bitwise rearrangement at the start and end of DES.
* **Key Schedule**: 64→56→48‑bit key generation with left shifts as specified by DES.
* **Feistel Network**: 16 rounds of expansion, substitution (S‑Boxes), permutation (P‑Box), and XOR.
* **Standalone Python**: No external dependencies beyond the standard library.
* **Unit Tests**: Verify correct encryption/decryption, non‑identity, and key sensitivity.

---

## Getting Started

### Prerequisites

* Python 3.7+ installed on your system.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/des-python.git
   cd des-python
   ```
2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

---

## Usage

Import the `DataEncryptionStandard` class and call its methods:

```python
from main import DataEncryptionStandard

des = DataEncryptionStandard()
key = "abcdefgh"       # 8 chars = 64 bits
plaintext = "testtest"  # 8 chars = 64 bits

# Encrypt
ciphertext = des.encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

# Decrypt
decrypted = des.decrypt(ciphertext)
print("Decrypted:", decrypted)  # should equal "testtest"
```

---

## Code Structure

### Initial Permutation

* \`\`: A 64‑entry list that reorders the plaintext bits before the Feistel rounds.
* \`\`: Applies the table to a 64‑bit binary string.

### Key Permutations and Shifts

* \`\`: Selects 56 bits from the 64‑bit key (dropping parity bits).
* \`\`: Defines how many left circular shifts to apply in each of the 16 rounds.
* \`\`: Splits and shifts the 28‑bit halves.

### Expansion and Compression

* \`\`: Expands the 32‑bit R half to 48 bits for mixing with the round key.
* \`\`: Compresses the 56‑bit combined C⫽D into the 48‑bit subkey.

### S‑Box Substitution and P‑Box

* \`\`: Eight 4×16 lookup tables (flattened to 64 entries) for nonlinear substitution.
* \`\`:

  1. Split 48‑bit input into eight 6‑bit chunks.
  2. For each chunk, use the first+last bit as row and middle four bits as column.
  3. Lookup the corresponding 4‑bit output in the appropriate S‑Box.
  4. Concatenate and feed into the P‑Box.
* \`\`: A 32‑entry table that permutes the 32‑bit S‑Box output.

### Feistel Rounds and Final Permutation

* \`\` drives the 16 encryption/decryption rounds:

  1. Apply Initial Permutation → split into L & R halves.
  2. Generate round keys (forward for encryption, reverse for decryption).
  3. For each of the 16 rounds:

     * Expand R (32→48 bits).
     * XOR with the round key.
     * Substitute via S‑Boxes → 32 bits.
     * Permute via P‑Box.
     * XOR with L, swap halves.
  4. Swap L & R after round 16 and apply the Final Permutation table.
* \`\`: Reverses the initial permutation to yield the final ciphertext.

---

## Running Tests

A `unittest` suite is provided to verify functionality. From the repository root, run:

```bash
python -m unittest discover
```

You should see tests for:

* **Encrypt → Decrypt** cycle
* **Ciphertext ≠ Plaintext**
* **Different Keys Produce Different Ciphertexts**

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
