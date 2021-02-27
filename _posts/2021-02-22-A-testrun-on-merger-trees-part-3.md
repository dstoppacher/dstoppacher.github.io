
This is the continuation of the post from <a href="https://dstoppacher.github.io/A-testrun-on-merger-trees/">2021-01-21</a>. The following questions are still open will be discussed in this post. Our main goal is to investigate wether the descendent information <tt>DescID</tt> in the <b>ROCKSTAR</b> (<a href="https://ui.adsabs.harvard.edu/#abs/2013ApJ...762..109B">Behroozi et al. 2013a</a>) standard output can be used to correctlyc track the halo on the main progenitor tree. To investigate that we use here particle data from the cosmological simulation <b>Cholla</b> (<a href="https://ui.adsabs.harvard.edu/abs/2015ApJS..217...24S">Schneider &amp; Robertson 2015</a>, <a href="https://ui.adsabs.harvard.edu/abs/2020arXiv200906652V">Villase&ntilde;or et al. 2020</a>) where <b>ROCKSTAR</b> was run on top of it between redshift $$0<z<6$$ (divided into 194 snapshots).

We show in the Fig.1 we show the fraction of shared particles (measured according to the unique particle ID) found in two halos which are connecet by their <tt>DescID</tt> for the first appeasing eight halos (<tt>0<treeIDs<7\tt>) and their direct progenitors. In Fig. 2 the fractional difference in the halo mass for the same <tt>treeIDs<\tt> and in Fig.3 and Fig.4 the corresponding growth rate function of redshifts for the virial mass $$M_{vir}$$ and the virial radius $$R_{vir}$$. 

<figure>
  <img src="{{ site.baseurl }}/plots/2021-02-22_Cholla-256_n_particles_shared1.png">
  <figcaption>Fraction of particles shared (according to their IDs) between two snapshots for eight example trees constructed by following the <b>ROCKSTAR</b> descendant ID 'DescID' as a function of redshift. At first 90% of the particles are present in halos connected by their 'DescID' later the fraction drops rapidly. That leads to the conclusion that not the correction progenitors had be tracked. However, there is also the possibility that a mergering or stripping event happened.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-02-22_Cholla-256_mhalo1_frac.png">
  <figcaption>Fractional difference in halo mass as a function of redshift for the first eight halos and their main progenitors appeared in the simulation.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-02-22_Cholla-256_mhalo1_gr.png">
  <figcaption>
    Growth history of the viral halo mass Mvir for the first eight halos and their main progenitors appeared in the simulation.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-02-22_Cholla-256_rvir1_gr.png">
  <figcaption>
        Growth history of the virial radius Rvir for the first eight halos and their main progenitors appeared in the simulation.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-02-22_Cholla-256_500_halos_all_SN.png">
  <figcaption>
    Redshift evolution and variation in the positions of the first 500 halos and their main progenitors appeared in the simulation. From this point of view the tracking of the progenitors seems correct.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-02-22_Cholla-256_treeID3.png">
  <figcaption>
        Redshift evolution and variation in the positions of the halo asigned the treeID=3 and their main progenitors. The variation in the position and location of the halo is reasonable.
  </figcaption>
</figure>


<figure>
  <img src="{{ site.baseurl }}/plots/2021-02-22_Cholla-256_treeID3_YZ.png">
  <figcaption>
    Same as in the privious figure but here the projection on the Y-Z axes is shown.
  </figcaption>
</figure>


<figure>
  <img src="{{ site.baseurl }}/plots/2021-02-22_Cholla-256_treeID3_XZ.png">
    Same as in the privious figure but here the projection on the X-Z axes is shown.
  <figcaption>
  </figcaption>
</figure>
