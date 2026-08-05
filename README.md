# pyMontage — Gaming Montage Maker

Automatically stitch your best Gaming clips into a single, polished montage — complete with smooth crossfade transitions, audio fades, VFR-safe clip normalization, and dedicated intro/outro support.

Drop your clips in a folder, run one command, and get a ready-to-upload `.mp4` with zero manual editing.

---

## ✨ Features

* 🎬 **Automatic clip discovery** — supports `.mp4`, `.mov`, `.avi`, `.mkv`, `.webm`
* 🔀 **Smooth crossfade transitions** between clips (video + audio)
* 🎯 **Intro/Outro pinning** — name a clip `intro` or `outro` and it's automatically placed first/last (errors out if more than one of either is found)
* 🎲 **Optional random ordering** for the middle clips
* 📐 **Automatic resolution normalization** — mismatched clip sizes won't break the export
* 🩹 **VFR → CFR normalization** — phone/mobile clips with variable frame rates are automatically re-encoded to a constant 30fps via `ffmpeg` before loading, and cached in `clips/.normalized/` so it only happens once per clip
* 🕒 **Timestamped, no-overwrite output** — every render gets a unique, timestamped filename; nothing gets clobbered
* 🖥️ **Full CLI** — override any setting from the command line without touching code
* 🧱 **Clean, modular OOP structure** — easy to extend with new effects or filters
* 🧹 **Automatic cleanup** — loaded clips are always closed, even if the build fails partway through

---

## 📂 Project Structure

```
pyMontage/
│
├── clips/                      # put your raw clips here
│   ├── intro.mp4                # optional — always plays first
│   ├── clip1.mp4
│   ├── clip2.mp4
│   ├── outro.mp4                # optional — always plays last
│   └── .normalized/             # auto-created cache of CFR-normalized clips
│
├── output_clips/                # rendered montages (auto-created)
│   └── CallOfDutyMobile_2026-08-05_22-53-18.mp4
│
├── src/
│   ├── config.py                  # MontageConfig — all settings in one place
│   ├── clip_loader.py             # finds, normalizes, orders & loads clips
│   ├── transition_engine.py       # crossfade + audio fade logic
│   ├── output_manager.py          # unique, timestamped filename handling
│   └── montage_builder.py         # orchestrates the full pipeline
│
├── main.py                        # CLI entry point
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo

```
git clone https://github.com/umashankar47/pyMontage.git
cd pyMontage
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

You'll also need **[ffmpeg](https://ffmpeg.org/download.html)** installed and available on your `PATH` — it's used to normalize variable-frame-rate clips before rendering.

### 3. Add your clips

Drop all your clips into the `clips/` folder. Optionally include:

* `intro.mp4` (or `.mov`/`.avi`/etc.) — always plays **first**
* `outro.mp4` — always plays **last**

Everything else in between is sorted (or shuffled, if `--random` is set) automatically.

### 4. Run it

```
python main.py
```

Your finished montage will be saved to `output_clips/` with a timestamped filename, e.g. `CallOfDutyMobile_2026-08-05_22-53-18.mp4`.

---

## ⚙️ Configuration

All settings live in `src/config.py` as `MontageConfig` defaults, and can be overridden per-run via CLI flags.

| Setting            | CLI flag           | Default                | Description                                          |
|---------------------|---------------------|-------------------------|--------------------------------------------------------|
| `input_folder`       | `--input`            | `clips/` (project root) | Folder to scan for input clips                        |
| `output_folder`      | `--output`           | `output_clips/` (project root) | Folder where the final video is saved          |
| `output_name`        | `--opfile`           | `CallOfDutyMobile.mp4`  | Base filename (timestamped + auto-incremented if it exists) |
| `transition`         | `--transition`       | `0.4`                   | Crossfade duration in seconds                          |
| `fps`                | `--fps`              | `60`                    | Output framerate                                        |
| `random_order`       | `--random`           | `False`                 | Shuffle middle clips (intro/outro stay pinned)          |
| `remove_audio`       | `--remove-audio`     | `False`                 | Strip audio from all clips                              |
| `target_resolution`  | `--resolution`       | `None`                  | Force a resolution, e.g. `1920x1080`                    |
| `codec`              | `--codec`            | `libx264`               | Video codec                                              |
| `audio_codec`        | `--audio-codec`      | `aac`                   | Audio codec                                              |
| `threads`            | `--threads`          | `8`                     | Number of threads for video processing                  |
| `preset`             | `--preset`           | `medium`                | Encoding speed/quality tradeoff                          |

Only flags you actually pass override the defaults — anything omitted falls back to `MontageConfig`.

### CLI example

```
python main.py --transition 0.6 --random --resolution 1920x1080 --preset fast
```

### Programmatic example

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

Both are optional — omit either (or both) and the montage builds normally. Including more than one `intro` or `outro` file raises an error.

---

## 🩹 VFR Normalization

Clips from phones and some capture tools use a variable frame rate (VFR), which can desync audio/video or crash MoviePy. Before loading, every clip is passed through `ffmpeg` and re-encoded to a constant 30fps (`libx264`, `crf 18`, AAC 192k audio) if it hasn't been normalized already. Normalized copies are cached in `clips/.normalized/` so repeat runs skip re-encoding.

---

## 🛠️ Requirements

* Python 3.9+
* [ffmpeg](https://ffmpeg.org/download.html) (system install, used for VFR normalization)
* [MoviePy](https://zulko.github.io/moviepy/)
* [tqdm](https://github.com/tqdm/tqdm)

```
moviepy
tqdm
```

---

## 🗺️ Roadmap

* [ ] Kill-cam zoom/slow-mo filter module
* [ ] Background music auto-mixing
* [ ] Watermark/logo overlay support

---

## 📄 License

MIT — use it, remix it, ship your montages.