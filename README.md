# mysql-selfmanaged

Google Cloud Platform (GCP) was used in this repo

# Setting up Virtual Machine
1. Open GCP and select Compute Engine
2. Click Create Instance. 
3. Select preferred settings <br>
    a. Name the virtual machine <br>
    b. Machine Configuration = For machine type, select E2 Medium. A mysql database requires minimum 2 CPU and 2GB RAM <br>
    c. Boot Disk = Click Change. For Operating System, select Ubuntu. For Version, select 19.04 LTS x86/64. Click select. <br>
    d. Firewall = "Select Allow HTTP traffic" and "Allow HTTPS traffic" <br>
    e. All other settings can be left at default.
4. Select Create 
5. Under the Connect column, click the drop down next to SSH. Select "Open in browser window". A new window with a terminal will open.

# Setting up OS and installing mysql
1. Type "sudo apt-get update" to update OS 
2. Type "sudo apt install mysql-server mysql-client". Type Y
    a. mysql-server = software that houses the database(s) <br>
    b. mysql-client = software that allows connecting to mysql server for queries, etc
3. Type "sudo mysql" to enter mysql server
4. Create user create user 'username'@'%' 
5. Grant all privileges on *.* to 'username'@'%' with grant option; <br>
    *.* = means to all databases and tables

# Make instance available to external computers
1. Exit out of mysql = \q
2. Type "sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf"
3. Scroll to find "bind-address"
4. Change the address to 0.0.0.0
5. Ctrl + O to save. Enter . Ctrl + X to exit
6. Type "sudo service mysql restart" to restart 
7. Go to console view to open port for mysql
8. Search for firewall. Select "Create Firewall Rule" at the top of page
9. Name firewall rule. Direction of traffic = ingress
10. Change Targets to "All instances in the network"
11. In the "Source IPv4 ranges" box, type 0.0.0.0/0 for accept connections from anywhere   
12. Scroll to "Protocols and Ports". Select TCP and add port 3306 in Ports box 
13. Create