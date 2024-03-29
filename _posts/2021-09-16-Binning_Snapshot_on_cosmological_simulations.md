---
layout: post
title: "Snapshot Binning Schemes of Cosmological Simulations"
date: 2021-09-16 #Default format is yyyy.mm.dd
categories: simulations
---

<blockquote><tt><b>Summary:</b> We compare snapshot binning schemes of multiple cosmological simulation in order to explain the "dip" in the particle fractions of 256-Cholla .</tt></blockquote>

### Simulations

We compare the binning schemes of snapshot numbers and redshifts for various cosmological simulations such as Cholla <tt>256-Cholla</tt> (<a href="https://ui.adsabs.harvard.edu/abs/2015ApJS..217...24S">Schneider &amp; Robertson 2015</a>, <a href="https://ui.adsabs.harvard.edu/abs/2020arXiv200906652V">Villase&ntilde;or et al. 2020</a>) and the <tt>3840-VSMDPL</tt> (<a href="https://arxiv.org/abs/1411.4001">Klypin et al. 2016</a>). In our post from <a href="https://dstoppacher.github.io/Shared-particle-fractions-in-direct-progenitors/">2021-09-13</a> we found that there are two pominent dips in the shared particle fractions of direct progenitor halos at $$z=1$$ and $$z=2$$ (see Figure 5).

### Snapshot identification number vs. redshift

<figure>
  <img src="{{ site.baseurl }}/plots/2021-09-14_DM-simulation_z-SN-relation_zoom-out.png">
  <img src="{{ site.baseurl }}/plots/2021-09-14_DM-simulation_z-SN-relation.png">
  <figcaption>Snapshot number to redshift relation for various cosmological simulations Top: total redshift range available is shown and Bottom: zoom-in. The Cholla simulation has a visibly disconutiny between the snapshot number and the redshift which cannot be found in any other cosmological simulation tested. 
  </figcaption>
</figure>

### Does that affect the growth history of halo properties?

It seems that the halo masses $$M_{vir}$$ (top), the maximum velocities $$V_{max}$$ (middle), and certain radii (bottom panel of Figure 2) is not affected by the discontinuity, however it is not clear if the mass accrection history of the halo mass would as we saw in e.g. Figure 2 or Figure 4 in <a href="https://dstoppacher.github.io/A-testrun-on-merger-trees-part-IV/">previous posts</a>.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-09-13_merger_trees_CT_mvir.png">
  <img src="{{ site.baseurl }}/plots/2021-09-13_merger_trees_CT_vmax.png">
  <img src="{{ site.baseurl }}/plots/2021-09-13_merger_trees_CT_radii.png">
  <figcaption>Redshift evolution of median values of halo properties. Top: halo mass $$M_{vir}$$, middle: max velocity $$V_{max}$$, and bottom: various radii. 
  </figcaption>
</figure>


