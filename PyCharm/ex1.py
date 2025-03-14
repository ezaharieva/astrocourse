import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.table import Table


a = (56, 43, 2, 4, 3)
b = np.mean(a)
print(b)

hdu = fits.open('hst_results_nd.fits')

hdr = hdu[0].header
data = hdu[0].data

t = Table.read('hst_results_nd.fits')
ra = t['RA']
dec = t['DEC']

plt.figure()
plt.plot(ra, dec, color='blue', marker='o')

plt.xlabel('RA')
plt.ylabel('DEC')
plt.title('RA vs DEC')

plt.show()


