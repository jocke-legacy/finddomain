#!/usr/bin/env python3

import sys, getopt, itertools, subprocess, re, time

tlds = ['biz', 'cat',
        'com', 'int',
        'net', 'org',
        'pro', 'tel',
        'xxx',
 
        # Country code
        'ac', 'ad', 'ae', 'af',
        'ag', 'ai', 'al', 'am',
        'an', 'ao', 'aq', 'ar',
        'as', 'at', 'au', 'aw',
        'ax', 'az', 'ba', 'bb',
        'bd', 'be', 'bf', 'bg',
        'bh', 'bi', 'bj', 'bm',
        'bn', 'bo', 'br', 'bs',
        'bt', 'bv', 'bw', 'by',
        'bz', 'ca', 'cc', 'cd',
        'cf', 'cg', 'ch', 'ci',
        'ck', 'cl', 'cm', 'cn',
        'co', 'cr', 'cs', 'cu',
        'cv', 'cx', 'cy', 'cz',
        'dd', 'de', 'dj', 'dk',
        'dm', 'do', 'dz', 'ec',
        'ee', 'eg', 'eh', 'er',
        'es', 'et', 'eu', 'fi',
        'fj', 'fk', 'fm', 'fo',
        'fr', 'ga', 'gd', 'ge',
        'gf', 'gg', 'gh', 'gi',
        'gl', 'gm', 'gn', 'gp',
        'gq', 'gr', 'gs', 'gt',
        'gu', 'gw', 'gy', 'hk',
        'hm', 'hn', 'hr', 'ht',
        'hu', 'id', 'ie', 'il',
        'im', 'in', 'io', 'iq',
        'ir', 'is', 'it', 'je',
        'jm', 'jo', 'jq', 'ke',
        'kg', 'kh', 'ki', 'km',
        'kn', 'kp', 'kr', 'kw',
        'ky', 'kz', 'la', 'lb',
        'lc', 'li', 'lk', 'lr',
        'ls', 'lt', 'lu', 'lv',
        'ly', 'ma', 'mc', 'mc',
        'md', 'me', 'mg', 'mh',
        'mk', 'ml', 'mm', 'mn',
        'mo', 'mp', 'mr', 'ms',
        'mt', 'mu', 'mv', 'mv',
        'mw', 'mx', 'my', 'mz',
        'na', 'nc', 'ne', 'nf',
        'ng', 'ni', 'nl', 'no',
        'np', 'np', 'nr', 'nu',
        'nz', 'om', 'pa', 'pe',
        'pf', 'pg', 'ph', 'pk',
        'pl', 'pm', 'pm', 'pn',
        'pr', 'ps', 'pt', 'pw',
        'py', 'qa', 're', 'ro',
        're', 'rs', 'ru', 'rw',
        'sa', 'sb', 'sc', 'sd',
        'sg', 'sh', 'si', 'sj',
        'sk', 'sl', 'sm', 'sn',
        'so', 'sr', 'ss', 'st',
        'su', 'sv', 'sx', 'sy',
        'sz', 'tc', 'td', 'tf',
        'tg', 'th', 'tj', 'tk',
        'tl', 'tm', 'tn', 'to',
        'tp', 'tr', 'tt', 'tv',
        'tw', 'ua', 'ug', 'uk',
        'us', 'uy', 'uz', 'va',
        'va', 'vc', 've', 'vg',
        'vi', 'vn', 'vu', 'wf',
        'ws', 'ye,' 'yt', 'yu',
        'za', 'zm', 'zw'        ]



def help():
    print('usage: finddomain -l <length> | --length=<length> [-t <tld> | --top-level-domain=<tld>]')

def main(argv):
    try: opts, args = getopt.getopt(argv, 'hc:t:l:', ['length=', 'top-level-domain=', 'letters='])
    except getopt.GetoptError as err:
        print(str(err))
        help()
        sys.exit(1)

    letters = 'abcdefghijklmnopqrstuvwxyz0123456789';
    for (opt, arg) in opts:
        if opt == '-h':
            help()
            exit(1)
        elif opt in ('-c', '--length'):
            domain_length = int(arg)
        elif opt in ('-t', '--top-level-domain'):
            tlds = [arg]
        elif opt in ('-l', '--letters'):
            letters = arg

    try:
        for x in itertools.permutations(letters, domain_length):
            x = ''.join(list(x))
            for tld in tlds:
                try: output = str(subprocess.check_output(['whois', '{}.{}'.format(x, tld)]))
                except subprocess.CalledProcessError:
                    if len(tlds) == 1:
                        print('Something went wrong, try again!')
 
                if re.search('(n|N)o (m|M)atch|NO MATCH|'            +
                             '((n|N)ot (f|F)ound)|NOT FOUND|'        +
                             '(n|N)ot (a|A)vailable|NOT AVAILABLE.*'   # <- Im not sure if this would mean
                             , output):                                #    not available as in "can't find
                                                                       #    domain in whois db or as in
                                                                       #    unavailable for registry.
                    print('{}.{} is available!'.format(x, tld))
                elif len(tlds) == 1:
                    print('{}.{} is unavailable.'.format(x, tld))
            time.sleep(1)
    except UnboundLocalError:
        help()
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])
