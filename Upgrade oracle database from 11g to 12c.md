
Open terminal or Command prompt: 

```
sqlplus / as sysdba 
SQL > select instance_name, version from v$instance;
INSTANCE_NAME VERSION  
------------- -------------
orcl11c       11.2.0.3.0

cd /u01/app/oracle/product/12.1.0/rdbms/admin
sqlplus / as sysdba 
SQL > @preupgrd.sql
SQL > ALTER SYSTEM SET PROCESSES=300 SCOPE=SPFILE;
SQL > exit;
emctl stop db console 

sqlplus / as sysdba 
SQL > SET ECHO ON;
SQL > SETSERVER OUTPUT ON;
SQL > @emremove.sql
SQL > EXECUTE dbms_stats.gather_dictionary_stats;
SQL > exit; 

cd /u01/app/oracle/product/11.2.0/db_1/olap/admin
sqlplus / as sysdba 
SQL > @catnoamd.sql

gedit cd /u01/app/oracle/cfgtoollogs/orcl11c/preupgrade/preupgrade.log
. oraenv 
ORACLE_SID = [orcl11g] ? orcl12
echo $ORACLE_HOME
dbua
```

![](/images/oracle_upgrade1.PNG)

```
echo $ORACLE_HOME
/u01/app/oracle/product/12.1.0/

sqlplus / as sysdba 
SQL > select instance_name, version from v$instance;
INSTANCE_NAME VERSION  
------------- -------------
orcl11c       12.1.0.1.0

SQL > EXECUTE DBMS_STATS.GATHER_FIXED_OBJECTS_STATS;

```
