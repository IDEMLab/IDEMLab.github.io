---
title: News
nav:
  order: 4
  tooltip: Lab news and life
---

# {% include icon.html icon="fa-solid fa-newspaper" %}News

<style>
  .news-feed {
    max-width: 760px;
    margin: 0 auto;
  }
  .news-item {
    margin: 0 0 34px;
  }
  .news-date {
    font-size: 0.8rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--gray);
    margin-bottom: 4px;
    text-align: left;
  }
  .news-text {
    line-height: 1.7;
    text-align: justify;
  }
  .news-image {
    display: block;
    width: 100%;
    max-width: 460px;
    margin: 8px 0 12px;
    border-radius: 8px;
  }
  .news-gallery {
    display: grid;
    grid-template-columns: 2fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 8px;
    width: 100%;
    max-width: 720px;
    aspect-ratio: 2 / 1;
    margin: 8px 0 12px;
  }
  .news-gallery img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 8px;
    display: block;
  }
  .news-gallery .g-big {
    grid-row: 1 / span 2;
  }
</style>

<div class="news-feed">
{% assign items = site.data.news | sort: "date" | reverse %}
{% for item in items %}
  <div class="news-item">
    <div class="news-date">{{ item.date | date: "%B %-d, %Y" }}</div>
    {% if item.images %}
      <div class="news-gallery">
        <img class="g-big" src="{{ item.images[0] | relative_url }}" alt="" loading="lazy">
        {% for img in item.images offset: 1 limit: 2 %}
          <img src="{{ img | relative_url }}" alt="" loading="lazy">
        {% endfor %}
      </div>
    {% elsif item.image %}
      <img class="news-image" src="{{ item.image | relative_url }}" alt="" loading="lazy">
    {% endif %}
    <div class="news-text">{{ item.text | markdownify | remove: "<p>" | remove: "</p>" }}</div>
  </div>
{% endfor %}
</div>
