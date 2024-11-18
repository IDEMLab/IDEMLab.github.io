---
title: People
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}People

Here you can learn more about the researchers who drive our lab’s exploration into the complexities of memory and cognition. Our team brings together a diverse set of skills and expertise, all interested in advancing our understanding of how memories are formed, stored, and retrieved.

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pi" %}

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: phd" %}

{% include list.html data="members" component="portrait" filters="role: labmanager" %}

{% include list.html data="members" component="portrait" filters="role: grad" %}

{% include list.html data="members" component="portrait" filters="role: undergrad" %}



{% include section.html background="images/background.jpg" dark=true %}



{% comment %}
{% include section.html %}

{% capture content %}

{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
{% endcomment %}
