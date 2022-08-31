"""Helper functions for working with markdown."""
from io import TextIOWrapper

def read_markdown_meta_data(file: TextIOWrapper):
    """This takes a markdown file and reads the meta-data off the top of the file.
    It will leave the file position set to after the meta-data block, 
    so then an html render can be used.
    """
    meta = {}

    current_line = file.readline().strip()
    # check if the file begins with the opening symbol
    if current_line == "===":  
        # consume and process the next lines until the break symbol is found
        found_end = False
        while not found_end:
            current_line = file.readline().strip()
            if current_line == "===":
                found_end = True
            else:
                # otherwise this is part of the metadata in the format Key: Value
                key, value = current_line.split(": ")
                meta[key.lower()] = value
    else:
        # oops it wasn't a opening ===
        # seek back to the start of the file.
        file.seek(0)
    return meta