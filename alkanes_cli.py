import argparse
import json
import gzip
import base64
from jsonschema import validate, ValidationError

# JSON schema for config validation (simplified example)
CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "version": {"type": "string"},
        "author": {"type": "string"},
        "description": {"type": "string"},
        "arguments": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": ["name", "version", "author", "description", "arguments"]
}

def validate_config(config_data):
    try:
        validate(instance=config_data, schema=CONFIG_SCHEMA)
    except ValidationError as e:
        print(f"Config validation error: {e.message}")
        return False
    return True

def compress_wasm(wasm_path):
    with open(wasm_path, "rb") as f:
        wasm_bytes = f.read()
    compressed = gzip.compress(wasm_bytes)
    return base64.b64encode(compressed).decode()

def build_inscription(config, wasm_b64):
    inscription = {
        "p": "alnks",
        "op": "deploy",
        "contract": {
            "name": config["name"],
            "version": config["version"],
            "author": config["author"],
            "description": config["description"],
            "arguments": config["arguments"],
            "wasm": wasm_b64
        }
    }
    return inscription

def main():
    parser = argparse.ArgumentParser(description="Alkanes CLI Deploy Tool")
    parser.add_argument("--config", required=True, help="Path to contract config JSON")
    parser.add_argument("--wasm", required=True, help="Path to contract wasm file")
    parser.add_argument("--out", default="inscription.json", help="Output inscription JSON file")

    args = parser.parse_args()

    # Load and validate config
    with open(args.config, "r") as f:
        config_data = json.load(f)

    if not validate_config(config_data):
        print("Invalid config. Exiting.")
        return

    # Compress and encode wasm
    wasm_b64 = compress_wasm(args.wasm)

    # Build inscription JSON
    inscription = build_inscription(config_data, wasm_b64)

    # Write output
    with open(args.out, "w") as f:
        json.dump(inscription, f, indent=4)

    print(f"Inscription JSON written to {args.out}")

if __name__ == "__main__":
    main()

