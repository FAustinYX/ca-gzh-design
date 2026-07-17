#!/usr/bin/env python3
"""把公司固定品牌素材嵌入公众号正文 HTML。"""

import base64
import os
import sys


TOKEN = "{{COMPANY_QR_SRC}}"


def main():
    if len(sys.argv) != 2:
        print("用法: embed_company_assets.py <section.html>")
        raise SystemExit(1)

    html_path = sys.argv[1]
    if not os.path.isfile(html_path):
        print(f"✗ 找不到文件: {html_path}")
        raise SystemExit(1)

    with open(html_path, encoding="utf-8-sig") as f:
        content = f.read()

    if TOKEN not in content:
        print("✓ 未发现公司二维码占位，无需嵌入")
        return

    asset_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "assets",
        "company-wechat-qr.jpg",
    )
    with open(asset_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("ascii")

    content = content.replace(TOKEN, f"data:image/jpeg;base64,{encoded}")
    with open(html_path, "w", encoding="utf-8-sig") as f:
        f.write(content)
    print("✓ 已嵌入公司微信二维码")


if __name__ == "__main__":
    main()
