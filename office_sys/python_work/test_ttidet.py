import ttide as tt
import numpy as np 

t = np.arange(1001)
m2_freq = 2 * np.pi/12.42 

# create a real scalar dataset

elev = 5 * np.cos(m2_freq * t)

#computing tidal fit

tfit_e = tt.t_tide(elev)

elev_fit = tfit_e(t)

extrap_fit = tfit_e(np.arange(2000,2500))

vel = 0.8 * elev + 1j * 2 * np.sin(m2_freq * t)

tfit_v = tt.t_tide(vel)

