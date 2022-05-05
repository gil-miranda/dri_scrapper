from __future__ import annotations

import sys

from dri_scrapper.dri_scrapper import fib

if __name__ == '__main__':
    n = int(sys.argv[1])
    print(fib(n))
