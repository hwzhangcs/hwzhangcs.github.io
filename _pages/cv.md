---
layout: academic
title: "CV"
permalink: /cv/
updated: 2026-09-24
excerpt: "Hanwen Zhang's education, research experience, publications, software projects, honors, and service."
redirect_from:
  - /resume
  - /cv-json/
  - /resume-json
---

<p class="cv-identity"><strong>Hanwen Zhang <span lang="zh">张瀚文</span></strong><br>
Sichuan University · Chengdu, China · <a href="mailto:hanwen_zhang@stu.scu.edu.cn">hanwen_zhang@stu.scu.edu.cn</a> · <a href="https://hwzhangcs.github.io/">hwzhangcs.github.io</a> · <a href="https://github.com/hwzhangcs">github.com/hwzhangcs</a><br>
Google Scholar: <a href="{{ site.author.googlescholar }}">scholar.google.com/citations?user=o_uTmywAAAAJ</a> · ORCID: <a href="{{ site.author.orcid }}">0009-0009-5637-1971</a></p>

Seeking long-term remote research internships. Planning to apply for Fall 2028 PhD admission.

<div class="cv-tools"><a href="{{ '/assets/hanwen-zhang-cv.pdf' | relative_url }}">Download PDF</a><button class="print-button" type="button" data-print>Print</button></div>

<nav class="cv-index" aria-label="CV sections">
<ul>
<li><a href="#education">Education</a></li>
<li><a href="#research-interests">Interests</a></li>
<li><a href="#research-experience">Research</a></li>
<li><a href="#publications">Publications</a></li>
<li><a href="#intellectual-property">Patents &amp; Copyrights</a></li>
<li><a href="#honors">Honors</a></li>
<li><a href="#projects">Projects</a></li>
<li><a href="#activities">Activities &amp; Service</a></li>
<li><a href="#skills">Skills</a></li>
</ul>
</nav>

## Education

{% assign edu = site.data.education %}
<div class="entry-heading"><h3>{{ edu.institution }}</h3><span class="entry-date">{{ edu.dates }}</span></div>
<p class="entry-meta">{{ edu.degree }}<br>{{ edu.program }}</p>

**GPA: {{ edu.gpa }} · Rank: {{ edu.rank }}**<br>
Weighted average: {{ edu.weighted_average }}. Grades as of {{ edu.as_of }}.

<details markdown="1">
<summary>Coursework and additional grade details</summary>

Compulsory-course GPA: {{ edu.compulsory_gpa }}; compulsory-course weighted average: {{ edu.compulsory_weighted_average }}.

Selected coursework: {% for course in edu.courses %}{{ course.name }} ({{ course.score }}){% unless forloop.last %}, {% endunless %}{% endfor %}.
</details>

## Research Interests

Visual generation and 3D reconstruction, with a longer-term interest in generative world models for spatial reasoning and action.

## Research Experience

{% include cv/research.html %}

## Publications

{% include publications.html %}

## Patents & Software Copyrights
{: #intellectual-property }

{% include cv/ip.md %}

## Honors

{% include cv/honors.md %}

### Competitions & Assessments
{: .cv-subheading }

- **2026 MCM:** Successful Participant.
- **CCF CSP:** highest score 250/500, March 30, 2025 (top 20.6% in that sitting); top 11.23% in the May 31, 2026 sitting.

## Software & Engineering Projects
{: #projects }

{% include projects.html %}


## Activities & Service
{: #activities }

### Academic Exchange
{: .cv-subheading }

- **UNSW Business School**, “Discovery: Foundations and Applications,” July 20–31, 2026. Completed a 30-hour in-person program; led development of a Hackathon prototype combining financial candlestick analysis and multi-agent collaboration.
- **CNCC 2025**, Harbin, October 22–25, 2025. Conference participant.

### Leadership & Service
{: .cv-subheading }

- **President**, Sichuan University AI Club; previously Vice President.
- **League Branch Secretary**, 2024 Honors Class, College of Computer Science; helped organize the class's successful “Jiang Jie Class” application.

## Skills

- **Programming:** C/C++, Python.
- **ML / Data:** PyTorch, scikit-learn.
- **Tools:** Linux, Git, Docker, LaTeX.
- **Languages:** Chinese (native); English (CET-6: 538).
