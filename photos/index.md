---
title: Photos
nav:
  order: 7
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}People

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pi" %}

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: phd" %}

{% include list.html data="members" component="portrait" filters="role: labmanager" %}

{% include list.html data="members" component="portrait" filters="role: masters" %}

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
