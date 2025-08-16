#!/usr/bin/env python3
import re, pathlib, os, datetime, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]

def grab(path, start, end):
    p = ROOT / path
    if not p.exists():
        print(f"[WARN] Missing file: {path}")
        return ''
    s = p.read_text(encoding='utf-8')
    m = re.search(re.escape(start)+r'(.*?)'+re.escape(end), s, re.S)
    if not m:
        print(f"[WARN] Markers not found in {path}: {start} … {end}")
        return ''
    block = m.group(1).strip()
    print(f"[INFO] Extracted {len(block)} chars from {path}")
    return block

# Pull the six sections in the requested order
home  = grab('index.md',                   '<!-- CV:START HOME -->',        '<!-- CV:END HOME -->')
teach = grab('teaching.md',                '<!-- CV:START TEACHING -->',    '<!-- CV:END TEACHING -->')
rsrch = grab('research.md',                '<!-- CV:START RESEARCH -->',    '<!-- CV:END RESEARCH -->')
supv  = grab('supervision.md',             '<!-- CV:START SUPERVISION -->', '<!-- CV:END SUPERVISION -->')
serv  = grab('service_contributions.md',   '<!-- CV:START SERVICE -->',     '<!-- CV:END SERVICE -->')
prof  = grab('professional_activities.md', '<!-- CV:START PROFESSIONAL -->','<!-- CV:END PROFESSIONAL -->')
profd = grab('professional_development.md', '<!-- CV:START DEVELOPMENT -->','<!-- CV:END DEVELOPMENT -->')

sha  = os.environ.get('GITHUB_SHA','')[:7]
when = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

# Assemble the CV page
tpl = f"""---
layout: single
title: Mustafa Avci bb - Curriculum Vitae
permalink: /cv/
---

<!-- NOTE: This file is auto-generated. Edit your normal pages instead. -->

# Mustafa Avci cc — Curriculum Vitae

{home}

## Teaching
{teach}

## Research
{rsrch}

## Supervision
{supv}

## Service & Contributions
{serv}

## Professional Activities
{prof}

## Professional Development
{profd}

---

<small>Auto-generated from <code>avcixm/academicprofile</code> — build <code>{sha}</code> on {when}.</small>
"""

cv_path = ROOT / 'cv.md'
before = cv_path.read_text(encoding='utf-8') if cv_path.exists() else ''
if before.strip() != tpl.strip():
    cv_path.write_text(tpl, encoding='utf-8')
    print(f"[OK] Wrote cv.md ({len(tpl)} bytes)")
else:
    print("[OK] cv.md unchanged")

