"""Python interface to unofficial Yahoo Finance API endpoints"""

# pylint: disable=invalid-name, wrong-import-position
name = "yahooquery"
__version__ = "2.3.7r2"

from .misc import (  # noqa
    get_currencies,
    get_exchanges,
    get_market_summary,
    get_trending,
    search,
)
from .research import Research  # noqa
from .screener import Screener  # noqa
from .ticker import Ticker  # noqa
