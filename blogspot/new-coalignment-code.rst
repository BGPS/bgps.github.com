New coalignment code
####################
:date: 2012-03-20 15:09
:author: Adam (noreply@blogger.com)
:tags: alignment

pixshift has been giving me issues for a long, long time. It finally
came to a head, though, when nothing I did could make l001 "work". It
turns out, when you do cross-correlation analysis, you're really only
interested in the most correlated pixel, NOT the junk around it - the
junk around it only provides a second-order correction.
Well, `cross\_cor\_taylor.pro`_, a tool from the solar physics
community, does exactly that. And it works far, far better than my
hacked-together pixshift code. A lesson I should always take to heart:
don't rewrite code if it's out there. Of course, if I'd known it was out
there, I wouldn't have rewritten it....
This is how good it looks now:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image0|`_

.. raw:: html

   </div>

(the circle has radius 6", or 1-sigma)

.. raw:: html

   </p>

.. _cross\_cor\_taylor.pro: http://solarmuri.ssl.berkeley.edu/~welsch/public/software/cross_cor_taylor.pro
.. _|image1|: http://2.bp.blogspot.com/--IDiMhSOWSg/T2idophFD3I/AAAAAAAAGxo/uwPBB9YWwrg/s1600/l029_align_to_reference.png

.. |image0| image:: http://2.bp.blogspot.com/--IDiMhSOWSg/T2idophFD3I/AAAAAAAAGxo/uwPBB9YWwrg/s320/l029_align_to_reference.png
.. |image1| image:: http://2.bp.blogspot.com/--IDiMhSOWSg/T2idophFD3I/AAAAAAAAGxo/uwPBB9YWwrg/s320/l029_align_to_reference.png
