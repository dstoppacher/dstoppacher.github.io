---
layout: post
title: "A testrun on merger trees part IV"
date: 2021-02-26 #Default format is yyyy.mm.dd
categories: mergertrees
---

<blockquote><tt><b>Summary:</b>Here we show the median variation of halo properties of main branch halos connected by the descendant information provided by a halo finder without running a tree builder on top of it. The median variations of the halo properties are shown within different uncertainty levels.</tt></blockquote>

This is the continuation of the post from <a href="https://dstoppacher.github.io/A-testrun-on-merger-trees-III/">2021-02-22</a>. Thereby we use only descendant information as the <tt>'DescID'</tt> provided directly by the halo finder <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a>. we show the redshift  between halos of different snapshots connected by the desctant ID provided by <tt>Rockstar</tt> as a standard output. We show in Fig. 1 the median values of variation of shared fraction of particle IDs with in 10 and 90^{-1

<figure>
  <img src="{{ site.baseurl }}/plots/2021-02-26_Cholla256_50Mpc_stats_one_np_MM_10_90.png">
  <figcaption>Median values with in 10 and 90 percentiles of the redshift evolution of the variation in the shared fraction of particle IDs in % between two halos found by <tt>Rockstar (RS)</tt> and connected by the descendant ID <tt>'DescID'</tt>. The particle fractions are given in dashed blue (fraction of particle of the halo at certain snapshot SN(z) in comparison to the subsequent  SN(z+1)) and in solid yellow (fraction of particle of the halo at certain snapshot SN(z+1) in comparison to the subsequent SN(z)) lines of the halos on the main branch of <tt>treeID19</tt>. 
  </figcaption>
</figure>
