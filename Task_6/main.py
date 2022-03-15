def main(args):
    dict0 = {'LFE': 0, 'COOL': 1}
    dict1 = {'TOML': 2, 'TCL': 3, 'NU': dict0[args[0]]}
    dict11 = {'NU': 7, 'TOML': 8, 'TCL': 9}
    dict3 = {1982: 5, 2003: 6, 1965: dict11[args[1]]}
    dict2 = {1984: 4, 1961: dict1[args[1]], 1970: dict3[args[3]]}
    return dict2[args[2]]
