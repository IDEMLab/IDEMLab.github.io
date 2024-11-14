---
---
<div style="text-align: center;">
    <strong>THIS WEBSITE IS UNDER CONSTRUCTION</strong><br><br>
    Welcome to the Interactive Dynamics of Episodic Memory (IDEM) Lab in New York University's Department of Psychology.<br>
    Our lab, led by Sebastian Michelmann, explores the complexities of episodic memory through cognitive and computational neuroscience.
</div>


{% include section.html %}



{% capture text %}

Explore how we investigate the neural dynamics of memory through cognitive neuroscience methods. 

{%
  include button.html
  link="research"
  text="See our research"
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

Stay tuned for our upcoming findings and contributions to the field of episodic memory research.

{%
  include button.html
  link="projects"
  text="Coming soon: Browse our publications"
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

Meet the researchers behind our lab, dedicated to advancing the understanding of memory and cognition.

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
