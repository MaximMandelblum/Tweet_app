# tweetMongo applicatio

Create a dockerized system for the storage &amp; retrieval of usernames the tweets of which contain the word "docker" to and from a NoSQL database (MongoDB).

Please follow the order below :


1. Run get_repo_files.yml playbook in order to clone the source code files to your local directory .

2. Install terraform , after that put the access key and secret key in credentials config file .
   Then run the terraform to build the AWS Environment .

Plesae note ! need to replace the keys and tokens variables with valid values from the Developer Twitter before running the running_scripts_file.yml playbook (locate in tweety.py file).

After bringing up the environment via terraform , please run the  playbooks in the following order :

1. init_system.yml - configuring and initing the system
2. install_docker.yml - install docker engine  
3. bring_up_application.yml - bring up the docker service (using docker-compose.yml file) , access apache on port 8082
4. running_scripts_files.yml - running the python scripts files  , to create the capped collection and start the tweeter application

In order to test the application by query  collection , live before using the apache use the script live_tweet_query.py .
