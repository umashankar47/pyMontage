# 🎯 Sniper Montage Maker

Automatically stitch your best COD sniper clips into a single, polished montage — complete with smooth crossfade transitions, audio fades, and dedicated intro/outro support.

Drop your clips in a folder, hit run, and get a ready-to-upload `.mp4` with zero manual editing.

---

## ✨ Features

- 🎬 **Automatic clip discovery** — supports `.mp4`, `.mov`, `.avi`, `.mkv`, `.webm`
- 🔀 **Smooth crossfade transitions** between clips (video + audio)
- 🎯 **Intro/Outro pinning** — name a clip `intro` or `outro` and it's automatically placed first/last
- 🎲 **Optional random ordering** for the middle clips
- 📐 **Automatic resolution normalization** — mismatched clip sizes won't break the export
- 📁 **No-overwrite output** — never lose a previous render; files auto-increment (`_1`, `_2`, ...)
- 🧱 **Clean, modular OOP structure** — easy to extend with new effects or filters

---

## 📂 Project Structure

```
sniper_montage_maker/
│
├── clips/                     # put your raw clips here
│   ├── intro.mp4               # optional — always plays first
│   ├── clip1.mp4
│   ├── clip2.mp4
│   └── outro.mp4                # optional — always plays last
│
├── output_clips/               # rendered montages (auto-created)
│   └── sniper_montage.mp4
│
├── src/
│   ├── config.py                 # all settings in one place
│   ├── clip_loader.py            # finds, orders & loads clips
│   ├── transition_engine.py      # crossfade + audio fade logic
│   ├── output_manager.py         # unique filename handling
│   └── montage_builder.py        # orchestrates the full pipeline
│
├── main.py                       # entry point
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/sniper_montage_maker.git
cd sniper_montage_maker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your clips

Drop all your clips into the `clips/` folder. Optionally include:

- `intro.mp4` (or `.mov`/`.avi`/etc.) — always plays **first**
- `outro.mp4` — always plays **last**

Everything else in between is sorted (or shuffled, if enabled) automatically.

### 4. Run it

```bash
python main.py
```

Your finished montage will be saved to `output_clips/sniper_montage.mp4` (or `_1`, `_2`, etc. if that name already exists).

---

## ⚙️ Configuration

All settings live in `src/config.py` / are passed into `MontageConfig`:

| Setting              | Default              | Description                                       |
|-----------------------|-----------------------|----------------------------------------------------|
| `input_folder`         | `"clips"`             | Folder to scan for input clips                     |
| `output_folder`        | `"output_clips"`      | Folder where the final video is saved              |
| `output_name`          | `"sniper_montage.mp4"`| Base filename (auto-incremented if it exists)       |
| `transition`           | `0.4`                 | Crossfade duration in seconds                       |
| `fps`                  | `60`                  | Output framerate                                    |
| `random_order`         | `False`               | Shuffle middle clips (intro/outro stay pinned)      |
| `remove_audio`         | `False`               | Strip audio from all clips                          |
| `target_resolution`    | `None`                | Force a resolution, e.g. `(1920, 1080)`             |
| `codec`                | `"libx264"`           | Video codec                                         |
| `audio_codec`          | `"aac"`               | Audio codec                                         |
| `preset`               | `"medium"`            | Encoding speed/quality tradeoff                     |

Example:

```python
from src.config import MontageConfig
from src.montage_builder import MontageBuilder

config = MontageConfig(
    transition=0.6,
    random_order=True,
    target_resolution=(1920, 1080),
)

MontageBuilder(config).build()
```

---

## 🎬 Intro / Outro Support

Name a clip `intro` or `outro` (any supported extension, case-insensitive) and it will automatically be pinned to the start/end of the montage — regardless of `random_order`.

```
clips/
    intro.mp4      →  plays first, always
    clip2.mp4
    clip1.mp4      →  shuffled/sorted in the middle
    outro.mov      →  plays last, always
```

Both are optional — omit either (or both) and the montage builds normally.

---

## 🛠️ Requirements

- Python 3.9+
- [MoviePy](https://zulko.github.io/moviepy/)
- [tqdm](https://github.com/tqdm/tqdm)

```
moviepy
tqdm
```

---

## 🗺️ Roadmap

- [ ] CLI flags (`--transition`, `--random`, `--resolution`)
- [ ] Kill-cam zoom/slow-mo filter module
- [ ] Background music auto-mixing
- [ ] Watermark/logo overlay support

---

## 📄 License

MIT — use it, remix it, ship your montages.
