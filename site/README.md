# Project website

Plain HTML, CSS, and a small optional clipboard script. No build dependencies, external fonts, analytics, or cookies. The installation commands and compatibility claims should stay aligned with the root README and `docs/compatibility.md`.

Preview from the repository root:

```bash
python3 -m http.server 8765 --directory site
```

Open `http://localhost:8765`. Check narrow and wide layouts, keyboard navigation, example disclosures, installation disclosures, and copy buttons. Reading the site and following installation instructions also works without JavaScript.

`.github/workflows/pages.yml` publishes this folder when it changes on `main`. GitHub Pages must use **GitHub Actions** as its publishing source. The deployment URL is `https://enzrossi.github.io/tech-leadership-skills/`; update the canonical and social metadata if that changes.

## Repository image

`assets/social-preview.png` is used in the root README and website sharing metadata. To apply it to links to the GitHub repository itself, upload it under repository **Settings → General → Social preview**. GitHub manages that image separately from website metadata.

Generated with the built-in OpenAI image-generation tool on 2026-09-16. Output: 1774 × 887 pixels (2:1); PNG compression was optimized without changing pixels. It is original project artwork, not an existing EnzRossi brand mark. The favicon is a simple site-specific lettermark.

Generation prompt:

> Use case: ads-marketing. Asset type: Open-source repository social preview card, landscape 1280x640 pixels, 2:1 aspect ratio. Primary request: Create a sophisticated editorial Swiss typographic graphic for EnzRossi Tech Leadership Skills. Scene/backdrop: Solid deep ink navy background. Style/medium: Sharp flat graphic design with clean Swiss sans-serif typography. Composition/framing: Generous safe margins. Oversized white title left aligned on two lines, occupying the left two thirds. Small publisher above. Supporting line below title. Small footer label. Restrained geometric branching decision motif on the right, in electric chartreuse, composed of crisp thin orthogonal lines and a few simple nodes, visually separate from text. Color palette: Deep ink navy, white, electric chartreuse accent. Text (verbatim): Publisher: "EnzRossi". Main title: "Tech Leadership Skills". Supporting line: "AI investment. Software delivery. Engineering capacity." Footer: "Open-source Agent Skills". Constraints: All text correctly spelled and legible at thumbnail size. Clear hierarchy with title dominant. Supporting line may wrap cleanly if necessary. Flat solid colors, polished understated editorial quality. Avoid: robots, brains, glow, gradients, 3D, photography, extra text, watermarks, clutter.
