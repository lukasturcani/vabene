"""
Random Bond Factory
===================

"""

import random

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
        max_internal_bonds=4,
        required_bonds=(),
        max_bond_order=None,
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

        max_bond_order : :class:`int`
            The maximum bond order the factory can make. If
            ``None`` the maximum will be the maximum shared valence
            between the two atoms.

        random_seed : :class:`int`, optional
            The random seed to use.

        """

        self._max_internal_bonds = max_internal_bonds
        self._required_bonds = required_bonds
        self._max_bond_order = (
            float('inf') if max_bond_order is None else max_bond_order
        )
        self._generator = random.Random(random_seed)

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

        bonds = {}
        while (
            valence_tracker.has_free_connected() and
            valence_tracker.get_num_disconnected() > 0
        ):
            atom1_id = self._generator.choice(
                seq=tuple(valence_tracker.get_free_connected()),
            )
            atom2_id = self._generator.choice(
                seq=tuple(valence_tracker.get_disconnected()),
            )
            bond = Bond(atom1_id, atom2_id, 1)
            bonds[frozenset((atom1_id, atom2_id))] = bond
            valence_tracker = valence_tracker.with_bond(bond)

        # Add bonds between connected atoms to form rings.
        num_internal_bonds = self._generator.randint(
            a=0,
            b=self._max_internal_bonds,
        )
        for i in range(num_internal_bonds):
            free_connected = tuple(
                valence_tracker.get_free_connected()
            )
            if len(free_connected) < 2:
                break

            atom1_id, atom2_id = self._generator.sample(
                population=free_connected,
                k=2,
            )
            bond = Bond(atom1_id, atom2_id, 1)
            bonds[frozenset((atom1_id, atom2_id))] = bond
            valence_tracker = valence_tracker.with_bond(bond)

        # Increase the valence of a random number of bonds, by a
        # random amount.
        num_incremented = self._generator.randint(0, len(bonds))
        for bond in self._generator.sample(
            population=list(bonds.values()),
            k=num_incremented,
        ):
            atom1_free_valence = min(
                valence_tracker.get_free_valence(bond.get_atom1_id()),
                self._max_bond_order-1,
            )
            atom2_free_valence = min(
                valence_tracker.get_free_valence(bond.get_atom2_id()),
                self._max_bond_order-1,
            )
            if atom1_free_valence and atom2_free_valence:
                orders = tuple(
                    set(range(1, atom1_free_valence+1))
                    &
                    set(range(1, atom2_free_valence+1))
                )
                order = self._generator.choice(orders)
                bond = Bond(
                    atom1_id=bond.get_atom1_id(),
                    atom2_id=bond.get_atom2_id(),
                    order=order,
                )
                valence_tracker = valence_tracker.with_bond(bond)
                bond_key = frozenset(
                    (bond.get_atom1_id(), bond.get_atom2_id())
                )
                bonds[bond_key] = Bond(
                    atom1_id=bond.get_atom1_id(),
                    atom2_id=bond.get_atom2_id(),
                    order=order+1,
                )

        yield from bonds.values()
