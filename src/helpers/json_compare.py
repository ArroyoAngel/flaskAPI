def _json_difference(json1, json2):
    _json1 = {}
    _json2 = {}
    for llave in json1:
        if json1[llave] != json2[llave]:
            # Si los valores son diferentes, agrega la llave y el valor a diferencias
            _json1[llave] = _json1[llave]
            _json2[llave] = _json2[llave]
    
    return [_json1, json2]