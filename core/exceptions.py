

class BetlError(Exception):
    def __init__(self, *a, **k):
        self.k = k
        super(BetlError).__init__(self, *a)


class ConfigurationError(BetlError):
    def __init__(self, *a, **k):
        super(ConfigurationError).__init__(self, *a, **k)


class DataError(BetlError):
    def __init__(self, *a, **k):
        super(DataError).__init__(self, *a, **k)
