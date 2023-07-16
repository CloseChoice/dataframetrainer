import json
import pandas as pd


def _load_from_json(df_as_json: str) -> pd.DataFrame:
    df = pd.DataFrame(json.loads(df_as_json))
    df.index = df.index.astype(int)
    return df


def sanity_checks(function_name: str, function_as_string: str):
    """Performs sanity checks on the function string.
    Current checks are:
      - no double quotes
      - all single quotes appear doubled, so no "'somestring'" but "''somestring''"

    Args:
        function_name (str): _description_
        function_as_string (str): _description_

    Raises:
        ValueError: _description_
    """
    # todo: maybe this needs to be a bit more concrete: We can't forbid double
    if '"' in function_as_string:
        raise ValueError(
            f"Found double quotes in function {function_name}. Please change to single quotes."
        )
    backup_string = function_as_string.replace("''", "<s>")
    if "'" in backup_string:
        raise ValueError(
            f"Found single double quote in function {function_name}. Expected duplicated single quotes."
        )


def transform_function_string(function_as_string: str) -> str:
    """Transform the function string into a format that PostGreSQL can parse.

    Args:
        function_as_string (str): Function as parsed from the Challenge Class.

    Returns:
        str: updated function as string, which can directly be inserted into PostGreSQL.
    """
    # just to make sure that we don't have double quotes in here already
    r_str = function_as_string.replace("''", "'")
    r_str = r_str.replace("'", "''").replace('"', "''")
    encoded_str = (
        r_str.strip()
        .strip("@staticmethod")
        .strip()
        .encode("unicode_escape")
        .decode("utf-8")
    )
    return f'"{encoded_str}"'
