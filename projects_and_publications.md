---
layout: page
title: "Projects and Publications"
---

<h3>Projects</h3>

<h5>Hidden Figures in the Sky</h5>


<h5>The Multi-Dark Galaxies</h5>


<h3>Publications</h3>
<section>
  <ul class="pub-list">
    {% for pub in site.data.publications %}
      <li class="pub-item">
        <strong>{{ pub.title }}</strong><br>
        {{ pub.authors }}<br>
        <em>{{ pub.journal }}</em>, {{ pub.year }}
        {% if pub.doi %}
          — <a href="https://doi.org/{{ pub.doi }}">DOI</a>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
</section>


<blockquote style="margin-bottom:2.5em">
	<tt><b>About: </b></tt>										     
</blockquote>
