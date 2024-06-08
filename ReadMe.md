[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FBzKYJru)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=15242247)
Bobby Kvidt
6/8/2024

Note: I'm not sure if there was supposed to be a column Status and Pending autofilling underneath it already, but there was. So I just added a second one.

Anyways, the code imports the csv library and then reads the security_incidents document. After reading, it then stores the document as a list where each row is an indicy -I have no idea if that's spelled correctly.

After storing it as a list, we then create some varibles that store our new header and default value strings.

Then, the header and rows variable are set up.
The header variable starts with the very first index in the list which is the first row. This adds a new column to the end of the row.
The rows variable then adds the new default value by iterating through every index from 1 and onwards.

Finally, we call the csv function in write mode, where we then have it write the new column and adjust the rows accordingly.