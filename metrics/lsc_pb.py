from typing import List, Dict, Tuple

def normalize_trace_via_L(trace: List[str], L_map: Dict[str, str]) -> List[str]:
    out = []
    for step in trace:
        tokens = []
        buf = []
        for ch in step:
            if ch.isalpha():
                buf.append(ch.lower())
            else:
                if buf:
                    tokens.append(''.join(buf)); buf=[]
        if buf:
            tokens.append(''.join(buf))
        mapped = [L_map.get(tok, tok) for tok in tokens]
        out.append(' '.join(mapped))
    return out

def multiset_residual(a: List[str], b: List[str]) -> float:
    from collections import Counter
    ca, cb = Counter(a), Counter(b)
    inter = sum((ca & cb).values())
    union = sum((ca | cb).values())
    if union == 0:
        return 0.0
    j = inter / union
    return 1.0 - j

def lsc_pb_score(trace_c: List[str], trace_d: List[str], L_map: Dict[str, str]) -> Tuple[float, float]:
    nc = normalize_trace_via_L(trace_c, L_map)
    nd = normalize_trace_via_L(trace_d, L_map)
    delta = multiset_residual(nc, nd)
    s = 1.0 - delta
    return s, delta
