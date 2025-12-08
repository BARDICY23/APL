import numpy as np
import pandas as pd
def numpy_stats():
    a = np.arange(1,11)
    return a.mean(), np.median(a), a.std()
def pandas_filter():
    df = pd.DataFrame({'Name':['A','B','C'],'Age':[20,30,40],'Score':[70,85,90]})
    return df[df['Score']>80]
if __name__ == '__main__':
    print(numpy_stats())
    print(pandas_filter())
