# 修正langchain stream 和 文心不兼容的问题
from __future__ import annotations

from typing import Any, Dict


def merge_dicts(left: Dict[str, Any], right: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dicts, handling specific scenarios where a key exists in both
    dictionaries but has a value of None in 'left'. In such cases, the method uses the
    value from 'right' for that key in the merged dictionary.

    Example:
        If left = {"function_call": {"arguments": None}} and
        right = {"function_call": {"arguments": "{\n"}}
        then, after merging, for the key "function_call",
        the value from 'right' is used,
        resulting in merged = {"function_call": {"arguments": "{\n"}}.
    """
    merged = left.copy()
    for k, v in right.items():
        if k not in merged:
            merged[k] = v
        elif merged[k] is None and v:
            merged[k] = v
        elif v is None:
            continue
        elif merged[k] == v:
            continue
        elif type(merged[k]) != type(v):
            merged[k] = str(v)
        elif isinstance(merged[k], str):
            merged[k] += v
        elif isinstance(merged[k], dict):
            merged[k] = merge_dicts(merged[k], v)
        elif isinstance(merged[k], list):
            merged[k] = merged[k] + v
        else:
            merged[k] = str(v)
    return merged

from langchain_core.utils import _merge
_merge.merge_dicts = merge_dicts