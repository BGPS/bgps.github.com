Simulations - Towards a Spatial Transfer Function
#################################################

:date: 2013-01-15 11:23
:tags: simulation, stf
:category: simulation, stf
:author: Adam Ginsburg

The :math:`alpha=-1` power law is the only one that seems to have even mildly
reasonable recovery; the others recover <50% of the power at *any* scale.

Is this what I saw in the original STFs?  Examining exp10 again, sky04 is the
first with a reasonable amount of recovery, and that did have a power of -1.
So it looks like I knew about this and just got the #'s wrong.

This is approximately what an STF sim should look like:

.. /Volumes/disk3/adam_work/artificial_sims/exp21_spatial_transfer_function/exp21_ds2_astrosky_arrang45_atmotest_amp3.2E-02_sky02_seed00_peak001.00_smooth_psds.png
.. image:: static/images/exp21_ds2_astrosky_arrang45_atmotest_amp3.2E-02_sky02_seed00_peak001.00_smooth_psds.png
   :width: 800


I'm still not entirely clear why there is an excess power loss at the angular scales the BGPS should
recover for power laws steeper than about 1.  The power spectra show major loss:

.. /Volumes/disk3/adam_work/artificial_sims/exp10_spatial_transfer_function/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E+01_sky03_seed00_peak010.00_smooth_scandir1_psds.png
.. image:: static/images/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E+01_sky03_seed00_peak010.00_smooth_scandir1_psds.png
   :width: 800

and in the comparison images, it's clear that there is missing information, but it's not clear on what scales

.. /Volumes/disk3/adam_work/artificial_sims/exp10_spatial_transfer_function/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E+01_sky03_seed00_peak010.00_smooth_compare.png
.. image:: static/images/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E+01_sky03_seed00_peak010.00_smooth_compare.png
   :width: 800

