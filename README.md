# Better Lifestyle Network / TV Network Interface

A modern, high-performance web dashboard and media showcase application built with a premium glassmorphic UI design. Originally created as a streaming and marketing hub for real estate specialists (**Better Lifestyle Network**), the application integrates an interactive AI model exploration interface showcasing AI models across OpenRouter, Hugging Face, Coding Assistants, ONNX, and Free open-source categories.

---

## 🌟 Overview & Key Features

- **TV Network Landing Page (`Tvnetwork copy.html`)**:
  - Fullscreen video hero banner featuring smooth autoplay, background video, and controls.
  - Custom glassmorphic design system inspired by Apple TV / SF Pro aesthetic with neutral ambient background light orbs.
  - Multi-category horizontal carousels displaying AI Models (OpenRouter LLMs, Hugging Face, Coding Assistants, ONNX models, and Free open-source LLMs) and US States directory.
  - Interactive modal slideshow and details viewer for each card element.
  - Multi-step SRES® agent registration flow with biometric (WebAuthn) and social auth options.
  - Fallback data pipeline: OpenRouter API → Local JSON (`openrouter-models.json`) → Grist database table → Static fallback.

- **Content Management System (`content-management.html`)**:
  - Media inventory dashboard with status tracking (Published, Draft, Archived).
  - Drag-and-drop media upload modal with file type and size restrictions.
  - Interactive table filters and item management.

- **Analytics Dashboard (`analytics.html`)**:
  - Key performance indicators (Total Views, Watch Time, Engagement Rate, New Subscribers).
  - Interactive bar chart for daily performance trends.
  - Demographic distribution breakdowns and top-performing content leaderboards.

- **Settings Hub (`settings.html`)**:
  - Account, profile, notification, privacy, and billing management.
  - Interactive section switching and preference toggles.

---

## 📁 Directory Structure

```
├── Tvnetwork copy.html        # Main landing page & TV interface
├── analytics.html             # Analytics & metrics dashboard
├── content-management.html    # CMS interface for media uploads
├── settings.html              # User preferences & account settings
├── grist-table-schema.json    # Schema configuration for Grist DB sync
├── openrouter-models.json     # Static model catalog data & fallbacks
├── take_screenshots.py        # Automated Playwright visual regression script
├── vercel.json                # Vercel deployment & route rewrite configuration
└── README.md                  # Main repository documentation
```

---

## 🛠️ Technology Stack

- **Frontend**: Pure HTML5, Modern CSS3 (CSS Variables, Flexbox, Grid, Backdrop Filters, Glassmorphism), ES6+ JavaScript (Vanilla JS).
- **Backend / DB Integration**:
  - RESTful integration with OpenRouter API (`https://openrouter.ai/api/v1/models`).
  - Optional sync with Grist database tables (`https://docs.getgrist.com/api/docs/`).
- **Hosting / Deployment**: Configured for Vercel Serverless hosting (`vercel.json`).
- **Testing & Tooling**: Python + Playwright for automated headful/headless visual capture.

---

## 🚀 Getting Started

### Local Development

No heavy build process or node modules are required to preview the application locally:

1. Open `Tvnetwork copy.html` directly in any web browser.
2. Alternatively, run a local web server (e.g. via Python or VS Code Live Server):
   ```bash
   python3 -m http.server 8000
   ```
3. Visit `http://localhost:8000` in your browser.

### Capturing Screenshots

To test visual rendering automatically across desktop screen sizes:

```bash
# Ensure Playwright dependencies are installed
pip install playwright
playwright install chromium

# Run the screenshot utility
python3 take_screenshots.py
```

---

## 📊 Deployment Configuration

The app is deployed on Vercel with clean URLs enabled. The root route (`/`) automatically rewrites to `/Tvnetwork copy.html` via `vercel.json`:

```json
{
  "version": 2,
  "cleanUrls": true,
  "trailingSlash": false,
  "rewrites": [
    { "source": "/", "destination": "/Tvnetwork copy.html" }
  ]
}
```

---

## 📝 License

Internal & Commercial Rights Reserved - Better Lifestyle Network / TV Network.
