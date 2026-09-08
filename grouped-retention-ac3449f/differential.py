import importlib.util
from pathlib import Path
import random
import tempfile
from graphify.extractors import resolution as candidate
from graphify.extractors.models import _SymbolResolutionFacts
spec = importlib.util.spec_from_file_location('original_resolution', '/private/tmp/graphify-3353-original/graphify/extractors/resolution.py')
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)
rng = random.Random(3353)
with tempfile.TemporaryDirectory() as directory:
    root = Path(directory).resolve()
    (root/'target.ts').write_text('export class Parent {}\nexport interface Shape {}\nexport function run() {}\n')
    paths = []
    for number in range(4):
        source = root/f'group{number}.ts'
        source.write_text('import {Parent, Shape, run} from "./target.ts";\n'
                          'export interface Own {}\nconst alias = run; export {alias};\n'
                          'export * from "./target.ts"; export * as ns from "./target.ts";\n'
                          'export default class Child extends Parent implements Shape { field: Shape; }\n'
                          'function caller() { alias(); function nested() { run(); } }\n')
        paths.append(source)
        for suffix in ('js', 'tsx'):
            link = root/f'group{number}.{suffix}'
            link.symlink_to(source)
            paths.append(link)
    paths += [root/'missing.ts', root/'ignored.py']
    original_parse, candidate_parse = original._parse_js_tree, candidate._parse_js_tree
    for case in range(200):
        selected = rng.choices(paths, k=rng.randrange(0, 25))
        failed = set(rng.sample(paths, rng.randrange(0, 5)))
        original._parse_js_tree = lambda p: None if p in failed else original_parse(p)
        candidate._parse_js_tree = lambda p: None if p in failed else candidate_parse(p)
        before, after = _SymbolResolutionFacts(), _SymbolResolutionFacts()
        original._collect_js_symbol_resolution_facts(selected, before)
        candidate._collect_js_symbol_resolution_facts(selected, after)
        assert before == after, (case, selected, failed)
print('200 seeded differential cases match the original collector exactly')
