import numpy as np
import WindfieldInterface.windmodels as windmodels

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

class WindProfileFigure(Figure):

    def __init__(self, lat, lon, eP, cP, rMax, beta):
        Figure.__init__(self)
        self.R = np.array(range(1, 201), 'f')
        self.lat = lat
        self.lon = lon
        self.rMax = rMax
        self.eP = eP
        self.cP = cP
        self.beta = beta
        self.beta1 = beta
        self.beta2 = beta

    def plot(self, profileType=None):
        profiles = []

        if profileType:
            profiles.append(profileType)
        else:
            for p in windmodels.PROFILES:
                profiles.append(p)

        ax = self.add_subplot(1, 1, 1)
        ax.hold(True)
        legend = []

        for name in profiles:
            try:
                cls = windmodels.profile(name)
                params = windmodels.profileParams(name)
                values = [getattr(self, p) for p in params if hasattr(self, p)]
                profile = cls(self.lat, self.lon, self.eP, self.cP, 
                              self.rMax, *values)
                V = profile.velocity(self.R)
                ax.plot(self.R, abs(V), linewidth=2)
                legend.append(name)
            except TypeError:
                pass

        ax.legend(legend)
        ax.grid()
        ax.set_xlabel('Radius (km)', fontsize=14)
        ax.set_ylabel('Wind speed (m/s)', fontsize=14)
        ax.set_title((r'$P_c = %d\hspace{0.5}hPa,\hspace{1} P_e' +
                      r'= %d \hspace{0.5} hPa,\hspace{1} R_{max}' + 
                      r'= %d \hspace{0.5}km$') %
                      (self.cP/100., self.eP/100., self.rMax))

def main():
    lat = -12.
    lon = 130.
    rMax = 30.
    eP = 100700.
    cP = 95000.
    beta = 1.6
    filename = 'windprofile.png'

    fig = WindProfileFigure(lat, lon, eP, cP, rMax, beta)
    canvas = FigureCanvas(fig)

    fig.plot()
    
    canvas.print_figure(filename)

if __name__ == "__main__":
    main()
