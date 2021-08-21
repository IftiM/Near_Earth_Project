import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    with open(filename, 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['datetime_utc', 'distance_au',
                         'velocity_km_s', 'designation', 'name',
                         'diameter_km', 'potentially_hazardous'])

        for i in results:
            d = [i.time_str, i.distance, i.velocity,
                 i.neo.designation, i.neo.name,
                 i.neo.diameter, i.neo.hazardous]
            writer.writerow(d)


def write_to_json(results, filename):
    """A JSON output file using ColseApproach objects.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """

    with open(filename, 'w') as outfile:
        list1 = []
        for i in results:
            list1.append({'datetime_utc': i.time_str,
                          'distance_au': i.distance,
                          'velocity_km_s': i.velocity,
                          'neo': {'designation': i.neo.designation,
                                  'name': i.neo.name, 'diameter_km': i.distance,
                                  'potentially_hazardous': i.neo.hazardous}})
        json.dump(list1, outfile, indent=2)
