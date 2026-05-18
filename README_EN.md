<div align="center">

# Nailong.skills

> *"Put Nailong into Codex, and let it keep you company while you code."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Codex Pet](https://img.shields.io/badge/Codex-Pet-blueviolet)](https://openai.com/codex/)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

A ready-to-install Codex pet skill.  
This repository bundles a Nailong `spritesheet.webp`, preview image, and installer script so Codex can install the pet locally without regenerating images.

[Quick Start](#quick-start) · [Install As A Skill](#install-as-a-codex-skill) · [State Mapping](#state-mapping) · [Make Your Own Pet](#make-your-own-pet) · [中文](README.md)

</div>

![Nailong preview](assets/nailong-reference.png)

## What Is Included

```text
.
├── SKILL.md                         # Codex skill entrypoint
├── README.md                        # Chinese documentation
├── README_EN.md                     # English documentation
├── agents/
│   └── openai.yaml                  # Codex UI metadata
├── assets/
│   ├── nailong-reference.png        # README preview image
│   └── nailong-spritesheet.webp     # Codex pet spritesheet atlas
└── scripts/
    └── install_nailong_pet.py       # One-command installer
```

## Quick Start

Clone the repository:

```bash
git clone https://github.com/Zhengyici/nailong-pet-skill.git
cd nailong-pet-skill
```

Install the pet:

```bash
python scripts/install_nailong_pet.py
```

Windows PowerShell:

```powershell
python .\scripts\install_nailong_pet.py
```

The script installs the pet into:

```text
~/.codex/pets/nailong/
  pet.json
  spritesheet.webp
```

Restart Codex, then select:

```text
Settings -> Appearance -> Pets -> Select -> 奶龙
```

## Install As A Codex Skill

To let Codex recognize requests such as "install the Nailong pet", copy this repository into your Codex skills directory.

macOS / Linux:

```bash
mkdir -p ~/.codex/skills
cp -R nailong-pet-skill ~/.codex/skills/nailong-pet
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\nailong-pet-skill" "$env:USERPROFILE\.codex\skills\nailong-pet"
```

Restart Codex after copying the skill.

## Custom Install Name

Default values:

- pet id: `nailong`
- display name: `奶龙`

Customize them:

```bash
python scripts/install_nailong_pet.py --pet-id my-pet --display-name "My Pet"
```

Use lowercase letters, digits, and hyphens for `pet-id`.

## State Mapping

Codex pets use a fixed 9-row spritesheet layout.

| Codex row | Nailong behavior |
|---|---|
| `idle` | Idle |
| `running-right` | Run right, used while dragging the pet right |
| `running-left` | Run left, used while dragging the pet left |
| `waving` | Happy wave fallback |
| `jumping` | Done / happy hop |
| `failed` | Sleeping |
| `waiting` | Waiting for input |
| `running` | Working / coding |
| `review` | Thinking with a question mark |

## Make Your Own Pet

You can use this repository as a template.

1. Replace:

```text
assets/nailong-spritesheet.webp
assets/nailong-reference.png
```

2. Update defaults in `scripts/install_nailong_pet.py`:

```python
parser.add_argument("--pet-id", default="nailong")
parser.add_argument("--display-name", default="奶龙")
```

3. Update `SKILL.md` and `agents/openai.yaml`.

4. Test:

```bash
python scripts/install_nailong_pet.py --pet-id test-pet --display-name "Test Pet"
```

## Atlas Specification

| Field | Value |
|---|---|
| Total size | `1536 x 1872` |
| Grid | `8 columns x 9 rows` |
| Cell size | `192 x 208` |
| Background | Transparent |
| Format | `WEBP` |

## Validate

If you have Codex's `skill-creator` system skill installed:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

Expected output:

```text
Skill is valid!
```

## License

MIT
