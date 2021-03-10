---
layout: post
title: "Parameterizing the mass growth history"
date: 2021-03-10 #Default format is yyyy.mm.dd
categories: mergertrees
---

<blockquote><tt><b>Summary:</b> We use a one parameter model form <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> to parametrize the mass assembly history of the main progenitor branch of a merger tree. </tt></blockquote>

We use the approach of <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> and their Eq.4 and Eq.5, respectively:

$$ a_c= a_0 \alpha/S $$

$$ M(a) = M_0 \times \exp  \Big[ -a_c S \big(a_0/a - 1\big)  \Big] $$

to parametrize the halo mass growth history. In Fig. 1 we compare the parametrizied mass accrection history using $$M_0$$ as the halo mass our main progenitor halo <tt>TreeID79509</tt> tracked by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a> holds at the snaphost of last detection and the parameter $$S=2$$ and $$\alpha=1.33$$ as suggested by the authors with the main branch progenitor. The merger tree and the main progentiors branch can be found also in Fig. 1 and Fig. 2 in the post from <a href="https://dstoppacher.github.io/A-testrun-on-merger-trees-4/">2021-03-23</a> we use the halo mass at the last snapshot the halo was detected as $$M_0$$ and S=2 and $$\alpha=1.33$$in the function.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-10_test.png">
  <figcaption>Mass accreaction history of the main branch halo with top node ID <tt>CT-ID79509</tt> as solid line and parameterizised using Ep.5 in <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a>. The halo was found by <tt>Rockstar (RS)</tt> and the merger trees build by <tt>Consitent-Trees (CT)</tt>.
  </figcaption>
</figure>

In the Fig.2 we show various mass assembly histories of the main progenitor trees found by <tt>Rockstar (RS)</tt> (solid colored lines) in comparision with the main brach tree from Fig. 1 <tt>CT-ID79509</tt> and the paramerized function using $$M_0=1 \times 10^{14}$$, $$a_0=1$$, S=2, and $$\alpha=1.33$$.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-10_test2.png">
  <figcaption>Compilation of visual inspected main progenitor trees found by <tt>Rockstar (RS)</tt> (solid colored lines) in comparision to the parameterized function using Ep.5 in <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a>.
  </figcaption>
</figure>
