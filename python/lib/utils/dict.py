def filter_fields(in_dict, fields):
    return {k: v for k, v in in_dict.items() if k in fields}


def reverse_dict(in_dict):
    return {v: k for k, v in in_dict.items()}


def to_dict(datas, key="id", fields=None):
    fields = list(set((fields or []) + [key]))

    return {
        data.get(key): filter_fields(data, fields) if len(fields) > 1 else data
        for data in datas
        if data.get(key)
    }
