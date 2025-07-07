This repository provides a simple Python script to compute factor scores based on regional brain age gap data. The scoring weights are derived from an exploratory factor analysis (EFA) using SPSS with regression-based scoring and Varimax rotation.

The approach is based on volBrain’s Brain Structure Ages pipeline, using brain age gap values (i.e., brain age minus chronological age) for individual brain regions as input.

Your input .csv file should contain one row per subject and one column per brain region, with brain age gap values (not raw brain ages). An optional SubjectID column will be retained in the output.
