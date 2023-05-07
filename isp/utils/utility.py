
def print_dict(d, logger, delimiter=0):
    """
    Recursively visualize a dict and
    indenting acrrording by the relationship of keys.
    """
    for k, v in sorted(d.items()):
        if isinstance(v, dict):
            logger.info("{}{} : ".format(delimiter * " ", str(k)))
            print_dict(v, logger, delimiter + 4)
        elif isinstance(v, list) and len(v) >= 1 and isinstance(v[0], dict):
            logger.info("{}{} : ".format(delimiter * " ", str(k)))
            for value in v:
                print_dict(value, logger, delimiter + 4)
        else:
            logger.info("{}{} : {}".format(delimiter * " ", k, v))


def parse_dict(path):
    """
    Parse a dict file.
    """
    dicts = []
    with open(path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line in dicts:
                print("Duplicate key: {}".format(line))
                continue
            dicts.append(line)
    return dicts
