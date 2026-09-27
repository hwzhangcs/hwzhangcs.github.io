<div class="entry-list">
{% for item in site.data.ip %}
<article class="entry">
<h3>{{ item.title }}</h3>
<p class="entry-meta" lang="zh">{{ item.zh }}</p>
<p>{{ item.role }}{% if item.applicant %} · Applicant: {{ item.applicant }}{% endif %}</p>
<p class="entry-meta">{{ item.kind }} {{ item.number }}<br>{{ item.dates }}</p>
{% if item.status %}<p class="entry-note">{{ item.status }}</p>{% endif %}
</article>
{% endfor %}
</div>
