---
title: Photos
nav:
  order: 6
  tooltip: Lab life
---

# {% include icon.html icon="fa-solid fa-camera-retro" %}Lab Life

<style>
  .feature-image {
    width: 60% !important;
  }
</style>

{% capture text %}
{% include icon.html icon="fa-solid fa-leaf" %} Lab outing at Cold Spring. Golden leaves and crisp, clear weather made it the perfect day to hike.
{% endcapture %}

{%
  include feature.html
  image="images/cold-spring.jpg"
  text=text
%}

{% capture text %}
{% include icon.html icon="fa-solid fa-dice" %} Who doesn't love a good board game break?
{% endcapture %}

{%
  include feature.html
  image="images/board-game.jpg"
  flip=true
  text=text
%}

{% capture text %}
{% include icon.html icon="fa-solid fa-beer-mug-empty" %} At Sugar Mouse celebrating big transitions: wishing Liv the best at Yale and welcoming our new post-doc, Ricardo. Lots of pool, foosball, and table tennis!
{% endcapture %}

{%
  include feature.html
  image="images/bar.jpg"
  text=text
%}
