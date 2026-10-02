import math

GRAMS_PER_TROY_OUNCE = 31.1035
CHART_MAX_GPT = 6.0


def _to_float(value):
    if value is None:
        return None

    if isinstance(value, bool):
        return None

    if isinstance(value, (int, float)):
        try:
            result = float(value)
        except (OverflowError, ValueError):
            return None
        return result if math.isfinite(result) else None

    try:
        text = str(value).strip().replace(",", "").replace(" ", "")
        if not text:
            return None
        result = float(text)
    except (ValueError, OverflowError):
        return None

    return result if math.isfinite(result) else None


def _validate_inputs(total_cost, gold_price, recovery):
    tc = _to_float(total_cost)
    gp = _to_float(gold_price)
    rec = _to_float(recovery)

    if tc is None:
        return None, None, None, "Total operating cost must be a valid number."
    if tc <= 0:
        return None, None, None, "Total operating cost must be greater than 0."

    if gp is None:
        return None, None, None, "Gold price must be a valid number."
    if gp <= 0:
        return None, None, None, "Gold price must be greater than 0."

    if rec is None:
        return None, None, None, "Recovery must be a valid number."
    if rec < 0 or rec > 100:
        return None, None, None, "Recovery must be between 0 and 100."
    if rec <= 0:
        return None, None, None, "Recovery must be greater than 0 to compute a cut-off grade."

    return tc, gp, rec, None


def classify_cut_off_grade(cut_off_gpt):
    if cut_off_gpt < 1.0:
        return "Low grade (subeconomic typical)", "#2e7d32"
    if cut_off_gpt <= 3.0:
        return "Typical operating grade", "#f9a825"
    return "High grade (selective mining)", "#c62828"


def calculate_cut_off_grade(total_cost, gold_price, recovery):
    tc, gp, rec, error = _validate_inputs(total_cost, gold_price, recovery)

    if error:
        return {
            "success": False,
            "error": error,
            "cut_off_gpt": None,
            "cut_off_ozpt": None,
            "classification": None,
            "classification_color": "#6c757d",
        }

    try:
        price_per_g = gp / GRAMS_PER_TROY_OUNCE
        rev_per_g = price_per_g * (rec / 100.0)

        if rev_per_g <= 0 or not math.isfinite(rev_per_g):
            raise ValueError("Revenue per gram must be positive and finite.")

        cut_off_gpt = tc / rev_per_g
        cut_off_ozpt = cut_off_gpt / GRAMS_PER_TROY_OUNCE

        if not math.isfinite(cut_off_gpt) or not math.isfinite(cut_off_ozpt):
            raise ValueError("Computed cut-off grade is not finite.")

    except Exception as exc:
        return {
            "success": False,
            "error": f"Calculation failed: {exc}",
            "cut_off_gpt": None,
            "cut_off_ozpt": None,
            "classification": None,
            "classification_color": "#6c757d",
        }

    classification, color = classify_cut_off_grade(cut_off_gpt)

    return {
        "success": True,
        "error": None,
        "cut_off_gpt": cut_off_gpt,
        "cut_off_ozpt": cut_off_ozpt,
        "classification": classification,
        "classification_color": color,
    }


def generate_chart_html(cut_off_gpt):
    if cut_off_gpt is None or not math.isfinite(cut_off_gpt):
        return ""

    marker = min(max(cut_off_gpt, 0.0), CHART_MAX_GPT)
    marker_pct = (marker / CHART_MAX_GPT) * 100.0
    marker_pct = min(max(marker_pct, 0.0), 99.5)

    return f"""
<div style="margin-top:14px;font-family:Arial,sans-serif;">
  <div style="font-size:13px;font-weight:700;margin-bottom:6px;color:#111827;">
    Cut-off grade range indicator (g/t)
  </div>
  <div style="position:relative;width:320px;height:24px;border:1px solid #cbd5e1;background:#f8fafc;overflow:hidden;">
    <div style="position:absolute;left:0%;top:0;height:100%;width:16.67%;background:#2e7d32;"></div>
    <div style="position:absolute;left:16.67%;top:0;height:100%;width:33.33%;background:#f9a825;"></div>
    <div style="position:absolute;left:50%;top:0;height:100%;width:50%;background:#c62828;"></div>
    <div style="position:absolute;left:{marker_pct:.2f}%;top:-2px;height:28px;width:2px;background:#111827;"></div>
  </div>
  <div style="position:relative;width:320px;height:18px;font-size:11px;color:#475569;">
    <div style="position:absolute;left:0%;">0</div>
    <div style="position:absolute;left:16.67%;transform:translateX(-50%);">1</div>
    <div style="position:absolute;left:50%;transform:translateX(-50%);">3</div>
    <div style="position:absolute;left:100%;transform:translateX(-100%);">6+</div>
  </div>
</div>
"""


def format_results_html(result):
    if not isinstance(result, dict):
        return """
<div style="font-family:Arial,sans-serif;color:#b91c1c;">
  ⚠️ Invalid calculation result.
</div>
"""

    if not result.get("success"):
        error = result.get("error", "Unknown calculation error.")
        return f"""
<div style="font-family:Arial,sans-serif;color:#b91c1c;font-weight:600;">
  ⚠️ {error}
</div>
"""

    cut_off_gpt = result.get("cut_off_gpt")
    cut_off_ozpt = result.get("cut_off_ozpt")
    classification = result.get("classification", "Unclassified")
    color = result.get("classification_color", "#6c757d")
    chart_html = generate_chart_html(cut_off_gpt)

    return f"""
<div style="font-family:Arial,sans-serif;color:#111827;">
  <div style="font-size:28px;font-weight:700;margin-bottom:6px;">
    {cut_off_gpt:,.2f} g/t
  </div>
  <div style="font-size:20px;font-weight:600;margin-bottom:12px;">
    {cut_off_ozpt:,.4f} oz/t
  </div>
  <div style="display:inline-block;padding:8px 12px;border-radius:6px;background:{color};color:#ffffff;font-weight:700;">
    {classification}
  </div>
  {chart_html}
</div>
"""
