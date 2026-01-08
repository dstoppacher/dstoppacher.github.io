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

<h4>Hidden Figures in the Sky</h4>

This project investigates the Universe’s faintest and most elusive galaxies. By combining cosmological simulations and data-driven analysis, the project reveals how low-surface-brightness galaxies (LSBGs) form and evolve within their dark matter halos. Once hidden by observational limits, these galaxies are now recognised as key to understanding galaxy evolution.

<div class="text-image">
	<div class="text-image-text">
	 <p> We developed a simple and robust method to estimate surface-brightness densities in hydrodynamical simulations even when full photometric information is unavailable. Using a strict stellar and halo mass selection, we obtained an unbiased comparison between low- and high-surface-brightness galaxies. We show that LSBGs follow more complex evolutionary pathways than previously assumed and introduce a new diagnostic based on the radius at maximum stellar circular velocity (RVmax). This evolutionary track, presented for the first time, reveals a clear divergence between LSBGs and HSBGs at 
z∼1.5, marking the onset of fundamentally different assembly histories and identifying RVmax as a powerful tracer of LSBG progenitors. < small>The figure shows the redshift evolution RVmax​​ for LSBGs (black dashed) and HSBGs (orange solid). Adapted from Stoppacher et al. 2025.</small>
	</p>
	</div>
	<div class="text-image-img">
			<img src="{{ site.baseurl }}/pictures/zevol_Rvmax.png" width="100%" style="border-radius: 5px" alt="Evolution of the radius at maximum circular velocity"/>
	</div>
</div>


<h5>The Multi-Dark Galaxies</h5>
The MultiDark-Galaxies (MD-Galaxies) are feature-rich catalogues generated from 3 independent semi-analytical models of galaxy formation and evolution (SAMs) applied to the 1 h-1Gpc MultiDark Planck 2 simulation (MDPL2, Klypin et al. 2016). These catalogues remain among the largest publicly available SAM datasets. For this project, I combined and processed several terabytes of simulation outputs and carried out all preparation, testing, and data-reduction steps required for their public release as MD-Galaxies. My work included pipeline development (publicly available on GitHub), validation and consistency checks, and full documentation. I ensured that the catalogues were scientifically robust, reproducible, and publicly accessible and continued to provide technical and scientific support to users, helping to maintain the long-term value and usability of these community data products.


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
