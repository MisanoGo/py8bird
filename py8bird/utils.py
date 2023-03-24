from dotenv import dotenv_values

# get environment varables from ./.env by dotenv
env_conf = dotenv_values(verbose=True)


def key_filters():
    """
    return key filters as listself.
    TODO: set this function as @property

    """
    file_name = "key_filters.list"

    with open(file_name,"r") as file:
        return file.read().splitlines()

