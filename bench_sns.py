#!/usr/bin/python3

import pl0t
import random
import pandas as pd
import numpy as np
import time

def gen_sin_series(series_nb, datas_nb=200,  x_min=0,
                    x_max=2 * np.pi, max_shift=5.0, max_offset=5.0):
    dat = []
    for i in range(series_nb):
        x = np.linspace(x_min, x_max, datas_nb)
        mul = random.uniform(0, 1) * max_shift
        offset = random.uniform(0, 1) * max_offset
        y = np.sin(mul * x + offset)
        for j in range(datas_nb):
            dat.append([i, x[j], y[j]])
    ret = pd.DataFrame(dat)
    ret.columns = ('cat', 'x', 'y')
    return ret

def split_panels(df, cat, step):
    for i in range(0, len(df[cat].unique()), step):
        beg = i + 1
        end = i + step
        if end > len(df[cat].unique()):
            end = len(df[cat].unique())
        slice = df[(df[cat] >= beg) & (df[cat] <= end)]
        pl0t.lplot_panel('cat', slice, ylab='y', xlab='x', col_nb=5)
        pl0t.save(str(i))
        pl0t.cls()
        print('Processed %i series' % i)
    
start_t = time.time()
df = gen_sin_series(200, 2000)
split_panels(df, 'cat', 8)
print('%2.3f s\n' % float(time.time() - start_t))
