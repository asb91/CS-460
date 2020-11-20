from prody import *
from pylab import *
ion()

def parse_data(file):
    
    data = []
    atoms=[]
    record=[]
    
    # PARSING FILES
    
    propdb = parsePDB(file)
    protein = propdb.select('protein or name N H')

    # EXTRACTING VALUES
    
    coord = protein.getCoords()
    coords = list(coord)

    length = len(list(coords))

    res = protein.getResnames()
    resid = list(res)

    residi = protein.getResnums()
    residid = list(residi)

    for i in range(length): 
        string = str(protein[i])
        atom = string.split()
        atoms.append(atom[1])

    for i in range(length):

        record.append(atoms[i])
        record.append(resid[i])
        record.append(residid[i])
        record.append(coords[i][0])
        record.append(coords[i][1])
        record.append(coords[i][2])
        data.append(record)
        record=[]

    return data


    
