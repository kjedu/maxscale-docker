
# Real World Project

## MariaDB MaxScale Docker Image


### Introduction

The following CNE 370 project is a demonstration of utilizing docker-compose and building a sharded database within maxscale docker-compose. Using best practice to edit files to set up a sharded database. Creating a python script to interact with maxscale instance through querys to get and display specific data. 


### Running 

**What you will need:**

In order for the project to work the following needs to be installed on your VM:

- Docker
- docker-compose
- python (latest version)
- mysql-connector-python (to connect to python script)
- Fork the [GitHub repository]: (https://github.com/Zohan/maxscale-docker) to than clone it to your Ubuntu VM

Once you have cloned the repository you must edit the following files

- docker-compose.yml
- example.cnf


### Configuration

**Clone the repository:**

```
git clone (paste or manually input your repository url)
```

Navigate into the docker-compose folder:

```
cd docker-compose
```

Navigate to maxscale:

```
cd maxscale
```

Run ls to view the files in maxscale:

```
ls
```

edit the [docker-compose.yml] (https://github.com/kjedu/maxscale-docker/blob/master/maxscale/docker-compose.yml)

```
sudo nano docker-compose.yml
``` 
or
```
nano docker.compose
```

cd into the maxscale.cnf.d

```
cd maxscale.cnf.d
```

list all the files

```
ls
```

edit the [example.cnf] (https://github.com/kjedu/maxscale-docker/blob/master/maxscale/maxscale.cnf.d/example.cnf) file

```
sudo nano example.cnf
``` 
or
```
nano example.cnf
```

### Maxscale docker-compose setup

Once all files have been edited, run them:

```docker-compose up -d```

check if they are running:

```docker ps``` or ```docker ps -a```

After verify they are running, run the following to list the servers:

```sudo docker-compose exec maxscale maxctrl list servers```

┌─────────┬─────────┬──────┬─────────────┬─────────────────┬──────┬─────────────────┐
│ Server  │ Address │ Port │ Connections │ State           │ GTID │ Monitor         │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────┼─────────────────┤
│ server1 │ master1 │ 3306 │ 0           │ Master, Running │      │ MariaDB-Monitor │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────┼─────────────────┤
│ server2 │ master2 │ 3306 │ 0           │ Running         │      │ MariaDB-Monitor │
└─────────┴─────────┴──────┴─────────────┴─────────────────┴──────┴─────────────────┘

To stop them run:

```
sudo docker-compose down
```

Go into MariaDB to look at your Databases:

```
sudo mariadb -umaxuser -pmaxpwd -h 127.0.0.1 -P 4000
```

Look at your Databases:

```
SHOW DATABASES;
```

+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| zipcodes_one       |
| zipcodes_two       |
+--------------------+

## Results for zipcode_one

### Largest zipcode in zipcodes_one

SELECT * FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;
+---------+-------------+------------+-------+--------------+-----------+------------+---------------------+---------------+-----------------+---------------------+------------+
| Zipcode | ZipCodeType | City       | State | LocationType | Coord_Lat | Coord_Long | Location            | Decommisioned | TaxReturnsFiled | EstimatedPopulation | TotalWages |
+---------+-------------+------------+-------+--------------+-----------+------------+---------------------+---------------+-----------------+---------------------+------------+
|   47750 | UNIQUE      | EVANSVILLE | IN    | PRIMARY      | 37.98     | -87.54     | NA-US-IN-EVANSVILLE | FALSE         |                 |                     |            |
+---------+-------------+------------+-------+--------------+-----------+------------+---------------------+---------------+-----------------+---------------------+------------+

### All zipcodes where state=KY

SELECT * FROM zipcodes_one.zipcodes_one WHERE State='KY';
+---------+-------------+------------------+-------+--------------+-----------+------------+---------------------------+---------------+-----------------+---------------------+------------+
| Zipcode | ZipCodeType | City             | State | LocationType | Coord_Lat | Coord_Long | Location                  | Decommisioned | TaxReturnsFiled | EstimatedPopulation | TotalWages |
+---------+-------------+------------------+-------+--------------+-----------+------------+---------------------------+---------------+-----------------+---------------------+------------+
|   41503 | STANDARD    | SOUTH WILLIAMSON | KY    | PRIMARY      | 37.66     | -82.29     | NA-US-KY-SOUTH WILLIAMSON | FALSE         |                 |                     |            |
|   42201 | PO BOX      | ABERDEEN         | KY    | PRIMARY      | 37.25     | -86.68     | NA-US-KY-ABERDEEN         | FALSE         |                 |                     |            |
|   42202 | STANDARD    | ADAIRVILLE       | KY    | PRIMARY      | 36.66     | -86.85     | NA-US-KY-ADAIRVILLE       | FALSE         | 977             | 1809                | 25747844   |
|   42120 | STANDARD    | ADOLPHUS         | KY    | PRIMARY      | 36.67     | -86.27     | NA-US-KY-ADOLPHUS         | FALSE         | 898             | 1759                | 24202921   |
|   40801 | PO BOX      | AGES BROOKSIDE   | KY    | PRIMARY      | 36.83     | -83.25     | NA-US-KY-AGES BROOKSIDE   | FALSE         |                 |                     |            |
|   42602 | STANDARD    | ALBANY           | KY    | PRIMARY      | 36.69     | -85.13     | NA-US-KY-ALBANY           | FALSE         | 3676            | 6893                | 81601218   |


### All zipcodes between 4000 and 4100

SELECT * FROM zipcodes_one.zipcodes_one WHERE zipcode BETWEEN 40000 and 41000;
+---------+-------------+-----------------+-------+--------------+-----------+------------+--------------------------+---------------+-----------------+---------------------+------------+
| Zipcode | ZipCodeType | City            | State | LocationType | Coord_Lat | Coord_Long | Location                 | Decommisioned | TaxReturnsFiled | EstimatedPopulation | TotalWages |
+---------+-------------+-----------------+-------+--------------+-----------+------------+--------------------------+---------------+-----------------+---------------------+------------+
|   40801 | PO BOX      | AGES BROOKSIDE  | KY    | PRIMARY      | 36.83     | -83.25     | NA-US-KY-AGES BROOKSIDE  | FALSE         |                 |                     |            |
|   40402 | STANDARD    | ANNVILLE        | KY    | PRIMARY      | 37.32     | -83.96     | NA-US-KY-ANNVILLE        | FALSE         | 1005            | 1985                | 26926278   |
|   40902 | STANDARD    | ARJAY           | KY    | PRIMARY      | 36.8      | -83.64     | NA-US-KY-ARJAY           | FALSE         | 296             | 556                 | 7170855    |
|   40903 | STANDARD    | ARTEMUS         | KY    | PRIMARY      | 36.83     | -83.84     | NA-US-KY-ARTEMUS         | FALSE         | 340             | 665                 | 7398555    |
|   40803 | PO BOX      | ASHER           | KY    | PRIMARY      | 37.04     | -83.4      | NA-US-KY-ASHER           | FALSE         |                 |                     |            |
|   40003 | STANDARD    | BAGDAD          | KY    | PRIMARY      | 38.26     | -85.05     | NA-US-KY-BAGDAD          | FALSE         | 861             | 1595                | 27922128   |
|   40906 | STANDARD    | BARBOURVILLE    | KY    | PRIMARY      | 36.86     | -83.88     | NA-US-KY-BARBOURVILLE    | FALSE         | 3781            | 7188                | 100928544  |
|   40946 | STANDARD    | GREEN ROAD      | KY    | PRIMARY      | 36.95     | -83.83     | NA-US-KY-GREEN ROAD      | FALSE         |                 |                     |            |
|   40004 | STANDARD    | BARDSTOWN       | KY    | PRIMARY      | 37.81     | -85.46     | NA-US-KY-BARDSTOWN       | FALSE         | 12918           | 22978               | 427573174  |
|   40104 | STANDARD    | BATTLETOWN      | KY    | PRIMARY      | 38.06     | -86.3      | NA-US-KY-BATTLETOWN      | FALSE         | 472             | 903                 | 13309777   |
|   40806 | STANDARD    | BAXTER          | KY    | PRIMARY      | 36.86     | -83.33     | NA-US-KY-BAXTER          | FALSE         | 852             | 1684                | 26622385   |
|   40006 | STANDARD    | BEDFORD         | KY    | PRIMARY      | 38.59     | -85.31     | NA-US-KY-BEDFORD         | FALSE         | 2188            | 4106                | 72579174   |
|   40807 | PO BOX      | BENHAM          | KY    | PRIMARY      | 36.96     | -82.95     | NA-US-KY-BENHAM          | FALSE         |                 |                     |            |
|   40403 | STANDARD    | BEREA           | KY    | PRIMARY      | 37.57     | -84.29     | NA-US-KY-BEREA           | FALSE         | 9852            | 18582               | 312176100  |
|   40404 | UNIQUE      | BEREA           | KY    | PRIMARY      | 37.57     | -84.29     | NA-US-KY-BEREA           | FALSE         |                 |                     |            |
|   40007 | STANDARD    | BETHLEHEM       | KY    | PRIMARY      | 38.4      | -85.06     | NA-US-KY-BETHLEHEM       | FALSE         |                 |                     |            |
|   40913 | STANDARD    | BEVERLY         | KY    | PRIMARY      | 36.93     | -83.53     | NA-US-KY-BEVERLY         | FALSE         |                 |                     |            |

### TotalWages column where state=PA

SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE state= 'PA';
+------------+
| TotalWages |
+------------+
| 11966378   |
| 62923182   |
|            |
| 7908593    |
|            |
| 8273435    |
| 13678147   |
| 57568042   |
|            |
|            |
| 34233845   |
| 565791203  |
|            |
|            |
| 667346676  |
|            |
| 428649297  |
| 379642102  |
| 4377418    |
| 22945575   |
|            |
|            |
| 166009726  |
| 25192378   |
|            |
| 244184876  |
|            |
|            |
| 16182812   |
|            |

## Results for zipcode_two

SELECT * FROM zipcodes_two.zipcodes_two ORDER BY Zipcode DESC LIMIT 1;
+---------+-------------+-----------+-------+--------------+-----------+------------+--------------------+---------------+-----------------+---------------------+------------+
| Zipcode | ZipCodeType | City      | State | LocationType | Coord_Lat | Coord_Long | Location           | Decommisioned | TaxReturnsFiled | EstimatedPopulation | TotalWages |
+---------+-------------+-----------+-------+--------------+-----------+------------+--------------------+---------------+-----------------+---------------------+------------+
|   88424 | STANDARD    | GRENVILLE | NM    | PRIMARY      | 36.59     | -103.61    | NA-US-NM-GRENVILLE | FALSE         |                 |                     |            |
+---------+-------------+-----------+-------+--------------+-----------+------------+--------------------+---------------+-----------------+---------------------+------------+


### Largest zipcode in zipcodes_two

SELECT * FROM zipcodes_two.zipcodes_two ORDER BY Zipcode DESC LIMIT 1;
+---------+-------------+-----------+-------+--------------+-----------+------------+--------------------+---------------+-----------------+---------------------+------------+
| Zipcode | ZipCodeType | City      | State | LocationType | Coord_Lat | Coord_Long | Location           | Decommisioned | TaxReturnsFiled | EstimatedPopulation | TotalWages |
+---------+-------------+-----------+-------+--------------+-----------+------------+--------------------+---------------+-----------------+---------------------+------------+
|   88424 | STANDARD    | GRENVILLE | NM    | PRIMARY      | 36.59     | -103.61    | NA-US-NM-GRENVILLE | FALSE         |                 |                     |            |
+---------+-------------+-----------+-------+--------------+-----------+------------+--------------------+---------------+-----------------+---------------------+------------+

### All zipcodes where state=KY

SELECT * FROM zipcodes_two.zipcodes_two WHERE State='KY';
+---------+-------------+------------------+-------+--------------+-----------+------------+---------------------------+---------------+-----------------+---------------------+------------+
| Zipcode | ZipCodeType | City             | State | LocationType | Coord_Lat | Coord_Long | Location                  | Decommisioned | TaxReturnsFiled | EstimatedPopulation | TotalWages |
+---------+-------------+------------------+-------+--------------+-----------+------------+---------------------------+---------------+-----------------+---------------------+------------+
|   42040 | STANDARD    | FARMINGTON       | KY    | PRIMARY      | 36.67     | -88.53     | NA-US-KY-FARMINGTON       | FALSE         | 465             | 896                 | 11562973   |
|   41524 | STANDARD    | FEDSCREEK        | KY    | PRIMARY      | 37.4      | -82.24     | NA-US-KY-FEDSCREEK        | FALSE         |                 |                     |            |
|   42533 | STANDARD    | FERGUSON         | KY    | PRIMARY      | 37.06     | -84.59     | NA-US-KY-FERGUSON         | FALSE         | 429             | 761                 | 9555412    |
|   40022 | STANDARD    | FINCHVILLE       | KY    | PRIMARY      | 38.15     | -85.31     | NA-US-KY-FINCHVILLE       | FALSE         | 437             | 839                 | 19909942   |
|   40023 | STANDARD    | FISHERVILLE      | KY    | PRIMARY      | 38.16     | -85.42     | NA-US-KY-FISHERVILLE      | FALSE         | 1884            | 3733                | 113020684  |
|   41743 | PO BOX      | FISTY            | KY    | PRIMARY      | 37.33     | -83.1      | NA-US-KY-FISTY            | FALSE         |                 |                     |            |
|   41219 | STANDARD    | FLATGAP          | KY    | PRIMARY      | 37.93     | -82.88     | NA-US-KY-FLATGAP          | FALSE         | 708             | 1397                | 20395667   |
|   40935 | STANDARD    | FLAT LICK        | KY    | PRIMARY      | 36.82     | -83.76     | NA-US-KY-FLAT LICK        | FALSE         | 752             | 1477                | 14267237   |
|   40997 | STANDARD    | WALKER           | KY    | PRIMARY      | 36.88     | -83.71     | NA-US-KY-WALKER           | FALSE         |                 |                     |            |
|   41139 | STANDARD    | FLATWOODS        | KY    | PRIMARY      | 38.51     | -82.72     | NA-US-KY-FLATWOODS        | FALSE         | 3692            | 6748                | 121902277  |
|   41526 | PO BOX      | FORDS BRANCH     | KY    | PRIMARY      | 37.32     | -82.57     | NA-US-KY-FORDS BRANCH     | FALSE         |                 |                     |            |
|   42343 | STANDARD    | FORDSVILLE       | KY    | PRIMARY      | 37.63     | -86.71     | NA-US-KY-FORDSVILLE       | FALSE         | 735             | 1360                | 18216579   |


### All zipcodes between 4000 and 4100

SELECT * FROM zipcodes_two.zipcodes_two WHERE zipcode BETWEEN 40000 and 41000;
+---------+-------------+------------------+-------+--------------+-----------+------------+---------------------------+---------------+-----------------+---------------------+------------+
| Zipcode | ZipCodeType | City             | State | LocationType | Coord_Lat | Coord_Long | Location                  | Decommisioned | TaxReturnsFiled | EstimatedPopulation | TotalWages |
+---------+-------------+------------------+-------+--------------+-----------+------------+---------------------------+---------------+-----------------+---------------------+------------+
|   40022 | STANDARD    | FINCHVILLE       | KY    | PRIMARY      | 38.15     | -85.31     | NA-US-KY-FINCHVILLE       | FALSE         | 437             | 839                 | 19909942   |
|   40023 | STANDARD    | FISHERVILLE      | KY    | PRIMARY      | 38.16     | -85.42     | NA-US-KY-FISHERVILLE      | FALSE         | 1884            | 3733                | 113020684  |
|   40935 | STANDARD    | FLAT LICK        | KY    | PRIMARY      | 36.82     | -83.76     | NA-US-KY-FLAT LICK        | FALSE         | 752             | 1477                | 14267237   |
|   40997 | STANDARD    | WALKER           | KY    | PRIMARY      | 36.88     | -83.71     | NA-US-KY-WALKER           | FALSE         |                 |                     |            |
|   40121 | STANDARD    | FORT KNOX        | KY    | PRIMARY      | 37.89     | -85.96     | NA-US-KY-FORT KNOX        | FALSE         | 2833            | 6397                | 101583167  |
|   40122 | STANDARD    | FORT KNOX        | KY    | PRIMARY      | 37.89     | -85.96     | NA-US-KY-FORT KNOX        | FALSE         |                 |                     |            |
|   40939 | STANDARD    | FOURMILE         | KY    | PRIMARY      | 36.79     | -83.74     | NA-US-KY-FOURMILE         | FALSE         |                 |                     |            |
|   40940 | STANDARD    | FRAKES           | KY    | PRIMARY      | 36.64     | -83.92     | NA-US-KY-FRAKES           | FALSE         |                 |                     |            |
|   40601 | STANDARD    | FRANKFORT        | KY    | PRIMARY      | 38.19     | -84.86     | NA-US-KY-FRANKFORT        | FALSE         | 22938           | 39539               | 721803780  |
|   40602 | PO BOX      | FRANKFORT        | KY    | PRIMARY      | 38.19     | -84.86     | NA-US-KY-FRANKFORT        | FALSE         | 562             | 872                 | 15398719   |
|   40603 | PO BOX      | FRANKFORT        | KY    | PRIMARY      | 38.19     | -84.86     | NA-US-KY-FRANKFORT        | FALSE         |                 |                     |            |
|   40604 | PO BOX      | FRANKFORT        | KY    | PRIMARY      | 38.19     | -84.86     | NA-US-KY-FRANKFORT        | FALSE         |                 |                     |            |
|   40618 | UNIQUE      | FRANKFORT        | KY    | PRIMARY      | 38.19     | -84.86     | NA-US-KY-FRANKFORT        | FALSE         |                 |                     |            |
|   40619 | UNIQUE      | FRANKFORT        | KY    | PRIMARY      | 38.19     | -84.86     | NA-US-KY-FRANKFORT        | FALSE         |                 |                     |            |
|   40620 | UNIQUE      | FRANKFORT        | KY    | PRIMARY      | 38.19     | -84.86     | NA-US-KY-FRANKFORT        | FALSE         |                 |                     |            |
|   40621 | UNIQUE      | FRANKFORT        | KY    | PRIMARY      | 38.19     | -84.86     | NA-US-KY-FRANKFORT        | FALSE         | 308             | 309                 | 429045     |
|   40622 | UNIQUE      | FRANKFORT        | KY    | PRIMARY      | 38.19     | -84.86     | NA-US-KY-FRANKFORT        | FALSE         |                 |                     |            |
|   40322 | STANDARD    | FRENCHBURG       | KY    | PRIMARY      | 37.95     | -83.62     | NA-US-KY-FRENCHBURG       | FALSE         | 1215            | 2297                | 29301156   |
|   40140 | STANDARD    | GARFIELD         | KY    | PRIMARY      | 37.78     | -86.35     | NA-US-KY-GARFIELD         | FALSE         | 303             | 590                 | 8251697    |
|   40941 | PO BOX      | GARRARD          | KY    | PRIMARY      | 37.12     | -83.74     | NA-US-KY-GARRARD          | FALSE         | 269             | 523                 | 4354249    |
|   40324 | STANDARD    | GEORGETOWN       | KY    | PRIMARY      | 38.2      | -84.55     | NA-US-KY-GEORGETOWN       | FALSE         | 17361           | 32541               | 775385492  |
|   40943 | STANDARD    | GIRDLER          | KY    | PRIMARY      | 36.93     | -83.84     | NA-US-KY-GIRDLER          | FALSE         | 364             | 748                 | 9130115    |
|   40025 | PO BOX      | GLENVIEW         | KY    | PRIMARY      | 38.3      | -85.65     | NA-US-KY-GLENVIEW         | FALSE         |                 |                     |            |
|   40944 | PO BOX      | GOOSE ROCK       | KY    | PRIMARY      | 37.09     | -83.69     | NA-US-KY-GOOSE ROCK       | FALSE         |                 |                     |            |
|   40026 | STANDARD    | GOSHEN           | KY    | PRIMARY      | 38.4      | -85.59     | NA-US-KY-GOSHEN           | FALSE         | 2340            | 4686                | 154893571  |
|   40328 | STANDARD    | GRAVEL SWITCH    | KY    | PRIMARY      | 37.58     | -85.05     | NA-US-KY-GRAVEL SWITCH    | FALSE         | 461             | 864                 | 10441430   |
|   40734 | STANDARD    | GRAY             | KY    | PRIMARY      | 36.94     | -84        | NA-US-KY-GRAY             | FALSE         | 1472            | 2862                | 33917723   |
|   40434 | PO BOX      | GRAY HAWK        | KY    | PRIMARY      | 37.39     | -83.93     | NA-US-KY-GRAY HAWK        | FALSE         |                 |                     |            |
|   40829 | PO BOX      | GRAYS KNOB       | KY    | PRIMARY      | 36.8      | -83.3      | NA-US-KY-GRAYS KNOB       | FALSE         | 351             | 663                 | 12121552   |


Once done run the following code to remove clusters and maxscale containers.

```
docker-compose down -v
```

BYE :)


### ISSUES

First issued encountered: "Need DNS lookup, Down"
Solution: in docker-compose.yml file change the "image: mariadb:latest" back to "image: mariadb:10.3"
* Initiialy changed it to latest so that docker would pull the most latest version of mariadb.

Second issued encountered: "Auth Error, Down"
Solution went into master1 and master2 roots and created a user and gave it permissions [Authentication Error](https://mariadb.com/kb/en/maxscale-troubleshooting/#authentication-errors)

## Thanks

Thanks to the CNE370 TA and professor for their help and quick reasponse.

