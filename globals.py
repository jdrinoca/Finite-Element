
# global variables

nodes = []
nodeX, nodeY, nodeColor = [], [], []
nodeScat = None

elements = []
elementsPlot = []

constraints = []
constraintX, constraintY, constraintColor = [], [], []
constraintScat = None

forces = []
forcesPlot = []
moments = []
momentsPlot = []

zoom = 0
coords = [0,0]
ax = None

displacement = []
stress = []
gain = 100
solved = False

solvedNodes = []
solvedX, solvedY, solvedColor = [], [], []
solvedScat = None

solvedElements = []
solvedPlot = []

defaultNodeColor = 'b'
defaultElementColor = 'k'
defaultConstraintColor = 'y'
defaultForceColor = 'darkred'
defaultMomentColor = 'darkred'
edgeColor = 'k'
selectedColor = 'c'
colormap = "gist_rainbow_r"

bSolve = None
bNode = None
bElement = None
bConstraint = None
bLoad = None
bSave = None
bImport = None
bReset = None
sGain = None
sBarDisp = None
axBarDisp = None
sBarStress = None
axBarStress = None
cBar = None
cBarAx = None