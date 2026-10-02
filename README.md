![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Gold Cut-off Grade Calculator
 
*For mining engineers and gold miners: enter total operating cost, gold price, and recovery to instantly compute the cut-off grade in grams per tonne (g/t) and get an economic grade classification.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Mining & Minerals
 
**Inputs:**
- Total operating cost (USD per tonne of ore) – numeric input, positive value.
- Gold price (USD per troy ounce) – numeric input, positive value.
- Recovery (%) – numeric input, between 0 and 100.

**Core calculation (step by step):**
1. Convert gold price per troy ounce to price per gram: price_per_g = gold_price / 31.1035.
2. Compute revenue per gram after recovery: rev_per_g = price_per_g × (recovery / 100).
3. Compute cut-off grade in g/t: cut_off_gpt = total_cost / rev_per_g.
4. Compute cut-off grade in oz/t: cut_off_ozpt = cut_off_gpt / 31.1035.
5. Classification: if cut_off_gpt < 1.0 → 'Low grade (subeconomic typical)'; if 1.0 ≤ cut_off_gpt ≤ 3.0 → 'Typical operating grade'; if cut_off_gpt > 3.0 → 'High grade (selective mining)'. Thresholds based on typical gold mining benchmarks.

**Gradio UI layout:**
- Title at top: 'Gold Cut-off Grade Calculator'.
- Two-column layout: Inputs on the left, Outputs on the right.
- Left column: three numeric inputs with labels and units (Total operating cost ($/t), Gold price ($/oz), Recovery (%)). A 'Calculate' button.
- Right column: Large numeric display of cut-off grade (g/t) and (oz/t). Below that, a colored classification label (green for low, yellow for typical, red for high). A small bar chart showing cut-off grade relative to the three ranges (0-1, 1-3, >3) as a visual indicator.

**Output:**
- Cut-off grade in g/t and oz/t (two decimal places).
- Classification text with associated color coding.
- No downloadable files, no AI/ML component.
 
## Run it
 
```bash
docker build -t gold-cut-off-grade-calculator .
docker run -p 7860:7860 gold-cut-off-grade-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-10-02.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
