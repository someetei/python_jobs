import ibm_db
import ibm_db_ctx

conn_str = "DATABASE=sample;HOSTNAME=172.18.0.2;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=db2inst1"
with ibm_db_ctx.Db2connect(conn_str, '','') as conn:
    stmt = ibm_db.exec_immediate(conn, "SELECT * FROM FLIGHTS_TRAIN limit 100 with ur")
    while ibm_db.fetch_row(stmt):
        row = ibm_db.fetch_tuple(stmt)
        print(row)