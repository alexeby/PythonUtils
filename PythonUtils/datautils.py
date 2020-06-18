class DataUtils:

    @staticmethod
    def get_key_from_value(d: dict, v):
        for key, value in d.items():
            if value == v:
                return key
