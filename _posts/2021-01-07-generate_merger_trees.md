---
layout: post
title: ""
date: 2021-01-07 #Default format is yyyy.mm.dd
categories: mergertrees
---

## Objectives of this testrun

In this testrun we aim to test if we can produce a valid merger tree of the main progenitor halos using only

1) the <b>Rockstar</b> halo finder (<a href="https://ui.adsabs.harvard.edu/#abs/2013ApJ...762..109B">Behroozi et al. 2013a</a>) to identify the halos

2) the descendent identification numbers (IDs) -- <tt>descIDs</tt> provided by <b>Rockstar</b> to link halos between snaphots.

These merger tree will only use the descID to make a connection between halos as a simple approach. Note that no tree builder alorithm was used therefore the merger tree was not fixed for e.g. missing links between snapshots or filling and correcting missing halos. See <a href="https://ui.adsabs.harvard.edu/#abs/2013ApJ...763...18B">Behroozi et al. 2013b</a> for details on that topic.

### Task overview

1) Run <b>Rockstar</b> on the <b>Cholla</b> simulation (<a href="https://ui.adsabs.harvard.edu/abs/2015ApJS..217...24S">Schneider &amp; Robertson 2015</a>, <a href="https://ui.adsabs.harvard.edu/abs/2020arXiv200906652V">Villase&ntilde;or et al. 2020</a>) (box with 50 $$h-1$$Mpc side-length)

2)

2) Milestone 2: Connect the hydro simulation with the dark matter only simulation


### Task1: Find halos!

Run the Rockstar halo finder catalog (Behroozi et. al 2013) on the Colla particle simulation box with side-lenght 50 $$h-1$$Mpc.\\

Status: Tasked completed 

### Task2: Link the halos between the snapshots

<img src="{{ site.baseurl }}/plots/2021-01-07_Tree3.png">

<img src="{{ site.baseurl }}/plots/2021-01-07_test_cube_SN21-23.png">

<img src="{{ site.baseurl }}/plots/2021-01-07_test_cube_SN21-24+51.png">

### Task3: Conctruct a merger tree of the main progenitors

<img src="{{ site.baseurl }}/plots/2021-01-07_diverse_merger_trees.png">


### Task4: Calculate halo mass function and accrection rates




