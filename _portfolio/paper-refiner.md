---
layout: "academic"
collection: "portfolio"
title: "Paper Refiner"
order: 1
purpose: "Multi-agent LaTeX paper revision system"
contribution: "Designed and implemented the workflow and orchestrator, including structured patch-based editing and reproducible runs with configurations and logs."
stack: "Python · LaTeX · JSON patches"
code_url: "https://github.com/hwzhangcs/paper-refiner"
excerpt: "Multi-agent LaTeX paper revision system. Designed and implemented the workflow and orchestrator, including structured patch-based editing and reproducible runs with configurations and logs."
---

<p class="project-deck">A multi-agent workflow that turns review feedback into traceable LaTeX revisions.</p>
<p class="entry-meta">My role: workflow and orchestrator design &amp; implementation</p>
<p class="resource-links"><a href="https://github.com/hwzhangcs/paper-refiner">Source code</a><a href="https://github.com/hwzhangcs/paper-refiner#readme">README &amp; setup</a></p>

## What the System Does

Paper Refiner connects paper review with source-level editing. A reviewer provides feedback, an editor proposes changes, and an orchestrator coordinates the revision process, compilation, and version tracking.

<figure class="project-diagram">
<img src="{{ '/assets/diagrams/paper-refiner.svg' | relative_url }}" alt="An orchestrator coordinates a reviewer and editor. Feedback leads to JSON patches, with version history and revision reports." width="560" height="360">
<figcaption>Architecture schematic based on the project’s documented workflow.</figcaption>
</figure>

## How It Works

<ol class="method-steps">
<li><strong>Establish a review baseline.</strong> The initial review uses a compiled PDF to identify prioritized issues and produce a baseline score.</li>
<li><strong>Revise in focused passes.</strong> Subsequent iterations address structure, coherence, paragraphs, sentences, and polish. Reviewer feedback guides the editor’s JSON patches to the LaTeX source.</li>
<li><strong>Check and record changes.</strong> The orchestrator manages compilation checks and revision history. Reports explain the edits and track issues.</li>
</ol>

## My Contribution

I designed and implemented the **workflow and orchestrator**, including coordination of review and editing, structured patch-based changes, and reproducible runs with configurations and logs.

## Outputs You Can Inspect

| Artifact | Purpose |
|---|---|
| `versions/` | Paper versions across iterations |
| `issues.json` | Identified and resolved issues |
| `FINAL_REVISION_REPORT.md` | Summary of revisions |

These output names and workflow stages are documented in the [project README](https://github.com/hwzhangcs/paper-refiner#readme).

## Run the Project

The project uses Python and a local LaTeX environment. The repository’s [setup guide](https://github.com/hwzhangcs/paper-refiner/blob/main/SETUP.md) covers dependencies and configuration for the reviewer and editor services.

<p class="resource-links"><a href="https://github.com/hwzhangcs/paper-refiner">Explore the repository →</a><a href="{{ '/portfolio/' | relative_url }}">Other software projects</a></p>
