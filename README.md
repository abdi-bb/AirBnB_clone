# AirBnB Clone
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
## Authors
* Abdi Berhe
* Daniel Tsega
