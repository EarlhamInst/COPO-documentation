.. _assemblies:

=====================
Submitting Assemblies
=====================

.. note::

  Files must be uploaded before **assemblies** can be submitted.
  See: :ref:`files`.

.. raw:: html

   <hr>

Access the Assembly Page
------------------------

Create a profile [#f1]_ following the steps in :ref:`Tree of Life profile
creation <profile-walkthrough-tol>`. Then, access the **Assembly** [#f2]_ page
via any of the following methods:

Using the Component Button
~~~~~~~~~~~~~~~~~~~~~~~~~~

Click |assembly-component-button| under the **Components** column for a
profile as shown below:

.. figure:: /assets/images/assemblies/ui/assembly_button_pointer_tol.png
   :alt: Assembly profile component button
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/assemblies/ui/assembly_button_pointer_tol.png
   :class: with-shadow with-border
   :height: 400px

   **Button to access the Assembly page (highlighted)**

.. raw:: html

   <br>

Using the Component Icon Navigation Pane
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /profile/components/navigation-pane-overview.rst

.. figure:: /assets/images/assemblies/icons/assembly_icon_pointer.png
   :alt: Assembly profile component icon
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/assemblies/icons/assembly_icon_pointer.png
   :class: with-shadow with-border
   :height: 120px

   **Navigation pane showing the Assembly component icon**

.. raw:: html

   <hr>

.. _assemblies-submission-section:

Submit Assemblies
-----------------

#. Click |add-assemblies-record-button| button to add an **assembly** as shown
   below:

    .. figure:: /assets/images/assemblies/ui/assemblies_pointer_to_add_record_button.png
      :alt: Pointer to 'Add record' button
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/assemblies/ui/assemblies_pointer_to_add_record_button.png
      :class: with-shadow with-border

      **Assembly submission: Click the 'Add record' button**

   .. raw:: html

      <br>

#. An **Add assembly** dialog is displayed. Provide the details then, click
   the **Submit assembly** button.

   .. hint::

      An asterisk (*) next to a form field label indicates that the field is
      mandatory.

   .. figure:: /assets/images/assemblies/modals/assemblies_add_assembly_dialog1.png
      :alt: Top section of 'Add Assembly' dialog
      :align: center
      :height: 60ex
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/assemblies/modals/assemblies_add_assembly_dialog1.png
      :class: with-shadow with-border

      **Add Assembly dialog (top section)**

   .. raw:: html

      <br>

   .. figure:: /assets/images/assemblies/modals/assemblies_add_assembly_dialog2.png
      :alt: Upper-middle section of 'Add Assembly' dialog
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/assemblies/modals/assemblies_add_assembly_dialog2.png
      :class: with-shadow with-border
      :height: 60ex

      **Add Assembly dialog (upper-middle section)**

   .. raw:: html

      <br>

   .. figure:: /assets/images/assemblies/modals/assemblies_add_assembly_dialog3.png
      :alt: Lower-middle section of 'Add Assembly' dialog
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/assemblies/modals/assemblies_add_assembly_dialog3.png
      :class: with-shadow with-border
      :height: 60ex

      **Add Assembly dialog (lower-middle section)**

   .. raw:: html

      <br>

   .. figure:: /assets/images/assemblies/modals/assemblies_add_assembly_dialog4.png
      :alt: Bottom section of 'Add Assembly' dialog
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/assemblies/modals/assemblies_add_assembly_dialog4.png
      :class: with-shadow with-border
      :height: 60ex

      **Add Assembly dialog (bottom section)**

   .. raw:: html

      <br>

#. The new assembly will be displayed on the **Assembly** page after a
   successful submission.

    .. figure:: /assets/images/assemblies/ui/assemblies_uploaded.png
      :alt: Assemblies uploaded
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/assemblies/ui/assemblies_uploaded.png
      :class: with-shadow with-border

      **Assembly submission: Page showing uploaded assemblies**

   .. raw:: html

      <br>

#. Click an assembly record in the data table on the **Assembly** page. Then,
   click |submit-record-button| located at the top-right of the table as shown
   below.

   Refer to the :ref:`assemblies-submission-status` section and
   :ref:`assemblies-submission-accessions` section below for more information
   about the submission.

   .. figure:: /assets/images/assemblies/ui/assemblies_pointer_to_submit_assembly_button.png
      :alt: Assemblies submit button
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/assemblies/ui/assemblies_pointer_to_submit_assembly_button.png
      :class: with-shadow with-border

      **Submitting an assembly by clicking the “Submit” button**

.. raw:: html

   <hr>

.. _assemblies-submission-status:

View Submission Status
----------------------

.. hint::

   The **Data status & progress** legend, located on the right side of the
   data table, shows the different stages of submission processing. Hover over
   the |info-icon| to see description for each status.

   For more details, see the :ref:`faq-data-status-and-progress-legend`
   :abbr:`FAQ (Frequently Asked Question)` section.

The submission will be scheduled for processing after the
|submit-record-button| button is clicked. The row of the submitted assembly
record will be highlighted in green indicating that the submission has been
successful.

If the submission was unsuccessful or has not been assigned any accessions,
the table row will be highlighted in red. Its status is indicated in the
**SUBMISSION ERROR** column and the **ENA FILE PROCESSING STATUS** column
displays the status of the data files associated with the submission.

.. raw:: html

   <hr>

.. _assemblies-submission-accessions:

View Accessions
---------------

Accessions are unique identifiers assigned to submissions after they have been
successfully submitted to public repositories.

The accession columns are:

* **ACCESSION** - Displays the accession assigned to assembly submission.
* **STUDY**: Displays the ENA Study accession assigned to the project
* **SAMPLE**: Displays the ENA biosample accession associated with sample
  associated with the submitted assembly.
* **RUN_REF**: Displays the ENA Run accession assigned to the reads associated
  with the submitted assembly.

Clicking any accession in the data table will open the corresponding record in
the associated repository. You can also find the same record by searching for
the accession directly in the repository.

.. tip::

   Alternatively, click the |accessions-component-icon| icon located in the
   top-right corner of the data table to navigate to the **Accessions** page
   that displays accessions for all submissions.

.. raw:: html

   <hr>

Related Topics
--------------

.. seealso::

   * :ref:`data-updates`
   * :ref:`files`
   * :ref:`Types of Files for Assembly Submissions
     <faq-assemblies-submission-file-types>`
   * :ref:`How to check if data files for assembly submissions have been
     processed after upload to ENA <files-ena-file-processing-status>`
   * :ref:`Creating a custom Locus Tag Prefix to Assemblies
     <faq-assemblies-submission-locus-tag-assignment>`
   * :ref:`accessions`

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Also known as COPO profile. See:
   :term:`COPO profile or work profile<COPO profile>`.
.. [#f2] See: :term:`Assembly`.

..
    Images declaration
..

.. |accessions-component-icon| image:: /assets/images/accessions/icons/components_accessions_icon.png
   :height: 3ex
   :class: no-scaled-link

.. |add-assemblies-record-button| image:: /assets/images/buttons/add_button.png
   :height: 4ex
   :class: no-scaled-link

.. |assembly-component-button| image:: /assets/images/assemblies/buttons/components_assembly_button.png
   :height: 4ex
   :class: no-scaled-link

.. |delete-record-button| image:: /assets/images/buttons/delete_record_button.png
   :height: 3ex
   :class: no-scaled-link

.. |info-icon| image:: /assets/images/icons/info_icon.png
   :height: 2.5ex
   :class: no-scaled-link

.. |submit-record-button| image:: /assets/images/buttons/submit_record_button.png
   :height: 3.5ex
   :class: no-scaled-link
