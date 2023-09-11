import pandas as pd
from dft import to_html
import os
import importlib
from copy import copy

for challenge_name in os.listdir(f"challenges"):
    if not os.path.isdir(f"challenges/{challenge_name}") or challenge_name in ["__pycache__", ".pytest_cache"]:
        continue
    challenge_module = importlib.import_module(f"challenges.{challenge_name}.{challenge_name}")
    challenge_class = getattr(challenge_module, challenge_name)
    try:
        static_example_dict = challenge_class.static_example()
    except AttributeError:
        continue
    if not isinstance(static_example_dict, dict):
        print(f"The return of {challenge_name}.static_example() is not a dict, but a {type(static_example_dict)}")
        continue
    static_example_html = {key: to_html(val).replace('\n', '').replace("th {        text-align: right;    }", "th {        text-align: left;    }")
                        for (key, val) in static_example_dict.items()}
    static_expected = challenge_class.expected_static()
    static_expected_html = to_html(static_expected).replace('\n', '').replace('\n', '').replace("th {        text-align: right;    }", "th {        text-align: left;    }")
    with open(f"challenges/{challenge_name}/intro.md", "r+") as f:
        intro = f.readlines()
        intro_modified = copy(intro)
        if "Example Input" not in "".join(intro):
            intro_modified.append("\n<h3> Example Input</h3>\n")
            static_example_to_add = "\n\n".join([f"<h4> {key}</h4>\n{val}" for (key, val) in static_example_html.items()])
            intro_modified.append(static_example_to_add)
        if "Expected Output" not in "".join(intro):
            intro_modified.append("\n\n<h3> Expected Output</h3>\n")
            intro_modified.append(static_expected_html)
    if intro != intro_modified:
        with open(f"challenges/{challenge_name}/intro.md", "w") as f:
            f.writelines(intro_modified)