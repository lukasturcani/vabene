class ValenceTracker:
    def __init__(self, atoms, bonds=()):
        self._atoms = atoms
        self._free_valences = {
            atom_id: atom.get_max_valence()
            for atom_id, atom in enumerate(atoms)
        }
        self._connected = (
            frozenset() if bonds else frozenset({0})
        )
        self._disconnected = (
            frozenset(range(len(atoms)))
            if bonds
            else frozenset(range(1, len(atoms)))
        )
        for bond in bonds:
            self._with_bond(bond)

    def clone(self):
        clone = self.__class__.__new__(self.__class__)
        clone._atoms = self._atoms
        clone._free_valences = dict(self._free_valences)
        clone._connected = self._connected
        clone._disconnected = self._disconnected
        return clone

    def with_bond(self, bond):
        return self.clone()._with_bond(bond)

    def _with_bond(self, bond):
        connected = set()
        for atom_id in bond.get_atom_ids():
            connected.add(atom_id)
            self._free_valences[atom_id] = max(
                self._free_valences[atom_id] - bond.get_order(),
                0,
            )

        self._connected |= connected
        self._disconnected -= connected
        return self

    def get_ids_with_free_valence(self):
        yield from (
            atom_id
            for atom_id, free_valence in self._free_valences.items()
            if free_valence > 0
        )

    def get_free_valence(self, atom_id):
        return self._free_valences[atom_id]

    def get_free_connected(self):
        yield from (
            atom_id for atom_id in self._connected
            if self._free_valences[atom_id] > 0
        )

    def has_free_connected(self):
        return any(map(self._free_valences.get, self._connected))

    def get_num_disconnected(self):
        return len(self._disconnected)

    def get_disconnected(self):
        yield from self._disconnected
