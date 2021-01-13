---
layout: post
title: "A testrun on merger trees"
date: 2021-01-07 #Default format is yyyy.mm.dd
categories: mergertrees
---

<blockquote><b>Summary:</b> In this post we study the redshift evolution of main progenitor halos in the Cholla simulation and show how we can easily construct merger trees of the same progenitor using two identification numbers provided by the halo finder itself.</blockquote>

### Objectives of this test run

In this test run we aim to test if we can produce a valid merger tree of the main progenitor halos using only

<ol>
  <li>the <b>ROCKSTAR</b> halo finder (<a href="https://ui.adsabs.harvard.edu/#abs/2013ApJ...762..109B">Behroozi et al. 2013a</a>) to identify the halos</li>

  <li>the descendant identification numbers (IDs) -- <tt>descIDs</tt> provided by <b>ROCKSTAR</b> to link halos between snapshots. This ID represents the ID of the same halo in the next snapshot (moved forward in time).</li>
</ol>

These merger tree will only use the <tt>descID</tt> to make a connection between halos as a simple approach. Note that no tree builder algorithm was used therefore the merger tree was not fixed for e.g. missing links between snapshots or filling and correcting missing halos. See <a href="https://ui.adsabs.harvard.edu/#abs/2013ApJ...763...18B">Behroozi et al. 2013b</a> for details on that topic.

### Task overview

<ol>
  <li>Run <b>ROCKSTAR</b> on the <b>Cholla</b> simulation (<a href="https://ui.adsabs.harvard.edu/abs/2015ApJS..217...24S">Schneider &amp; Robertson 2015</a>, <a href="https://ui.adsabs.harvard.edu/abs/2020arXiv200906652V">Villase&ntilde;or et al. 2020</a>) (box with 50\\h^{-1}\\Mpc side-length)</li>

  <li>Convert ASCII output files of Rockstar which are named as <small><tt>out[snapshot].list</tt></small>  into a custom HDF5 format.</li>

  <li>Use the <tt>haloid</tt> (ID of a certain halo in this snapshot) and the <tt>descIDs</tt> (the ID of the same halo in the next snapshot) to link a halo between snapshots.</li>

  <li>Introduce to more IDs which form together with the <tt>haloid</tt> and <tt>descIDs</tt> a set of IDs which identifies a certain halo uniquely within the entire merger tree and at every snapshot. Those are the <tt>predID</tt> (the ID of the same halo a snapshot one step back in time) and the <tt>treeID</tt> (an ascending counter assigned when the very first halo in the merger tree was detected. The lower the number the earlier the first progenitor was detected!) of the tree the halo sits on.</li>

  <li>Construct a merger tree using the set of four IDs <tt>[haloid,descID,predID,treeID]</tt>.</li>

  <li>Validate the merger tree with comparing the number of particles found for a certain halo.</li>
</ol>

#### Task1: Find halos!

Run the <b>ROCKSTAR</b> halo finder catalog <a href="https://ui.adsabs.harvard.edu/#abs/2013ApJ...762..109B">Behroozi et al. 2013a</a> on the Colla particle simulation box with side-length 50 $$h^{-1}$$Mpc.

<small><tt>Status:</tt>&nbsp;<i class="fa fa-check-square-o" aria-hidden="true"></i>&nbsp;<b>Task completed </b></small>

<hr class="fancyLine3">

#### Task2: Convert raw output from ROCKSTAR to custom file format

Thereby the units of <small><tt>kpc</tt></small> were converted to <small><tt>Mpc</tt></small> and the Hubble parameter absorbed in the value of the halo property.

<small><tt>Status:</tt>&nbsp;<i class="fa fa-check-square-o" aria-hidden="true"></i>&nbsp;<b>Task completed </b></small>

<hr class="fancyLine3">

#### Task3: Link the halos between the snapshots

In this section we show that with the combination of <tt>haloid</tt> and <tt>descID</tt> which were provided by the <b>ROCKSTAR</b> as standard outputs the main progenitors (also the most massive progenitors) can be traced easily back and fourth in redshift.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-01-07_Tree3.png">
    <figcaption>The tables in this figure show lists of halo properties over four subsequent snapshots <tt>SN21</tt> to <tt>SN24</tt>. In each table a particular halo is selected with the initial <tt>haloid</tt> of <tt>3</tt>. This halo can be traced from one snapshot to another by comparing the <tt>haloid</tt> with the <tt>descID</tt>. Thereby the <tt>descID</tt> of e.g. <tt>SN21</tt> for this halo is <tt>29</tt> which corrsponds to the <tt>haloid</tt> of the same halo in the next snapshot <tt>SN22</tt>. The <tt>treeID</tt> of the halo in this example is <tt>3</tt> which means that is was the third tree ever identified. This ID stays for all progenitors on the tree of this particular halo. If a new halo is identified in another snapshot with no progenitor, the <tt>treeID</tt> for this tree is simply assigned with <tt>+1</tt> of the last identified progenitor tree.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-01-07_test_cube_SN21-23.png">
  <figcaption>In this cube visualize the location of the halos from Table 1 above for three subsequent snapshots. The halos in our initial snapshot <tt>SN21</tt> are marked with a red cross. One can see that their progenitors can be clearly identified at the same location (<i>blue</i> circles for <tt>SN22</tt> and <i>green</i> dots for <tt>SN23</tt>). If a halo was not already identified at <tt>SN21</tt> or <tt>SN22</tt>, so its was newly found in the current snapshot it is only marked with a blue circle or a green dot, respectively.
  </figcaption>
</figure>

<figure>
  <img src="{{ site.baseurl }}/plots/2021-01-07_test_cube_SN21-24+51.png">
    <figcaption>Same as Figure 1 but the main progenitor halos at snapshot <tt>SN51</tt> at z=0.81 are also visualized.
  </figcaption>
</figure>

<small><tt>Status:</tt>&nbsp;<i class="fa fa-check-square-o" aria-hidden="true"></i>&nbsp;<b>Task completed </b></small>

<hr class="fancyLine3">

### Task3: Construct a merger tree of the main progenitors

After providing that we identify the correct halos when linking <tt>haloid</tt> and <tt>descID</tt> for each snapshot we can construct a simple merger tree considering the main progenitor halos.

<figure>
  <img src="{{ site.baseurl }}/plots/2021-01-07_diverse_merger_trees.png">
    <figcaption>The figure shows the location of all progenitors (progs) from selected trees (<i>pink</i> dots) from <tt>SN21</tt> to <tt>SN51</tt> at z=0.81 (the final snapshot for this test run was set arbitrarily). Various main progenitor are highlighted by their color coding corresponding to the <tt>treeID</tt>. Thereby our example form Figure 1 is represented by <i>salmon</i> dots. Some tree are marked extra with two color circles which represents their position at redshift z=2.03 (<i>green</i> circle) and z=0.81 (<i>gray</i> circle). If there are no circle in a certain tree that means that it did not exits at that snapshot anymore.
  </figcaption>
</figure>

<small><tt>Status:</tt>&nbsp;<i class="fa fa-check-square-o" aria-hidden="true"></i>&nbsp;<b>Task completed </b></small>

<hr class="fancyLine3">

### Follow-up task & open questions

<ol>
  <li>Verify the approach of connection halos by the provided <tt>haloid</tt> and <tt>descID</tt> by comparing directly with the numbers of particle assigned to the halos between snapshots.</li>

  <li>How does <b>ROCKSTAR</b> assign the <tt>descID</tt> when running?</li>

  <li>Calculate halo mass function and accretion rates.</li>
 </ol>



