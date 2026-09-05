# Dynamic import rescue evidence

This directory contains the reviewed before and after CLI screenshots, a portable three-file fixture, and a reproduction script.

The screenshots were captured from the exact base commit `33362d9` and candidate commit `2236f54`.
The base reports a false edge from text in comments, strings, and template text.
The candidate reports only the executable dynamic import edge.

To reproduce, provide checkouts at both commits:

```sh
BASE_CHECKOUT=/path/to/graphify-33362d9 \
CANDIDATE_CHECKOUT=/path/to/graphify-2236f54 \
PYTHON=python \
./REPRODUCE.sh
```

The output should show the base with `false_dep` and `real_dep`, and the candidate with `real_dep` only.
