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

This project investigates the Universe’s faintest and most elusive galaxies. By combining cosmological simulations and data-driven analysis, the project reveals how low-surface-brightness galaxies (LSBGs) form and evolve within their dark matter halos. Historically, LSBGs received little attention because of observational biases, leading to an underestimation of their relevance for galaxy formation studies.

<div class="text-image">
	<div class="text-image-text">
	 <p>
		 We developed a straightforward method to estimate surface-brightness densities in high-impact hydro-simulations when full photometric information is unavailable. I enforced a strict stellar and halo mass selection to guarantee an unbiased characterisation of LSBGs relative to high-surface-brightness systems (HSBGs). We analysed the evolutionary pathways of LSBGs and found that their assembly histories are more complex than previously assumed. Fig. 1 introduces a novel diagnostic tool to characterise LSBGs using the radius at maximum stellar circular velocity (RVmax​​). Such an evolutionary track has not been presented in the literature before, making it a unique probe of how the inner halo structure of LSBGs develops over cosmic time. We identify a clear divergence in RVmax​​ z∼1.5 (red arrow) between LSBGs and HSBGs, marking the most pronounced separation of evolutionary paths between the two populations, in our analysis. From this epoch onward, the RVmax​​ of HSBGs do not evolve whereas LSBGs undergo substantial dynamical and structural evolution, indicating a fundamentally different assembly pathway and possibly unique galaxy-halo connection for those systems. Studying RVmax​​ provides a most-relevant diagnostic tool for identifying LSBG progenitors.
	</p>
	</div>
	<div class="text-image-img">
			<img src="{{ site.baseurl }}/pictures/zevol_Rvmax.png" width="40%" style="border-radius: 10px" alt="Evolution of the radius at maximum circular velocity"/>
		 	<small>Figure 1: Figure 1: Redshift evolution RVmax​​ for LSBGs (black dashed) and HSBGs (orange solid, with white dots indicating simulation snapshots). Adapted from Stoppacher et al. 2025).</small>

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
