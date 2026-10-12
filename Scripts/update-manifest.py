#!/usr/bin/env python3
"""Point bucket/usage-relay.json at an AI·mana release.

Usage: Scripts/update-manifest.py [TAG]   (default: the latest release)
Prints the new version, or nothing when the manifest is already current.
"""
import json, pathlib, re, sys, urllib.request

REPO = "p4ranoic0/AI-mana"
MANIFEST = pathlib.Path(__file__).resolve().parent.parent / "bucket" / "usage-relay.json"


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "scoop-bucket-updater"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode()


tag = sys.argv[1] if len(sys.argv) > 1 else json.loads(
    fetch(f"https://api.github.com/repos/{REPO}/releases/latest"))["tag_name"]
if not re.fullmatch(r"v\d+\.\d+\.\d+", tag):
    sys.exit(f"Unexpected tag: {tag}")
version = tag[1:]
asset = f"usage-relay-{version}-windows-x86_64.zip"

sums = {}
for line in fetch(f"https://github.com/{REPO}/releases/download/{tag}/SHA256SUMS.txt").splitlines():
    digest, name = line.split()
    sums[name.removeprefix("./")] = digest
if asset not in sums:
    sys.exit(f"{asset} is missing from {tag}/SHA256SUMS.txt")

manifest = json.loads(MANIFEST.read_text())
arch = manifest["architecture"]["64bit"]
new_url = f"https://github.com/{REPO}/releases/download/{tag}/{asset}"
if manifest["version"] == version and arch["url"] == new_url and arch["hash"] == sums[asset]:
    sys.exit(0)
manifest["version"] = version
arch["url"] = new_url
arch["hash"] = sums[asset]
MANIFEST.write_text(json.dumps(manifest, indent=4, ensure_ascii=False) + "\n")
print(version)
