---
layout: post
title: "Halo mass accrection and growth histories"
date: 2021-06-07 #Default format is yyyy.mm.dd
categories: mergertrees
---

<blockquote><tt><b>Summary:</b> We evaluate the mass accretion history and halo growth function for selected most massive top-node halos and their progenitors on the main branch. Thereby we compare the Cholla simulation with two MultiDark boxes.</tt></blockquote>

### Comparison of various dark matter only simulations

In our previous posts we studied the accretion history of main branch progenitor and also parameterized the mass growth history. We used thereby the 256-Cholla dark matter simulation run on a side-length of 50$$h^{-1}$$Mpc box with a total amount of $$256^3$$ particles. We used further <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a> to find halos and tracked them with the tree-builder code <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a>. However, we used an older version of CT (v1.00) in all previous posts which did allow us to extract the main branches of the halos directly and extra assumption on the correct progenitors at each snapshot needed to be made. Here we use an updated version of <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>CT</tt></a> released as v1.01 which has the <b>allows for an easy extraction of the main progenitor branch for any top-node halo</b>. More information on this procedure can be found on <a href="https://www.cosmosim.org/cms/documentation/database-structure/merger-trees/">here</a>, in <a href="https://arxiv.org/abs/1602.04813v2">Rodriguez-Puebla et al. (2016)</a>, and in <a href="https://ui.adsabs.harvard.edu/abs/2013AN....334..691R/abstract">Riebe et al. (2013)</a>.
  
In this post we compare mass accretion and growth histories of halos from various dark matter simulations all run with <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>RS</tt></a> and <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>CT</tt></a>. We use a new version of <tt>Cholla</tt> with a higher resolution of $$512^3$$ particles but equal initial conditions. The purpose of this post is to verify that the obtained halo catalog and merger trees from <tt>Cholla</tt> are valid and serve our necessity in order to develop a star formation feedback model on its basis. We compare the following simulation in this post:

<ul class="post-list">
  <li><a href="https://www.cosmosim.org/cms/simulations/smdpl/"><tt>Small MultiDark Planck</tt></a></li>
      <ul class="post-list">
        <li>resolution: 3840^3 particles</li>
        <li>hereafter: <tt>3840-SMDPL</tt> (<a href="https://arxiv.org/abs/1411.4001">Klypin et al. 2016</a>)</li>
        <li>box side-length: 400 h-1Mpc</li>
        <li>particle mass: 9.63x10^7 h-1Msun</li>
        <li>force resolution: 1.5 h-1kpc </li>  
      </ul>

  <li><a href="https://www.cosmosim.org/cms/simulations/vsmdpl/"><tt>Very Small MultiDark Planck</tt></a></li>
    <ul class="post-list">
      <li>resolution: 3840^3 particles</li>
      <li>hereafter: <tt>3840-VSMDPL</tt> (<a href="https://arxiv.org/abs/1411.4001">Klypin et al. 2016</a>)</li>
      <li>box side-length: 160 h-1Mpc</li>
      <li>particle mass: 6.20x10^6 h-1Msun</li>
      <li>force resolution: -- </li>  
    </ul>

  <li><tt>Cholla</tt></li>
    <ul class="post-list">
      <li>resolution: 512^3 particles</li>
      <li>hereafter: <tt>512-Cholla</tt> (<a href="https://ui.adsabs.harvard.edu/abs/2015ApJS..217...24S">Schneider &amp; Robertson 2015</a>, <a href="https://ui.adsabs.harvard.edu/abs/2020arXiv200906652V">Villase&ntilde;or et al. 2020</a>)</li>
      <li>box side-length: 50 h-1Mpc</li>
      <li>particle mass: 8.04x10^7 h-1Msun</li>
      <li>force resolution: 97.7 h-1kpc </li>  
    </ul>
</ul>

All three simulations have comparable cosmologies and use the same <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>RS</tt></a>-configurations (e.g. FOF refinment: 0.7, linking length: 0.28, unbound threshold: 0.5). <small>The SMDPL and VSMDPL simulation and halo finding has been performed at LRZ Munich within the project pr87yi and pr47no (PI: Stefan Gottloeber). <a href="www.cosmosim.org">The CosmoSim database</a> providing the file access is a service by the Leibniz-Institute for Astrophysics Potsdam (AIP).</small>  
  
### Halo mass assembly history
  
<figure>
  <img src="{{ site.baseurl }}/plots/2021-06-07_MAH_Mvir_most_massive_var-sims.png">
  <figcaption>Mass accretion histories of halo masses as a function of the scale factor of selected most massive top-node halos from various dark matter simulations. The small white dots repsents the time steps between snapshots for each simulation.
  </figcaption>
</figure>
 
The 512-Cholla main branch halos show considerable variations in the mass accretion compared to the MultiDark simulations which have smoother accretion histories. <b>Cholla tracks halos in considerable smaller time steps as the MultiDark simulations.</b> For comparison reason the scale factor evolution of $$V_{max}$$ which shows a similar results.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-06-07_MAH_Vmax_most_massive_var-sims.png">
  <figcaption>Histories of the evolution of the maximum halo velocity as a function of the scale factor of selected most massive top-node halos from various dark matter simulations.
  </figcaption>
</figure>
  
### Halo mass growth history normalized by their final masses

<figure>
  <img src="{{ site.baseurl }}/plots/2021-06-07_MAH_Mvir-growth_most_massive_var-sims.png">
  <figcaption>Halo mass growth histories of most massive top-node halos as a function of the scale factor from various dark matter simulation normalized by there final mass.
  </figcaption>
</figure>

The growth history normalized by the final halo mass of each main progenitor draws a similar picture as Fig.1 and Fig.2. Two of the three selected most massive top-node halos show considerable dips in the growth function.
  
### Fractional variation of the mass accrection history (MAH)
  
  <figure>
  <img src="{{ site.baseurl }}/plots/2021-06-07_MAH_Mvir_fraction_var-sims.png">
  <figcaption>Fractional variation in % of the halo mass between two progenitor halos of most massive top-node halos as a function of the scale factor from various dark matter simulations.
  </figcaption>
</figure>

All simulation show considerable variations in the mass accretion history (MAH) between direct progenitors on the main branch. However, Cholla has the functions  with the most "spikes" visible in the accretion history of its progenitors. For comparison reason we also show the evolution of $$V_{max}$$ which shows less variations than the halo mass.
   
  <figure>
  <img src="{{ site.baseurl }}/plots/2021-06-07_MAH_Vmax-fraction_var-sims.png">
  <figcaption>Fractional variation in % of the Vmax property between direct progenitors of most massive top-node halos as a function of the scale factor from various dark matter simulations.
  </figcaption>
</figure>




