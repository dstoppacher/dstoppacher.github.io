---
layout: post
title: "A testrun on merger trees part II"
date: 2021-01-21 #Default format is yyyy.mm.dd
categories: mergertrees
---

<blockquote><tt><b>Summary:</b>TBA</tt></blockquote>


This is the continuation of the post from <a href="https://dstoppacher.github.io/A-testrun-on-merger-trees/">2021-01-07</a>. The following questions are still open will be discussed in this post.

<ol>
  <li>Verify the approach of connection halos by the provided <tt>haloid</tt> and <tt>descID</tt> by comparing directly with the numbers of particle assigned to the halos between snapshots.</li>

  <li>How does <b>ROCKSTAR</b> assign the <tt>descID</tt> when running?</li>

  <li>Calculate halo mass function and accretion rates.</li>
</ol> 
 
### Task1: Merger tree verification
 
 
#### The example of merger tree <tt>treeID13</tt>
 
In this analysis we scanned through the entire box of <b>Cholla</b> with side-lenght 50$$h^{-1}$$Mpc and a resolution of $$256^3$$. We approximate the halo mass of <b>Cholla</b> buy gathering all dark matter particles within a certain radius (e.g. $$5\times$$ the virial radius $$R_{vir}$$). Then we multiplied the number of particel $$n_{particle}$$ by the mass of one dark matter particle in the simulation being $$m_{DM}=5.407\times 10^8$$ $$[h^{-1}M_{\odot}]$$. We compare this result with the halo mass the halo finder <b>ROCKSTAR</b> provided. In <i>Figure 1</i> we show the offset between the two halo masses on the x-axis for <b>ROCKSTAR</b> and on the y-axis for <b>Cholla</b>. The differences are up to $$\pm50\%$$ in masses. <i>Figure 2</i> gives a detail list of the data plotted in <i>Figure 1</i>.
 
<figure>
  <img src="{{ site.baseurl }}/plots/2021-01-21_mhalo_offset.png">
  <figcaption>The figure visualizes the offset between the halos from merger tree with ID13 provided by <b>ROCKSTAR</b> (x-axis) in comparision what we can approximate when summing up dark matter particles within $5\times$ the virial radius $R_{vir}$ (y-axis). The number of particles are given by the color bar
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-01-21_Table_treeID13.png">
  <figcaption>In this table we list all main progenitor halos for the merger tree <tt>treeID13</tt>. The halo mass provided by <b>ROCKSTAR</b> is shown in column <tt>mhalo</tt> and the approximated in column <tt>m_particles</tt>. In column <tt>n_particles</tt> we shown the number of dark matter particles we found to determine the halo mass. In column <tt>mhalo-m_particle(%)</tt> we show the difference between the halo masses from <b>ROCKSTAR</b> and <b>Cholla</b> in \%. The halo masses are given in $[h^{-1}M_{\odot}$ and the positions columns <tt>X</tt>, <tt>Y</tt>, and <tt>Z</tt> in $[h^{-1}comvkpc]$.
  </figcaption>
</figure>

Although the difference in halo masses are significant high, we can still confirm that <b>ROCKSTAR</b> sets the <tt>descIDs</tt> correctly. In <i>Figure 3</i> we illustrated that by tracking the position of the main progenitor halos of <tt>treeID13</tt> between $$2.19<z<10.33$$.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-01-21_treeID13_2.19_z_11.51.png">
  <figcaption>Positions of the main progenitor halos for the merger tree <tt>treeID13</tt> througout redshift.
  </figcaption>
</figure>

#### Positions of all main progenitors at z=4.15
 
  <figure>
  <img src="{{ site.baseurl }}/plots/2021-01-21_all_main_prog_4.15.png">
  <figcaption>Positions of the main progenitor halos at z=4.15. The black dots show halos which have less then 10% difference in the halo masses for <b>ROCKSTAR</b> and <b>Cholla</b>.
  </figcaption>
</figure>


#### Halo mass function (HMF) of all main progenitors at z=4.15
  <figure>
  <img src="{{ site.baseurl }}/plots/2021-01-21_HMF.png">
  <figcaption>Halo mass function of the main progenitor halos at z=4.15 for <b>ROCKSTAR</b> (red line), <b>Cholla</b> (blue line), and halos with less than 10% difference in halo mass (black dashed line).
  </figcaption>
</figure>
 
#### Position of all main progenitors between 2<z<11

<figure>
  <img src="{{ site.baseurl }}/plots/2021-01-21_all_main_prog_2.19_z_11.51.png">
  <figcaption>Positions of the main progenitor halos for the merger tree <tt>treeID13</tt> througout redshift.
  </figcaption>
</figure>

#### Halo mass function (HMF) of all main progenitors between 2<z<11
 
<figure>
  <img src="{{ site.baseurl }}/plots/2021-01-21_HMF_4.15.png">
  <figcaption>Halo mass function of the main progenitor halos bewteen 2<z<11 for <b>ROCKSTAR</b> (red line), <b>Cholla</b> (blue line), and halos with less than 10% difference in halo mass (black dashed line).
  </figcaption>
</figure>





 
 
