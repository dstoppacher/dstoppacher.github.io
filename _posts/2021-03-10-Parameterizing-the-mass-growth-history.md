---
layout: post
title: "Parameterizing the mass growth history"
date: 2021-03-10 #Default format is yyyy.mm.dd
categories: mergertrees
---

<blockquote><tt><b>Summary:</b> We use a one parameter model form <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> to parametrize the mass growth history of the main progenitor branch of a merger tree. </tt></blockquote>

We use the approach of <a href="https://ui.adsabs.harvard.edu/abs/2002ApJ...568...52W/abstract">Wechsler et al. 2002</a> and their Eq.5:

$$ M(a) = M_0  exp  \Bigg( -a_0*S(a_0/a - 1)  \Bigg) $$

to parametrize the halo mass growth history. In Fig. 1 we use this parametrization and compare to the mass accrection history of the main branch progenitor halo tracked by <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt>. Thereby we use the halo mass at the last snapshot the halo was detected as $$M_0$$ in the funciton.
  
  we show the  This is the continuation of the post from <a href="https://dstoppacher.github.io/A-testrun-on-merger-trees-4/">2021-02-26</a> were we showed results on the median variation of halo properties when following halos on the their main progenitor branch. Thereby we used only descendant information provided directly by the halo finder <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a>. In this post we compare our findings using this simplified approach with results when running the tree finder <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consistent-Trees (CT)</tt></a>.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-03_test.png">
  <figcaption>Full merger tree and main branch only of most massive halo with top node <tt>TreeID79509</tt>. The halo was found by <tt>Rockstar</tt> and the merger trees build by <tt>Consitent-Trees (CT)</tt>.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-10_test2.png">
  <figcaption>Full merger tree and main branch only of most massive halo with top node <tt>TreeID79509</tt>. The halo was found by <tt>Rockstar</tt> and the merger trees build by <tt>Consitent-Trees (CT)</tt>.
  </figcaption>
</figure>
