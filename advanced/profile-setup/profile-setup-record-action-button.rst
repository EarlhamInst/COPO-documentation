.. _profile-setup-record-action-button:

RecordActionButton
~~~~~~~~~~~~~~~~~~~~~

Record action buttons are individual elements or modules that make up the
profile and managed through a Django Admin model. Each button in the profile
serves a specific function, enabling users to perform various actions on
records within the profile.

.. raw:: html

   <hr>

RecordActionButton Database Table Structure
-------------------------------------------

The **RecordActionButton** in Django Admin provides a structured way to manage
and perform actions on profile records. Each button is meticulously defined
with attributes that ensure it functions correctly and provides clear feedback
to users.

These actions can include creating, updating, submitting or deleting records
among other functions. Understanding the fields and their purposes can
significantly enhance the management and usability of profiles in a Django
application.

The PostgreSQL table **RecordActionButton** consists of the following fields:

* ``id`` (Integer):
      The unique identifier for the action button. It is auto-incremented by
      the database.

* ``name`` (String):
      The internal name of the action button, used in the back-end code to
      reference the button.

* ``title`` (String):
      The display title of the action button, shown to users in the
      :abbr:`UI (User Interface)`. It describes the action the button
      performs in a concise manner.

* ``label`` (String):
      The short label shown on the button, providing a brief indication was the
      button does.

* ``type`` (String):
      The type of action the button performs, such as single (acting on a
      single record) or multi (acting on multiple records).

* ``error_message`` (String):
      The error message displayed to users if the action cannot be completed.
      This helps in providing feedback to users about why an action failed.

* ``icon_class`` (String):
      The :abbr:`CSS (Cascading Style Sheets)` class for the icon associated
      with the button, providing a visual representation of the button's
      action and help improve user interface design.

* ``action`` (String):
      The specific action performed by the button, often mapped to a function
      or a :abbr:`URL (Uniform Resource Locator)` ndpoint that the action
      will call.

* ``icon_colour`` (String):
      The colour of the icon used for :abbr:`UI (User Interface)` consistency
      and visual cues thereby helping users to quickly identify the type of
      action.

* ``tour_id`` (String):
      The identifier for the tour associated with the button. It links the
      button to a specific tour that provides guidance or help messages to
      users.

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents

.. collapse:: Example records for the ProfileActionButton model, detailing
              the various actions available within a profile

   .. code-block:: console

       id |              name                       |                   title                    |          label           |  type  |                                     error_message                                     |      icon_class       |          action                     | icon_colour |             tour_id
      ----+-----------------------------------------+--------------------------------------------+--------------------------+--------+---------------------------------------------------------------------------------------+-----------------------+-------------------------------------+-------------+----------------------------------
        1 | add_local_all                           | Add file by browsing local file system     | Add                      |        | Add file by browsing local file system                                                | fa fa-desktop         | add_files_locally                   | blue        | add_file_record_button_local
        2 | add_record_all                          | Add record                                 | Add                      |        |                                                                                       | fa fa-plus-circle     | add                                 | blue        | add_record_button
        3 | add_terminal_all                        | Add file by terminal                       | Add                      |        |                                                                                       | fa fa-terminal        | add_files_by_terminal               | blue        | add_file_record_button_terminal
        4 | delete_read_multi                       | Delete records                             | Delete                   | multi  | Please select one or more records to delete                                           | fa fa-trash-can       | delete_read                         | red         | delete_record_button
        5 | delete_record_multi                     | Delete records                             | Delete                   | multi  | Please select one or more records to delete                                           | fa fa-trash-can       | validate_and_delete                 | red         | delete_record_button
        6 | delete_sample_multi                     | Delete records                             | Delete                   | multi  | Please select one or more records to delete                                           | fa fa-trash-can       | delete_sample                       | red         | delete_record_button
        7 | delete_singlecell_multi                 | Delete records                             | Delete                   | multi  | Please select one or more records to delete                                           | fa fa-trash-can       | delete_singlecell                   | red         | delete_record_button
        8 | download_general_sample_manifest_single | Download manifest                          | Download manifest        | single | Please select one of samples in the manifest to download                              | fa fa-download        | download-sample-manifest            | blue        | download_manifest_record_button
        9 | download_permits_multiple               | Download permits                           | Download permits         | multi  | Please select one or more sample records from the table shown to download permits for | fa fa-download        | download-permits                    | orange      | download_permits_record_button
       10 | download_sample_manifest_single         | Download manifest                          | Download manifest        | single | Please select one of samples in the manifest to download                              | fa fa-download        | download-sample-manifest            | blue        | download_manifest_record_button
       11 | download_singlecell_manifest_single     | Download manifest                          | Download manifest        | single | Please select one of studies in the manifest to download                              | fa fa-download        | download-singlecell-manifest        | blue        | download_manifest_record_button
       12 | download_tagged_seq_single              | Download manifest                          | Download manifest        | single | Please select one of tagged sequences (or barcoding data) in the table to download    | fa fa-download        | download-tagged-seq-manifest        | blue        | download_manifest_record_button
       13 | edit_record_single                      | Edit record                                | Edit                     | single | Please select a record to edit                                                        | fa fa-pencil-square   | edit                                | green       | edit_record_button
       14 | make_snapshot                           | Make snapshot                              | Make snapshot            | single | Please select one record to make snapshot                                             | fa fa-camera-retro    | make_snapshot                       | grey        | make_snapshot_record_button
       15 | publish_singlecell_single_ena           | Publish record to ENA                      | Publish to ENA           | single | Please select one record to publish                                                   | fa fa-info-circle     | publish_singlecell_ena              | teal        | publish_record_button publish_study
       16 | publish_singlecell_single_zenodo        | Publish record to ZENODO                   | Publish to ZENODO        | single | Please select one record to publish                                                   | fa fa-info-circle     | publish_singlecell_zenodo           | blue        | publish_record_button_zenodo
       17 | releasestudy                            | Publish study                              | Publish study            | single |                                                                                       | fa fa-globe           | release_study                       | blue        | publish_record_button
       18 | submit_annotation_multi                 | Submit annotation                          | Submit                   | multi  | Please select one or more record to submit                                            | fa fa-info-circle     | submit_annotation                   | teal        | submit_record_button
       19 | submit_assembly_multi                   | Submit assembly                            | Submit                   | multi  | Please select one or more record to submit                                            | fa fa-info-circle     | submit_assembly                     | teal        | submit_record_button
       20 | submit_general_sample_multi             | Submit sample to ENA                       | Submit to ENA            | multi  | Please select one or more record to submit                                            | fa fa-info-circle     | submit_sample                       | teal        | submit_record_button
       21 | submit_read_multi                       | Submit read                                | Submit                   | multi  | Please select one or more record to submit                                            | fa fa-info-circle     | submit_read                         | teal        | submit_record_button
       22 | submit_singlecell_single_ena            | Submit record to ENA                       | Submit to ENA            | single | Please select one record to submit                                                    | fa fa-info-circle     | submit_singlecell_ena               | teal        | submit_record_button
       23 | submit_singlecell_single_zenodo         | Submit record to ZENODO                    | Submit to ZENODO         | single | Please select one record to submit                                                    | fa fa-info-circle     | submit_singlecell_zenodo            | blue        | submit_record_button_zenodo
       24 | submit_tagged_seq_multi                 | Submit Tagged sequence                     | Submit                   | multi  | Please select one or more record to submit                                            | fa fa-info-circle     | submit_tagged_seq                   | teal        | submit_record_button
       25 | view_images_multiple                    | View images                                | View images              | multi  | Please select one or more sample records from the table shown to view images for      | fa fa-eye             | view-images                         | teal        | view_images_record_button

.. raw:: html

   <br><br>

.. collapse:: Description of some RecordActionButton records

   .. raw:: html

      <br>

  * **add_record_all**: *Add new record* button

       Allows users to add a new record to the profile. It displays the tooltip *Add*
       when hovered over and uses a blue ``fa fa-plus`` icon.

  * **edit_record_single**: *Edit record* button

       Enables users to edit an existing record. This button is labeled *Edit*
       and it uses a green
       ``fa fa-pencil-square-o`` icon. It shows an error message, *Please
       select a record to edit*, if no record is
       selected.

  * **delete_record_multi**: *Delete records* button

       Allows users to delete multiple records at once. This multi-action
       button uses a red ``fa fa-trash-can`` icon
       and prompts users to *Please select one or more records to delete* if no
       records are selected.

  * **submit_assembly_multi**: Submit Assembly

       |section| :ref:`Section on Button Usage in the Project
       <assemblies-submission-section>`

  * **submit_annotation_multi**: Submit Sequence Annotation

       |section| :ref:`Section on Button Usage in the Project
       <sequence-annotations-submission-section>`

  * **submit_read_multi**: Submit Reads

       |section| :ref:`Section on Button Usage in the Project
       <reads>`

  * **add_local_all**: Add new file by browsing local file system

       |section| :ref:`Section on Button Usage in the Project
       <files-submission-via-browser>`

  * **add_terminal_all**: Add new file by terminal

       |section| :ref:`Section on Button Usage in the Project
       <files-submission-via-terminal>`

  * **submit_tagged_seq_multi**: Submit Tagged Sequence

       |section| :ref:`Section on Button Usage in the Project
       <submit-manifest-barcoding-submission-section>`

  * **download_sample_manifest_single**: Download Sample Manifest

       |section| :ref:`Section on Button Usage in the Project <data-download>`

  * **view_images_multiple**: View Images

       |section| :ref:`Section on Button Usage in the Project
       <image-submission-view-images>`

  * **download_permits_multiple**: Download Permits

       |section| :ref:`Section on Button Usage in the Project
       <permits-submission-download-permits>`

  * **releasestudy**: Publish Study

       |section| :ref:`Section on Button Usage in the Project
       <publishing-data>`

.. raw:: html

   <hr>

Referencing Created RecordActionButton in Project
-------------------------------------------------

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents

* In the ``views.py``, define the views to render the template containing the
  buttons

.. collapse:: RecordActionButton example views.py

   .. raw:: html

      <br>

   .. literalinclude:: /assets/files/setup/profile/record-action-button-views.py
      :language: python

* In the template HTML file (``myapp.html``), reference each element from the
  RecordActionButton table.

.. collapse:: RecordActionButton example template

   .. raw:: html

      <br>

   .. literalinclude:: /assets/files/setup/profile/record-action-button.html
      :language: html

.. raw:: html

   <hr>

* Handle any JavaScript functionality needed for the buttons in the
  :abbr:`JS (JavaScript)` file (``myapp.js``)

.. collapse:: RecordActionButton example javascript

   .. raw:: html

      <br>

   .. literalinclude:: /assets/files/setup/profile/record-action-button.js
      :language: javascript

.. raw:: html

   <hr>

.. _visual-representation-record-action-button:

Visualisation of RecordActionButton in Project
----------------------------------------------

.. figure:: /assets/images/django-admin-interface/profile/record-action-button/visualisation-record-action-button-assembly-web-page.png
   :alt: Visualisation of the add, edit, delete and submit record action
         buttons on the Assembly page
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/django-admin-interface/profile/record-action-button/visualisation-record-action-button-assembly-web-page.png
   :class: with-shadow with-border

   **Assembly page: Visualisation of the add, edit, delete and submit
   action buttons**

* **add_record_all** button displays the tooltip ``Add record`` when hovered
  over and uses a |add-icon| icon. It is indicated by the blue arrow.

* **edit_record_single** button displays the tooltip ``Edit record`` when
  hovered over and uses |edit-icon| icon. It is indicated by the green arrow.

* **delete_record_multi** button displays the tooltip ``Delete records``
  when hovered over and uses a |delete-icon| icon. It is indicated by the red
  arrow. The icon and colour of this button is used on multiple pages with
  different actions.

* **submit_assembly_multi** button displays the tooltip ``Submit assembly``
  when hovered over and uses a |info-icon| icon. The icon and colour used in
  for this button, is also used for the **submit_annotation_multi**,
  **submit_read_multi** and **submit_tagged_seq_multi** buttons.

  The difference is in the label assigned and the action performed by the
  button. The button is indicated by the teal arrow in the image above.

.. raw:: html

   <hr>

.. figure:: /assets/images/django-admin-interface/profile/record-action-button/visualisation-record-action-button-files-web-page.png
   :alt: Visualisation of the 'download sample manifest' button, 'view images'
         button and 'download permits' buttons on the Samples page
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/django-admin-interface/profile/record-action-button/visualisation-record-action-button-files-web-page.png
   :class: with-shadow with-border

   **Samples page:  Visualisation of the download sample manifest action
   button, view images action button and download permits action button**

* **add_local_all** button displays the tooltip ``Add new file by browsing
  local file system`` when hovered over and uses a |computer-icon| icon. It
  is indicated by the blue arrow on the right in the image above.

* **add_terminal_all** button displays the tooltip
  ``Add new file by terminal`` when hovered over and uses a |terminal-icon|
  icon. It is indicated by the blue arrow on the left in the image above.

.. raw:: html

   <hr>

.. figure:: /assets/images/django-admin-interface/profile/record-action-button/visualisation-record-action-button-samples-web-page.png
   :alt: Visualisation of the 'add file by browser' record action button and
         'add file via terminal' record action button on the Samples page
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/django-admin-interface/profile/record-action-button/visualisation-record-action-button-samples-web-page.png
   :class: with-shadow with-border

   **Samples page: Visualisation of the add file via browser record action
   button and add file via terminal record action button**

* **download_sample_manifest_single** button displays the tooltip
  ``Download Sample Manifest`` when hovered over and uses a |download-icon1|
  icon. It is indicated by the blue arrow in the image above.

* **view_images_multiple** button displays the tooltip ``View Images`` when
  hovered over and uses a |eye-icon| icon. It is indicated by the teal arrow.

* **download_permits_multiple** button displays the tooltip
  ``Download Permits`` when hovered over and uses a |download-icon2| icon. It
  is indicated by the orange arrow.

.. raw:: html

   <hr>

.. figure:: /assets/images/django-admin-interface/profile/record-action-button/visualisation-record-action-button-work-profiles-web-page.png
   :alt: Visualisation of the publish study record action button on the 'Work
         profiles' page
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/django-admin-interface/profile/record-action-button/visualisation-record-action-button-work-profiles-web-page.png
   :class: with-shadow with-border
   :height: 300px

   **Work profiles page: Visualisation of the publish study record action
   button on a profile**

* **releasestudy** button displays the tooltip ``Publish Study`` when
  hovered over and uses a |globe-icon| icon. It is indicated by the blue
  arrow in the image above.

.. raw:: html

   <hr>

Related Topics
--------------

.. seealso::

   * :ref:`Defining RecordActionButton Django model <django-model-definition>`
   * :ref:`Component structure <profile-setup-component>`
   * :ref:`ProfileType structure <profile-setup-profile-type>`
   * :ref:`TitleButton structure <profile-setup-title-button>`

.. raw:: html

   <hr>

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/arrow-right.png
   :height: 2ex
   :class: no-scaled-link

.. |add-icon| image:: /assets/images/icons/add-icon.png
   :height: 2.5ex
   :class: no-scaled-link

.. |computer-icon| image:: /assets/images/icons/computer-icon.png
   :height: 2ex
   :class: no-scaled-link

.. |download-icon1| image:: /assets/images/icons/download-icon1.png
   :height: 2ex
   :class: no-scaled-link

.. |download-icon2| image:: /assets/images/icons/download-icon2.png
   :height: 2ex
   :class: no-scaled-link

.. |edit-icon| image:: /assets/images/icons/edit-icon.png
   :height: 3ex
   :class: no-scaled-link

.. |eye-icon| image:: /assets/images/icons/eye-icon.png
   :height: 2ex
   :class: no-scaled-link

.. |delete-icon| image:: /assets/images/icons/delete-icon.png
   :height: 3ex
   :class: no-scaled-link

.. |globe-icon| image:: /assets/images/icons/globe-icon.png
   :height: 3ex
   :width: 2.6ex
   :class: no-scaled-link

.. |info-icon| image:: /assets/images/icons/info-icon2.png
   :height: 3ex
   :class: no-scaled-link

.. |terminal-icon| image:: /assets/images/icons/terminal-icon.png
   :height: 2ex
   :class: no-scaled-link

..
    Unicode declaration
..


.. |section| unicode:: U+1F4D6
