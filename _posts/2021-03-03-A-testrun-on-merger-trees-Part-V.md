---
layout: post
title: "A testrun on merger trees Part 5"
date: 2021-03-03 #Default format is yyyy.mm.dd
categories: mergertrees
---

<blockquote><tt><b>Summary:</b> In this post we compare the redshift evolution of halo properties of main branch halos of the most massive halo in the simulation using descendant information from a halo finder directly and from a tree finder run on top. We found that there is little difference between the two approaches and that surprisingly less variation in e.g. the fraction of shared particle IDs between two snapshots was found (compare Fig. 3 and Fig. 4). However, if a tree builder is not used then the full redshift history of the particular halo might not be able to be traced (see Fig. 2).</tt></blockquote>

This is the continuation of the post from <a href="https://dstoppacher.github.io/A-testrun-on-merger-trees-4/">2021-02-26</a> were we showed results on the median variation of halo properties when following halos on the their main progenitor branch. Thereby we used only descendant information provided directly by the halo finder <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a>. In this post we compare our findings using this simplified approach with results when running the tree finder <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a>.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-03_MB-TreeID79509.png">
  <figcaption>Full merger tree and main branch only of most massive halo with top node <tt>treeID79509</tt>. The halo was found by <tt>Rockstar</tt> and the merger trees build by <tt>Consitent-Trees (CT)</tt>.
  </figcaption>
</figure>


<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-03_RS_vs_CT.png">
  <figcaption>Projection on X-Z axis of main branch of most massive halo. The red circles represent halos on the main branch if only<tt>Rockstar's (RS)</tt> descendant IDs were used to build the main branch and the colored dots the same information when <tt>Consistent-Trees (CT)</tt> was used to correct connections.
  </figcaption>
</figure>


<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-03_MB-TreeID79509_delta.png">
  <figcaption>Redshift evolution of the variation in the shared fraction of particle IDs in % between two halos found by <tt>Rockstar (RS)</tt> and connected by <tt>Consistent-Trees (CT)</tt>. The particle fractions are given in red (fraction of particle of the halo at certain snapshot SN(z) in comparison to the subsequent  SN(z+1)) and blue red (fraction of particle of the halo at certain snapshot SN(z+1) in comparison to the subsequent SN(z)) of the halos on the main branch of <tt>treeID79509</tt>.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-03_TreeID3_delta.png">
  <figcaption>Same as in Fig.4 but here the halos were connected only by the descendant ID provided directly by <tt>Rockstar</tt> and <tt>Consistent-Trees (CT)</tt> was NOT run on top. Interestingly our results show less variations in the fraction of shared particle IDs and halo mass for the most massive halo with the <tt>treeID3</tt>.
  </figcaption>
</figure>
