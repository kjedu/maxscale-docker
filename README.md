
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
- Fork the [GitHub repository](https://github.com/Zohan/maxscale-docker) to than clone it to your Ubuntu VM

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

edit the [docker-compose.yml](https://github.com/kjedu/maxscale-docker/blob/master/maxscale/docker-compose.yml)

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

edit the [example.cnf](https://github.com/kjedu/maxscale-docker/blob/master/maxscale/maxscale.cnf.d/example.cnf) file

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

```
sudo docker-compose exec maxscale maxctrl list servers
```

![image](https://github.com/user-attachments/assets/34dd497e-9370-4a5e-a5a7-c140aace4375)

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

![image](https://github.com/user-attachments/assets/82286c6d-9bad-4407-a0a7-5f9c97e3a6ae)

## Results for zipcode_one

### Largest zipcode in zipcodes_one

```
SELECT * FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;
```
![image](https://github.com/user-attachments/assets/d1ba17eb-06cc-4c9e-bdcd-a8831ef43bf3)

### All zipcodes where state=KY

```
SELECT * FROM zipcodes_one.zipcodes_one WHERE State='KY';
```
![image](https://github.com/user-attachments/assets/946dedca-0f73-4656-9978-1d4418ca88f2)

### All zipcodes between 4000 and 4100

```
SELECT * FROM zipcodes_one.zipcodes_one WHERE zipcode BETWEEN 40000 and 41000;
```
![image](https://github.com/user-attachments/assets/094c91be-810b-4ad4-b4db-b4231fe6c6d1)

### TotalWages column where state=PA

```
SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE state= 'PA';
```
![image](https://github.com/user-attachments/assets/10248297-dc90-426c-842d-3a55f839fe09)

## Results for zipcode_two

### Largest zipcode in zipcodes_two

```
SELECT * FROM zipcodes_two.zipcodes_two ORDER BY Zipcode DESC LIMIT 1;
```
![image](https://github.com/user-attachments/assets/fdb18a34-10b9-495f-b3a6-d01c15d6c74b)

### All zipcodes where state=KY

```
SELECT * FROM zipcodes_two.zipcodes_two WHERE State='KY';
```

![image](https://github.com/user-attachments/assets/9c343d2d-8c85-4ca4-816e-4d4ff28b4d3d)

### All zipcodes between 4000 and 4100

```
SELECT * FROM zipcodes_two.zipcodes_two WHERE zipcode BETWEEN 40000 and 41000;
```

![image](https://github.com/user-attachments/assets/aab4a30f-3733-49be-a390-1f8dabe32c27)


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

Thanks to the CNE370 TA and professor for their help and quick response.

