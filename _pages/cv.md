---
layout: academic
title: "CV"
permalink: /cv/
updated: 2026-10-04
excerpt: "Hanwen Zhang's official PDF CV, research focus, selected experience, and academic links."
redirect_from:
  - /resume
  - /cv-json/
  - /resume-json
---

<div class="cv-landing">
<p class="cv-identity"><strong>Hanwen Zhang <span lang="zh">张瀚文</span></strong><br>
Computer Science Honors Class · Sichuan University · Chengdu, China<br>
<a href="mailto:hanwen_zhang@stu.scu.edu.cn">hanwen_zhang@stu.scu.edu.cn</a> · <a href="https://hwzhangcs.github.io/">hwzhangcs.github.io</a></p>

<div class="cv-actions">
<a class="button-link" href="{{ '/assets/hanwen-zhang-cv.pdf' | relative_url }}">View or download CV PDF</a>
<span class="cv-action-note">One-page academic CV · Updated October 4, 2026</span>
</div>

<h2 id="research-focus">Research focus</h2>

<p>I am interested in how multimodal models and agents reason about the physical world: where things are, how views relate, and what lies out of view. I am also interested in generative models that fill in what a model cannot see, and in keeping their predictions consistent with what was observed. My background is in generative 3D vision: single-image animal reconstruction with shape priors and novel views from a pretrained video diffusion model, and sparse-view 3D scene reconstruction with 3D generative priors. In a team course project on hallucination mitigation, I also wrote the preference-data pipeline and the DPO training code for a vision-language model.</p>

<h2 id="selected-experience">Selected experience</h2>

<ul class="cv-highlight-list">
<li><strong>City University of Hong Kong.</strong> Research intern improving the generation process of GenRecon, a TRELLIS-based generative scene reconstructor, for sparse-view 3D reconstruction; reproduced the GenRecon and ReconViaGen pipelines and analyzed where reconstruction errors arise across their stages. A paper on this work is in preparation.</li>
<li><strong>Bone-to-Shape.</strong> Project lead on single-image animal reconstruction using animal pose and shape priors, novel views from a pretrained video diffusion model, and 3D Gaussian Splatting. <a href="{{ '/research/bone-to-shape/' | relative_url }}">Project overview →</a></li>
<li><strong>MLLM hallucination mitigation with DPO.</strong> Team course project (3 students). Wrote the LLM-judge pipeline (judging, re-judging, and auditing) that built 10,000 DPO preference pairs from on-policy answers, and the LoRA DPO training code for Qwen2.5-VL-3B-Instruct. In the teammates' runs, the AMBER hallucination rate (Hal) fell from 49.4 to 29.2 and discriminative F1 rose from 57.4 to 74.8. <a href="{{ '/portfolio/mllm-dpo/' | relative_url }}">Project page →</a></li>
<li><strong>Deep-Hole Guardian.</strong> Team member processing depth-camera point clouds for deep blind-hole defect detection in a SCARA-robot inspection system.</li>
<li><strong>Publication.</strong> Third author of a 2026 <em>International Journal of Approximate Reasoning</em> article on kernel self-representation learning based fuzzy-neighborhood outlier detection.</li>
</ul>

<h2 id="academic-links">Academic links</h2>

<p class="cv-profile-links"><a href="{{ site.author.googlescholar }}">Google Scholar</a><a href="{{ site.author.orcid }}">ORCID</a><a href="https://github.com/{{ site.author.github }}">GitHub</a><a href="mailto:{{ site.author.email }}">Email</a></p>

<p class="cv-next-step">The one-page PDF covers education, research, projects, publication, patent, selected honors and skills. A fuller record of honors, software copyrights, service and activities is available on request.</p>
</div>
