# Named-export forwarding evidence

before.json and after.json are unmodified graph.json outputs from actual CLI runs over source/.
The base is upstream 937e59a5476fcb2665d6c4f4b7c0d0a4142011b6.
The candidate contains only explicit export-origin resolution and its tests.
Both runs use extract --code-only --no-cluster --max-workers 1.
stdout and stderr are preserved per run.
The receipt records hashes and missing endpoint checks.
raw-graph-audit.png is an offline Pillow report rendered from these raw outputs, not a browser or Graphify viewer screenshot.
render_report.py reproduces that report on macOS with Pillow and Arial.
The existing browser capture denial was respected; no alternate browser or HTTP routing was attempted.
