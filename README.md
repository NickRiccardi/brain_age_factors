This repository provides a simple Python script to compute factor scores based on regional brain age gap data. The scoring weights are derived from an exploratory factor analysis (EFA) using SPSS with regression-based scoring and Varimax rotation.

The approach is based on volBrain’s Brain Structure Ages pipeline, using brain age gap values (i.e., brain age minus chronological age) for individual brain regions as input.

In addition to the scoring weights, the script uses region-specific means and standard deviations from our reference cohort (N=188) to standardize your input data before applying the factor scoring coefficients. This ensures consistency with the original scale used to derive the factors. If you have a large enough dataset, you can modify this to calculate it based on the means and standard deviations of your own data.
