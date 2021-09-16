---
layout: post
title: "Shared particle fractions in direct progenitors"
date: 2021-09-13 #Default format is yyyy.mm.dd
categories: mergertrees
---

<blockquote><tt><b>Summary:</b> We calculate the shared particle fractions of direct progenitor halos after crossmatching all halos and progenitors from the original dark matter simulation (run with Rockstar) and their merger trees output (from Consistent-Trees).</tt></blockquote>

### Simulation

<ul class="post-list">
      <li>resolution: 256^3 particles</li>
      <li>hereafter: <tt>256-Cholla</tt> (<a href="https://ui.adsabs.harvard.edu/abs/2015ApJS..217...24S">Schneider &amp; Robertson 2015</a>, <a href="https://ui.adsabs.harvard.edu/abs/2020arXiv200906652V">Villase&ntilde;or et al. 2020</a>)</li>
      <li>box side-length: 50 h-1Mpc</li>
      <li>particle mass: 8.04x10^7 h-1Msun</li>
        <li>total particles processed: 2097124</li>
      <li>force resolution: 195.3 h-1kpc </li>  
    </ul>



### Detection of phantom halos

<figure>
  <img src="{{ site.baseurl }}/plots/2021-09-13_merger_trees_CT_all_halo_phantoms.png">
  <figcaption>All halos an merger trees. Highlighted are in the first halo of the tree (red cross), phantom halos (solid yellow dot), the next halo in the tree after the phantom halo (black circle). 
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-09-13_merger_trees_CT_all_halo_phantoms_TreeID-79198.png">
  <figcaption>Same as in Fig: 1 but only TreeID-79198 and its subtrees are shown as an example.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-09-13_merger_trees_CT_all_halo_phantoms_TreeID-79561.png">
  <figcaption>Same as in Figure 1 but only TreeID-79561 and its subtrees are shown as an example.
  </figcaption>
</figure>

### Shared particle fractions

<figure>
  <img src="{{ site.baseurl }}/plots/2021-09-13_merger_trees_CT_all_halo_phantoms_shared_fracs.png">
  <figcaption>Redshift evolution of the shared particle fractions of direct progenitors.
  </figcaption>
</figure>


### Redshift evolutin of shared fraction

<figure>
  <img src="{{ site.baseurl }}/plots/2021-09-13_merger_trees_CT_all_shared_frac1.png">
  <figcaption>The shared particle fractions of direct progenitors within 10^{th} and 90^{th} percentiles.
  </figcaption>
</figure>


### Observations & Open Questions

<ul class="post-list">
  <li>Median on shared particle fraciton is mostly over 90 %</li>
  <li>There are two dips in the z-evolution of the shared particle fraction at 1.0 and 2.0. Where do they come from?</li>
</ul>
