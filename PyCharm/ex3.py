import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.table import Table

cat = Table.read('hlsp_scylla_hst_wfc3_lmc-04_multi_v1_st.fits')

f475 = cat['F475W_VEGA']
f814 = cat['F814W_VEGA']

col=f475 - f814
mag = f475
n = len(f475)



plt.figure()
plt.plot(col, mag, ',b', ls='', label='N = %s' % n)
plt.legend()
plt.xlabel('F475W - F814W')
plt.ylabel('F475W')
plt.title('hlsp_scylla_hst_wfc3_lmc-04_multi_v1_st')
plt.xlim(-3,6)
plt.ylim(30,17)
plt.savefig('hlsp_scylla_hst_wfc3_lmc-04_multi_v1_st.png')

print(n)
plt.show()




