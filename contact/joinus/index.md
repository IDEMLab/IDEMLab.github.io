---
title: Get involved
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}People

# Join us!

{% include section.html %}

{% include list.html data="content" component="portrait" filters="role: pi" %}


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
