.. _project-local-setup-index:

========================
Local Setup Instructions
========================

.. _copo-project-setup-with-docker:

Project Setup With Docker
-------------------------

The central instance of COPO runs on a pool of three virtual machines (VMs) -
a swarm manager and two swarm workers that host the service and web
containers. However, for simplicity, this local setup uses a single node.

.. raw:: html

   <hr>

Step 1: Create Secrets
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   :caption: Create a directory to store file-based secrets

   mkdir local-project-setup
   cd local-project-setup

* Replace ``local-project-setup`` in the command above with the name of the
  directory you would like to create.

.. code-block:: bash
   :caption: Create secrets in an .env file in the directory created above

   cat <<EOF > .env
   vault_copo_mongo_initdb_root_password=secret123
   vault_copo_bioimage_path=secret123
   vault_copo_mail_password=secret123
   vault_copo_nih_api_key=secret123
   vault_copo_orcid_client_id=secret123
   vault_copo_orcid_secret_key=secret123
   vault_copo_public_name_service_api_key=secret123
   vault_copo_web_secret_key=secret123
   vault_copo_webin_user=secret123
   vault_copo_webin_user_password=secret123
   vault_ecs_secret_key=secret123
   vault_ecs_access_key=secret123
   ZENODOTOKEN=secret123
   vault_copo_bioimage_password=secret123
   EOF

.. raw:: html

   <hr>

Step 2: Download COPO project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the COPO project to your local machine. It does not have to be
downloaded in the same directory (``local-project-setup``) where the secrets
were created in step 1.

.. note::

   Take note of the absolute path to the project directory on your local
   machine as it will be used in the Docker compose file to mount the
   project directory as a volume in the Docker container in step 3.

.. code-block:: bash
   :caption: Clone the COPO project from GitHub to your local machine

   git clone https://github.com/EarlhamInst/COPO-production.git

* Alternatively, download the :download:`GitHub project ZIP file
  <https://github.com/EarlhamInst/COPO-production/archive/refs/heads/main.zip>`
  then, extract it on your local machine.

.. raw:: html

   <hr>

Step 3: Create a Docker Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   The following commands should be executed in the terminal in the
   ``local-project-setup`` directory that was created in step 1.

.. tip::

   Substitute all items enclosed in angle brackets (<>) with the appropriate
   values for your local setup.

.. code-block:: bash
   :caption: Navigate to the setup directory

   cd local-project-setup

.. tab-set::

   .. tab-item:: On Linux OS

      .. code-block:: bash
         :caption: Download the local Docker compose file from GitHub

         wget https://raw.githubusercontent.com/EarlhamInst/COPO-production/refs/heads/main/deployment/local.copo.compose.linux.yaml

      * Alternatively, download the :download:`Linux Docker compose file
        <https://raw.githubusercontent.com/EarlhamInst/COPO-production/refs/heads/main/deployment/local.copo.compose.linux.yaml>`
        then, extract it on your local machine.

      .. code-block:: bash
         :caption: Edit the local Docker compose file to reflect the Docker
                   image tag

         vim  local.copo.compose.linux.yaml

   .. tab-item:: On Mac OS

      .. code-block:: bash
         :caption: Download the local Docker compose file from GitHub

         wget https://raw.githubusercontent.com/EarlhamInst/COPO-production/refs/heads/main/deployment/local.copo.compose.mac.yaml

      * Alternatively, download the :download:`Mac Docker compose file
        <https://raw.githubusercontent.com/EarlhamInst/COPO-production/refs/heads/main/deployment/local.copo.compose.mac.yaml>`
        then, extract it on your local machine.

      .. code-block:: bash
         :caption: Edit the local Docker compose file to reflect the Docker
                   image tag

         vim  local.copo.compose.mac.yaml

.. code-block:: yaml
   :caption: Edit the image tag for the "copo_web" service in the Docker
             compose file

   services:
     copo_web:
       # Edit the image tag to reflect what you would like to build
       image: local_copo_web:v1.0.0
       ...
       ...
       # Edit the absolute path to the project directory on your local machine
       volumes:
         - /<path-to-project-directory>/COPO-production:/copo


Explanation of the commands above:

* ``vim`` is used as an example to edit files but you can use any text editor
  of your choice to edit the compose file like ``nano``.

* The local Docker image is created with the tag, ``local_copo_web:v1.0.0``.

  ``local_copo_web`` is the name of the Docker image and ``v1.0.0`` is the
  version.

* The path, ``/<path-to-project-directory>/COPO-production`` is the absolute
  path to the project directory on your local machine.

* ``/copo`` is the path to the Django project app within the Docker container.

*  In the Docker compose file, the environment variables related to
   European Nucleotide Archive (ENA) are configured to use the ENA development
   server. Submissions to this server are deleted after 24 hours. To submit to
   the production ENA server, remove ``dev`` from the values.

.. raw:: html

   <hr>

Step 4: Build Docker Image
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   The following commands should be executed in the terminal in the
   ``COPO-production`` directory that was downloaded in step 2.

.. code-block:: bash
   :caption: Navigate to the project root directory (if you are not already
             there)

   cd COPO-production

.. tab-set::

   .. tab-item:: On Linux OS

      .. code-block:: bash
         :caption: Build Docker image

         docker build . -f  'deployment/web/Dockerfile_local_linux' -t local_copo_web:v1.0.0

   .. tab-item:: On Mac OS

      .. code-block:: bash
         :caption: Build Docker image

         docker build . -f  'deployment/web/Dockerfile_local_mac' -t local_copo_web:v1.0.0


* The Docker image tag, ``local_copo_web:v1.0.0``, references the tag that was
  created in the Docker compose file in step 3.

* The Dockerfile is located in the **deployment/web** directory of the COPO
  project. Use the appropriate Dockerfile for your operating system (OS).

.. raw:: html

   <hr>

Step 5: Deploy the Docker Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   The following commands should be executed in the terminal in the
   ``local-project-setup`` directory that was created in step 1.

   It should have the **.env** file and Docker compose file that were created
   in step 1 and step 3 respectively.

.. code-block:: bash
   :caption: Navigate to the setup directory

   cd local-project-setup

.. tab-set::

   .. tab-item:: On Linux OS

      .. code-block:: bash
         :caption: Deploy Docker image

          export $(cat .env) > /dev/null 2>&1; docker compose -f local.copo.compose.linux.yaml up -d

   .. tab-item:: On Mac OS

      .. code-block:: bash
         :caption: Deploy Docker image

          export $(cat .env) > /dev/null 2>&1; docker compose -f local.copo.compose.mac.yaml up -d

.. code-block:: bash
   :caption: View the created Docker containers

   docker ps

.. raw:: html

   <hr>

Step 6: Execute Celery & Django commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console
   :caption: Enter the **local_copo_web** Docker container

   # Retrieve the "local_copo_web" container ID
   $ docker ps

   # Enter the container using the ID
   $ docker exec -it <local-copo-web-container-id> bash

.. code-block:: console
   :caption: Setup scripts to be executed in the **local_copo_web** Docker
             container

   python manage.py makemigrations
   python manage.py makemigrations allauth
   python manage.py migrate
   python manage.py setup_groups
   python manage.py createcachetable
   python manage.py setup_sequencing_centres
   python manage.py social_accounts

.. code-block:: console
   :caption: Enter the **copo/copo-mongo** Docker container

   # Exit the "local_copo_web" container by inputting:
     CTRL + P
     CTRL + Q

   # Retrieve the "copo/copo-mongo" container ID
   $ docker ps

   # Enter the container using the ID
   $ docker exec -it <copo-mongo-container-id> bash

.. code-block:: bash
   :caption: Initialise Mongo database replica set as "copo_admin" user in the
             **copo/copo-mongo** Docker container

   # Enter the Mongo shell
   mongosh

   # Switch to the "admin" database
   use admin

   # Authenticate as "copo_admin" user
   db.auth("copo_admin", "password")

   # Initialise the replica set
   rs.initiate()

.. code-block:: console
   :caption: Return to the **local_copo_web** Docker container

   # Exit the "copo-mongo" container by inputting:
     CTRL + P
     CTRL + Q

   # Retrieve the "local_copo_web" container ID
   $ docker ps

   # Enter the container using the ID
   $ docker exec -it <local-copo-web-container-id> bash

.. code-block:: python
   :caption: Run additional Django commands in the **local_copo_web** Docker
             container

   python manage.py setup_schemas
   python manage.py setup_associated_profile_types
   python manage.py setup_profile_types
   python manage.py setup_news

.. code-block:: python
   :caption: Create a Django admin user in the **local_copo_web** Docker
             container

   python manage.py createsuperuser

* Enter the required details to create a Django admin or superuser. This
  individual will have the privilege to log into the admin section of the COPO
  project using URL, http://127.0.0.1:8000/admin.

.. code-block:: bash
   :caption: Run celery commands to populate the database with data

   # Switch to root user if not already it
   sudo -i

   # Execute celery commands
   celery -A src call src.apps.copo_single_cell_submission.tasks.update_singlecell_schema
   celery -A src call src.apps.copo_core.tasks.update_ena_read_checklist
   celery -A src call src.apps.copo_core.tasks.update_ena_checklist
   celery -A src call src.apps.copo_core.tasks.update_ena_read_platform

.. raw:: html

   <hr>

Step 7: Launch COPO website
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

7.1: Download Visual Studio Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Visual Studio Code (VS Code) is an integrated development environment (IDE)
recommended for running the COPO project on your local machine. It
can be downloaded from the `VS Code website <https://code.visualstudio.com/>`__.

7.2: Install extensions to Visual Studio Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to the **Extensions** tab (indicated by the |vs-code-extensions-icon|
icon) on the left-hand side of the :abbr:`VS Code (Visual Studio Code)` window.
Then, search for and install the following extensions:

* `Dev Containers <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers>`__
  by Microsoft Corporation
* `Python <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`__
  by Microsoft Corporation
* `Python Debugger <https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy>`__
  by Microsoft Corporation

7.2.1: Optional applications to install on your local machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Docker Desktop**: a graphical user interface (GUI) application
  that allows you to manage Docker containers and images. It can be
  downloaded from the
  `Docker Desktop website <https://www.docker.com/products/docker-desktop>`__.

* **Studio 3T Community Edition**: a :abbr:`GUI (Graphical User Interface)`
  application that allows  you to manage your MongoDB databases. It can be
  downloaded from the `Studio 3T website <https://studio3t.com/download/>`__.

  .. code-block:: bash
     :caption: Local connection string to connect to MongoDB database in the Docker container

     mongodb://copo_user:password@localhost:27017/admin?retryWrites=true&loadBalanced=false&connectTimeoutMS=10000&authSource=admin&authMechanism=SCRAM-SHA-1

7.3: Use Dev Containers extension to launch the COPO project application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**7.3.1**: Click the **Dev Containers** extension (which was installed in step
7.2) on the left-hand side of the :abbr:`VS Code (Visual Studio Code)` as shown
in the image below.

.. figure:: /assets/images/setup/ui/project-setup-pointer-to-vscode-extension.png
   :alt: Accessing the Dev Containers extension in VS Code
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/project-setup-pointer-to-vscode-extension.png
   :class: with-shadow with-border
   :height: 400px

   **Click** ``Dev Containers`` **VS Code extension**

**7.3.2**: Right-click on the ``local_copo_web:v1.0.0`` container under the
**CONTAINERS** section then, click "Attach Visual Studio Code" as shown in the
image below.

.. note::

   Note that the example below uses the Docker tag, *local_copo:v1.0.0*.
   This corresponds to the tag you created for the local Docker image in
   step 3 where it was specified as ``local_copo_web:v1.0.0``.

.. figure:: /assets/images/setup/ui/project-setup-pointer-to-open-docker-container-with-vscode.png
   :alt: Opening the COPO project application in VS Code using the Dev Containers extension
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/project-setup-pointer-to-open-docker-container-with-vscode.png
   :class: with-shadow with-border
   :height: 400px

   **Click** ``Attach Visual Studio Code`` **option for** ``local_copo_web:v1.0.0`` **Docker container**

**7.3.3**: Click "Open Folder" button under the **EXPLORER** section. Then,
enter ``/copo`` in the prompt that appears and click "OK" to open the project
folder in the container.

.. figure:: /assets/images/setup/ui/project-setup-pointer-to-open-project-folder-in-container-in-vscode.png
   :alt: Opening the COPO project folder in Docker container in VS Code
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/project-setup-pointer-to-open-project-folder-in-container-in-vscode.png
   :class: with-shadow with-border

   **Open** ``/copo`` **directory in the Docker container**

* If prompted, enable **Manage Unsafe Repositories** in **Source Control**
  section in VS Code to allow it to access the project directory.

**7.3.4**: Click |vs-code-run-and-debug-icon| to navigate to the
**Run and Debug** section. Then, click the dropdown menu next to the green
play button.

.. figure:: /assets/images/setup/ui/project-setup-pointer-run-and-debug-project-in-vscode.png
   :alt: Opening the COPO project folder in Docker container in VS Code
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/project-setup-pointer-run-and-debug-project-in-vscode.png
   :class: with-shadow with-border

   **Click run and debug icon**

**7.3.5**: A list of configurations will be displayed. They are set up in
the **launch.json** file located in the ``.vscode`` directory in the project.

Click the following configurations to run the COPO project application:

* Python: Django
* Python: Celery Beat
* Python: Celery Workers

.. collapse:: Click to view the contents of the VS Code launch.json
              configuration file

   .. literalinclude:: /assets/files/setup/project/launch.json
      :language: json
      :caption: VS Code **launch.json** configuration file contents

.. raw:: html

   <br>

.. figure:: /assets/images/setup/ui/project-setup-pointer-run-and-debug-project-in-vscode-with-configurations-list.png
   :alt: Opening the COPO project folder in Docker container in VS Code
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/project-setup-pointer-run-and-debug-project-in-vscode-with-configurations-list.png
   :class: with-shadow with-border

   **List of configurations set up in the launch.json file**

**7.3.6**: Access the COPO project application locally on port 8000 by
searching for http://127.0.0.1:8000 in your web browser.

Searching for http://127.0.0.1:8000/copo will take you to the **Work profiles**
page of the application. An Orcid login will be required to access the
application. You can `create an Orcid account <https://orcid.org/register>`__
after which, you can use the credentials to log into the application.

.. raw:: html

   <hr>

Useful Git Commands
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   :caption: Set GitHub configuration in terminal

   git config --global user.name "<github-username>"
   git config --global user.email "<github-email-address>"

.. code-block:: bash
   :caption: Create a tag via the terminal

   git tag <tag-name>

.. code-block:: bash
   :caption: Push a particular tag to GitHub via the terminal

   git push origin <tag-name>

.. code-block:: bash
   :caption: Remove an existing tag from GitHub via the terminal

   git tag -d <tag-name>

.. raw:: html

   <hr>

Related Topics
~~~~~~~~~~~~~~~

.. seealso::

   `Docker documentation: Building an application <https://docs.docker.com/get-started/02_our_app/>`__

.. raw:: html

   <hr>

.. _copo-project-setup-without-docker:

Project Setup Without Docker
-----------------------------

Choose the appropriate link below based on your operating system (OS) to
set up the project locally.

.. toctree::
   :titlesonly:

   Set Up Project on Linux <copo-project-setup-linux>
   Set Up Project on Windows <copo-project-setup-windows>

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/arrow-right.png
   :height: 2ex
   :class: no-scaled-link

.. |vs-code-extensions-icon| image:: /assets/images/setup/icons/vscode-icon-extensions.png
   :height: 3ex
   :class: no-scaled-link

.. |vs-code-run-and-debug-icon| image:: /assets/images/setup/icons/vscode-icon-debug.png
   :height: 3ex
   :class: no-scaled-link
