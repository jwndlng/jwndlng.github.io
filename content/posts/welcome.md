---
title: "Welcome to my blog"
date: "2026-02-24"
description: "The first post on Wndlng's Blog."
categories:
  - "general"
---

Welcome to my blog.

Here is a quick Python example to test code highlighting:

```python
import hashlib

def hash_file(path: str) -> str:
    """Return the SHA-256 digest of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    digest = hash_file("example.txt")
    print(f"SHA-256: {digest}")
```

And a shell snippet:

```bash
#!/usr/bin/env bash
set -euo pipefail

for file in /var/log/*.log; do
    echo "Processing $file"
    grep -i "error" "$file" | tail -n 20
done
```
