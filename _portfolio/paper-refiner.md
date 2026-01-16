---
title: "Paper Refiner: Multi-Agent Academic Paper Revision System"
excerpt: "An automated academic paper revision system using dual-agent architecture (Yuketang AI + OpenAI) for iterative LaTeX paper refinement"
collection: portfolio
---

## Overview

Paper Refiner is an intelligent academic paper revision system that leverages multi-agent collaboration to automatically improve LaTeX papers through iterative refinement.

## Key Features

* **Dual-Agent Architecture**: Combines Yuketang AI (Reviewer) and OpenAI (Editor) for comprehensive paper analysis and revision
* **Iterative Refinement Process**:
  - Initial comprehensive review with prioritized issues (P0-Critical to P2-Nice-to-have)
  - Multi-pass refinement covering structure, coherence, paragraphs, sentences, and polish
* **Transparent Audit Trail**: All changes applied via structured JSON patches, making them fully reversible
* **Automatic Validation**: Ensures LaTeX compilability after each modification

## Technical Stack

* **Language**: Python 3.10+
* **APIs**: OpenAI API, Yuketang AI
* **Package Management**: uv
* **Input/Output**: LaTeX files, JSON patches, Markdown reports

## Impact

This project demonstrates the practical application of multi-agent systems in academic writing assistance, combining LLM capabilities for both critique and generation tasks.

[View on GitHub](https://github.com/hwzhangcs/paper-refiner)
