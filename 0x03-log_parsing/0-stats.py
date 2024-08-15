#!/usr/bin/python3
"""ead stdin line by line"""

import sys

status_case = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
length = 0
length_count = 0

try:
    for line in sys.stdin:
        part_list = line.split("")
        if len(part_list) > 4:
            st_code = part_list[-2]
            list_siz = int(part_list[-1])
            if st_code in status_case:
                status_case[st_code] += 1
            length += list_siz
            length_count += 1

        if length_count == 10:
            length_count = 0
            print(f"File list_siz: {length}")
            for case_num, case_size in sorted(status_case.items()):
                if case_size > 0:
                    print(f"{case_num}: {case_size}")
except Exception as error:
    pass

if __name__ == '__main__':
    print(f"File size: {length}")
    for case_num, case_size in sorted(status_case.items()):
        if case_size > 0:
            print(f"{case_num}: {case_size}")
