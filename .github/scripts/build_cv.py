#!/usr/bin/env python3
# Build cv.md from your public site sections, matching your framework
# and expanding <details> blocks (e.g., Papers) so everything is visible in the PDF.

import os, re, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]  # repo root

# ---------- helpers ----------
def read_text(path: pathlib.Path) -> str:
    if not path.exists():
        print(f"[WARN] Missing file: {path}")
        return ""
    return path.read_text(encoding="utf-8")

def grab(path_rel, start_marker, end_marker) -> str:
    """Return the markdown between two HTML comment markers (non-greedy)."""
    s = read_text(ROOT / path_rel)
    if not s:
        return ""
    m = re.search(re.escape(start_marker) + r"(.*?)" + re.escape(end_marker), s, re.S)
    if not m:
        print(f"[WARN] Markers not found in {path_rel}: {start_marker} … {end_marker}")
        return ""
    block = m.group(1).strip()
    print(f"[INFO] Extracted {len(block)} chars from {path_rel}.")
    return block

def strip_small(md: str) -> str:
    # Replace <small>…</small> with plain text
    return re.sub(r"</?small>", "", md, flags=re.I)

def expand_details(md: str) -> str:
    """
    Turn <details><summary>Title</summary> … </details> into a visible sub-section:
      ### Title
      (inner content)
    Works well for your Papers section and any other collapsibles.
    """
    def repl(m: re.Match) -> str:
        summary = m.group(1)
        inner = m.group(2).strip()
        # Strip any tags around the summary like <strong>…</strong>
        summary_txt = re.sub(r"<.*?>", "", summary).strip()
        return f"\n\n### {summary_txt}\n\n{inner}\n\n"

    # Unwrap nested details first (greedy from inside out)
    while re.search(r"<details>(.*?)</details>", md, flags=re.S | re.I):
        md = re.sub(r"<details>\s*<summary>(.*?)</summary>(.*?)</details>",
                    repl, md, flags=re.S | re.I)
    return md

def cleanup(md: str) -> str:
    md = strip_small(md)
    md = expand_details(md)
    # Remove left-over empty lines
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()

STYLE = """<style>
:root{
  --au-navy:   #1C355E;
  --au-orange: #F05A28;
  --ink:       #000000;
}

/* body + lists default to black text */
body { color: var(--ink); font-family: "Segoe UI", Arial, Helvetica, sans-serif; line-height: 1.35; }
ul, ol, li { color: var(--ink); }

/* top name remains navy (h1 in your CV) */
h1 { color: var(--au-navy); margin: 0 0 .2rem 0; font-weight: 700; }

/* MAIN SECTION HEADINGS (RESEARCH, TEACHING, …) */
h2 {
  color: var(--au-navy);
  text-transform: uppercase;
  letter-spacing: .4px;
  font-weight: 700;
  margin: 1.1rem 0 .4rem;
  padding-bottom: .2rem;
  border-bottom: 1.5px solid #d9d9d9;
  page-break-after: avoid;
}

/* Sub-section headings (Research Interests, Funding, …) */
h3 {
  color: var(--au-orange);
  margin: .7rem 0 .25rem;
  font-weight: 700;
  page-break-after: avoid;
}

/* Links match site palette */
a { color: var(--au-navy); text-decoration: none; }
a:hover { color: var(--au-orange); }

/* Light divider if needed */
hr { border: 0; border-top: 1px solid #e6e6e6; margin: .8rem 0; }
</style>
"""

# ---------- pull sections from your public pages ----------
home  = grab("index.md",
             "<!-- CV:START HOME -->", "<!-- CV:END HOME -->")

teach = grab("teaching.md",
             "<!-- CV:START TEACHING -->", "<!-- CV:END TEACHING -->")

rsrch = grab("research.md",
             "<!-- CV:START RESEARCH -->", "<!-- CV:END RESEARCH -->")

supv  = grab("supervision.md",
             "<!-- CV:START SUPERVISION -->", "<!-- CV:END SUPERVISION -->")

serv  = grab("service_contributions.md",
             "<!-- CV:START SERVICE -->", "<!-- CV:END SERVICE -->")

prof  = grab("professional_activities.md",
             "<!-- CV:START PROFESSIONAL -->", "<!-- CV:END PROFESSIONAL -->")

# Make research (and anything else that used <details>) fully visible in PDF
rsrch = cleanup(rsrch)

# ---------- static sections that you want to keep “as is” ----------
STATIC_CPD = """\
## CONTINUED PROFESSIONAL DEVELOPMENT

- Higher Education Teaching Certificate — Online Course by Harvard University, Derek Bok Center for Teaching and Learning, Oct–Dec 2020.
- Orientation for Distance Education — The Centre for Professional and Part-time Learning, Durham College, 2020.
- Valuing Diversity and Supporting Inclusivity — Trent University, 2020.
- How to Deliver Experiential Learning in a Remote Course — CTL, Trent University, 2020.
- Learning How to Increase Learner Engagement — LinkedIn Learning, 2020.
- Flipping the Classroom — Lynda.com, 2020.
- Teaching Online: Synchronous Classes — Lynda.com, 2020.
- How to Engage your Students in a Virtual Environment — McGraw-Hill, 2020.
- Developing Your Course Syllabus — The Gwenna Moss Centre for Teaching and Learning, University of Saskatchewan, 2020.
- Remote Teaching Essentials: Constructive Alignment — GMCTL, University of Saskatchewan, 2020.
- Teach Adult Learners in Higher Education — Lynda.com, 2020.
- Educational Technology for Student Success — Lynda.com, 2020.
- Communication in the 21st Century Classroom — Lynda.com, 2020.
- Learning Microsoft Teams for Education — Lynda.com, 2020.
- Foundations of Learning Management Systems (LMS) — Lynda.com, 2020.
- Pedagogical Courses (credit, taken during PhD), Dicle University, 2011.
- Certificate of Pedagogy Formation for Teachers, Dicle University, 2001.
"""

STATIC_SKILLS = """\
## TECH SKILLS

- Teaching in a variety of formats: face-to-face, online, hybrid/blended.
- Lectures, seminars and labs delivered synchronously and asynchronously.
- LMS experience: Möbius, Blackboard, Canvas, Moodle, Google Classroom, Brightspace by D2L.
- Software: MS Office, MS Teams, MATLAB, SPSS.
- Programming: Python (competent).
"""

STATIC_PROFILES = """\
## RESEARCHER WEB PROFILES

- Website: https://avcixm.github.io/academicprofile/
- ORCID: **0000-0002-6001-627X**
- Google Scholar: https://scholar.google.com.tr/citations?user=kzgJh58AAAAJ&hl=tr
- ResearchGate: https://www.researchgate.net/profile/Mustafa_Avci
- AU Profile: Dr. Mustafa Avci | Faculty of Science and Technology | Athabasca University
"""

# ---------- header/footer ----------
sha  = os.environ.get("GITHUB_SHA", "")[:7]
when = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

FRONT_MATTER = """---\ntitle: Curriculum Vitae — Mustafa Avci\n---\n"""

HEADER = """# Mustafa Avci

Department of Mathematics, Athabasca University  
mavci@athabascau.ca · https://avcixm.github.io/academicprofile/
"""

FOOTER = f"""
---

_Auto-generated from_ **avcixm/academicprofile** — build `{sha}` on {when}
"""

# ---------- assemble to match your CV framework ----------
# Your “HOME” block already contains “Degrees” and “Professional Experience”
# with H2 headings; Teaching/Research/Supervision/Service/Professional
# carry their own sub-sections as authored on the site.

parts = [
    FRONT_MATTER,
    HEADER,

    # DEGREES + PROFESSIONAL EXPERIENCE
    home,

    # RESEARCH (includes Research Interests, Keywords, Research in Progress,
    # Funding, Books/Chapters, Proceedings, Papers, Presentations & Talks)
    "## RESEARCH\n\n" + rsrch,

    # TEACHING (all institutions/categories authored on the page)
    "## TEACHING\n\n" + teach,

    # SUPERVISION
    "## SUPERVISION\n\n" + supv,

    # SERVICE & CONTRIBUTIONS
    "## SERVICE & CONTRIBUTIONS\n\n" + serv,

    # PROFESSIONAL ACTIVITIES
    "## PROFESSIONAL ACTIVITIES\n\n" + prof,

    # Static sections kept “as is”
    STATIC_CPD,
    STATIC_SKILLS,
    STATIC_PROFILES,

    # Footer note moved to the end
    FOOTER,
]

cv_md = "\n\n".join([p for p in parts if p and p.strip()])

# Write to out/cv.md for the workflow to commit/push
OUTDIR = ROOT / "out"
OUTDIR.mkdir(exist_ok=True)
(OUTDIR / "cv.md").write_text(cv_md, encoding="utf-8")

print("\n===== Preview (first 60 lines) =====")
print("\n".join(cv_md.splitlines()[:60]))
print("===== End preview =====")
