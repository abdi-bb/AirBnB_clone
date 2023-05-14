# AirBnB Clone
![Hbnb logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230514%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230514T202435Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5cfbbfedfb7b1bd4a00671850b774a78602afc7d815140247175cd00183a7612 "Hbnb Logo")
## Overview
Airbnb is an online platform that connects travelers with unique accommodations and experiences around the world. It allows individuals to rent out their homes or spare rooms to travelers, providing a personalized and local alternative to traditional hotels.
## Description
This is the first phase of the **AirBnB** clone series which is done while attending **ALX Full Stack Software Engineering** program. In this phase of the project we focused on building the **Console** using python **cmd** module. This command line interface let's developers to **create**, **destroy**, **update** and **show** several classes and objects, But the main idea is to enable developers with a good debuging and testing enviroment.
## Technologies
This projcet is build on **Ubuntu 20.04 LTS** in **Python 3**
## Showcase
###### Example
```
root@1f6c38b9068b:/AirBnB_clone# ./console.py 
(hbnb) create User
db3532fc-9cce-4234-b88d-b1e5200acf71
(hbnb) show User db3532fc-9cce-4234-b88d-b1e5200acf71
[User] (db3532fc-9cce-4234-b88d-b1e5200acf71) {'id': 'db3532fc-9cce-4234-b88d-b1e5200acf71', 'created_at': datetime.datetime(2023, 5, 14, 14, 39, 7, 408474), 'updated_at': datetime.datetime(2023, 5, 14, 14, 39, 7, 408487)}
(hbnb) all User
["[User] (a8d9cb26-8dcd-4aeb-a745-230c683aa9ec) {'id': 'a8d9cb26-8dcd-4aeb-a745-230c683aa9ec', 'created_at': datetime.datetime(2023, 5, 14, 14, 36, 49, 719683), 'updated_at': datetime.datetime(2023, 5, 14, 14, 36, 49, 719697)}", "[User] (db3532fc-9cce-4234-b88d-b1e5200acf71) {'id': 'db3532fc-9cce-4234-b88d-b1e5200acf71', 'created_at': datetime.datetime(2023, 5, 14, 14, 39, 7, 408474), 'updated_at': datetime.datetime(2023, 5, 14, 14, 39, 7, 408487)}"]
(hbnb) update User db3532fc-9cce-4234-b88d-b1e5200acf71 name "Danny"
(hbnb) show User db3532fc-9cce-4234-b88d-b1e5200acf71
[User] (db3532fc-9cce-4234-b88d-b1e5200acf71) {'id': 'db3532fc-9cce-4234-b88d-b1e5200acf71', 'created_at': datetime.datetime(2023, 5, 14, 14, 39, 7, 408474), 'updated_at': datetime.datetime(2023, 5, 14, 14, 41, 5, 778488), 'name': 'Danny'}
(hbnb) all
["[User] (a8d9cb26-8dcd-4aeb-a745-230c683aa9ec) {'id': 'a8d9cb26-8dcd-4aeb-a745-230c683aa9ec', 'created_at': datetime.datetime(2023, 5, 14, 14, 36, 49, 719683), 'updated_at': datetime.datetime(2023, 5, 14, 14, 36, 49, 719697)}", "[User] (db3532fc-9cce-4234-b88d-b1e5200acf71) {'id': 'db3532fc-9cce-4234-b88d-b1e5200acf71', 'created_at': datetime.datetime(2023, 5, 14, 14, 39, 7, 408474), 'updated_at': datetime.datetime(2023, 5, 14, 14, 41, 5, 778488), 'name': 'Danny'}"]
(hbnb) destroy User a8d9cb26-8dcd-4aeb-a745-230c683aa9ec
(hbnb) destroy User db3532fc-9cce-4234-b88d-b1e5200acf71
(hbnb) all
[]
(hbnb) show User
** instance id missing **
(hbnb) 
```
## Installation
```
$ git clone https://github.com/..../AirBnB_clone.git
```
## Authors
* Abdi Berhe
* Daniel Tsega
