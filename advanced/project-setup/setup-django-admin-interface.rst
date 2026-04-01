.. _setup-django-admin-interface:

Getting Started with COPO Admin Tools
-------------------------------------

The Django administration interface ("admin") is used to manage data and models
in the COPO web application. Once models are created and populated, the admin
interface provides an easy way to view and manage them.

Here are the steps to get started with it:

1. Setting Up the Admin Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you can use the Django admin interface, ensure that the project is
configured correctly:

**Admin app**: Ensure that ``django.contrib.admin`` is included in the
**INSTALLED_APPS** setting in ``settings.py``.

.. code-block:: python
   :caption: Snippet of settings.py file

   INSTALLED_APPS = [
        ...
        'django.contrib.admin',
        ...
   ]

**URLs**: Ensure that the admin URLs are included in the project’s ``urls.py``
file.

.. code-block:: python
   :caption: Snippet of urls.py file

   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
        path('admin/', admin.site.urls),
        path('myapp/', include('myapp.urls')),
   ]

**Superuser**: Create a superuser account to access the admin interface

.. code-block:: bash
   :caption: Command to create a superuser

    python manage.py createsuperuser

Follow the prompts to create a username, email and password.

.. raw:: html

   <hr>

2. Navigating to the Admin Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Run the development server**: Ensure that the development server is running.

.. code-block:: bash

   python manage.py runserver

**Access the admin interface**: Open your web browser and navigate to
http://127.0.0.1:8000/admin/. You will be presented with the Django admin login
page.

**Note**: ``127.0.0.1:8000`` refers to the machine running the COPO server.
If COPO is hosted elsewhere, replace it with the appropriate server address
(for example, https://your-server-name/admin/).

.. raw:: html

   <hr>

3. Logging into the Admin Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Login**: Use the superuser credentials you created earlier to log in. Enter
your username and password then, click the ``Log in`` button.

.. raw:: html

   <hr>

4. Using the Admin Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once logged in, you will be directed to the Django Admin dashboard, which
provides an overview of all registered models and available actions.

**Admin dashboard overview**

   **Site administration**: This section lists all the models registered in
   the admin site. For example, if you registered the
   :ref:`profile type model <profile-setup-profile-type>`, it will appear here.

   See the
   :ref:`Registering Django models <profile-setup-register-django-model>`
   section for more information on registering models.

**Groups and users**: By default, Django includes models for managing users
and groups.


**Managing actions**

   **Bulk actions**: Perform actions on multiple profiles simultaneously, such
   as deleting multiple profiles.

   **Custom actions**: Define custom actions for specific tasks.

.. raw:: html

   <hr>

Related Topics
~~~~~~~~~~~~~~

.. seealso::

  * `Official Django documentation <https://docs.djangoproject.com>`__
  *  `Official Python documentation <https://docs.python.org>`__
  * :ref:`project-application-structure`
  * :ref:`profile-setup-index`
