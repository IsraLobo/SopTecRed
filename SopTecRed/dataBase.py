from datetime import datetime
from SopTecRed import controlInfo
import cx_Oracle
import json

class OracleConnection():
    connection = None;
    databaseConn = None;
    cursor = None;

    def __init__(self):
        try:
            self.connection = 'CL/CL@192.168.82.181:1521/EDI83';
            self.databaseConn = cx_Oracle.connect(self.connection);
            self.cursor = self.databaseConn.cursor();
        except Exception as error:
            return('[Error en la BD]: ', error);

    def execute_query(self, query):
        self.cursor.execute(query);
        return self.cursor.fetchall();

    def execute_query_description(self, query):
        curs = self.cursor.execute(query);
        columns = [column[0] for column in curs.description];
        results = [dict(zip(columns, row)) for row in curs.fetchall()];
        return json.dumps(results, ensure_ascii=False);

    def execute_Trans(self, query):
        self.cursor.execute(query);
        return self.cursor;

    def commit(self):
        self.databaseConn.commit();

    def close(self):
        self.databaseConn.close()


def coneversorDate(fech):
    a = fech.strftime('%Y/%m/%d')
    return a;


def consultUserBD(user,cntrs):
    try:
        queryUser = ''' SELECT NOMBRE FROM CL_SYS_USUARIO WHERE USUARIO_ID = '{}' AND CONTRASENA = '{}' '''.format(user,cntrs);
        conex = OracleConnection();
        nomResul = conex.execute_query(queryUser);
        conex.close();
        return nomResul;
    except Exception as error:
        return 'No se pudo conectar a la BD [ERROR]: ', error
print('', end='')


def cosultNumber(done,dtwo,dthree):
    try:
        queryNumber = ''' SELECT RU.NOMBRE,RU.PATERNO,RU.MATERNO,RU.EMAIL,RU.RFC,RU.CELULAR,RU.USUARIO,
                                 RUC.SIM,RUC.REFERENCIA,RUC.TIPO_PAGO,TO_CHAR(TO_DATE(RUC.HORA_PAGO,'DD-MM-YYYY')) HORA_PAGO,
                                 TO_CHAR(TO_DATE(RUC.FECHA_REGISTRO,'DD-MM-YYYY')) FECHA_REGISTRO,
                                 ROF.IMSI,ROF.MSISDN, ASL.CVE_ARTICULO,ASL.NSERIE
                            FROM RP_USUARIO RU, RP_USUARIO_COMPRAS RUC, RP_OUTPUT_FILE ROF, AL_SERIES_LOTE ASL
                           WHERE RU.ID_USUARIO = RUC.USUARIO_ID
                             AND RUC.SIM = ROF.ICC
                             AND RUC.SIM = ASL.NUM_SERIE
                             AND ROF.MSISDN = NVL('{}',ROF.MSISDN)
                             AND ASL.NSERIE = NVL('{}',ASL.NSERIE)
                             AND RUC.SIM = NVL('{}', RUC.SIM)
                      '''.format(done,dtwo,dthree);
        conex = OracleConnection();
        numberResul = conex.execute_query_description(queryNumber);        
        conex.close();
        return numberResul;
    except Exception as error:
        return 'No se pudo conectar a la BD [ERROR]: ', error
print('', end='')