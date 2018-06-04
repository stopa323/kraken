NODES = ['USD', 'EUR', 'BTC', 'BCH', 'ETH', 'XRP']

EDGES = [
    ('USD', 'BTC', 0.1),
    ('USD', 'BCH', 0.3),
    ('USD', 'ETH', 0.5),
    ('USD', 'XRP', 2.0),

    ('EUR', 'BTC', 0.15),
    ('EUR', 'BCH', 0.5),
    ('EUR', 'ETH', 0.7),
    ('EUR', 'XRP', 3.0),

    ('XRP', 'BTC', 0.01),
    ('XRP', 'BCH', 0.05),

    ('ETH', 'BTH', 0.1),
    ('ETH', 'BCH', 0.2),
]

NODES_CYCLE = ['USD', 'XRP', 'BTC', 'ETH']

EDGES_CYCLE = [
    ('USD', 'XRP', 2.0),
    ('USD', 'BTC', 0.5),
    ('USD', 'ETH', 0.5),

    ('XRP', 'USD', 0.5),
    ('XRP', 'BTC', 0.5),
    ('XRP', 'ETH', 1.0),

    ('BTC', 'USD', 2.0),
    ('BTC', 'XRP', 2.0),
    ('BTC', 'ETH', 0.5),

    ('ETH', 'USD', 1.0),
    ('ETH', 'XRP', 0.5),
    ('ETH', 'BTC', 0.5),
]
