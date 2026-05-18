#!/usr/bin/env python3
"""Install the bundled Nailong Codex pet into ~/.codex/pets."""

from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path


def codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser().resolve()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pet-id", default="nailong")
    parser.add_argument("--display-name", default="奶龙")
    parser.add_argument(
        "--description",
        default="一个带待机、敲代码、思考、等待、完成、睡觉和左右跑动状态的黄色 Codex 陪伴宠物。",
    )
    parser.add_argument("--dest-root", default=str(codex_home() / "pets"))
    args = parser.parse_args()

    skill_dir = Path(__file__).resolve().parents[1]
    source_sheet = skill_dir / "assets" / "nailong-spritesheet.webp"
    if not source_sheet.exists():
        raise SystemExit(f"missing bundled spritesheet: {source_sheet}")

    pet_id = args.pet_id.strip()
    if not pet_id:
        raise SystemExit("--pet-id cannot be empty")

    dest_root = Path(args.dest_root).expanduser().resolve()
    pet_dir = dest_root / pet_id
    pet_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy2(source_sheet, pet_dir / "spritesheet.webp")
    manifest = {
        "id": pet_id,
        "displayName": args.display_name,
        "description": args.description,
        "spritesheetPath": "spritesheet.webp",
    }
    (pet_dir / "pet.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps({"ok": True, "pet_dir": str(pet_dir), "manifest": manifest}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
