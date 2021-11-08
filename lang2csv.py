
import os


from collections import defaultdict, OrderedDict

from category_def import *
from lang_def import *
from lang_doc import *
import json
pwd = os.path.dirname(os.path.abspath(__file__))


def dict2var(dictionary):
    text = []
    for k, v in dictionary.items():  # sort_keys = True,
        d = json.dumps(v, ensure_ascii=False, indent=2)
        text.append(k + " = " + d + "\n\n")
    return ('\n').join(text)
 
def get_lang_examples():
    ie = defaultdict()
    for fn_name in sub_list(all_lang_ref, is_to_hide):
        if fn_name in funct_doc:
            ex_l = set() # avoid duplicates
            examples = funct_doc[fn_name]["examples"].splitlines()
            for ex in examples:
                if fn_name in ex: # get the lines where the fn is present in the doc
                    if '#' in ex: ex = ex.rpartition('#')[0].replace('"', '') # remove comments
                    ex = ex.strip()
                    if len(ex): ex_l.add(ex)

            if len(ex_l): ie[fn_name] = list(ex_l)
        else:
            print(fn_name + " not in doc "+ '*'*10)
    return ie


def write2csv(ex_dict):
    import csv
    with open('build/ex_all.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for fn_name, ex in ex_dict.items():
            csv_writer.writerow([fn_name] + ex)
    with open('build/ex_functions.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for fn_name, ex in ex_dict.items():
            if fn_name in is_fn:
                csv_writer.writerow([fn_name] + ex)
if __name__ == '__main__':
    '''
    To help develop this programs list all extracted def that have a documentation 
    in a csv file extracting relevant examples
    '''
    import sys
    if not len(sys.argv[1:]):
        ie = get_lang_examples()
        write2csv(ie)
        #print(dict2var(ie))

