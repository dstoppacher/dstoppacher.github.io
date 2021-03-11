---
layout: post
title: "Parameterizing the mass growth history"
date: 2021-03-10 #Default format is yyyy.mm.dd
categories: mergertrees
---

<blockquote><tt><b>Summary:</b> We use a one parameter model from <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> to parameterize the mass assembly history of the main progenitor branch of a merger tree or the most massive progenitor of a halo, respectively. </tt></blockquote>

We use the approach of <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> and their Eq.4 and Eq.5, respectively:

$$ a_c= a_0 \alpha/S \text{  (1)}$$

$$ M(a) = M_0 \times \exp  \Big[ -a_c S \big(a_0/a - 1\big)  \Big] \text{  (2)}$$

to parametrize the halo mass growth history. In <b>Fig.1</b> we compare the parameterized mass accretion history using $$M_0$$ as the halo mass our main progenitor halo <tt>CT-ID79509</tt> found by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a> and tracked by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a> holds at the snapshot of last detection. More details about this particular tree can be found in <b>Fig.1</b> and <b>Fig.2</b> our previous post from <a href="https://dstoppacher.github.io/A-testrun-on-merger-trees-4/">2021-03-03</a>. We further us $$S=2$$, and $$\alpha=1.33$$ in the equations (1) and (2).

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-10_test.png">
  <figcaption>Mass accretion history of the main branch halo with top node ID <tt>CT-ID79509</tt> as solid blue line and parameterized using Ep.5 in <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> as dashed black line. The halo was found by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a> and the merger trees build by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a>.
  </figcaption>
</figure>

In the <b>Fig.2</b> we show various visually inspected mass assembly histories of the main progenitor trees found by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a> (solid colored lines) in comparison to the assembly history of <tt>CT-ID79509</tt> and various the paramerized functions using $$M_0=1 \times 10^{14}$$ $$[h^{-1}M_{\odot}]$$, $$S=2$$, and values for $$\alpha$$ as indicated in <b>Fig.2</b>.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-10_test2.png">
  <figcaption>Compilation of visual inspected main progenitor trees found by <tt>Rockstar (RS)</tt> (solid colored lines) in comparison to the parameterized function using Ep.5 in <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> using various values for the parameter alpha (solid, dashed, and dotted black lines).
  </figcaption>
</figure>
