---
title: "MLLM Hallucination Mitigation with DPO"
order: 0
home: true
purpose: "Hallucination mitigation in a vision-language model with preference optimization"
contribution: "Built the LLM-judge pipeline for DPO pair construction, fine-tuned Qwen2.5-VL-3B-Instruct with LoRA DPO on 8×A100 GPUs, and evaluated on AMBER."
stack: "Python · Qwen2.5-VL · LLaMA-Factory · pixi"
code_url: "https://github.com/hwzhangcs/multimodal"
excerpt: "Course project. Built an LLM-judge pipeline that turns on-policy VQA answers into 5,059 DPO preference pairs, fine-tuned Qwen2.5-VL-3B-Instruct with LoRA DPO, and evaluated hallucination on AMBER."
---

<p class="project-deck">Turning a model's own answers into preference data for hallucination mitigation.</p>
<p class="entry-meta">Course project · My role: full pipeline, training, and evaluation</p>
<p class="resource-links"><a href="https://github.com/hwzhangcs/multimodal">Source code</a><a href="https://github.com/hwzhangcs/multimodal#readme">README &amp; setup</a></p>

## What the Project Does

The course provided ten on-policy answers from Qwen2.5-VL-3B-Instruct for each of 10,000 visual questions. For each question, the pipeline selects the least-hallucinated answer as *chosen* and the most-hallucinated one as *rejected*, then trains the model with standard DPO.

## How It Works

<ol class="method-steps">
<li><strong>Judge the candidates.</strong> An LLM judge scores the ten answers per question. Each decision is stored with its confidence, score gap, and reasoning, so the preference data can be audited.</li>
<li><strong>Keep only clear pairs.</strong> Pairs with low judge confidence or a small score gap are refined or dropped. The final dataset has 5,059 preference pairs.</li>
<li><strong>Train and evaluate.</strong> The model is fine-tuned with LoRA DPO in LLaMA-Factory on 8×A100 GPUs and compared with the base model on the AMBER hallucination benchmark, without changing the benchmark's evaluation code.</li>
</ol>

<p class="resource-links"><a href="https://github.com/hwzhangcs/multimodal">Explore the repository →</a><a href="{{ '/portfolio/' | relative_url }}">Other software projects</a></p>
