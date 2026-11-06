#!/usr/bin/env python3
"""Safely import the project lead's native Altium template ZIP."""
from pathlib import Path
import hashlib
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1] / "templates" / "altium-rnd"
DEST = ROOT / "source"

def main():
    if len(sys.argv) != 2:
        print("Usage: python hardware/tools/import_altium_template.py SOURCE.zip")
        return 2
    manifest = {}
    for line in (ROOT / "MANIFEST.sha256").read_text().splitlines():
        if line.strip() and not line.startswith("#"):
            sha, name = line.split(maxsplit=1)
            manifest[name] = sha
    verified = {}
    try:
        with zipfile.ZipFile(sys.argv[1]) as archive:
            for name, sha in manifest.items():
                matches = [entry for entry in archive.infolist()
                           if not entry.is_dir() and entry.filename.split("/")[-1] == name]
                if len(matches) != 1:
                    raise ValueError(f"Expected exactly one {name} in source ZIP")
                data = archive.read(matches[0])
                if hashlib.sha256(data).hexdigest() != sha:
                    raise ValueError(f"Checksum mismatch: {name}")
                verified[name] = data
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        print("Import aborted:", error)
        return 1
    # Preflight prevents partial writes when an existing file differs.
    for name, data in verified.items():
        target = DEST / name
        if target.exists() and target.read_bytes() != data:
            print("Refusing to overwrite:", target)
            return 1
    DEST.mkdir(parents=True, exist_ok=True)
    for name, data in verified.items():
        path = DEST / name
        if not path.exists():
            path.write_bytes(data)
        print("Verified:", path)
    print("Open the .PrjPcb in Altium and independently validate all rules.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
