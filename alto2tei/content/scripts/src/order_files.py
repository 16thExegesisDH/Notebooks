# -----------------------------------------------------------
# Code by: Kelly Christensen
# Python class to organize the file paths in the data directory.
# -----------------------------------------------------------
"""
import re
from collections import namedtuple

class Files:
    def __init__(self, document, filepaths):
        self.d = document
        self.fl = filepaths  # list

    def order_files(self):
        File = namedtuple("File", ["num", "filepath"])
        ordered_files = sorted([File(int(re.search(r"(\d+).xml$", f.name).group(1)), f)for f in self.fl])
        return ordered_files
"""
# -----------------------------------------------------------
# Code adapted by : Floriane Goy
# Python class to organize the file paths in the data directory.
# Adapted to the file_name of the OBN
# -----------------------------------------------------------

import re
from collections import namedtuple

class Files:
    def __init__(self, document, filepaths):
        self.d = document
        self.fl = filepaths  # list

    def order_files(self):
        File = namedtuple("File", ["num", "filepath"])
        ordered_files = []

        for f in self.fl:
            match = (
                re.search(r"(\d+)\.xml$", f.name) or   # new correct rule
                re.search(r"(\d+).xml$", f.name)       # old rule (kept)
            )

            if match:
                num = int(match.group(1))
                ordered_files.append(File(num, f))
            else:
                print(f"Skipping file (no match): {f.name}")

        return sorted(ordered_files, key=lambda x: x.num)