# 🐟 PhishOracle Web App — Adversarial Phishing Webpage Generator
Official implementation of  
**"From ML to LLM: Evaluating the Robustness of Phishing Webpage Detection Models against Adversarial Attacks"**  
Accepted at **ACM Digital Threats: Research and Practice (DTRAP), 2025** [Paper](https://dl.acm.org/doi/10.1145/3737295)

PhishOracle Web App is a lightweight, interactive tool for generating **adversarial phishing webpages** by injecting both **content-based** and **visual-based** features into real legitimate websites. Please refer to the [Phish-Blitz GitHub repository](https://github.com/Duddu-Hriday/Phish-Blitz) for the latest code to download webpages.

This project is a web-based wrapper built around the [PhishOracle](https://github.com/LetsBeSecure/PhishOracle-Project) toolset, intended to help researchers explore phishing evasions and evaluate the robustness of phishing webpage detection systems.

---

## ⚙️ Features

- 🧠 Adds **content-based features** (like fake login forms, links, injected DOM elements)
- 🎨 Applies **visual distortions** (like watermarks, logo blur, Gaussian noise)
- 🔍 Processes entire batches of legitimate webpages
- 📄 Outputs `phishing_webpage.html` inside each folder with modified `local_resources`

---

## 🚀 How It Works

### 🧭 Flow

1. 🗂 **Input** a path to a folder containing legitimate webpages
2. ✅ The app scans subfolders to detect HTML and assets
3. 🧩 It shows **selectable features** (from 15 content + 5 visual options)
4. 🧪 The chosen features are injected into the original HTML
5. 💥 Adversarial webpages are saved as `phishing_webpage.html` inside each subfolder

---

## 🛠 Key Python Scripts

### 🔹 `app.py`
- Flask app with 3 routes:
  - `/`: Input form for folder path
  - `/select_features`: Shows available features
  - `/generate`: Applies selected features and creates phishing pages

### 🔹 `adding_15_features_modified.py`
- Contains 15 pre-defined **DOM injection functions**
- Ex: fake login form, fake button, updates anchor `<a>` tags
- Selectively applies features using `apply_selected_content_features()`

### 🔹 `add_visual_features_main_modified.py`
- Contains **logo/image transformation** functions:
  - watermark, noise, rotation, blur, mesh
- Scans for images in `local_resources/img/`
- Exposes `apply_features()` to:
  - Modify HTML and inject visual & content features
  - Save phishing page as `phishing_webpage.html`

---

## ✅ How to Run

```bash
# Install dependencies (if not done already)
pip install flask beautifulsoup4 pillow cairosvg numpy

# Run the app
python app.py
