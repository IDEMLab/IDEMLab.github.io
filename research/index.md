---
title: Research
nav:
  order: 1
  tooltip: What we do
---

# {% include icon.html icon="fa-solid fa-brain" %}Research

<style>
  .research-container {
    display: flex;
    flex-direction: column; /* Change layout to column to stack text and cards */
    gap: 20px;
  }

  .research-text {
    padding-bottom: 20px; /* Add space between the text and cards */
  }

  .research-cards {
    display: flex;
    flex-wrap: wrap; /* Allow cards to wrap if there are many */
    justify-content: center; /* Center the cards horizontally */
    gap: 15px; /* Space between the cards */
  }

  .research-cards .card {
    max-width: 250px; /* Limit the card width */
  }
</style>

<div class="research-container">
  <div class="research-text">
    <div style="text-align: center; margin-bottom: 50px;">
      <p>In the IDEM Lab, we want to understand how fast neural dynamics enable human episodic memory formation and retrieval. We are especially interested in how memories are formed and retrieved under real-life conditions. For example, when there is no explicit study or test phase, how does the brain determine when to store or retrieve information? And how do different memory systems work together when we process information-rich and continuous stimuli?
  To answer these questions, we leverage a wide array of methods, including electrophysiology (EEG, MEG, and intracranial EEG), computational modeling, and behavioral experiments.</p>
  </div>
  <!--
  <div class="research-cards">
    {% include list.html component="card" data="projects" %}
  </div>
  -->
</div>
