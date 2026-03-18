.. _reads-submission-tol:

Tree of Life Profile Reads Submission
-------------------------------------

.. _reads-submission-tol-note:

Prerequisites & Notes
~~~~~~~~~~~~~~~~~~~~~

.. important::

   * This section applies if you are submitting reads to a Tree of Life
     profile (ToL) [#f1]_. For reads submissions under Biodata
     profiles [#f2]_, see :ref:`reads-submission-biodata` section.

   * A Tree of Life profile is needed to proceed with this section. Refer to
     :ref:`Steps to Create a Tree of Life Profile <profile-walkthrough-tol>`
     to create one. Skip this step if you have already done so.

.. note::

  * Once reads have been submitted, they **cannot** be deleted.

  * Submit samples before uploading Reads manifests. See
    :ref:`Samples submission <samples-submission-tol>` for details.

  * Upload all required data files before submitting
    Reads manifests. See: :ref:`files`.

.. raw:: html

   <hr>

.. _accessing-reads-page-tol:

Accessing the Reads Page
~~~~~~~~~~~~~~~~~~~~~~~~

The Reads [#f3]_ page can be accessed via the **Components** button or via the
components icon navigation pane when viewing another component's page
associated with a Tree of Life profile [#f1]_.

.. _accessing-reads-page-via-components-button-tol:

Using the Components Button
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click the |reads-component-button| component button in the **Components**
column as shown below:

.. figure:: /assets/images/reads/tol/buttons/reads_button_pointer_tol.png
   :alt: Reads profile component button
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/reads/tol/buttons/reads_button_pointer_tol.png
   :class: with-shadow with-border
   :height: 300px

   **Reads component button (located under Tree of Life profiles)**

.. raw:: html

   <br>

Using the Components Icon Navigation Pane
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: /profile/components/navigation-pane-overview.rst

.. figure:: /assets/images/reads/tol/icons/reads_icon_pointer_tol.png
   :alt: Reads profile component icon
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/reads/tol/icons/reads_icon_pointer_tol.png
   :class: with-shadow with-border
   :height: 120px

   **Navigation pane showing the Reads component icon**

.. raw:: html

   <hr>

.. _submit-manifest-reads-tol:

Upload Reads
~~~~~~~~~~~~

1. Click the dropdown menu to choose a checklist [#f4]_.

   Currently, only one option is available.

   .. figure:: /assets/images/reads/tol/ui/reads_pointer_to_dropdown_menu_tol.png
      :alt: Pointer to Reads checklist dropdown menu
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/reads/tol/ui/reads_pointer_to_dropdown_menu_tol.png
      :class: with-shadow with-border

      **Pointer to dropdown menu for reads**

   .. raw:: html

      <br>

   Hover over each option to view its description.

   .. raw:: html

      <br>

   .. figure:: /assets/images/reads/tol/ui/reads_with_checklist_dropdown_list_tol.png
      :alt: Available reads checklist options within a Tree of Life profile
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/reads/tol/ui/reads_with_checklist_dropdown_list_tol.png
      :class: with-shadow with-border

      **Checklist options for read submissions**

   .. raw:: html

      <br>

2. Click the |reads-blank-manifest-download-button-tol| button to download
   a blank manifest [#f5]_.

   A manifest is a spreadsheet file used to record metadata for submission.

3. Fill in the downloaded manifest then, click the
   |add-reads-manifest-button-tol| button to upload it from your local
   (computer) system.

   .. warning::

      If you are submitting a **Reads** manifest that includes the column,
      ``Sample``, please ensure that the sample alias (i.e. sample name or
      accession number) is accurate. Once submitted, the value **cannot** be
      changed. Reads uploaded to COPO will also be sent to
      :abbr:`ENA (European Nucleotide Archive)`.

   .. note::

      * The colour of the |add-reads-manifest-button-tol| button is based on
        the type of profile that you are making a submission to.

        See the :ref:`profile-types-legend` section regarding the colour code
        for the various types of project profiles on COPO.

      * Please ensure that the manifest that you are uploading matches the
        checklist type selected in step 1. You will encounter errors if the
        uploaded manifest does not correspond with the selected dropdown menu
        checklist option.

   .. tip::

      For guidance on how to fill in the **Reads** manifest to submit *paired*
      reads, please see the
      :ref:`Reads manifest for paired reads <faq-reads-manifest-paired-reads>`
      :abbr:`FAQ (Frequently Asked Question)`.


   .. figure:: /assets/images/reads/tol/ui/reads_pointer_to_add_manifest_button_tol.png
      :alt: Pointer to 'Add study from spreadsheet' button
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/reads/tol/ui/reads_pointer_to_add_manifest_button_tol.png
      :class: with-shadow with-border

      **Click "Add study from spreadsheet" button to open an upload dialog**

   .. raw:: html

      <br>

4. A dialog is displayed. Click the |reads-upload-button-tol|
   button in the dialog to choose the spreadsheet file from your local system.

   .. figure:: /assets/images/reads/tol/modals/reads_upload_spreadsheet_dialog_tol.png
      :alt: Upload Reads spreadsheet dialog
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/reads/tol/modals/reads_upload_spreadsheet_dialog_tol.png
      :class: with-shadow with-border
      :height: 300px

      **Click 'Upload manifest' button**

   .. raw:: html

      <br>

5. The uploaded data is shown in a preview before final submission. Click
   the |finish-button| button to finalise the upload.

   .. figure:: /assets/images/reads/tol/modals/reads_dialog_with_uploaded_data_tol.png
      :alt: Dialog with uploaded Reads data
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/reads/tol/modals/reads_dialog_with_uploaded_data_tol.png
      :class: with-shadow with-border
      :height: 400px

      **Reads upload preview**

   .. raw:: html

      <br>

6. The new reads data will be displayed on the **Reads** page
   after a successful validation.

   .. figure:: /assets/images/reads/tol/ui/reads_page_with_uploaded_data_tol.png
      :alt: Reads data uploaded
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/reads/tol/ui/reads_page_with_uploaded_data_tol.png
      :class: with-shadow with-border

      **Reads page showing the uploaded data**

   .. raw:: html

      <br>

Submit Reads
~~~~~~~~~~~~

.. note::

   * Follow the steps in :ref:`submit-manifest-reads-tol` to upload data
     before proceeding with the submission.

   * The following repositories are supported for Reads submissions:

     * European Nucleotide Archive (ENA) via |submit-record-button| button

7. After uploading data, select a row in the data table.

   Then, click the |submit-record-button| button to submit the selected
   record to European Nucleotide Archive (ENA).

   .. note::

      Please ensure that the selected record is under the desired checklist
      option. If not, choose another option from the dropdown menu, then
      select a row in the data table.

   .. figure:: /assets/images/reads/tol/ui/reads_pointer_to_submit_reads_button_tol.png
      :alt: Reads data uploaded
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/reads/tol/ui/reads_pointer_to_submit_reads_button_tol.png
      :class: with-shadow with-border

      **Click** ``Submit`` **buton**

   .. raw:: html

      <br>

8. Wait for the submission process to be completed. The submitted record's
   status and accessions can be viewed in the data table's respective columns.
   See the sections below for details.

.. _reads-submission-make-public-tol:

Make Data Public
~~~~~~~~~~~~~~~~

9. Submissions are private by default. You can make the data publicly
   accessible by referring to the steps in the
   :ref:`publishing-data-from-profile-level` section.

.. raw:: html

   <hr>

.. _reads-submission-status-tol:

View Submission Status
~~~~~~~~~~~~~~~~~~~~~~

.. hint::

   The **Data status & progress** legend, located on the right side of the
   data table, shows the different stages of submission processing. Hover over
   the |info-icon| to see description for each status.

   For more details, see the :ref:`faq-data-status-and-progress-legend`
   :abbr:`FAQ (Frequently Asked Question)` section.

The submission will be scheduled for processing after the
|submit-record-button| button is clicked.
The row of the submitted record will be highlighted in green indicating that
the submission has been successful.

If the submission was unsuccessful or has not been assigned any accessions,
the table row will be highlighted in red. Its status is indicated in the
following columns:

* **STATUS** - Displays the European Nucleotide Archive (ENA) status assigned
  to the project
* **ENA FILE UPLOAD STATUS** - Displays the
  :abbr:`ENA (European Nucleotide Archive )` status assigned to the uploaded
  data files
* **ENA FILE PROCESSING STATUS** - Displays the outcome after
  :abbr:`ENA (European Nucleotide Archive )` has verified and validated the
  uploaded data files.

  Refer to the :ref:`files-ena-file-processing-status`
  :abbr:`FAQ (Frequently Asked Question)` for more details

.. raw:: html

   <hr>

.. _-tol:

View Accessions
~~~~~~~~~~~~~~~

Accessions are unique identifiers assigned to submissions after they have been
successfully submitted to public repositories.

The accession columns are:

* **STUDY ACCESSION** - Displays the project accession assigned by
  European Nucleotide Archive (ENA)
* **RUN ACCESSION** - Displays the accession assigned to the submitted reads
  by :abbr:`ENA (European Nucleotide Archive )`
* **EXPERIMENT ACCESSION** - Displays the experiment accession assigned to the
  project by :abbr:`ENA (European Nucleotide Archive )`

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
~~~~~~~~~~~~~~

.. seealso::

   * :ref:`data-updates`
   * :ref:`files`
   * :ref:`How to check if data files for reads submissions have been
     processed after upload to ENA <files-ena-file-processing-status>`
   * :ref:`Types of Files for Read Submissions
     <faq-reads-submission-file-types>`
   * :ref:`accessions`

.. raw:: html

   <br>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Tree of Life profile <ToL profile>`.
.. [#f2] See term: :term:`Biodata profile`.
.. [#f3] See: :term:`Reads`.
.. [#f4] See term: :term:`Checklist`.
.. [#f5] See term: :term:`Manifest`.

..
    Images declaration
..

.. |accessions-component-icon| image:: /assets/images/accessions/icons/components_accessions_icon.png
   :height: 3ex
   :class: no-scaled-link

.. |add-reads-manifest-button-tol| image:: /assets/images/buttons/add_manifest_button_for_tol_profile.png
   :height: 4ex
   :class: no-scaled-link

.. |finish-button| image:: /assets/images/buttons/finish_button2.png
   :height: 4ex
   :class: no-scaled-link

.. |info-icon| image:: /assets/images/icons/info_icon.png
   :height: 2.5ex
   :class: no-scaled-link

.. |reads-blank-manifest-download-button-tol| image:: /assets/images/buttons/download_button_blank_manifest.png
   :height: 4ex
   :class: no-scaled-link

.. |reads-component-button| image:: /assets/images/reads/buttons/components_reads_button.png
   :height: 4ex
   :class: no-scaled-link

.. |reads-upload-button-tol| image:: /assets/images/reads/tol/buttons/reads_upload_button_tol.png
   :height: 4ex
   :class: no-scaled-link

.. |submit-record-button| image:: /assets/images/buttons/submit_record_button.png
   :height: 3.5ex
   :class: no-scaled-link
