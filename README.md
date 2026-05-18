# 奶龙.skills

一个开箱即用的 Codex 宠物 skill。它把奶龙宠物资源和安装脚本打包在一起，让 Codex 不需要重新生图，就能直接把宠物安装到本地 `~/.codex/pets`。

![奶龙预览](assets/nailong-reference.png)

## 功能

- 一键安装奶龙 Codex 宠物
- 内置已经验证过的 `spritesheet.webp`
- 支持自定义 `pet-id` 和显示名
- 包含 Codex skill 元数据，可放进 `~/.codex/skills` 自动触发

## 安装这个 skill

把本仓库复制到 Codex skills 目录：

```bash
git clone https://github.com/notdog1998/nailong-pet-skill.git
mkdir -p ~/.codex/skills
cp -R nailong-pet-skill ~/.codex/skills/nailong-pet
```

Windows PowerShell 示例：

```powershell
git clone https://github.com/notdog1998/nailong-pet-skill.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\nailong-pet-skill" "$env:USERPROFILE\.codex\skills\nailong-pet"
```

如果你已经把仓库 fork/改名了，把上面的 GitHub 地址换成你的仓库地址即可。

安装 skill 后，重启 Codex，让它加载新的 skill。

## 安装奶龙宠物

在仓库根目录运行：

```bash
python scripts/install_nailong_pet.py
```

Windows PowerShell：

```powershell
python .\scripts\install_nailong_pet.py
```

安装后会生成：

```text
~/.codex/pets/nailong/
  pet.json
  spritesheet.webp
```

然后重启 Codex，进入：

```text
Settings -> Appearance -> Pets -> Select -> 奶龙
```

## 自定义名称

```bash
python scripts/install_nailong_pet.py --pet-id huang-tuan-tuan --display-name "黄团团"
```

`pet-id` 建议使用小写英文和连字符；`display-name` 可以使用中文。

## 动作映射

Codex 宠物使用固定的 9 行 spritesheet。奶龙当前映射如下：

| Codex 状态行 | 奶龙动作 |
|---|---|
| `idle` | 待机 |
| `running-right` | 向右跑，拖动宠物右移时 |
| `running-left` | 向左跑，拖动宠物左移时 |
| `waving` | 开心挥手备用 |
| `jumping` | 完成后开心跳一下 |
| `failed` | 趴下睡觉 |
| `waiting` | 等待输入 |
| `running` | 敲代码中 |
| `review` | 歪头冒问号 |

## 仓库结构

```text
.
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── nailong-reference.png
│   └── nailong-spritesheet.webp
└── scripts/
    └── install_nailong_pet.py
```

## 校验

如果你本机有 Codex 的 `skill-creator` 系统 skill，可以运行：

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

Windows PowerShell：

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .
```

## 说明

这个仓库专注于“直接安装现成宠物”。如果要重新生成角色图、重做动作或修复 spritesheet，可以结合 OpenAI curated `hatch-pet` skill 另行制作，然后替换 `assets/nailong-spritesheet.webp`。
