#!/usr/bin/env python3
import re, pathlib, os, datetime

def grab(path, start, end):
    p = pathlib.Path(path)
    if not p.exists():
        print(f"[WARN] Missing file: {path}")
        return ''
    s = p.read_text(encoding='utf-8')
    m = re.search(re.escape(start)+r'(.*?)'+re.escape(end), s, re.S)
    if not m:
        print(f"[WARN] Markers not found in {path}: {start} … {end}")
        return ''
    block = m.group(1).strip()
    print(f"[INFO] Extracted {len(block)} chars from {path}.")
    return block

home  = grab('index.md',                   '<!-- CV:START HOME -->',        '<!-- CV:END HOME -->')
teach = grab('teaching.md',                '<!-- CV:START TEACHING -->',    '<!-- CV:END TEACHING -->')
rsrch = grab('research.md',                '<!-- CV:START RESEARCH -->',    '<!-- CV:END RESEARCH -->')
supv  = grab('supervision.md',             '<!-- CV:START SUPERVISION -->', '<!-- CV:END SUPERVISION -->')
serv  = grab('service_contributions.md',   '<!-- CV:START SERVICE -->',     '<!-- CV:END SERVICE -->')
prof  = grab('professional_activities.md', '<!-- CV:START PROFESSIONAL -->','<!-- CV:END PROFESSIONAL -->')

sha = os.environ.get('GITHUB_SHA','')[:7]
when = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

tpl = f"""---
title: Curriculum Vitae — Mustafa Avci
---

> _Auto-generated from_ **avcixm/academicprofile** — build `{sha}` on {when}

# Mustafa Avci
Department of Mathematics, Athabasca University  
mavci@athabascau.ca · https://avcixm.github.io/academicprofile/

## Summary
{home or '_(empty — add CV:START/END HOME markers in index.md)_'}

## Research
{rsrch or '_(empty — add CV:START/END RESEARCH markers in research.md)_'}

## Teaching
{teach or '_(empty — add CV:START/END TEACHING markers in teaching.md)_'}

## Supervision
{supv or '_(empty — add CV:START/END SUPERVISION markers in supervision.md)_'}

## Service & Contributions
{serv or '_(empty — add CV:START/END SERVICE markers in service_contributions.md)_'}

## Professional Activities
{prof or '_(empty — add CV:START/END PROFESSIONAL markers in professional_activities.md)_'}
"""

out = pathlib.Path('out'); out.mkdir(exist_ok=True)
(out/'cv.md').write_text(tpl, encoding='utf-8')
print("\n===== Preview (first 60 lines) =====")
print("\n".join((out/'cv.md').read_text(encoding='utf-8').splitlines()[:60]))
print("===== End preview =====")

