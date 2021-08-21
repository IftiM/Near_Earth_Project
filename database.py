"""Course: Udacity Intermediate Python Nanodegree
Project: Near Earth Object
Name of Student: Iftikhar Mustafa
Date: JUly 5th, 2021


A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

"""

from extract import load_neos, load_approaches


class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """
    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches

        # Creating 2 empty dictionaries (Auxiliary data structure) for Neos by designation, and Neos by name
        self.neos_dict = dict()
        self.neos_dict_name = dict()

        # Creating dictionary for Neos by designation, and Neos by name
        for i in self._neos:
            self.neos_dict[i.designation] = i
            if i.name != '':
                self.neos_dict_name[i.name] = i

        for i in self._approaches:
            i.neo = self.neos_dict[i._designation]
            self.neos_dict[i._designation].approaches.append(i)

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """

        # Quering inside the dictionary of Neos by designation
        if designation in self.neos_dict.keys():
            return self.neos_dict[designation]
        else:
            return None

    def get_neo_by_name(self, _name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """

        # Quering inside the dictionary of Neos by name
        if (_name == '') or (_name == None):
            return None
        elif _name in self.neos_dict_name.keys():
            return self.neos_dict_name[_name]
        else:
            return None

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaninfully, although is often sorted by time.
        
        Source: The maint concept of the part below was done with the help of following link:
        https://github.com/verbistjoel

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """

        # Creating a CloseApproach object to match all the filters.

        """
        Initializing flag as True by default,
        once it if False, the 2nd loop will break
        Iterating through filters
        (It was enterred by user or by file command)
        If the entered item
        was not found in Approach
        object -> break and go to next query
        The queried item wasn't found,
        therfore flag is false -> break
        By the end of this loop,
        if the item was found then we will
        yieled (return the item) and loop over
        again until it matches all the quering conditions
        Sending found query one by one.
        Will return None if nothing was found
        """

        for approach in self._approaches:
            flag = True
            for _filter in filters:
                if not _filter(approach):
                    flag = False
                    break
            if flag is True:
                yield approach
