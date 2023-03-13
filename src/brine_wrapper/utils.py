def params_to_dict(dict: dict) -> dict:
    del dict['self']
    d = {}
    for key, val in dict.items():
        if(val):
            d[key] = val
    return d
