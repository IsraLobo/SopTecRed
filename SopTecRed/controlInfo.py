from SopTecRed import dataBase
from SopTecRed import vistas

def cosultUser(user,cntrs):
    return dataBase.consultUserBD(user,cntrs);

def consultaNum(msisdn,serie,sim):
    if msisdn or serie or sim:
        return valid(dataBase.cosultNumber(msisdn,serie,sim));
    else:
        return 0;

valid = lambda resulNumCnsl: resulNumCnsl if len(resulNumCnsl) > 5 else 0;