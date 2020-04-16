"""
Random Atom Factory
===================

"""

import random
import itertools as it

from .atom_factory import AtomFactory


class RandomAtomFactory(AtomFactory):
    """
    Creates a random collection of atoms.

    """

    def __init__(
        self,
        atoms,
        num_atoms,
        required_atoms=(),
        random_seed=None,
    ):
        """
        Initialize a :class:`.RandomAtomFactory`.

        Parameters
        ----------
        atoms : :class:`tuple` of :class:`.Atom`
            The atoms, which are randomly selected, with replacement,
            in each :meth:`~.RandomAtomFactory.get_atoms` call.

        num_atoms : :class:`int`
            The number of atoms which should be yielded in each
            :meth:`~.RandomAtomFactory.get_atoms` call.

        required_atoms : :class:`tuple` of :class:`.Atom`, optional
            Atoms, which must be yielded in each
            :meth:`~.RandomAtomFactory.get_atoms` call.

        random_seed : :class:`int`, optional
            The random seed to use.

        """

        self._atoms = atoms
        self._num_atoms = num_atoms
        self._required_atoms = required_atoms
        self._generator = random.Random(random_seed)

    def get_atoms(self):
        yield from it.islice(self._required_atoms, self._num_atoms)

        num_atoms = self._num_atoms - len(self._required_atoms)
        if num_atoms > 0 and self._atoms:
            yield from self._generator.choices(
                population=self._atoms,
                k=num_atoms,
            )
