---
name: nailong-pet
description: Install or recreate the local Codex custom pet named 奶龙 from bundled assets. Use when the user asks for 奶龙.skills, 奶龙宠物, this yellow character pet, Hatch Pet setup for this specific image, or wants Codex to directly install the prebuilt pet package into ~/.codex/pets without regenerating images.
---

# 奶龙.skills

## Purpose

Use this skill to install the bundled 奶龙 Codex pet immediately. The skill includes a validated Codex-compatible `spritesheet.webp` and a reference preview, so do not regenerate images unless the user explicitly asks for a new visual version.

## Quick Install

From this skill directory, run:

```bash
python scripts/install_nailong_pet.py
```

This creates:

```text
~/.codex/pets/nailong/
  pet.json
  spritesheet.webp
```

After installing, tell the user to restart Codex and select the pet from:

```text
Settings -> Appearance -> Pets -> Select -> 奶龙
```

## Custom Name

If the user wants a different installed name or id:

```bash
python scripts/install_nailong_pet.py --pet-id huang-tuan-tuan --display-name "黄团团"
```

Use lowercase ASCII ids with hyphens. Display names may be Chinese.

## Bundled Assets

- `assets/nailong-spritesheet.webp`: Codex pet atlas, 1536 x 1872, 8 columns x 9 rows, transparent background.
- `assets/nailong-reference.png`: First-frame preview of the pet.

The bundled state mapping is:

| Codex row | Pet behavior |
|---|---|
| `idle` | 待机 |
| `running-right` | 向右跑，拖动宠物右移时 |
| `running-left` | 向左跑，拖动宠物左移时 |
| `waving` | 开心挥手备用 |
| `jumping` | done / 开心跳一下 |
| `failed` | sleeping / 趴下睡觉 |
| `waiting` | 等待输入 |
| `running` | working / 敲代码中 |
| `review` | thinking / 歪头冒问号 |

## If The User Wants A New Version

Use the installed `hatch-pet` skill if available for a full image-generation workflow. Preserve this skill's bundled assets unless the user explicitly asks to update 奶龙.skills itself.
