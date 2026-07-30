---
layout: page
title: "Projects and Publications"
---
<blockquote>
	<b>About: </b>This page provides an overview of my current and past research projects, along with a complete list of my publications.
	<div class="large-margin" style="text-align:center">
		<img src="{{ site.baseurl }}/pictures/1280px-Messier51_sRGB.jpg" width="75%" alt="The Whirlpool Galaxy"/><br>		
		<i><small>The Whirlpool Galaxy, a classic spiral galaxy located in the Canes Venatici constellation, and its companion NGC 5195 (NASA and European Space Agency)</small></i>
	</div>	
</blockquote>

<h3>Projects</h3>

<div>
	<div class="text-block">
		<h4>Hidden Figures in the Sky</h4>
		<h5>Low-surface-brightness galaxies in cosmological simulations</h5>
		<p>
This project explores the formation and evolution of low-surface-brightness galaxies (LSBs), a fascinating and still poorly understood population that remains highly underrepresented in the literature despite its potential to reshape our understanding of galaxy formation. Using cosmological hydrodynamical simulations, I investigate how these faint galaxies form and evolve, and develop new methods to identify and characterise them in simulated data, connecting their observable properties to their underlying dark matter haloes.
		</p>
	</div>
</div>

<div class="text-image">
	<div class="text-image-text">
		 <p><b>In Stoppacher et al. (2025b), we investigated the evolutionary pathways of LSBs and found that their assembly histories are considerably more complex than previously assumed. We introduced a novel diagnostic based on the radius at which the stellar circular velocity reaches its maximum, Rvmax, which has not previously been used in the literature to characterise LSB galaxies. This provides a unique probe of the evolution of their inner halo structure across cosmic time</b><br>
<small>The figure reveals a clear divergence in Rvmax at z~1.5 (red arrow) between LSBs (black dashed line) and high-surface-brightness galaxies (HSBs; orange solid line with white dots), marking it the strongest separation between the evolutionary pathways of the two populations identified in our analysis. Figure adapted from Stoppacher et al. (2025b)</small>
		 </p>
	</div>
	<div class="text-image-img">
		<img src="{{ site.baseurl }}/pictures/zevol_Rvmax.png" width="100%" style="border-radius: 5px" alt="Evolution of the radius at maximum circular velocity"/>
	</div>
</div>


<div align="center" style="margin-bottom: 2em; margin-top:2em">&mdash;&nbsp;<i class='fa fa-rocket'>&nbsp;</i><i class='fa fa-rocket'>&nbsp;</i><i class='fa fa-rocket'></i>&nbsp;&mdash;</div>    

<div>
	<div class="text-block">
		<h4>The Multi-Dark Galaxie</h4>
		<h5>A semi-analytical perspective on galaxies and their evolution on the largest-scale</h5>
		<p>
MultiDark-Galaxies provides a comprehensive view of galaxy formation within the cosmic web by combining large cosmological simulations with semi-analytical models of galaxy evolution (SAM). We developed and released publicly available galaxy catalogues and analysis tools, enabling researchers to explore the connection between galaxies and their dark matter environments across cosmic time.
		</p>
	</div>
</div>

<div class="text-image">
	<div class="text-image-text">
		 <p><b>The MultiDark-Galaxies are feature-rich catalogues generated from three independent SAMs applied to the 1 h-1Gpc MultiDark Planck 2 simulation (MDPL2, Klypin et al. 2016). These catalogues remain among the largest publicly available SAM datasets.</b><br>
			 For this project, I combined and processed several terabytes of simulation outputs and carried out all preparation, testing, and data-reduction steps required for their public release as MD-Galaxies. My work included pipeline development (publicly available on GitHub), validation and consistency checks, and full documentation. I ensured that the catalogues were scientifically robust, reproducible, and publicly accessible and continued to provide technical and scientific support to users, helping to maintain the long-term value and usability of these community data products. Figure adapted from Knebe, Stopacher, Prada et al. (2018).
		 </p>
	</div>
	<div class="text-image-img">
		<img src="{{ site.baseurl }}/pictures/MDGalaxies_SMF.png" width="100%" style="border-radius: 5px" alt="Stellar mass function of the MultiDark-Galaxies a z=0.1"/>
	</div>
</div>

<div align="center" style="margin-bottom: 2em; margin-top:2em">&mdash;&nbsp;<i class='fa fa-rocket'>&nbsp;</i><i class='fa fa-rocket'>&nbsp;</i><i class='fa fa-rocket'></i>&nbsp;&mdash;</div>    

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
  <hr class="fancyLine">
</div>


<simplequote>
	<tt>
		<b>Once you took the first step, anything was possible.</b>
		<ul class="note-list">
	  		<li> &mdash; Katherine Johnson, <small>NASA Mathematician</small></li>
		</ul>
	</tt>
</simplequote>		
