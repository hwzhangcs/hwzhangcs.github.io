---
layout: academic
title: "Sitemap"
permalink: /sitemap/
excerpt: "Explore Hanwen Zhang's research, publications, software projects, and CV."
---

- [Home]({{ '/' | relative_url }})
- [Research]({{ '/#research' | relative_url }})
- [Publications]({{ '/#publications' | relative_url }})
- [Software]({{ '/portfolio/' | relative_url }})
- [CV]({{ '/cv/' | relative_url }})

## Research Project Details

- [Bone-to-Shape]({{ "/research/bone-to-shape/" | relative_url }})

## Software Project Details

{% assign projects = site.portfolio | sort: 'order' %}
{% for project in projects %}
- [{{ project.title }}]({{ project.url | relative_url }})
{% endfor %}

[XML sitemap]({{ '/sitemap.xml' | relative_url }})
