 #!/usr/bin/env python
"""
DAFoam primal run script for the Cylinder test case using the
unsteady DASonicFoam solver.
"""

from mpi4py import MPI
from dafoam import PYDAFOAM

gcomm = MPI.COMM_WORLD

daOptions = {
    "solverName": "DAHisaFoam",   # use DARhoPimpleFoam for compressible unsteady
    "designSurfaces": ["wall1"],       # or [] if you want analysis only
    "primalMinResTol": 1.0e-12,
    "primalBC": {
        "useWallFunction": True,       # let OpenFOAM BCs control the inlet
    },
    "normalizeStates": {
        "U": 100.0,
        "p": 1e5,
        "nuTilda": 1e-3,
        "phi": 1.0,
        "T": 300.0,
    },
}

DASolver = PYDAFOAM(options=daOptions, comm=gcomm)
DASolver()
