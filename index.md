---
layout: single
title: Welcome to my Academic Portfolio
---
<!-- Export buttons (no 404; PDF opens print dialog, Word/TXT download locally) -->
<div class="download-bar">
  <button class="btn export" data-kind="pdf">PDF</button>
  <button class="btn export" data-kind="doc">Word</button>
  <button class="btn export" data-kind="txt">Text</button>
  <button class="btn" onclick="window.print()">Print</button>
</div>

{% assign cv_url = '/assets/exports/cv.pdf' | relative_url %}
<div class="download-bar">
  <!-- View in new tab -->
  <a class="btn"
     href="{{ cv_url }}?v={{ site.github.build_revision }}"
     target="_blank" rel="noopener"
     type="application/pdf"
     aria-label="View CV (PDF) in a new tab">
    View CV (PDF)
  </a>

  <!-- Download file -->
  <a class="btn"
     href="{{ cv_url }}?v={{ site.github.build_revision }}"
     download="Mustafa-Avci-CV.pdf"
     type="application/pdf"
     aria-label="Download CV as PDF">
    Download CV
  </a>
</div>


<div class="home-media">
  <img src="{{ '/assets/images/me.png' | relative_url }}" alt="Dr. Mustafa Avci" class="home-photo">
  <a href="https://www.athabascau.ca/science-and-technology/index.html" target="_blank" rel="noopener">
    <img src="{{ '/assets/images/AU_background.png' | relative_url }}" alt="Athabasca University" class="home-au">
  </a>

  <div class="home-links">
    <h3>Web Presence</h3>
    <ul>
      <li>ORCID: <a href="https://orcid.org/0000-0002-6001-627X" target="_blank" rel="noopener">https://orcid.org/0000-0002-6001-627X</a></li>
      <li>Google Scholar: <a href="https://scholar.google.com.tw/citations?user=kzgJh58AAAAJ&hl=en" target="_blank" rel="noopener">profile</a></li>
      <li>ResearchGate: <a href="https://www.researchgate.net/profile/Mustafa-Avci-7" target="_blank" rel="noopener">profile</a></li>
      <li>GitHub: <a href="https://github.com/avcixm" target="_blank" rel="noopener">avcixm</a></li>
    </ul>

    <h3>Contact</h3>
    <ul>
      <li>Email (primary): <a href="mailto:mavci@athabascau.ca">mavci@athabascau.ca</a></li>
      <li>Email: <a href="mailto:avcixmustafa@gmail.com">avcixmustafa@gmail.com</a></li>
    </ul>
  </div>
</div>

I am an Assistant Professor in Applied Mathematics at Athabasca University. This academic portfolio provides an up-to-date, structured summary of my professional contributions as a faculty member at Athabasca University, highlighting my work in teaching, research, and service to the academic and broader community. The introductory section includes my full curriculum vitae, contact information, and a detailed account of my academic background prior to joining Athabasca University in July, 2022.

## Educational Background
 - PhD Mathematics, Dicle University
 - MSc Mathematics, Dicle University
 - BSc Mathematics, Dicle University

## Past Academic Positions
 - Lecturer (Term), Department of Finance and Management Science, Edwards School of Business, University of Saskatchewan (2021/7 - 2022/6).
 - Assistant Professor (Term), Department of Mathematics, Trent University (2020/8 - 2021/7).
 - Instructor (Term), Department of Science and Technology, Northwestern Polytechnic (2019/8 - 2020/4)
 - Instructor (Sessional), Department of Finance and Management Science, Edwards School of Business, University of Saskatchewan (2019/5 - 2019/8).
 - Postdoctoral Fellow, Department of Mathematics, Morgan State University (2014/9 - 2015/10).
 - Associate Professor, Department of Economics and Administrative Sciences, Batman University (2013/3 - 2018/10).
 - Instructor, Economics and Administrative Sciences Programmes, Dicle University (2009/1 - 2013/3).
