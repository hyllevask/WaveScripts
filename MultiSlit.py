
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser("Compute multislit interference/diffraction")
parser.add_argument("--l",help="Wavelength", default=0.630,type=float)
parser.add_argument("--d",help="Slit Distance", default=600,type=float)
parser.add_argument("--a",help="Slit Width",default=200,type=float)
parser.add_argument("--N",help="Number of slits",default=2,type=int)
parser.add_argument("--L",help="Distance in meters",default=4,type=float)
parser.add_argument("--x_max",help="Screen Distance",default=0.05,type=float)
args = parser.parse_args()

x = np.linspace(-args.x_max,args.x_max,num=1024*8)

theta = np.arcsin(x/args.L)

I0 = 1

l = args.l
d = args.d
a = args.a
N = args.N


k = 2*np.pi/l

phi = k*d*np.sin(theta)
beta =  k*a*np.sin(theta)



Ip = I0 * np.sin(beta/2)**2/(beta/2)**2 * np.sin(N*phi/2)**2 / np.sin(phi/2)**2

plt.figure(1)
#plt.style.use('dark_background')
plt.plot(x*1000,Ip,color=(3/255,32/255,84/255))
plt.xlabel("x [mm]")
plt.ylabel("I [W/m^2]")
if N == 1:
    plt.title("Intensity with N = %i, a = %i\u03BCm" % (N,a))
else:
    plt.title("Intensity with N = %i, d = %i\u03BCm, a = %i\u03BCm" % (N,d,a))
plt.show(block=True)
