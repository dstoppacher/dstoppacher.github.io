---
layout: page
title: "Projects and Publications"
---


<blockquote>
	<tt><b>About: </b>This page provides an overview of my current and past research projects, along with a complete list of my publications.</tt>	
	<div class="large-margin" style="text-align:center">
		<img src="{{ site.baseurl }}/pictures/1280px-Messier51_sRGB.jpg" width="75%" alt="The Whirlpool Galaxy"/><br>		
		<i><small>The Whirlpool Galaxy (Spiral Galaxy M51, NGC 5194), a classic spiral galaxy located in the Canes Venatici constellation, and its companion NGC 5195 (NASA and European Space Agency)
		</small></i>
	</div>	
</blockquote>

<h3>Projects</h3>

<div> 
	<h4>Hidden Figures in the Sky</h4>
	This project investigates the Universe’s faintest and most elusive galaxies. By combining cosmological simulations and data-driven analysis, the project reveals how low-surface-brightness galaxies (LSBGs) form and evolve within their dark matter halos. Historically, LSBGs received little attention because of observational biases, leading to an underestimation of their relevance for galaxy formation studies.
</div>

<blockquote>
	<div id="address-image">
	  <div id="address-image-left">
For the <b>Hidden Figures in the Sky</b> project, I developed a straightforward method to estimate surface-brightness densities in high-impact hydro-simulations when full photometric information is unavailable. I enforced a strict stellar and halo mass selection to guarantee an unbiased characterisation of LSBGs relative to high-surface-brightness systems (HSBGs). I analysed the evolutionary pathways of LSBGs and found that their assembly histories are more complex than previously assumed. Fig. 1 introduces a novel diagnostic tool to characterise LSBGs using the radius at maximum stellar circular velocity (RVmax​​); to my knowledge, such an evolutionary track has not been presented in the literature before, making it a unique probe of how the inner halo structure of LSBGs develops over cosmic time.
	  </div>
	  <div id="address-image-right">
		<img src="{{ site.baseurl }}/pictures/zevol_Rvmax.jpg" style="border-radius: 10px" height="50%" alt="Evolution of the radius at maximum circular velocity"/>
	  </div>
	</div>
</blockquote>


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
