import json
from bs4 import BeautifulSoup
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ogp_parser.parser import domparser


def check_keys(dst, gt):
    dst_keylist = sorted(dst.keys())
    gt_keylist = sorted(gt.keys())
    assert len(dst_keylist) == len(gt_keylist), '親のキーの数が違う'
    for key in gt_keylist:
        assert key in dst_keylist, f'キー"{key}"がない'

def check_data(dst, gt, datakey):
    for key, values in gt[datakey].items():
        assert len(values) == len(dst[datakey][key]), f'件数不一致[key={key}]'
        val_dst = sorted(values)
        val_gt  = sorted(dst[datakey][key])
        for idx, value in enumerate(val_gt):
            assert value == val_dst[idx], '値不一致'

thisdir = os.path.dirname(__file__)
srcfile = os.path.join(thisdir, 'dummy.html')
dstfile = os.path.join(thisdir, 'dummy_result.json')
with open(srcfile, 'r') as f:
    dom = BeautifulSoup(f.read())
with open(dstfile, 'r') as f:
    gt = json.loads(f.read())

result = domparser(dom)

assert gt['title'] == result['title'], 'タイトルが違う!!'
check_keys(result, gt)
check_data(result, gt, 'ogp')
check_data(result, gt, 'seo')
