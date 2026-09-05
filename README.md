# Graphify declaration ownership evidence

These are real code-only CLI extractions of the four synthetic files in `source/`.
The upstream base is `937e59a5476fcb2665d6c4f4b7c0d0a4142011b6`.
The fixed revision is `dcd9a7ee2d546fbc56168e3e536a6bae36ac7eac`.

| Output | Nodes | Edges | Missing source endpoints |
| --- | ---: | ---: | ---: |
| Before | 12 | 24 | 2 |
| After | 12 | 22 | 0 |

The two removed records originate from `Hidden` and `Hidden.method`, whose declarations have no AST nodes.
The represented callback-local `Visible` class retains both its inheritance and method return-type relationships.
This fixes source ownership within existing extraction scope; it does not add extraction support for omitted local declarations.

`before.png` and `after.png` are offline-rendered audit reports generated from the raw JSON, not Graphify viewer screenshots.
`render_report_image.py` contains the rendering code.
`receipt.json` records the exact raw graph hashes and commands.
The raw graphs, stdout, and stderr are retained under `before/` and `after/`.

To reproduce with each checkout:

```sh
python -m graphify extract /path/to/source --code-only --no-cluster --max-workers 1 --out /path/to/fresh-output
```

Use a separate fresh output for each revision.
No LLM calls are needed.
