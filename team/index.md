---
title: People
nav:
  order: 2
  tooltip: About our team
---

<style>
  /* People page: keep every section background white (no alternating grey) */
  main > section:nth-of-type(even) { background: var(--background); }
</style>

# {% include icon.html icon="fa-solid fa-users" %}People

<div class="team-grid">
{% include list.html data="members" component="portrait" filters="role: pi" %}
{% include list.html data="members" component="portrait" filters="role: postdoc" %}
{% include list.html data="members" component="portrait" filters="role: phd" %}
{% include list.html data="members" component="portrait" filters="role: labmanager" %}
{% include list.html data="members" component="portrait" filters="role: masters" %}
{% include list.html data="members" component="portrait" filters="role: undergrad" %}
{% include list.html data="members" component="portrait" filters="role: volunteer" %}
</div>


{% include section.html %}

## {% include icon.html icon="fa-solid fa-graduation-cap" %}Alumni

{% include list.html data="members" component="portrait" filters="role: alumni" %}



{% comment %}
{% include section.html %}

{% capture content %}

{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
{% endcomment %}
