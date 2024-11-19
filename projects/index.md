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
    flex-direction: row;
    align-items: flex-start;
    gap: 20px;
  }
  
  .research-text {
    flex: 2; /* Larger portion for the text */
    padding-right: 20px; /* Add some spacing between text and cards */
  }
  
  .research-cards {
    flex: 1; /* Smaller portion for the cards */
  }
  
  .research-cards .card {
    max-width: 250px; /* Limit the card width */
    margin-bottom: 15px; /* Add space between cards */
  }
</style>

<div class="research-container">
  <div class="research-text">
    <h1>{% include icon.html icon="fa-solid fa-brain" %}Research</h1>
    <p>Our lab investigates how general knowledge representations and unique memories interact on a fast timescale. We use electrophysiology (EEG, MEG, and intracranial EEG) combined with computational modeling and behavioral experiments to understand the neurophysiological mechanisms and the computational principles underlying such interactive dynamics of episodic memory.</p>
    <p>In our lab, we investigate how the continuous, temporally dynamic content we encounter in the world is neurally represented, along with the mechanisms and computational principles that enable its encoding and retrieval. For instance, when humming a melody heard only once, the brain reproduces memory patterns with remarkable temporal accuracy, requiring precise neural representations. Conversely, tasks like remembering where we placed our keys involve rapidly scanning through extensive memories, often filled with irrelevant details—raising the question of how the brain balances such efficient memory search with the need for temporally accurate representations.</p>
    <p>We are particularly interested in how memories are formed and retrieved under unconstrained conditions, where there is no explicit study or test phase, and how neural processes align with the continuous flow of information. This leads us to ask: how are fast memory processes integrated into our ongoing experiences? How does the brain determine when to store or retrieve information without predefined cues?</p>
    <p>A key focus of our research is understanding the role of generalized event knowledge in fast-timescale episodic memory processes. Everyday experiences naturally structure themselves into events, like a train ride or a restaurant visit, which can shape how memories are encoded and retrieved. For example, knowledge about typical event structures may help us recall details from unique past experiences. Our lab explores how general knowledge representations interact with unique memories at fast timescales, employing electrophysiology (EEG, MEG, and intracranial EEG), computational modeling, and behavioral experiments. By examining these interactive dynamics, we aim to uncover the neurophysiological mechanisms and computational principles underlying episodic memory.</p>
  </div>
  
  <div class="research-cards">
    {% include list.html component="card" data="projects" %}
  </div>
</div>
