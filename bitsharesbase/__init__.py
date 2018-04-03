from graphenebase import base58
__all__ = [
    'account',
    'bip38',
    'chains',
    'memo',
    'objects',
    'objecttypes',
    'operationids',
    'operations',
    'signedtransactions',
    'transactions',
]

base58.known_prefixes.append("GRV")

