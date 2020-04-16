"""
Random Bond Factory
===================

"""

import numpy as np

from .utilities import ValenceTracker
from ..bond_factory import BondFactory
from ...bond import Bond


class RandomBondFactory(BondFactory):
    """
    Creates random collections of bonds.

    The bonds yielded will not necessarily create a single molecule.

    """

    def __init__(
        self,
        max_internal_bonds=10,
        required_bonds=(),
        random_seed=None,
    ):
        """
        Initialize a :class:`.RandomBondFactory` instance.

        Parameters
        ----------
        max_internal_bonds : :class:`int`, optional
            Once all atoms have been connected into a single molecule,
            the factory will create a random number of internal bonds
            between atoms in the molecule. This sets the maximum number
            of such bonds.

        required_bonds : :class:`tuple` of :class:`.Bond`
            Bonds, which must be yielded by each
            :meth:`~.BondFactory.get_bonds` call.

        random_seed : :class:`int`, optional
            The random seed to use.

        """

        self._max_internal_bonds = max_internal_bonds
        self._required_bonds = required_bonds
        self._generator = np.random.RandomState(random_seed)

    def get_bonds(self, atoms):
        yield from self._required_bonds

        valence_tracker = ValenceTracker(atoms, self._required_bonds)

        # To make sure a connected molecule is sampled, create two sets
        # of atoms. The first set of atoms holds atoms which have
        # been added to the molecule, while the second set of atom
        # holds atoms which have not yet been added to the molecule.

        # To randomly sample a connected molecule, first randomly
        # pick an atom from set 1 and then randomly pick an atom from
        # set 2. Yield a bond between these two atoms, and transfer
        # the atom from set 2 into set 1. Repeat this process until
        # set 2 is empty.
        while (
            valence_tracker.has_free_connected() and
            valence_tracker.get_num_disconnected() > 0
        ):
            atom1_id = self._generator.choice(
                a=tuple(valence_tracker.get_free_connected()),
            )
            atom2_id = self._generator.choice(
                a=tuple(valence_tracker.get_disconnected()),
            )
            orders = tuple(
                valence_tracker.get_valid_valences(atom1_id)
                & valence_tracker.get_valid_valences(atom2_id)
            )
            order = self._generator.choice(orders)
            bond = Bond(atom1_id, atom2_id, order)
            valence_tracker = valence_tracker.with_bond(bond)
            yield bond

        # Add bonds between connected atoms to form rings.
        num_internal_bonds = self._generator.randint(
            low=0,
            high=self._max_internal_bonds+1,
        )
        for i in range(num_internal_bonds):
            free_connected = tuple(
                valence_tracker.get_free_connected()
            )
            if len(free_connected) < 2:
                return

            atom1_id, atom2_id = self._generator.choice(
                a=free_connected,
                size=2,
                replace=False,
            )
            orders = tuple(
                valence_tracker.get_valid_valences(atom1_id)
                & valence_tracker.get_valid_valences(atom2_id)
            )
            order = self._generator.choice(orders)
            bond = Bond(atom1_id, atom2_id, order)
            valence_tracker = valence_tracker.with_bond(bond)
            yield bond