.. _samples-submission-biodata:

Biodata Profile Sample Submission
---------------------------------

.. _samples-submission-biodata-note:

Prerequisites & Notes
~~~~~~~~~~~~~~~~~~~~~

.. important::

   * This section applies if you are submitting samples to a Biodata
     profile [#f1]_. For sample submissions under Tree of Life (ToL) [#f2]_
     profiles, see :ref:`samples-submission-tol` section.

   * A Biodata profile is needed to proceed with this section. Refer to
     :ref:`Steps to Create a Biodata Profile <profile-walkthrough-biodata>` to
     create one. Skip this step if you have already done so.

.. note::

   Samples **cannot** be deleted after they have been submitted.

.. raw:: html

   <hr>

.. _accessing-samples-page-biodata:

Accessing the Samples Page
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Samples page can be accessed via the **Components** button or via the
components icon navigation pane when viewing another component's page
associated with a Biodata profile.

.. _accessing-samples-page-via-components-button-biodata:

Using the Components Button
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click the |samples-component-button| component button in the **Components**
column as shown below:

.. figure:: /assets/images/samples/buttons/samples-button-pointer-biodata.png
   :alt: Samples profile component button
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/buttons/samples-button-pointer-biodata.png
   :class: with-shadow with-border
   :height: 300px

   **Samples component button (located under Biodata profiles)**

.. raw:: html

   <br>

Using the Components Icon Navigation Pane
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: /profile/components/navigation-pane-overview.rst

.. figure:: /assets/images/samples/icons/samples-icon-pointer-biodata.png
   :alt: Samples profile component icon
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/icons/samples-icon-pointer-biodata.png
   :class: with-shadow with-border
   :height: 120px

   **Navigation pane showing the Samples component icon**

.. raw:: html

   <hr>

.. _submit-manifest-samples-biodata:

Upload Samples
~~~~~~~~~~~~~~

1. Click the dropdown menu to choose a checklist [#f3]_.

   .. figure:: /assets/images/samples/biodata/ui/samples-pointer-to-dropdown-menu-biodata.png
      :alt: Pointer to Samples checklist dropdown menu
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/biodata/ui/samples-pointer-to-dropdown-menu-biodata.png
      :class: with-shadow with-border

      **Pointer to dropdown menu for samples**

   .. raw:: html

      <br>

   Hover over each option to view its description. An overview of each option
   is provided in the
   :ref:`Sample manifest checklist section <sample-manifest-checklists>`.

   .. raw:: html

      <br>

   .. figure:: /assets/images/samples/biodata/ui/samples-with-checklist-dropdown-list-biodata.png
      :alt: Available samples checklist options within a Biodata profile
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/biodata/ui/samples-with-checklist-dropdown-list-biodata.png
      :class: with-shadow with-border

      **Checklist options for sample submissions**

   .. raw:: html

      <br>

2. Click the |samples-blank-manifest-download-button-biodata| button to
   download a blank manifest [#f4]_.

   A manifest is a spreadsheet file used to record metadata for submission.

3. Fill in the downloaded manifest then, click the
   |add-samples-manifest-button-biodata| button to upload it from your local
   (computer) system.

   .. note::

      Please ensure that the manifest that you are uploading matches the
      checklist type selected in step 1. You will encounter errors if the
      uploaded manifest does not correspond with the selected dropdown menu
      checklist option.

   .. figure:: /assets/images/samples/biodata/ui/samples-pointer-to-add-manifest-button-biodata.png
      :alt: Pointer to 'Add or update samples from spreadsheet' button
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/biodata/ui/samples-pointer-to-add-manifest-button-biodata.png
      :class: with-shadow with-border

      **Click "Add or update samples from spreadsheet" button to open an upload dialogue**

   .. raw:: html

      <br>

4. A dialogue is displayed. Click the |samples-upload-button-biodata|
   button in the dialogue to choose the spreadsheet file from your local system.

   .. figure:: /assets/images/samples/biodata/modals/samples-upload-spreadsheet-dialogue-biodata.png
      :alt: Upload Samples spreadsheet dialogue
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/biodata/modals/samples-upload-spreadsheet-dialogue-biodata.png
      :class: with-shadow with-border

      **Click 'Upload sample manifest' button**

   .. raw:: html

      <br>

5. The uploaded data is shown in a preview before final submission. Click
   the |samples-finish-button| button to finalise the upload.

   .. figure:: /assets/images/samples/biodata/modals/samples-dialogue-with-uploaded-data-biodata.png
      :alt: Dialogue with uploaded Samples data
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/biodata/modals/samples-dialogue-with-uploaded-data-biodata.png
      :class: with-shadow with-border
      :height: 400px

      **Samples upload preview**

   .. raw:: html

      <br>

6. The new samples data will be displayed on the **Samples** page
   after a successful validation.

   .. figure:: /assets/images/samples/biodata/ui/samples-page-with-uploaded-data-biodata.png
      :alt: Samples data uploaded
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/biodata/ui/samples-page-with-uploaded-data-biodata.png
      :class: with-shadow with-border

      **Samples page showing the uploaded data**

   .. raw:: html

      <br>

Submit Samples
~~~~~~~~~~~~~~

.. note::

   * Follow the steps in :ref:`submit-manifest-samples-biodata` to upload data
     before proceeding with the submission.

   * The following repositories are supported for Samples submissions:

     * European Nucleotide Archive (ENA) via |submit-record-button-ena| button

7. After uploading data, select a row in the data table.

   Then, click the |submit-record-button-ena| button to submit the selected
   record to ENA.

   .. hint::

      Selected rows are indicated by a blue background colour.

   .. note::

      Please ensure that the selected record is under the desired checklist
      option. If not, choose another option from the dropdown menu, then
      select a row in the data table.

   .. raw:: html

      <br>

8. Wait for the submission process to be completed. The submitted record's
   status and accessions can be viewed in the data table's respective columns.
   See the sections below for details.

.. _samples-submission-make-public-biodata:

Make Data Public
~~~~~~~~~~~~~~~~

9. Sample submissions are automatically made public after they have been
   submitted. You can therefore access the data publicly in the associated
   repository after a couple of days of processing. via the accessions.

   See the :ref:`samples-submission-accessions-biodata` section below for
   more details.

.. raw:: html

   <hr>

.. _samples-submission-status-biodata:

View Submission Status
~~~~~~~~~~~~~~~~~~~~~~

.. hint::

   The **Data status & progress** legend, located on the right side of the
   data table, shows the different stages of submission processing. Hover over
   the |info-icon| to see description for each status.

   For more details, see the :ref:`faq-data-status-and-progress-legend`
   :abbr:`FAQ (Frequently Asked Question)` section.

The submission will be scheduled for processing after the
|submit-record-button-ena| button is clicked.
The row of the submitted record will be highlighted in green indicating that
the submission has been successful.

If the submission was unsuccessful or has not been assigned any accessions,
the table row will be highlighted in red. Its status is indicated in the
following columns:

* **STATUS** - Displays the status returned from the repository, European
  Nucleotide Archive (ENA), assigned to the project
* **ERROR** - Displays any error message associated with the submission.

.. raw:: html

   <hr>

.. _samples-submission-accessions-biodata:

View Accessions
~~~~~~~~~~~~~~~

Accessions are unique identifiers assigned to submissions after they have been
successfully submitted to public repositories.

The accession columns are:

* **BIOSAMPLEACCESSION** - the biosample accession is the primary identifier
  for the sample submission.

* **SRAACCESSION** - the :abbr:`SRA (Sequence Read Archive )` [#f5]_ accession
  is the secondary identifier for the sample submission.

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
   * :ref:`data-download`
   * :ref:`accessions`

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Biodata profile`.
.. [#f2] See term: :term:`Tree of Life profile <ToL profile>`.
.. [#f3] See term: :term:`Checklist`.
.. [#f4] See term: :term:`Manifest`.
.. [#f5] See term: :term:`Sequence Read Archive (SRA) accession
   <SRA accession>`.

.. raw:: html

   <br><br>

..
    Images declaration
..

.. |accessions-component-icon| image:: /assets/images/accessions/icons/components-accessions-icon.png
   :height: 3ex
   :class: no-scaled-link

.. |add-samples-manifest-button-biodata| image:: /assets/images/buttons/add-manifest-button-for-biodata-profile.png
   :height: 4ex
   :class: no-scaled-link

.. |info-icon| image:: /assets/images/icons/info-icon.png
   :height: 2.5ex
   :class: no-scaled-link

.. |samples-blank-manifest-download-button-biodata| image:: /assets/images/buttons/download-button-blank-manifest.png
   :height: 4ex
   :class: no-scaled-link

.. |samples-component-button| image:: /assets/images/samples/buttons/components-samples-button.png
   :height: 4ex
   :class: no-scaled-link

.. |samples-finish-button| image:: /assets/images/buttons/finish-button2.png
   :height: 4ex
   :class: no-scaled-link

.. |samples-upload-button-biodata| image:: /assets/images/samples/biodata/buttons/samples-upload-manifest-button.png
   :height: 4ex
   :class: no-scaled-link

.. |submit-record-button-ena| image:: /assets/images/buttons/submit-record-button-ena.png
   :height: 3.5ex
   :class: no-scaled-link
