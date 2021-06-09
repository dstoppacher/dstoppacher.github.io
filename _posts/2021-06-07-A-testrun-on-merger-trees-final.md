---
layout: post
title: "Halo mass accrection and growth histories"
date: 2021-06-07 #Default format is yyyy.mm.dd
categories: mergertrees
---

<blockquote><tt><b>Summary:</b> We evaluate the mass accrection history of 512-Cholla halos and compare to MultiDark simulation boxes</tt></blockquote>

### Comparision of various dark matter only simulations

In our previous posts we studied the accrection history of main branches with Rockstar and also parameterized the mass growth history. We used therefore the 256-Cholla dark matter simulation run a side-length of 50$$h^{-1}$$Mpc box with a total amount of particle of $$256^3$$. We used further <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a> to find halos and tracked them with the tree-builder code <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a>. However, we used an older version of CT, namely 1.00, in all previous posts. There was an update of it released as 1.01 which has the advantage to easily extracth the main progenitor branch of any top-node halo. More information on that procedure can be found on <a href="https://www.cosmosim.org/cms/documentation/database-structure/merger-trees/"><tt>CosmoSim-documentation</tt></a> and in <a href="https://arxiv.org/abs/1602.04813v2"><tt>Rodriguez-Puebla et al. 2016</tt></a> and <a href="https://ui.adsabs.harvard.edu/abs/2013AN....334..691R/abstract"><tt>Riebe et al. 2013</tt></a>.
  
In this post we compare mass accrection and growth history of halos from various dark matter simulation all run with <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>RS</tt></a> and <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>CT</tt></a>. We use a new version of Cholla-512 with a higher resolution of $$512^3$$ particles but equal initial conditions. The purpose of this post is to verify that the obtained halo catalog from Cholla-512 and merger trees are valid to develop a star formation feedback model on its basis. We use 

<ul class="post-list">
  <li><a href="https://www.cosmosim.org/cms/simulations/smdpl/"><tt>Small MultiDark Planck</tt></a></li>
      <ul class="post-list">
        <li>3840^3 particles</li>
        <li>hereafter <tt>3840-SMDPL</tt> (<a href="https://arxiv.org/abs/1411.4001">Klypin et al. 2016</a>)</li>
        <li>400 h-1Mpc box</li>
        <li>particle mass 9.63x10^7 h-1Msun/li>
        <li>force resolution: 1.5 h-1kpc </li>  
      </ul>

  <li><a href="https://www.cosmosim.org/cms/simulations/vsmdpl/"><tt>Very Small MultiDark Planck</tt></a></li>
    <ul class="post-list">
      <li>3840^3 particles</li>
      <li>hereafter <tt>3840-VSMDPL</tt> (<a href="https://arxiv.org/abs/1411.4001">Klypin et al. 2016</a>)</li>
      <li>160 h-1Mpc box</li>
      <li>particle mass 6.20x10^6 h-1Msun/li>
      <li>force resolution: -- </li>  
    </ul>

  <li>Cholla</li>
    <ul class="post-list">
      <li>512^3 particles</li>
      <li>hereafter <tt>512-Cholla</tt> (<a href="https://ui.adsabs.harvard.edu/abs/2015ApJS..217...24S">Schneider &amp; Robertson 2015</a>, <a href="https://ui.adsabs.harvard.edu/abs/2020arXiv200906652V">Villase&ntilde;or et al. 2020</a>)</li>
      <li>50 h-1Mpc box</li>
      <li>particle mass 8.04x10^7 h-1Msun</li>
      <li>force resolution: 97.7 h-1kpc </li>  
    </ul>
</ul>
All three simulations have comparable cosmolog and use the same ROCKSTAR-configuration. The SMDPL and VSMDPL simulation and halo finding has been performed at LRZ Munich within the project pr87yi (PI: Stefan Gottloeber). <a href="www.cosmosim.org">The CosmoSim database</a> providing the file access is a service by the Leibniz-Institute for Astrophysics Potsdam (AIP).
 
  
  
  
### Halo mass accembly history
  
<figure>
  <img src="{{ site.baseurl }}/plots/2021-06-07_MAH_Mvir_most_massive_var-sims.png">
  <figcaption>Mass accretion histories of most massive top node halos from various dark matter simulations.
  </figcaption>
</figure>
  
 For comparision reason the redshift evolution of $$V_{max}$$.

  <figure>
  <img src="{{ site.baseurl }}/plots/2021-06-07_MAH_Vmax_most_massive_var-sims.png">
  <figcaption>Mass growth histories of most massive top node halos from various dark matter simulation normalised by there final mass.
  </figcaption>
</figure>
  
### Halo mass growth history compared to their final masses

<figure>
  <img src="{{ site.baseurl }}/plots/2021-06-07_MAH_Mvir-growth_most_massive_var-sims.png">
  <figcaption>Mass growth histories of most massive top node halos from various dark matter simulation normalised by there final mass.
  </figcaption>
</figure>

### Halo mass growth history compared to its final mass

<figure>
  <img src="{{ site.baseurl }}/plots/2021-06-07_MAH_Mvir-growth_most_massive_var-sims.png">
  <figcaption>Mass growth histories of most massive top node halos from various dark matter simulation normalised by there final mass.
  </figcaption>
</figure>
  
### Fractional variation of the mass accrection history (MAH)
  
  <figure>
  <img src="{{ site.baseurl }}/plots/2021-06-07_MAH_Mvir_fraction_var-sims.png">
  <figcaption>Fractional variation in % of the mass growth histories of most massive top node halos from various dark matter simulations.
  </figcaption>
</figure>

 For comparision reason the redshift evolution of $$V_{max}$$.
   
  <figure>
  <img src="{{ site.baseurl }}/plots/2021-06-07_MAH_Vmax-fraction_var-sims.png">
  <figcaption>Fractional variation in % of the V_max property of most massive top node halos from various dark matter simulations.
  </figcaption>
</figure>


