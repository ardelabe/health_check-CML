#!/usr/bin/env python3

from disk_space_checker import check_partitions, raise_alert


if __name__ == "__main__":
    notify_partitions, settings = check_partitions()
    raise_alert(notify_partitions, settings)
