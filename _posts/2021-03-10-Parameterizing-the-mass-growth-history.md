---
layout: post
title: "Parameterizing the mass growth history"
date: 2021-03-10 #Default format is yyyy.mm.dd
categories: mergertrees
---

<blockquote><tt><b>Summary:</b> We use a one parameter model from <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> to parameterize the mass assembly history of the main progenitor branch of a merger tree or the most massive progenitor of a halo, respectively. </tt></blockquote>

### Background

We use the approach of <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> and their Eq.4 and Eq.5, respectively:

$$ a_c= a_0 \alpha/S \text{  (1)}$$

$$ M(a) = M_0 \times \exp  \Big[ -a_c S \big(a_0/a - 1\big)  \Big] \text{  (2)}$$

to parametrize the halo mass growth history. $$\alpha$$ is the singe free parameter in the model and can be related to a characteristic epoch of formation $$a_c$$. $$a_c$$ is defined as the expansion factor $$a$$ when the logarithmic slope of the accretion rate $$d\log M/d\log a$$ falls below some specified value $$S$$. $$S$$ is connected via $$a_c$$ to the singe free parameter $$\alpha$$ as $$a_c=\alpha/S$$. In the same way the formation epoch is defined for any "observing" epoch $$z_0$$ by replacing $$a$$ by $$a/a_0$$ to find Eq.(1).

At any observing redshift $$z_0$$ with the scale factor $$a_0=1/(1+z_0)$$ and the mass of the halo $$M_0=M(z_0)$$ the mass growth is fit by Eq.(2). For more details please see Sec.4 in <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a>.

In <b>Fig.1</b> we compare the parameterized mass accretion history using $$M_0$$ as the halo mass our main progenitor halo <tt>CT-ID79509</tt> found by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a> and tracked by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a> holds at the snapshot of last detection. More details about this particular tree can be found in <b>Fig.1</b> and <b>Fig.2</b> our previous post from <a href="https://dstoppacher.github.io/A-testrun-on-merger-trees-4/">2021-03-03</a>. We further us $$S=2$$, and $$\alpha=1.33$$ in the Eq.(1) and Eq.(2).

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-10_test.png">
  <figcaption>Mass accretion history of the main branch halo with top node ID <tt>CT-ID79509</tt> as solid blue line and parameterized using Ep.5 in <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> as dashed black line. The halo was found by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a> and the merger trees build by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a>.
  </figcaption>
</figure>

### Parameterization Test with using custom-built trees & Consitent-Trees

In the <b>Fig.2</b> we show various visually inspected mass assembly histories of the main progenitor trees found by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a> (solid colored lines) in comparison to the assembly history of <tt>CT-ID79509</tt> and various the parameterized functions using $$M_0=1 \times 10^{14}$$ $$[h^{-1}M_{\odot}]$$, $$S=2$$, and values for $$\alpha$$ as indicated in <b>Fig.2</b>. In <b>Fig.3</b> we show the median mass accretion history within uncertainties for all identified halos and their most massive progenitors.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-10_test2.png">
  <figcaption>Compilation of visual inspected main progenitor trees found by <tt>Rockstar (RS)</tt> (solid colored lines) in comparison to the parameterized function using Ep.5 in <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> using various values for the parameter alpha (solid, dashed, and dotted black lines).
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-10_test_median.png">
  <figcaption>Median mass accretion history incorporating all halos and their most massive progenitor identified in the simulation with <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a>  (solid red line, the shaded region represents the median absolute deviation) parameterized using Ep.5 in <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> and various values for the free parameter alpha (solid, dashed, and dotted black lines).
  </figcaption>
</figure>

### Parameterization Test using only trees from Consitent-Trees

Here we show plots using the merger tree information from Consiten-Trees. In Fig. 5 we show the posistions of all halos found by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a> and tracked by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a> in the 3D-box of Cholla-256 with a side-lenght of 50$$h^{-1}$$Mpc. In Fig.6 and Fig.7we show in the redshift evolution of the position of selected mergertrees from the same box, among them the most massive (CT-ID79509), largest (CT-ID79622) and the least massive trees (CT-ID79224).

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-11_all_CT.png">
  <figcaption>Redshift evolution of the positions of all halos and their corresponding trees found by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a>  and tracked by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a> from the Cholla-256 simulation with a side-lenght of 50$$h^{-1}$$Mpc. The scale factor of each snapshot is represented by the colorbar.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-11_selected_CT.png">
  <figcaption>Redshift evolution of the positions of selected merger trees tracked by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a> from the Cholla-256 simulation with a side-lenght of 50$$h^{-1}$$Mpc. The scale factor of each snapshot is represented by the colorbar.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-11_selected_indv_color_CT.png">
  <figcaption>Positions of selected merger trees tracked by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a> from the Cholla-256 simulation with a side-lenght of 50$$h^{-1}$$Mpc$$, among them the most massive (CT-ID79509), largest (CT-ID79622) and the least massive trees (CT-ID79224) as indicated by the colors.
  </figcaption>
</figure>


<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-16_selected_traj_CT.png">
  <figcaption>Redshift evolution of the positions of four selected merger trees shown in Fig.8 tracked by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a> from the Cholla-256 simulation with a side-lenght of 50$$h^{-1}$$Mpc. The scale factor of each snapshot is represented by the colorbar. Their main branch is marked by a black open cycle.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-16_Parameterization_Test_selected_CT.png">
  <figcaptionP>arameterized function of our selected merger trees from Fig.8 using Ep.5 in <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> using various values for the parameter alpha and M_0 (solid, dashed, and dotted black lines).
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-15_Parameterization_Test_CT.png">
  <figcaption>Median mass accretion history incorporating all halos and their most massive progenitor identified in the simulation with <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a>  and the merger trees build by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a> (solid red line, the shaded region represents the median absolute deviation) parameterized using Ep.5 in <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> and various values for the free parameter alpha (solid, dashed, and dotted black lines).
  </figcaption>
</figure>

A <i>Python</i> script which creates the figures in this post can be found <a href="https://dstoppacher.github.io/python_scripts/2021-03-10_Parameterization_test.py"><tt>here</tt></a>
