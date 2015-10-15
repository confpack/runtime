Confpack Runtime Vendor Libraries
=================================

Instead of using PIP, we vendor the libraries here because we want to ensure
that all installation scripts can use the SAME version of templating, and other
libraries.

We also require that python is >=2.7 but <2.8 for now. This should mean there
are minimal deviations from distribution to distribution.

To update all the vendored library, check out the Makefile

