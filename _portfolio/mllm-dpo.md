---
title: "MLLM Hallucination Mitigation with DPO"
order: 0
home: true
purpose: "Hallucination mitigation in a vision-language model with preference optimization"
contribution: "Team course project (3 students). Wrote the LLM-judge pipeline that built 10,000 audited DPO pairs and the LoRA DPO training code; teammates ran the experiments."
stack: "Python · Qwen2.5-VL · LLaMA-Factory · pixi"
code_url: "https://github.com/hwzhangcs/multimodal"
excerpt: "Team course project. An LLM judge turned 100,000 on-policy VQA answers into 10,000 audited DPO preference pairs; LoRA DPO on Qwen2.5-VL-3B-Instruct lowered AMBER Hal from 49.4 to 29.2 and raised discriminative F1 from 57.4 to 74.8."
---

<p class="project-deck">Turning a model's own answers into preference data for hallucination mitigation.</p>
<p class="entry-meta">Team course project (3 students) · Introduction to Multimodal Learning, Sichuan University · 2026<br>My role: preference-data pipeline (judging, re-judging, auditing) and the LoRA DPO training code. Teammates ran the training and AMBER evaluation.</p>
<p class="resource-links"><a href="https://github.com/hwzhangcs/multimodal">Source code</a><a href="https://github.com/hwzhangcs/multimodal#readme">README &amp; setup</a></p>

## What the Project Does

The course provided ten on-policy answers from Qwen2.5-VL-3B-Instruct for each of 10,000 visual questions. For each question, the pipeline selects the least-hallucinated answer as *chosen* and the most-hallucinated one as *rejected*, then trains the model with standard DPO.

## How It Works

<ol class="method-steps">
<li><strong>Judge the candidates.</strong> A multimodal LLM judge scores the ten answers per question. Each decision is stored with its confidence, score gap, and reasoning, so the preference data can be audited.</li>
<li><strong>Re-judge uncertain cases.</strong> Pairs with low judge confidence or a small score gap are re-judged by a second model on the same image, prompt, and candidates. About 3,100 of the final 10,000 pairs were revised this way.</li>
<li><strong>Train and evaluate.</strong> The model is fine-tuned with LoRA DPO in LLaMA-Factory for two epochs and compared with the base model on the AMBER hallucination benchmark, using the same queries and unchanged evaluation code.</li>
</ol>

## Results on AMBER

| Metric | Base | LoRA DPO |
|---|---:|---:|
| CHAIR (lower is better) | 8.1 | 5.7 |
| Hal (lower is better) | 49.4 | 29.2 |
| Cog (lower is better) | 5.2 | 2.3 |
| Cover (higher is better) | 69.3 | 62.9 |
| Discriminative accuracy | 55.2 | 69.6 |
| Discriminative F1 | 57.4 | 74.8 |

Hallucination dropped on every generative metric, and discriminative F1 rose mainly through higher recall. Cover also fell, so the fine-tuned model answers more conservatively: it describes less that it cannot support, but also covers fewer of the objects in the image.

<p class="resource-links"><a href="https://github.com/hwzhangcs/multimodal">Explore the repository →</a><a href="{{ '/portfolio/' | relative_url }}">Other software projects</a></p>
