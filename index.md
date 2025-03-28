---
---
<div style="text-align: center;">
    <!--<strong> -->Welcome to the Interactive Dynamics of Episodic Memory (IDEM) Lab at NYU! <!-- </strong><br><br> -->
</div>


{% include section.html %}



{% capture text %}

<!--Learn more about what we investigate and the methods we use. -->

{%
  include button.html
  link="projects"
  text="Learn more about our research"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/our_research.png"
  link="research"
  text=text
%}

{% capture text %}

<!--Explore some of our work. -->

{%
  include button.html
  link="research"
  text="Browse our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/our_publications.png"
  link="projects"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

<!--Meet the researchers in our lab.-->

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/our_team.png"
  link="team"
  text=text
%}

{% capture text %}

<!--See what we're up to outside of research.-->

{%
  include button.html
  link="photos"
  text="View photos and events"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/our_photos.png"
  link="team"
  flip=true
  style="bare"
  text=text
%}
