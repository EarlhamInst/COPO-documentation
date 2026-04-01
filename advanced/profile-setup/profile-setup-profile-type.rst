.. _profile-setup-profile-type:

ProfileType
~~~~~~~~~~~~~~

ProfileType is an individual element or module that make up the profile. Each
profile type is uniquely identified and characterised by various fields that
determine its behaviour and appearance.

.. raw:: html

   <hr>

ProfileType Database Table Structure
-------------------------------------

**ProfileType** represents the overarching category or classification of a
profile. It defines the primary characteristics and settings that apply to
the profile as a whole. Understanding the structure and purpose of each
field helps in efficiently configuring and managing profile types in the
application.

The PostgreSQL table **ProfileType** consists of the following fields:

* ``id`` (Integer):
      The unique identifier for the profile type. It is used as the primary
      key to uniquely identify each profile type within the table.

      **Example**: ``1``, ``2``, ``3``, etc.

* ``type`` (String):
      The name or designation of the profile type. It serves as a label to
      easily identify the profile type. It is often used as the abbreviation
      or short form of the profile type.

      **Examples**: ``biodata``, ``dtol``, ``asg``, ``erga`` etc.

* ``description`` (String):
     A detailed description of the profile type.  It provides a comprehensive
     understanding of what the profile type represents and its scope.

     **Examples**:

        * ``Aquatic Symbiosis Genomics (ASG)``: A profile related to the
          :abbr:`ASG (Aquatic Symbiosis Genomics)` project.

        * ``Biodata``: A profile that operates independently. It was
          previously known as (Genomics(.

        * ``Darwin Tree of Life (DTOL)``: A profile related to the
          :abbr:`DToL (Darwin Tree of Life)` project.

        * ``Darwin Tree of Life Environmental Samples (DTOLENV)``: A profile
          for environmental samples within the
          :abbr:`DTOLENV (Darwin Tree of Life Environmental Samples)` project.

        * ``Genomics``: A profile that operates independently. It has been
          renamed *Biodata*.

        * ``European Reference Genome Atlas (ERGA)``: A profile related to the
          :abbr:`ERGA (European Reference Genome Atlas)` project.

        * ``Test New Profile``: A profile for testing purposes.

* ``widget_colour`` (String):
      The colour associated with the profile type, used for UI elements. It
      enhances the visual distinction and user interface by providing a
      specific colour for each profile type.

      **Examples**:

        * ``#00AAFF`` (blue)
        * ``#009c95`` (cyan)
        * ``#16ab39`` (green)
        * ``#fb7d0d`` (orange)
        * ``#5829bb`` (purple)
        * ``#E61A8D`` (magenta)
        * violet

* ``is_dtol_profile`` (Boolean):
      Indicates whether the profile type is related to the
      :abbr:`DToL (Darwin Tree of Life)` project. It helps in categorising and
      filtering profiles that are part of the
      :abbr:`DToL (Darwin Tree of Life)` project.

      **Examples**:

        * ``t`` (true): The profile is part of the
          :abbr:`DToL (Darwin Tree of Life)` project.
        * ``f`` (false): The profile is not part of the
          :abbr:`DToL (Darwin Tree of Life)` project.

* ``is_permission_required`` (Boolean):
      Indicates whether permissions are required to access this profile type.
      It ensures that sensitive or restricted profiles are only accessible by
      authorised users.

      **Examples**:

        * ``t`` (true): Permissions are required to access the profile
        * ``f`` (false): No special permissions are required to access the
          profile

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents

.. collapse:: ProfileType database fields and records

   .. code-block:: console

      id |   type   |                     description                     | widget_colour | is_dtol_profile | is_permission_required
      ----+----------+-----------------------------------------------------+---------------+-----------------+------------------------
       1 | asg      | Aquatic Symbiosis Genomics (ASG)                    | #5829bb       | t               | t
       2 | biodata  | Biodata                                             | #00AAFF       | f               | f
       3 | dtol     | Darwin Tree of Life (DTOL)                          | #16ab39       | t               | t
       4 | dtolenv  | Darwin Tree of Life Environmental Samples (DTOLENV) | #fb7d0d       | t               | t
       5 | erga     | European Reference Genome Atlas (ERGA)              | #E61A8D       | t               | t
       6 | genomics | Genomics                                            | #009c95       | f               | f
       7 | test     | Test New Profile                                    | violet        | f               | t

.. raw:: html

   <hr>

Usage of ProfileType
---------------------

Please check back soon for more information on how to use the profile type in
the project.

.. raw:: html

   <hr>

.. _visual-representation-profile-type:

Visualisation of ProfileType in Project
----------------------------------------

.. figure:: /assets/images/django-admin-interface/profile/profile-type/visual-display-profile-types-without-dropdown-menu.png
   :alt: Work profiles page where a profile type can be chosen to be created
         from the dropdown menu
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/django-admin-interface/profile/profile-type/visual-display-profile-types-without-dropdown-menu.png
   :class: with-shadow with-border

   **Work profiles page: Dropdown menu where a profile type can be chosen to
   be created**

.. figure:: /assets/images/django-admin-interface/profile/profile-type/visual-display-profile-types-with-dropdown-menu.png
   :alt: Profile types shown as dropdown menu options on the Work profiles page
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/django-admin-interface/profile/profile-type/visual-display-profile-types-with-dropdown-menu.png
   :class: with-shadow with-border

   **Work profiles page: Dropdown menu options of profile types that can be
   *created**

.. figure:: /assets/images/django-admin-interface/profile/profile-type/visual-display-profile-types-created-profiles.png
   :alt: A grid of created profiles on the Work profiles page
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/django-admin-interface/profile/profile-type/visual-display-profile-types-created-profiles.png
   :class: with-shadow with-border

   **Work profiles page: A grid of created profiles**

.. raw:: html

   <hr>

Related Topics
---------------

.. seealso::

   * :ref:`Defining ProfileType Django model <django-model-definition>`
   * :ref:`Component structure <profile-setup-component>`
   * :ref:`RecordActionButton structure <profile-setup-record-action-button>`
   * :ref:`TitleButton structure <profile-setup-title-button>`

.. raw:: html

   <hr>

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/arrow-right.png
   :height: 2ex
   :class: no-scaled-link

..
    Unicode declaration
..

.. |globe| unicode:: U+1F310

.. |section| unicode:: U+1F4D6
