
# Slider Instance.  The silder controls the deflection magnification (gain)

# Joseph Rudick
# Edited: 8/31/2020

import globals as g
import numpy as np

class btn(object):
    def interface(self):
        
        g.gain = self
        for i in range(0, len(g.solvedX)):
            g.solvedX[i] = g.nodeX[i] + np.float(g.displacement[i*3])*g.gain
            g.solvedY[i] = g.nodeY[i] + np.float(g.displacement[i*3+1])*g.gain

