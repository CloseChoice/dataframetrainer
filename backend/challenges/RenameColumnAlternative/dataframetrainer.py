# This module should be importable by all challenges


def toHtmlRepresentation(x):
    # Create a html string based on object type
    pass

class Challenge:
    def __init__(self, params, transform) -> None:
        self.params = params
        self.transform = transform

    def run(self, userTransform):
        params = self._get_params()
        userTransform(**params)

    def initial(self):
        params = self._get_params()
        expected_output = self.transform(**params)

        params_html = {key: toHtmlRepresentation(val) for (key, val) in params}
        expected_output_html = toHtmlRepresentation(expected_output)

        # By calling challenge.initial() in the last line of pyodide the return values will be available in JS
        return params_html, expected_output_html

    
    def _get_params(self):
        params = {key: generator.example() for (key, generator) in self.params}
        return params