from tephigram_python import Tephigram

from collections.abc import Mapping
from collections.abc import MutableMapping
from collections.abc import Sequence


tephigram = Tephigram()

sounding = np.loadtxt('sounding_example.dat', unpack=True)
P = sounding[0]
T = sounding[2]
T_dp = sounding[3]
RH = sounding[4]/100.

tephigram.plot_sounding(P=P, T=T, T_dp=T_dp)
tephigram.plot_legend()
parcel_info = tephigram.plot_test_parcel(z=z, P=P, T=T, RH=RH)

tephigram.savefig('tephigram_example.png')