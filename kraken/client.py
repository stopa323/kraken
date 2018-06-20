import ccxt
import logging

from kraken.computation import utils
from kraken.computation import arbitrage
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

kraken = ccxt.kraken()
symbols = kraken.load_markets().keys()

import re
regex = re.compile(r'[A-Z]{3}/[A-Z]{3}')
symbols = filter(regex.search, symbols)


def load_market_data(symbol, limit=500):
    LOG.info("Loading order book for %s" % symbol)
    data = kraken.fetch_order_book(symbol, limit=limit)

    E1, E2 = utils.get_edge_from_data(symbol, data['bids'], data['asks'],
                                      strategy='best')
    return E1, E2


V = set()
E = list()
for s in symbols:
    e1, e2 = load_market_data(s)
    V.add(e1[0])
    V.add(e1[1])
    E.append(e1)
    E.append(e2)

# arbitrage.get_profitable_chain(list(V), E)
