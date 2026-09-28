---
layout: academic
title: "Bone-to-Shape"
permalink: /research/bone-to-shape/
back_url: /#research
back_label: Research
excerpt: "Single-image animal reconstruction with animal shape priors and video diffusion, with potential veterinary applications."
---
{% assign project = site.data.research | where: 'id', 'animal-reconstruction' | first %}

<p class="project-deck">Animal reconstruction from a single image with shape priors and video diffusion <span lang="zh">· 骨影生形</span></p>
<p class="entry-meta">{{ project.role }} · {{ project.institution }} · {{ project.date }}<br>{{ project.program }}</p>

## Research Question

{{ project.question }} The project explores this question in the context of animal reconstruction with potential veterinary applications.

## Reconstruction Workflow

<figure class="project-diagram">
<img src="{{ project.diagram | relative_url }}" alt="Conceptual workflow: a single animal image leads to generated orbit views, followed by a 3D Gaussian Splatting representation. Anatomy and body-shape priors are the research focus." width="560" height="360">
<figcaption>Conceptual workflow. The illustration describes the approach; it is not an experimental reconstruction result.</figcaption>
</figure>

<ol class="method-steps">
<li><strong>Start from a single animal image.</strong> This is the observed input to the project’s reconstruction pipeline.</li>
<li><strong>Generate novel views.</strong> Draw on a ReconX-inspired video diffusion approach to produce an orbit-view video and supply additional views for reconstruction.</li>
<li><strong>Reconstruct a 3D representation.</strong> Use the generated video to build a 3D Gaussian Splatting (3DGS) representation.</li>
</ol>

The research explores **animal pose, anatomical, and body-shape priors** as constraints on the reconstructed geometry. AniMer provides the animal pose and shape prior; the video diffusion stage supplies predicted views in the spirit of sparse-view reconstruction. Generated views and observed evidence play different roles: the additional views are predictions from the model, rather than new observations.

<p class="resource-links"><a href="https://luoxue-star.github.io/AniMer_project_page/">AniMer: animal pose and shape estimation</a><a href="https://arxiv.org/abs/2408.16767">ReconX: sparse-view reconstruction with video diffusion</a></p>

## My Role

I led the project. My work focused on combining the animal pose and shape prior with the single-image-to-novel-view-to-3DGS workflow, and on studying how anatomical and body-shape constraints affect the reconstructed geometry.

## Outcomes

- Applied to Sichuan University's Undergraduate Innovation Training Program in the {{ project.applied }} round; approved in the 2026 project list announced {{ project.approved }}.
- Passed the college midterm review and the final review under the Provincial Undergraduate Innovation Training Program; completed September 20, 2026.
- First-listed inventor on the related Chinese invention patent application, **202611403381.7**, filed September 10, 2026.
- The application passed preliminary examination on September 22, 2026. It is pending publication and **has not been granted**.

<p class="project-status"><strong>Completed September 20, 2026.</strong> This overview describes the reconstruction workflow, research focus, and project milestones.</p>

<p class="resource-links"><a href="{{ '/#patents' | relative_url }}">Patent application details</a><a href="mailto:hanwen_zhang@stu.scu.edu.cn">Contact about this project</a></p>
