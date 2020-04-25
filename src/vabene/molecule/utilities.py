def dedupe(iterable, get_key):
    """
    Yield from `iterable` without duplicates.

    Parameters
    ----------
    iterable : :class:`iterable`
        The iterable whose items should be deduped.

    get_key : :class:`callable`
        Takes an item from `iterable` and a key. If two items return
        the same key, they are considered duplicates.

    Yields
    ------
    :class:`object`
        An item in `iterable`.

    """

    seen = set()
    for item in iterable:
        key = get_key(item)
        if key not in seen:
            seen.add(key)
            yield item
