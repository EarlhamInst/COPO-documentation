.. _profile-setup-index:

Setting Up Profiles with Python/Django
--------------------------------------

This section explores how to use the Django administration interface ("admin")
to set up and configure profiles [#f1]_.

See :ref:`Project Application Structure <project-application-structure>` to
understand the structure of the Django project.

.. note::

   This section assumes basic knowledge of Django and Python. If you are new
   to either, see the official `Django <https://docs.djangoproject.com>`__
   and `Python <https://docs.python.org>`__ documentation.

.. raw:: html

   <hr>

.. _profile-structure:

1. Defining the Profile Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Profile setup is modular, meaning each part of a profile is managed separately.
Each part has its own model and can be configured independently, while still
contributing to the overall profile.

These parts are stored in separate PostgreSQL database tables and managed
through the Django Admin interface. Understanding how each part works helps
administrators manage profiles more efficiently.

Select a link below to learn how to configure each part.

.. toctree::
   :titlesonly:

   profile-setup-profile-type
   profile-setup-component
   profile-setup-record-action-button
   profile-setup-title-button

.. raw:: html

   <hr>

.. _django-model-definition:

2. Defining Django Model
~~~~~~~~~~~~~~~~~~~~~~~~

Define the  model in a ``models.py`` Python file. This model describes the
structure of the database table.

.. note::

   The  ``models.py`` file should be located in the same directory as the
   ``admin.py`` file. It can be used to define all models for the Django
   application. There is **no** need to create a separate model file for
   each model.

.. hint::

   * Click the |collapsible-item-arrow| button below to view the contents of
     the Python Django model file.

   * View the implementation of the models used in the
     `COPO project on GitHub <copo-github-models-file_>`_

.. collapse:: ProfileType model

   .. literalinclude:: /assets/files/setup/profile/profile_type_model.py
      :language: python
      :caption: ProfileType Python Django model definition

.. raw:: html

   <br>

.. collapse:: Component model

   .. literalinclude:: /assets/files/setup/profile/component_model.py
      :language: python
      :caption: Component Python Django model definition

.. raw:: html

   <br>

.. collapse:: RecordActionButton model

   .. literalinclude:: /assets/files/setup/profile/record_action_button_model.py
      :language: python
      :caption: RecordActionButton Python Django model definition

.. raw:: html

   <br>

.. collapse:: TitleButton model

   .. literalinclude:: /assets/files/setup/profile/title_button_model.py
      :language: python
      :caption: TitleButton Python Django model definition

.. raw:: html

   <hr>

.. _profile-setup-register-django-model:

3. Registering Django Model with Django Admin Site
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This step makes the model available in the Django Admin interface after the
model has been defined.

An admin class can be defined in the ``admin.py`` file to describe how the
model is displayed in the Django Admin interface. The display and behaviour
of each field in the model can be customised on the Django admin interface
like filters, search fields and more.

No admin class is required if you want to use the default Django Admin
interface for the model. The example below demonstrates how to register a
model with the default Django Admin interface using the
``admin.site.register()`` method.

The ``admin.site.register()`` method associates the model with the admin class
and makes it available in the Django Admin interface.

.. note::

   * The  ``admin.py`` file should be located in the same directory as the
   * ``models.py`` file. It can be used to register all models with the Django
     Admin interface. There is **no** need to create a separate admin file
     for each model.

   * Replace ``ModelName`` with the actual model name in the code snippet
     below.

.. hint::

   View the implementation of the ``admin.py`` file used in the
   `COPO project on GitHub <copo-github-admin-file_>`_

.. code-block:: python

   # admin.py
   from django.contrib import admin
   # Import the model. Replace ModelName with the actual model name
   from .models import ModelName

   # Register the admin class with the associated model
   admin.site.register(ModelName)

.. raw:: html

   <hr>

.. _profile-setup-migrating-django-models:

4. Make Migrations and Migrate the Django Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   Skipping these steps will cause the database to not match the models,
   leading to errors when using Django.

After creating and registering a Django model, run ``makemigrations`` and
``migrate``. ``makemigrations`` generates migration files for model changes
and ``migrate`` applies these changes to the database.

Run the following commands in the terminal to create and apply migrations:

.. code-block:: bash

   python manage.py makemigrations
   python manage.py migrate

.. raw:: html

   <hr>

.. _creating-setup-profile-python-command:

5. Automating Profile Creation with manage.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After registering the models, create a ``setup_profile_types.py`` Django
management command to automate the profile and subpart creation. Store this
command in the ``management/commands/`` directory of the Django app.

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents of the
   Python management command file, ``setup_profile_types.py``. The actual
   implementation may vary based on your specific requirements.

   View the implementation of the COPO
   `management command on GitHub <copo-github-management-command-file_>`__.

.. collapse:: Setup profile management command

   .. literalinclude:: /assets/files/setup/profile/setup_profile_types.py
      :language: python
      :caption: Python **setup_profile_types.py** Python management command
                file contents

.. raw:: html

   <br><br>

Execute the management command using the following:

.. code-block:: bash

   python manage.py setup_profile_types


.. raw:: html

   <hr>

.. _visual-representation-profile-subparts:

Visual Representation of Profile Subparts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select a link below to view each profile subpart within COPO.

* :ref:`ProfileType <visual-representation-profile-type>`

* :ref:`Component <visual-representation-component>`

* :ref:`RecordActionButton <visual-representation-record-action-button>`

* :ref:`TitleButton <visual-representation-title-button>`

.. raw:: html

   <hr>

Related Topics
~~~~~~~~~~~~~~

.. seealso::

   * :ref:`project-local-setup-index`

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Also known as COPO profile.

         See: :term:`COPO profile or work profile<COPO profile>`.

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/arrow_right.png
   :height: 2ex
   :class: no-scaled-link

..
    Link declaration
..

.. _copo-github-admin-file: https://github.com/EarlhamInst/COPO-production/blob/main/src/apps/copo_core/admin.py
.. _copo-github-models-file: https://github.com/EarlhamInst/COPO-production/blob/main/src/apps/copo_core/models.py
.. _copo-github-management-command-file: https://raw.githubusercontent.com/EarlhamInst/COPO-production/refs/heads/main/src/apps/copo_core/management/commands/setup_profile_types.py
