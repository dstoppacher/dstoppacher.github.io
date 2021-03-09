---
layout: post
title: "A testrun on merger trees part V"
date: 2021-03-03 #Default format is yyyy.mm.dd
categories: mergertrees
---

<blockquote><tt><b>Summary:</b> In this post we compare the redshift evolution of halo properties using descendant information from a halo finder directly and from a tree finder run on top. We found that there is little difference between the two approaches and that surprisingly less variation in e.g. the fraction of shared particle IDs between two snapshots was found (compare Fig. 3 and Fig. 4). However, if a tree builder is not used then the full redshift history of the particular halo might not be traced correctly (see Fig. 2).</tt></blockquote>

This is the continuation of the post from <a href="https://dstoppacher.github.io/A-testrun-on-merger-trees-4/">2021-02-26</a> were we showed results on the median variation of halo properties when following halos on the their main progenitor branch. Thereby we used only descendant information provided directly by the halo finder <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a>. In this post we compare our findings using this simplified approach with results when running the tree finder <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a>.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-03_MB-TreeID79509.png">
  <figcaption>Full merger tree and main branch only of most massive halo with top node <tt>TreeID79509</tt>. The halo was found by <tt>Rockstar</tt> and the merger trees build by <tt>Consitent-Trees (CT)</tt>.
  </figcaption>
</figure>


<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-03_RS_vs_CT.png">
  <figcaption>Projection on X-Z axis of main branch of most massive halo. The red circles represent halos on the main branch if only <tt>Rockstar's (RS)</tt> descendant IDs were used to build the main branch and the colored dots the same information when <tt>Consistent-Trees (CT)</tt> was used to correct connections.
  </figcaption>
</figure>


<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-03_MB-TreeID79509_delta.png">
  <figcaption>The variation in the shared fraction of particle IDs between two direct progenitor halos found by <tt>Rockstar (RS)</tt> and connected by <tt>Consistent-Trees (CT)</tt>. The fraction of particle IDs of a halo at a certain snapshot SN(z) in comparison to the fraction found in the direct progenitor at the subsequent SN(z+1)) is given in red and the fraction of particle IDs of the direct progenitor at certain snapshot SN(z+1) in comparison to the halo at SN(z) in blue for the main branch halos with <tt>TreeID79509</tt>.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-03_TreeID3_delta.png">
  <figcaption>Same as in Fig.4 but here the halos were connected only by the descendant ID <tt>descID</tt> provided directly by <tt>Rockstar</tt>. Interestingly our results show less variations in the fraction of shared particle IDs and halo mass for the most massive halo found in our simulation <tt>treeID3</tt> (Note that this halo is not the same as in Fig. 3).
  </figcaption>
</figure>

Possible reason of uncertainties might be:

<ul class="post-list">
  <li>the resolution of the simulation (only $$256^3$$ particles in a box of 50$$h^{-1}$$Mpc)</li>
  <li>too large time steps between simulation</li>
  <li>parameter using for <tt>Consitent-Trees</tt> were not particularly chosen but the default setting used</li>
</ul>


