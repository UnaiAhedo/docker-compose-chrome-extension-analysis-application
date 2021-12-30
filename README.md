# Docker compose for the services needed into the chrome extension analysis application

This project is created for the use of [Chrome extension analysis application](https://github.com/UnaiAhedo/Chrome-extensions-market-analisys).

## How to use it
Download and extract the project. In the extracted folder, where you can find the **docker-compose.yml** do the following:

First you need yo build the containers, for that, use the next command.
> docker-compose build --build-arg GDRIVE_DL_LINK=1GA2Idb9LhpepGwGIRCiqoPok6mYWWE3M

After building the containers, use the next command to run them.
> docker-compose up
