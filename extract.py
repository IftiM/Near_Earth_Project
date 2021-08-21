"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

"""
import csv
import json
from models import NearEarthObject, CloseApproach


def load_neos(filename='data/neos.csv'):
    # Aded a neos_file empty list, opened the corresponding CSV file,
    # and entered all the data into the list, then created a
    # NearEarthObject object and returned the collection.
    neos_file = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for i in reader:
            if i[15] == '':  # Going through some inspection process if there's any empty data found
                i[15] = float('nan')
            if i[4] == '':
                i[4] = None
            if i[7] == 'Y':
                i[7] = True
            if i[7] == 'N':
                i[7] = False
            neos_file.append(NearEarthObject(i[3], name=i[4],
                             diameter=float(i[15]),
                             hazardous=bool(i[7])))
    return neos_file

    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """


def load_approaches(filename='data/cad.json'):
    # ade a neos_file empty list, opened the corresponding JSON file, and appended all the data into the list, then created a CloseApproach object and returned the collection.
    approaches_file = []
    with open(filename) as g:
        all_data = json.load(g)
        for data in all_data["data"]:
            approaches_file.append(CloseApproach(_designation=data[0],
                                                 time=data[3], distance=float(data[4]),
                                                 velocity=float(data[7])))
        return (approaches_file)
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
