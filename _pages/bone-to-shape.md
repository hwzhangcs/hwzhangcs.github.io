---
layout: academic
title: "Bone-to-Shape"
permalink: /research/bone-to-shape/
back_url: /#research
back_label: Research
excerpt: "Anatomy-constrained single-image animal reconstruction for veterinary applications: project workflow, research questions, and Hanwen Zhang's role."
---
{% assign project = site.data.research | where: 'id', 'animal-reconstruction' | first %}

<p class="project-deck">Anatomy-Constrained 3D Reconstruction for Veterinary Applications <span lang="zh">· 骨影生形</span></p>
<p class="entry-meta">{{ project.role }} · {{ project.institution }} · {{ project.date }}<br>{{ project.program }}</p>

## Research Question

{{ project.question }} The project explores this question in the context of animal reconstruction for veterinary applications.

## Reconstruction Workflow

<figure class="project-diagram">
<img src="{{ project.diagram | relative_url }}" alt="Conceptual workflow: a single animal image leads to generated orbit views, followed by a 3D Gaussian Splatting representation. Anatomy and body-shape priors are the research focus." width="560" height="360">
<figcaption>Conceptual workflow. The illustration describes the approach; it is not an experimental reconstruction result.</figcaption>
</figure>

<ol class="method-steps">
<li><strong>Start from a single animal image.</strong> This is the observed input to the project’s reconstruction pipeline.</li>
<li><strong>Generate novel views.</strong> Produce an orbit-view video to supply additional views for reconstruction.</li>
<li><strong>Reconstruct a 3D representation.</strong> Use the generated video to build a 3D Gaussian Splatting (3DGS) representation.</li>
</ol>

The research explores **anatomical and body-shape priors** as constraints on the reconstructed animal geometry. Generated views and observed evidence play different roles: the additional views are predictions from the model, rather than new observations.

## My Role

I lead the project. My work focuses on the single-image-to-novel-view-to-3DGS workflow and the exploration of priors for animal geometry.

## Progress

- Passed the college midterm review under the Provincial Undergraduate Innovation Training Program.
- First-listed inventor on the related Chinese invention patent application, **202611403381.7**, filed September 10, 2026.
- The application passed preliminary examination on September 22, 2026. It is pending publication and **has not been granted**.

<p class="project-status"><strong>Ongoing work.</strong> This overview describes the reconstruction workflow, research focus, and current project milestones.</p>

<p class="resource-links"><a href="{{ '/cv/#intellectual-property' | relative_url }}">Patent application details</a><a href="mailto:hanwen_zhang@stu.scu.edu.cn">Contact about this project</a></p>
