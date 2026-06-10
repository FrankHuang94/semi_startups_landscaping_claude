"""Minimal YAML-subset loader for this database's data/ files.

Uses PyYAML if available; otherwise falls back to a constrained parser that
handles exactly the shapes used in data/*.yaml:
  - top-level scalars:           key: value
  - top-level mapping of lists:  key:\n  - field: value\n    field2: value
  - inline flow lists:           field: ["a", "b"]
  - comments (# ...) and blank lines are ignored.

This is intentionally small and not a general YAML implementation.
"""
from __future__ import annotations
import os


def _strip_comment(line: str) -> str:
    # remove trailing comments not inside quotes/brackets (good enough for our data)
    in_s = in_d = in_b = False
    out = []
    for ch in line:
        if ch == "'" and not in_d:
            in_s = not in_s
        elif ch == '"' and not in_s:
            in_d = not in_d
        elif ch == '[' and not in_s and not in_d:
            in_b = True
        elif ch == ']' and not in_s and not in_d:
            in_b = False
        elif ch == '#' and not in_s and not in_d and not in_b:
            break
        out.append(ch)
    return ''.join(out)


def _coerce(val: str):
    v = val.strip()
    if v == '' or v == '~':
        return None
    if v.startswith('[') and v.endswith(']'):
        inner = v[1:-1].strip()
        if not inner:
            return []
        return [_coerce(x) for x in _split_flow(inner)]
    if (v[0] == '"' and v[-1] == '"') or (v[0] == "'" and v[-1] == "'"):
        return v[1:-1]
    low = v.lower()
    if low in ('true', 'false'):
        return low == 'true'
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        pass
    return v


def _split_flow(inner: str):
    parts, buf, in_s, in_d = [], [], False, False
    for ch in inner:
        if ch == "'" and not in_d:
            in_s = not in_s
            buf.append(ch)
        elif ch == '"' and not in_s:
            in_d = not in_d
            buf.append(ch)
        elif ch == ',' and not in_s and not in_d:
            parts.append(''.join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    if buf:
        parts.append(''.join(buf).strip())
    return [p for p in parts if p != '']


def _fallback_load(text: str):
    root = {}
    cur_list = None      # list currently being appended to
    cur_item = None      # dict item currently being filled
    for raw in text.splitlines():
        line = _strip_comment(raw.rstrip('\n'))
        if line.strip() == '':
            continue
        indent = len(line) - len(line.lstrip(' '))
        stripped = line.strip()
        if indent == 0 and not stripped.startswith('-'):
            # top-level key
            key, _, val = stripped.partition(':')
            key = key.strip()
            if val.strip() == '':
                cur_list = []
                root[key] = cur_list
                cur_item = None
            else:
                root[key] = _coerce(val)
                cur_list = None
                cur_item = None
        elif stripped.startswith('- '):
            # new list item
            cur_item = {}
            if cur_list is None:
                cur_list = []
            cur_list.append(cur_item)
            field = stripped[2:]
            key, _, val = field.partition(':')
            cur_item[key.strip()] = _coerce(val)
        else:
            # continuation field of current item
            if cur_item is not None:
                key, _, val = stripped.partition(':')
                cur_item[key.strip()] = _coerce(val)
    return root


def load(path: str):
    with open(path, 'r', encoding='utf-8') as fh:
        text = fh.read()
    try:
        import yaml  # type: ignore
        return yaml.safe_load(text)
    except ImportError:
        return _fallback_load(text)


def repo_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
