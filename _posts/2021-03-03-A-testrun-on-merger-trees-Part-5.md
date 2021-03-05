
<blockquote><tt><b>Summary:</b> In this post we compare the redshift evolution of halo properties of main branch halos using descentend information firstly from a halo finder directly and secondly from a tree finder run on top. For this particular example of the most massive halo identified in both cases we found that there is little difference between the two approaches and that suprisingly less variation in the for example the fraction of shared particles in halos between two snaphsots was found (compare Fig. 3 and Fig. 4). However, if a tree builder is not run then the full redshift history of the particular halo might not be able to be traced as we showed in Fig. 2.</tt></blockquote>

This is the continuation of the post from <a href="https://dstoppacher.github.io/A-testrun-on-merger-trees-4/">2021-02-26</a> were we showed results on the median variation of halo properties when following halos on the their main progenitor branch. Thereby we used only descendent information provided directly by the halo finder <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10008B/abstract"><tt>Rockstar (RS)</tt></a>. In this post we compare our findings using this simplified approach with results when running the tree finder <a href="https://ui.adsabs.harvard.edu/abs/2012ascl.soft10011B/abstract"><tt>Consitent-Trees (CT)</tt></a>.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-03_MB-TreeID79509.png">
  <figcaption>Full merger tree and main branch only of most massive halo with top node rootIndex/treeID 79509. The halo was found by ROCKSTAR and the merger trees build by Consitent-Trees.
  </figcaption>
</figure>


<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-03_RS_vs_CT.png">
  <figcaption>Projection on X-Z axis of main branch of most massive halo. The red circles represent halos on the main branch if only ROCKSTAR's descendent IDs were used to build the main branch and the coloured dots the same information when Consistent-Trees was used to correct connections.
  </figcaption>
</figure>


<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-03_MB-TreeID79509_delta.png">
  <figcaption>Redshift evolution ofthe variation in the shared fraction of particle IDs in % between two halos found by ROCKSTAR and connected by Consitent-Trees. The particle fractions are given in red (fraction of particle of the halo at certain snapshot SN(z) in comparision to the subsequent  SN(z+1)) and blue red (fraction of particle of the halo at certain snapshot SN(z+1) in comparision to the subsequent SN(z)) of the halos on the main branch of rootIndex 79509.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-03-03_TreeID3_delta.png">
  <figcaption>Same as in Fig.4 but here the halos were connected only by the descendent ID provided directly by ROCKSTSTAR and Connsitent-Trees was NOT run on top. Interestingly our results show less variations in the fraction of shared particle IDs and halo mass for the most massive halo with the treeID3.
  </figcaption>
</figure>
