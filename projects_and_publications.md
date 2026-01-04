---
layout: page
title: "Projects and Publications"
---

<blockquote style="margin-bottom:2.5em">
	<tt><b>About: </b>Past and ongoing reseach projects and publications</tt>										     
</blockquote>

<h2>Projects</h2>
<h3>Hidden Figures in the Sky</h3>


<h2>Publications</h3>

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
