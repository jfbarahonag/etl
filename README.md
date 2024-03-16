**Taller #1**

Creación de una tubería de datos
==============================================================================

Una compañia dedicada a la venta de inmuebles a decidido reemplazar su sistema
de manejo de datos de inmuebes por una base de datos. La información 
actual se encuentra almacenada en varios archivos CSV. La compañia a decidido 
modernizar todo su sistema de información y la base de datos se encontrará 
ubicada en un datalake.

Este es un **caso práctico** que tiene como objetivo la creación de una 
tubería de ingestión de datos en Python. Siga las siguientes instrucciones para
su creación.

* Se usará `SQLite` como gestor de bases de datos.
* Se usará `Pandas` para la manipulación de datos.
* La estructura del datalake es la siguiente:
    
    ```
    datalake/
    ├── databases
    │   └── house_prices.db
    ├── raw/
    │   ├── stagging/
    │   └── ingested/
    └── logs/
    ``` 

