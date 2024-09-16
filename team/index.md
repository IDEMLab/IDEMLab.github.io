---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pi" %}
{% include list.html data="members" component="portrait" filters="role: ^(?!pi$)" %}

{% include section.html background="images/background.jpg" dark=true %}

# Diversity, Equity, and Inclusion Statement
Research and innovation thrive when different voices, perspectives, and experiences come together. In our lab, we welcome members from all backgrounds and identities, including but not limited to race, age, gender identity, religion, neurodiversity, and citizenship. We are committed to creating an inclusive environment where everyone feels a sense of belonging. Through a culture of listening, mutual understanding, mutual respect, open-mindedness, and a dedication to continuous learning and unlearning, we actively foster an atmosphere where every lab member can thrive and be their best self.

{% include section.html %}

{% capture content %}

{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
