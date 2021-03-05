---
layout: post
title: "A testrun on merger trees part IV"
date: 2021-02-26 #Default format is yyyy.mm.dd
categories: mergertrees
---

<blockquote><tt><b>Summary:</b> In this post we show the median variations of main branch halo properties connected by the descendant information without running a tree builder on top. Our results and their estimated uncertainties are reasonable given the fact that we do not used a tree builder to improve the connection between halos.</tt></blockquote>

This is the continuation of the post from <a href="https://dstoppacher.github.io/A-testrun-on-merger-trees-III/">2021-02-22</a>. Thereby we use only descendant information as the <tt>'DescID'</tt> provided directly by the halo finder <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a>. The halos between snapshots are connected by the descendant ID provided by <tt>Rockstar</tt> as a standard output. When we need to decide whether a halo is serves a main progenitor or not in case on halo has various progenitors, then we choose the most massive (MM) one.

We show in Fig. 1 the median values of variation of shared fraction of particle IDs within $$10^{th}$$ and $$90^{th}$$ percentiles and in Fig. 2 the variaton of the virial halo mass $$M_{vir}$$ $$h^{-1}M_{\odot}$$, virial radius $$R_{vir}$$ $$h^{-1}$$Mpc, and X/Y/Z-positions in $$h^{-1}$$Mpc. In Fig. 3 and Fig. 4 show the same results but use the <a href="https://en.wikipedia.org/wiki/Median_absolute_deviation"><i>median absolute deviation (MAD)</i></a> as an error estimator which is the median of the absolute deviations and a robust measurement for uncertainties when dealing with outliers.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-02-26_Cholla256_50Mpc_stats_one_np_MM_10_90.png">
  <figcaption>Redshift evolution of median values of the variations the fraction of shared particle IDs in % and their estimated errors within 10 and 90 percentiles between direct progenitor halos found by <tt>Rockstar (RS)</tt> and connected by the descendant ID <tt>'DescID'</tt>. The dashed blue lines corresponds to the fraction of shared particle of the halo at certain snapshot SN(z) in comparison to the subsequent  SN(z+1) and the solid yellow line to the fraction of particles of the halo at certain snapshot SN(z+1) in comparison to the subsequent SN(z) of the halos on the main progenitor branch of <tt>treeID19</tt> test. 
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-02-26_Cholla256_50Mpc_stats_one_MM_10_90.png">
  <figcaption>Redshift evolution of median values of the variations of halo properties in % and their estimated errors within 10 and 90 percentiles between direct progenitor halos from <tt>treeID19</tt> found by <tt>Rockstar (RS)</tt> and connected by the descendant ID <tt>'DescID'</tt>. 
  </figcaption>
</figure>


<figure>
  <img src="{{ site.baseurl }}/plots/2021-02-26_Cholla256_50Mpc_stats_one_np_MM_MAD.png">
  <figcaption>Redshift evolution of median values of the variations the fraction of shared particle IDs in % and their estimated errors using the MAD between direct progenitor halos found by <tt>Rockstar (RS)</tt> and connected by the descendant ID <tt>'DescID'</tt>. The dashed blue lines corresponds to the fraction of shared particle of the halo at certain snapshot SN(z) in comparison to the subsequent  SN(z+1) and the solid yellow line to the fraction of particles of the halo at certain snapshot SN(z+1) in comparison to the subsequent SN(z) of the halos on the main progenitor branch of <tt>treeID19</tt>. 
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-02-26_Cholla256_50Mpc_stats_one_MM_MAD.png">
  <figcaption>Redshift evolution of median values of the variations of halo properties in % and their estimated errors using the MAD between direct progenitor halos from <tt>treeID19</tt> found by <tt>Rockstar (RS)</tt> and connected by the descendant ID <tt>'DescID'</tt>. 
  </figcaption>
</figure>
