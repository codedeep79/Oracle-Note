# Oracle Note

Migrate Oracle:

[Upgrade oracle database from 11g to 12c](/Upgrade%20oracle%20database%20from%2011g%20to%2012c.md) (Don't migrate database 10g to Database 12c)

[Migrating Oracle Databases to Database Cloud Service](https://docs.oracle.com/en/cloud/paas/database-dbaas-cloud/csdbi/mig-migrating-premises-oracle-db-cloud.html) 

cx_Oracle:

+ Support Python 2.7, Python 3.5 and higher are supported by cx_Oracle 7
+ Support Oracle 11.2, 12.1 and 12.2 and 18.3 client libraries
+ Install:
  `python -m pip install cx_Oracle --upgrade`
  + [Detail more](https://cx-oracle.readthedocs.io/en/latest/installation.html#installing-cx-oracle-on-linux)
+ cx_Oracle example: https://github.com/oracle/python-cx_Oracle/tree/master/samples

C and C++ connect Oracle through Pro*C:

+ Pro\*C is an embedded SQL programming language and it's installed in Oracle database. Pro*C uses either C or C++ as its host language 

+ Detailed:
  + Create new project in Visual studio 20xx
  + Right click into Header Files or Resource Files, choose **Add -> Exist Item**, go to folder direct **oracle/precomp/lib/msvc/** in your Drive and choose 2 items **oraSQL9.LIB and oraSQX9.LIB**
  + Right click Source Files and create a file .pc extension. Ex: test.pc
    
    ```cpp
    exec sql begin declare section;
    char *cons="scott/tiger";
    char val1[30],val2[30];
    exec sql end declare section;
    exec sql include sqlca;

    #include<stdio.h>
    #include<conio.h>
    #include<stdlib.h>

     void main()
     {
      printf("Connecting to the database...\n");

      exec sql connect :cons;

      if(sqlca.sqlcode==0) printf("Connection established successfully...\n");
      else
      exit(0);


      printf("Enter the value u want to update :");
      scanf("%s",val1);

      printf("Enter the value u want to update with :");
      scanf("%s",val2);


      exec sql update dept set loc= :val2 where loc= :val1;

      if(sqlca.sqlcode==0)
      {
       printf("Updation success...");
       exec sql commit work release;
      }

      else
      printf("Error message: %s",sqlca.sqlerrm.sqlerrmc);

      getch();
    }
    ```
   + Compile Pro\*C to C or C++:
   
     Press Shift button + right click -> Command prompt dialog display -> type `proc test.pc` to compile and generate [test.c](update_value.pc) -> run [test.c](update_value.c) to trial  
