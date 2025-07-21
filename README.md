 🔥**Alkanes CLI Deployer**

A command-line tool for building and validating **Alkanes smart contract inscriptions**, built for developers preparing for Alkanes on-chain deployment.

This tool helps you:
- ✅ Validate your contract config
- ✅ Compress and encode your WASM contract
- ✅ Generate a full Alkanes deployment inscription JSON

> 🔐 Built with security and reproducibility in mind. Tested in a Python virtual environment.

---

## 🧰 Features

- **Config Validation**: Checks required fields like name, version, description, and arguments.
- **WASM Compression**: Gzip-compress and base64-encode your contract for efficient inscription.
- **Output Builder**: Generates clean `inscription.json` ready for testnet or devnet broadcast.
- **Command Line Friendly**: Pass config and wasm paths easily via CLI.

---

## 🛠 Requirements

- Python 3.8+
- Virtual environment (`venv`) recommended

To install dependencies:

```bash
pip install -r requirements.txt
````

---

## 🚀 Usage

### 1. Activate your virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Run the deploy tool

```bash
python3 alkanes_cli.py --config examples/config.json --wasm examples/contract.wasm --out inscription.json
```

You’ll see:

```
Inscription JSON written to inscription.json
```

### 3. Sample Output (Truncated)

```json
{
  "p": "alnks",
  "op": "deploy",
  "contract": {
    "name": "HelloAlkanes",
    "version": "0.1",
    ...
    "wasm": "H4sICODtfWgC/2NvbnRyYWN0..."
  }
}
```

---

## 📂 Project Structure

```
alkanes-cli-deployer/
├── alkanes_cli.py            # Main CLI tool
├── requirements.txt          # Dependencies
├── examples/
│   ├── config.json           # Example contract metadata
│   └── contract.wasm         # Example WASM contract
└── inscription.json          # Output file (generated)
```

---

## 📜 License

MIT License © 2025 [Phantagyro](https://github.com/Phantagyro)

---

## 🙋‍♂️ Want to Contribute?

Alkanes is still early. Contributions that align with its mission may get future recognition or rewards.

> Let’s build with integrity and readiness. Smart, secure, and simple.


