---
layout: page
title: "Projects and Publications"
---

<h3>Projects</h3>
<blockquote>
	<tt><b>About: </b>Past and ongoing Projects</tt>	
	<div class="large-margin" style="text-align:center">
		<img src="{{ site.baseurl }}/pictures/whirlpool_galaxy" width="75%" alt="The Whirlpool Galaxy"/><br>		
		<i><small>The Whirlpool Galaxy (Spiral Galaxy M51, NGC 5194), a classic spiral galaxy located in the Canes Venatici constellation, and its companion NGC 5195 (NASA and European Space Agency)</small></i>
	</div>	
</blockquote>

<h4>Hidden Figures in the Sky</h4>


<h5>The Multi-Dark Galaxies</h5>


<h3>Publications</h3>
<div>
  <ul class="pub-list">
    {% for pub in site.data.publications %}
      <li class="pub-item">
        <strong>{{ pub.title }}</strong><br>
        {{ pub.authors }}<br>
        <em>{{ pub.journal }}</em>, {{ pub.year }}
        {% if pub.doi %}
          — <a href="https://doi.org/{{ pub.doi }}">Link to paper</a>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
</div>


<blockquote>
	<tt><b>Once you took the first step, anything was possible.</b><br>
		&mdash; Katherine Johnson, <small>NASA Mathematician</small></tt><br>								     
</blockquote>	
