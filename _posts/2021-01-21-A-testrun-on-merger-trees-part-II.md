---
layout: post
title: "A testrun on merger trees part II"
date: 2021-01-21 #Default format is yyyy.mm.dd
categories: mergertrees
---

This is the continuation of the post from <a href="https://dstoppacher.github.io/A-testrun-on-merger-trees/">2021-01-07</a>. The following questions are still open will be discussed in this post.

<ol>
  <li>Verify the approach of connection halos by the provided <tt>haloid</tt> and <tt>descID</tt> by comparing directly with the numbers of particle assigned to the halos between snapshots.</li>

  <li>How does <b>ROCKSTAR</b> assign the <tt>descID</tt> when running?</li>

  <li>Calculate halo mass function and accretion rates.</li>
 </ol>
 
 <hr class="fancyLine3">
 
 ### Merger tree verification
 
 In this analysis we scanned through the entire box of Cholla 256 with side-lenght 50$$h^{-1}$$Mpc and gathered all dark matter particle within a certain radius. Then we multiplied the number of particel $$n_{particle}$$ by the mass of one dark matter particle in the simulation being $$m_DM=5.407\times10^8$$ $$[h^{-1}M_{\odot}]$$. We compare this result with the halo mass the halo finder <b>ROCKSTAR</b> provided.
 
 <figure>
  <img src="{{ site.baseurl }}/plots/2021-01-21_.mhalo_offset.png">
  <figcaption>The figure visualizes the offset between the halos from merger tree with ID13 provided by <b>ROCKSTAR</b> in comparision what we can approximate when summing up dark matter particles within $$5\times$$ the virial radius $$R_{vir}$$.
  </figcaption>
</figure>
 
 
