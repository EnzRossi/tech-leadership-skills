# Project website

Plain HTML, CSS, and a small optional clipboard script. No build dependencies, third-party requests, analytics, or cookies. Montserrat and JetBrains Mono are self-hosted with their SIL Open Font License notices in `assets/fonts/`. Sources: [Montserrat](https://github.com/google/fonts/tree/main/ofl/montserrat) and [JetBrains Mono](https://github.com/google/fonts/tree/main/ofl/jetbrainsmono). The installation commands and compatibility claims should stay aligned with the root README and `docs/compatibility.md`.

Preview from the repository root:

```bash
python3 -m http.server 8765 --directory site
```

Open `http://localhost:8765`. Check narrow and wide layouts, keyboard navigation, example disclosures, installation disclosures, and copy buttons. Reading the site and following installation instructions also works without JavaScript.

`.github/workflows/pages.yml` publishes this folder when it changes on `main`. GitHub Pages must use **GitHub Actions** as its publishing source. The deployment URL is `https://enzrossi.github.io/tech-leadership-skills/`; update the canonical and social metadata if that changes.

## Repository image

`assets/social-preview.png` is used in the root README and website sharing metadata. GitHub manages its repository social preview separately from website metadata. This detailed PNG exceeds GitHub’s 1 MB repository-upload limit; export a smaller file before uploading under **Settings → General → Social preview**. The full PNG is suitable for the README and website sharing metadata.

Generated with the built-in OpenAI image-generation tool on 2026-09-16, at 1774 × 887 pixels (2:1). The user requested a playful, photographic paper-sculpture direction after reviewing the typographic covers. The origami rocket and anchored checklist connect ambition with evidence. Smaller typography and branding leave the illustration as the focal point.

The supplied paper-unicorn artwork was a style reference, not copied into the repository. The supplied white EnzRossi logo was an image-generation reference; raster generation does not guarantee exact logo geometry or font reproduction. The website itself uses the original supplied logo files and licensed fonts. Photographic lighting and paper texture follow the user's requested direction; they are not flat brand-color swatches.

The local brand-guidelines HTML remains ignored and must not be committed or included in a manually packaged deployment.

Generation prompt:

> Create a premium conceptual photographic artwork for an open-source technology leadership repository. Landscape 2:1, requested 1280x640.
> Reference image 1: STYLE ONLY. Borrow its delightfully absurd physical paper sculpture, realistic paper folds, quiet dark studio, tactile material and editorial wit. Do NOT copy the unicorn or chair scene. Reference image 2: official EnzRossi white logo, use this asset with its original geometry and proportions, discreetly, no redesign.
> Concept: a brilliant cobalt blue (#0256FF) origami rocket poised diagonally upward on a small charcoal executive desk, but instead of fire, a long folded white paper checklist unrolls from its base across the desk, like the reference's paper CV. A small ordinary binder clip gently holds the checklist to the desk: ambitious launch, grounded in evidence. Three simple checked boxes and abstract grey lines on the paper, absolutely no tiny written text. A single understated executive chair partially visible behind the desk. Rocket and sculptural paper are the hero, surprising and a little funny, meticulously photographed miniature practical set. No people. Natural shadows on the physical objects only, tactile paper, elegant hard folds and cinematic controlled side lighting. Sharp focus, highly art-directed, realistic object photography rather than cartoon, no spaceship machinery, no flames, no smoke, no glowing effects.
> Composition: scene on right 60% of image, rocket fully in frame with ample space above nose; quiet near-black backdrop across the whole image. Left 40% generous negative space for modest editorial text. Graphic typography modest, NOT giant. Main title occupies only roughly one fifth of entire canvas area, set in Montserrat Bold white (#FCFCFE), on two lines: "Tech Leadership" / "Skills". Small supporting line in Montserrat Regular white: "Open-source Agent Skills". Discreet EnzRossi white logo at top-left, only about 12% of canvas width, generous clear space; keep proportions exactly like supplied asset. Small footer "enzrossi.com" in JetBrains Mono white. No other copy, no panel of numbered services, no giant brand mark, no huge type. Hierarchy: intriguing tactile sculpture first, title second, logo third.
> Brand: near-black studio, white paper and white type, cobalt blue rocket as the one bold accent, charcoal desk. Flat graphic typography and logo, no decorative gradients or neon. User explicitly requests this photographic sculptural direction. Make it feel like a clever design magazine cover for a CTO, not a startup sales banner.
