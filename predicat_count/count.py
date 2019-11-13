import pandas as pd
import numpy as np
import re

files = [
    'Часть вторая', 
    'aviator_analiz_ch.1',
]

for file in files:

    transes = set() #
    times = set()   # 

    with open(file, 'r') as f:
        for line in f:

            matches = re.findall('{?([A-Z, 0-9, a-z]+;[^}]+)}', line)

            for one in matches:

                    trans, time = one.split(';')

                    trans.replace('{', '')
                    time.replace('}', '')

                    transes.add(trans)
                    times.add(time)



    df = pd.DataFrame(
        np.zeros(
            (len(transes), len(times),),
            dtype=int,
        ),
        columns=sorted(times),
        index=sorted(transes),
    )


    with open(file, 'r') as f:
        for line in f:
            matches = re.findall('{?([A-Z, 0-9, a-z]+;[^}]+)}', line)

            for one in matches:
                trans, time = one.split(';')
                
                df.loc[trans,time] += 1 

    df.to_csv(file + '_table.csv')
    # print(df)

