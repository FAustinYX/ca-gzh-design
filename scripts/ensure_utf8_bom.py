#!/usr/bin/env python3
"""为正文 HTML 添加 UTF-8 BOM，避免 Safari 将无 head 的片段误判编码。"""

from pathlib import Path
import sys


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("用法: ensure_utf8_bom.py <section.html>")
    path = Path(sys.argv[1])
    raw = path.read_bytes()
    bom = b"\xef\xbb\xbf"
    if not raw.startswith(bom):
        path.write_bytes(bom + raw)
    print(f"✓ 已确保 UTF-8 BOM: {path}")


if __name__ == "__main__":
    main()
