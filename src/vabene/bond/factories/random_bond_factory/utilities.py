class ValenceTracker:
    def __init__(self, atoms, bonds=()):
        self._atoms = atoms
        self._valid_valences = {
            atom_id: tuple(filter(
                lambda valence: valence > 0,
                atom.get_valid_valences(),
            ))
            for atom_id, atom in enumerate(atoms)
        }
        self._connected = (
            frozenset() if bonds else frozenset(atoms[0:1])
        )
        self._disconnected = (
            frozenset(atoms) if bonds else frozenset(atoms[1:])
        )

        for bond in bonds:
            self._with_bond(bond)

    def clone(self):
        clone = self.__class__.__new__(self.__class__)
        clone._atoms = self._atoms
        clone._valid_valences = dict(self._valid_valences)
        clone._connected = self._connected
        clone._disconnected = self._disconnected
        return clone

    def with_bond(self, bond):
        return self.clone()._with_bond(bond)

    def _with_bond(self, bond):

        def new_valence(valence):
            return valence - bond.get_order()

        connected = {}
        for atom_id in bond.get_atom_ids():
            connected.add(atom_id)

            self._valid_valences[atom_id] = tuple(filter(
                lambda valence: valence > 0,
                map(new_valence, self._valid_valences[atom_id]),
            ))

        self._connected |= connected
        self._disconnected ^= connected
        return self

    def get_ids_with_free_valence(self):
        yield from (
            atom_id
            for atom_id, valid_valences in self._valid_valences.items()
            if valid_valences
        )

    def get_valid_valences(self, atom_id):
        yield from self._valid_valences[atom_id]

    def get_free_connected(self):
        yield from (
            atom_id for atom_id in self._connected
            if self._valid_valences[atom_id]
        )

    def has_free_connected(self):
        return any(map(self._valid_valences.get, self._connected))

    def get_num_disconnected(self):
        return len(self._disconnected)

    def get_disconnected(self):
        yield from self._disconnected
