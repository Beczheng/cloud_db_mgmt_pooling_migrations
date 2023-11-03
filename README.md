# cloud_db_mgmt_pooling_migrations

### Assignment
- Course: HHA 504
- Homework assignment #4c: Gain practical experience in managing a cloud-based MySQL database with a focus on implementing connection pooling and performing database migrations.

### Connection Pooling Setup
#### 1. Azure
- Login to your Microsoft Azure account.
- Type in `Azure Database for MySQL` in the search bar.
- Click `create`.
- Click `create` under flexible server.
- Now, follow the table in order:
<br>

  | Tab | Section | Steps |
  | --- | --- | --- |
  | Basics | Project details | Create a name for your resource group. |
  | Basics | Server details | Create a name for your instance. Then, click `configure server` and change the compute tier `Burstable (1-20 vCores)`. Then, change the compute size to `Standard_B1s (1 vCore, 1 GiB memory, 400 max iops)`.|
  | Basics | Authentication | Create a username and password. |
  | Networking | Network connectivity | Click the `public access (allowed IP addresses) and private endpoint` option. |
  | Networking | Firewall rules | Click `+ Add 0.0.0.0 - 255.255.255.255` and `+ Add current client IP address (xx.xxx.xxx.xxx)`. |
  | | | Click create instance. |

- Once you've created your instance, go to server parameters and set `max_connections` to `20` and `connect_timeout` to `3`.

#### 2. GCP
- Login to your Google Cloud account.
- Click the navigation menu and then click `SQL`.
- Click `create instance` and then click `choose MySQL`.
- Now, follow the table in order:
<br>

  | Section | Subsection | Steps |
  | --- | --- | --- |
  | Instance info | | Create an instance ID and password. |
  | Choose a Cloud SQL edition | | Click the `enterprise` option. |
  | Choose a Cloud SQL edition | Choose preset for this edition. Presets can be customized later as needed. | Click `sandbox` option. |
  | Customize your instance | Machine configuration | Click the `shared core` option. Then click the `1 vCPU, 0.164GB` option. |
  | Customize your instance | Connections | Click the `public IP address` option. Then, under authorized network, click `add a network`. Name the network as `allow all` and set it to `0.0.0.0/0`. |
  | | | Click create instance. |

### Database Schema and ERD
- For the database, I created two tables: `patients` and `doctors`. In the `patients` table, I included the following columns: `id, first_name, last_name, date_of_birth, and gender`. In the `doctors` table: I included the following columns: `id, patient_id, first_name, last_name, and specialization`. Then, I created an `address` column for both tables using Alembic. To see screenshots of the ERD, click [here](https://github.com/Beczheng/cloud_db_mgmt_pooling_migrations/tree/main/screenshots).

### Flask
- To see screenshots of my flask applicaition, click [here](https://github.com/Beczheng/cloud_db_mgmt_pooling_migrations/tree/main/screenshots).
