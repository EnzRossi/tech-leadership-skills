# Project website

Plain HTML, CSS, and a small optional clipboard script. No build dependencies, third-party requests, analytics, or cookies. Montserrat and JetBrains Mono are self-hosted with their SIL Open Font License notices in `assets/fonts/`. Sources: [Montserrat](https://github.com/google/fonts/tree/main/ofl/montserrat) and [JetBrains Mono](https://github.com/google/fonts/tree/main/ofl/jetbrainsmono). The installation commands and compatibility claims should stay aligned with the root README and `docs/compatibility.md`.

Preview from the repository root:

```bash
python3 -m http.server 8765 --directory site
```

Open `http://localhost:8765`. Check narrow and wide layouts, keyboard navigation, example disclosures, installation disclosures, and copy buttons. Reading the site and following installation instructions also works without JavaScript.

`.github/workflows/pages.yml` publishes this folder when it changes on `main`. GitHub Pages must use **GitHub Actions** as its publishing source. The deployment URL is `https://enzrossi.github.io/tech-leadership-skills/`; update the canonical and social metadata if that changes.

## Repository image

`assets/social-preview.png` is used in the root README and website sharing metadata. To apply it to links to the GitHub repository itself, upload it under repository **Settings → General → Social preview**. GitHub manages that image separately from website metadata.

Generated with the built-in OpenAI image-generation tool on 2026-09-16. Output: 1774 × 887 pixels (2:1); PNG compression was optimized without changing pixels. The card was revised to match the supplied EnzRossi branding. The website uses the supplied logo files, and its favicon uses the official mark geometry. The local brand-guidelines HTML is ignored and must not be committed or included in a manually packaged deployment.

Generation prompt:

> Use case: ads-marketing. Asset type: Open-source repository social preview card, landscape 1280x640 pixels, 2:1 aspect ratio. Primary request: Create a sophisticated editorial Swiss typographic graphic for EnzRossi Tech Leadership Skills. Scene/backdrop: Solid deep ink navy background. Style/medium: Sharp flat graphic design with clean Swiss sans-serif typography. Composition/framing: Generous safe margins. Oversized white title left aligned on two lines, occupying the left two thirds. Small publisher above. Supporting line below title. Small footer label. Restrained geometric branching decision motif on the right, in electric chartreuse, composed of crisp thin orthogonal lines and a few simple nodes, visually separate from text. Color palette: Deep ink navy, white, electric chartreuse accent. Text (verbatim): Publisher: "EnzRossi". Main title: "Tech Leadership Skills". Supporting line: "AI investment. Software delivery. Engineering capacity." Footer: "Open-source Agent Skills". Constraints: All text correctly spelled and legible at thumbnail size. Clear hierarchy with title dominant. Supporting line may wrap cleanly if necessary. Flat solid colors, polished understated editorial quality. Avoid: robots, brains, glow, gradients, 3D, photography, extra text, watermarks, clutter.


Brand revision prompt (built-in image-generation edit, existing card plus supplied white logo):

> Use case: style-transfer. Asset type: repository social preview, requested 1280x640 pixels, 2:1 landscape. Input images: Image 1 is the existing preview card and edit target. Image 2 is the official white EnzRossi horizontal logo, a supporting insert whose exact artwork must be preserved. Primary request: Update the existing card to the official EnzRossi branding. Replace the top-left plain typed publisher with the supplied official horizontal white logo, including its hash mark and precise wordmark artwork; use the supplied logo accurately, never retype or reinterpret it. Keep it modest in size with generous space above the main title. Palette: Solid flat charcoal #212934 background, #FCFCFE white text, primary blue #0256FF only for decision geometry and large graphic accents. Replace every lime accent with this blue. Typography: Main title Montserrat Bold 700/800 with -2% tracking. Body Montserrat Regular. Small footer JetBrains Mono. Text invariants, exact verbatim: "Tech Leadership Skills"; "AI investment. Software delivery. Engineering capacity."; "Open-source Agent Skills". Composition: Preserve the sophisticated clean editorial left-aligned hierarchy, large two-line title, supporting copy, footer, generous safe margins and restrained branching decision motif on the right. All copy must be clear at thumbnail size. Keep all text white; blue only for graphic shapes. Constraints: Minimal sharp flat graphic. Preserve exact supplied logo proportions and design. No glows, shadows, gradients, lime, robots, brains, extra copy or watermark.
