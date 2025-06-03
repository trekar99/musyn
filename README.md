<div align="center" style="display: flex; justify-content: center; align-items: center; text-align: center;">
  <a href="https://github.com/trekar99/musyn" style="margin-right: 20px; text-decoration: none; display: flex; align-items: center;">
    <img src="https://github.com/user-attachments/assets/b7a19a44-37f9-4245-9b43-499e3bdc7025" alt="Musyn" width="300">
  </a>
</div>
<div align="center" style="display: flex; justify-content: center; align-items: center; text-align: center;">
    <h2>
    Musyn: A Real-time Music-to-Image Co-creation System
    </h2>
</div>

## Overview

MUSYN is an innovative system designed for real-time musical co-creation, focusing on generating visual art from music. This project proposes a modular workflow that integrates various phases to achieve this transformation: from audio capture and preprocessing, through the transformation of music into textual descriptions, to image synthesis. This flexible and adaptable architectural design is intended to allow the integration of specific artificial intelligence models within each of its parts, depending on needs and technological advancements. By establishing a direct and reactive connection between sound and image, MUSYN goes beyond the traditional concept of synesthesia, providing a platform to explore and materialize a new form of interactive visual art, where music becomes the creative engine for visual expression.

---

## Installation

```bash
./start.sh
```

- Installs all Python dependencies (see `setup.py`).
- Downloads the required music captioning and image generation models.

---

## Usage

1. **Run the app**  
   ```bash
   ./start.sh
   ```
2. **Open the web interface**  
   The app launches a Gradio interface in your browser.
3. **Choose your mode**  
   - **Live Audio**: Use your microphone to generate images from live music.
   - **File Audio**: Upload an audio file for processing.
4. **Interact**  
   - View generated captions and images in real time.
   - Adjust image width/height and use example prompts.

---

## Musyn Architecture

- **Audio Preprocessing**:  
  Audio is captured (live/file) and preprocessed using utilities in [`utils/audio_utils.py`](utils/audio_utils.py).
- **Music Captioning**:  
  The audio is passed to a music captioning model ([`model/music2txt.py`](model/music2txt.py)), which uses a BART-based architecture to generate descriptive text.
- **Image Generation**:  
  The caption is fed into a Stable Diffusion XL Turbo pipeline ([`model/txt2img.py`](model/txt2img.py)) to generate an image.
- **Web Interface**:  
  The Gradio app ([`app.py`](app.py)) provides a user-friendly interface for real-time interaction.

---

## Code Structure

```
musyn/
├── app.py                # Main Gradio web application
├── config.py             # UI and model configuration
├── setup.py              # Python package setup and dependencies
├── start.sh              # Installation and model download script
├── utils/
│   └── audio_utils.py    # Audio loading and preprocessing utilities
├── model/
│   ├── bart.py           # BART-based captioning model definition
│   ├── modules.py        # Audio encoder and feature extraction modules
│   ├── music2txt.py      # Music-to-text (captioning) pipeline
│   └── txt2img.py        # Text-to-image (Stable Diffusion XL Turbo) pipeline
├── model/models/         # Downloaded model weights (auto-created)
├── LICENSE
└── README.md
```

---

## References

- [Exploring Real-Time Music-to-Image Systems for Creative Inspiration in Music Creation](https://arxiv.org/html/2407.05584v1#Sx3)
- [LP-MusicCaps: LLM-Based Pseudo Music Captioning](https://github.com/seungheondoh/lp-music-caps)
- [ArtSpew](https://github.com/aifartist/ArtSpew/)
- [SDXLTurbo](https://static1.squarespace.com/static/6213c340453c3f502425776e/t/65663480a92fba51d0e1023f/1701197769659/adversarial_diffusion_distillation.pdf)
- [Ultimate guide to optimizing Stable Diffusion XL](https://www.felixsanz.dev/articles/ultimate-guide-to-optimizing-stable-diffusion-xl)
- [StreamDiffusion](https://github.com/cumulo-autumn/StreamDiffusion)

---

## Next Steps

- [x] Generate Images in RT.
- [ ] Option of 5s audio input.
- [ ] Improve RT Image Generation.
- [ ] Publish a demo on a Hugging Face Space

---

**License:**  
[GNU GPLv3](LICENSE)