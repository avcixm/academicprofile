#!/usr/bin/env python3
# Build out/cv.md by harvesting sections from the public site

import re, pathlib, os, datetime, sys

ROOT = pathlib.Path(".").resolve()

def read(path):
    p = ROOT / path
    return p.read_text(encoding="utf-8") if p.exists() else ""

def grab_between(text, start, end):
    """Return substring between start and end markers (first match), else ''."""
    m = re.search(re.escape(start) + r"(.*?)" + re.escape(end), text, re.S)
    return (m.group(1).strip() if m else "")

def grab_file_section(path, start_marker, end_marker):
    s = read(path)
    if not s:
        print(f"[WARN] Missing file: {path}")
        return ""
    block = grab_between(s, start_marker, end_marker)
    if block:
        print(f"[INFO] Extracted {len(block)} chars from {path}")
    else:
        print(f"[WARN] Markers not found in {path}: {start_marker} … {end_marker}")
    return block

def split_on_h2(src, h2_text):
    """
    Fallback splitter: find '## h2_text' and return content until next '## '.
    """
    if not src: return ""
    pat = rf"(?ms)^\s*##\s+{re.escape(h2_text)}\s*\n(.*?)(?=^\s*##\s+|\Z)"
    m = re.search(pat, src)
    return (m.group(1).strip() if m else "")

# ---- Harvest from your public pages ----------------------------------------

home_all  = grab_file_section("index.md",
                              "<!-- CV:START HOME -->",
                              "<!-- CV:END HOME -->")

# Optional fine-grained markers (if you ever add them):
degrees   = grab_file_section("index.md", "<!-- CV:START DEGREES -->", "<!-- CV:END DEGREES -->")
exp       = grab_file_section("index.md", "<!-- CV:START EXPERIENCE -->", "<!-- CV:END EXPERIENCE -->")

# If fine-grained markers are not present, split by h2 headings inside HOME:
if not degrees: degrees = split_on_h2(home_all, "Degrees")
if not exp:      exp     = split_on_h2(home_all, "Professional Experience")

research  = grab_file_section("research.md",
                              "<!-- CV:START RESEARCH -->",
                              "<!-- CV:END RESEARCH -->")

teaching  = grab_file_section("teaching.md",
                              "<!-- CV:START TEACHING -->",
                              "<!-- CV:END TEACHING -->")

superv    = grab_file_section("supervision.md",
                              "<!-- CV:START SUPERVISION -->",
                              "<!-- CV:END SUPERVISION -->")

service   = grab_file_section("service_contributions.md",
                              "<!-- CV:START SERVICE -->",
                              "<!-- CV:END SERVICE -->")

profact   = grab_file_section("professional_activities.md",
                              "<!-- CV:START PROFESSIONAL -->",
                              "<!-- CV:END PROFESSIONAL -->")

# ---- Footer build note ------------------------------------------------------

sha  = os.environ.get("GITHUB_SHA","")[:7]
when = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
build_note = f'<div class="cv-build">_Auto-generated from_ **avcixm/academicprofile** — build `{sha}` on {when}</div>'

# ---- Compose cv.md (headings match your framework) -------------------------

tpl = f"""\
<!-- inlined styling for wkhtmltopdf (also see separate assets/cv.css) -->
<style>
:root{{--au-navy:#1C355E;--au-orange:#F05A28;--ink:#0F1B2A}}
h2{{color:var(--au-navy);text-transform:uppercase;border-bottom:1px solid #d9e1ec;padding-bottom:2px;margin-top:18pt}}
h3{{color:var(--au-orange);margin-top:10pt}}
ul,ol,li{{color:#000}}
.cv-build{{margin-top:18pt;font-size:10pt;color:#5b6a7a}}
</style>

# Mustafa Avci, PhD

Athabasca University  
Applied Mathematics  
Faculty of Science & Technology

[mavci@athabascau.ca](mailto:mavci@athabascau.ca) · [avcixmustafa@gmail.com](mailto:avcixmustafa@gmail.com)  
+1 639-998-9329

<h2 class="cap">DEGREES</h2>
{degrees or "_(add Degrees in **index.md** under the CV markers)_"}

<h2 class="cap">PROFESSIONAL EXPERIENCE</h2>
{exp or "_(add Professional Experience in **index.md** under the CV markers)_"}

<h2 class="cap">RESEARCH</h2>

### Research Interests
{split_on_h2(research, "Research Interests") or "_(add in **research.md**)_"}

### Research Specialization Keywords
{split_on_h2(research, "Research Specialization Keywords") or "_(add in **research.md**)_"}

### Research in Progress
{split_on_h2(research, "Current Projects") or split_on_h2(research, "Research in Progress") or ""}

### Research Funding (Awards & Grants)
{split_on_h2(research, "Research Funding") or ""}

### Book & Book Chapters
{split_on_h2(research, "Book & Book Chapters") or ""}

### Conference Proceedings
{split_on_h2(research, "Conference Proceedings") or ""}

### Papers
{split_on_h2(research, "Papers") or ""}

### Presentations & Talks
{split_on_h2(research, "Presentations & Talks") or ""}

<h2 class="cap">TEACHING</h2>
{teaching or ""}

<h2 class="cap">SUPERVISION</h2>
{superv or ""}

<h2 class="cap">SERVICE &amp; CONTRIBUTIONS</h2>
{service or ""}

<h2 class="cap">PROFESSIONAL ACTIVITIES</h2>
{profact or ""}

<h2 class="cap">CONTINUED PROFESSIONAL DEVELOPMENT</h2>
(kept verbatim as in your template)

- Higher Education Teaching Certificate—Online Course by Harvard University Derek Bok Center for Teaching and Learning, Oct–Dec 2020.  
- Orientation for Distance Education—Centre for Professional and Part-time Learning, Durham College, 2020.  
- Valuing Diversity and Supporting Inclusivity—Trent University, 2020.  
- How to Deliver Experiential Learning in a Remote Course—Trent University, 2020.  
- Learning How to Increase Learner Engagement—LinkedIn Learning, 2020.  
- Flipping the Classroom—Lynda.com, 2020.  
- Teaching Online: Synchronous Classes—Lynda.com, 2020.  
- … (remaining items unchanged; you can keep editing them in this builder if you prefer)

<h2 class="cap">TECH SKILLS</h2>
(kept verbatim as in your template)

- Teaching in face-to-face, online, hybrid/blended formats  
- Remote seminars & labs (sync/async)  
- LMS: Möbius, Blackboard, Canvas, Moodle, Google Classroom, Brightspace by D2L  
- MS Office, MS Teams, MATLAB, SPSS; Python (competent)

<h2 class="cap">RESEARCHER WEB PROFILES</h2>
(kept verbatim as in your template)

- ORCID: 0000-0002-6001-627X  
- https://avcixm.github.io/academicprofile/  
- https://scholar.google.com.tr/citations?user=kzgJh58AAAAJ&hl=tr  
- https://www.researchgate.net/profile/Mustafa_Avci  
- AU profile page

{build_note}
"""

out = pathlib.Path("out")
out.mkdir(exist_ok=True)
(out / "cv.md").write_text(tpl, encoding="utf-8")
print("[OK] Wrote out/cv.md")
