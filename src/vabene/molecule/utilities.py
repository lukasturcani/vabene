def dedupe(iterable, get_key):
    seen = set()
    for item in iterable:
        key = get_key(item)
        if key not in seen:
            seen.add(key)
            yield item
