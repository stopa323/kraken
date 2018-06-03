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