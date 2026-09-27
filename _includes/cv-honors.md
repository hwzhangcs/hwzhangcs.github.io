{% for honor in site.data.honors %}
- **{{ honor.title }}{% if honor.zh %} ({{ honor.zh }}){% endif %}**, {{ honor.detail }}, {{ honor.date }}.
{% endfor %}
