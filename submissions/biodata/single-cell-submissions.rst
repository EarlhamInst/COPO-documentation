.. _single-cell-submissions:

===========================
Submitting Single-cell Data
===========================

Prerequisites
-------------

.. note::

   * **Samples**: Submit samples before uploading Single-cell manifests. See
     :ref:`Samples submission (under Biodata Profiles) <samples-submission-biodata>` for details.

   * **Data files**: Upload all required data files before submitting
     Single-cell manifests. See: :ref:`files`.

.. _accessing-single-cell-page:

Accessing the Single-cell Page
------------------------------

Create a profile [#f1]_ following the steps in
:ref:`Biodata profile creation <profile-walkthrough-biodata>`. Then, access
the **Single-cell** [#f2]_ page via any of the following methods:

Using the Components Button
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click the |single-cell-component-button| component button in the
**Components** [#f3]_ column as shown below:

.. figure:: /assets/images/single-cell/buttons/single-cell-button-pointer-biodata.png
   :alt: Single-cell profile component button
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/single-cell/buttons/single-cell-button-pointer-biodata.png
   :class: with-shadow with-border
   :height: 400px

   **Button to access the Single-cell page (highlighted)**

.. raw:: html

   <br>

Using the Components Icon Navigation Pane
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /profile/components/navigation-pane-overview.rst

.. figure:: /assets/images/single-cell/icons/single-cell-icon-pointer.png
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/single-cell/icons/single-cell-icon-pointer.png
   :class: with-shadow with-border
   :height: 120px

   **Navigation pane showing the Single-cell component icon**

.. raw:: html

   <hr>

.. _submit-manifest-single-cell:

Upload Data
-----------

1. Click the dropdown menu to choose a checklist [#f4]_. Hover over each
   option to view its description.

   .. _single-cell-submission-types:

   Supported Single-cell checklists include the following. Click
   below |collapsible-item-arrow| to view all types.

   * `Darwin Core (DwC) <https://dwc.tdwg.org/list>`__
   * `Functional Annotation of Animal Genomes (FAANG)
     <https://www.animalgenome.org/community/FAANG>`__
   * `Minimum Information about any (x) Sequence (MIxS)
     <https://genomicsstandardsconsortium.github.io/mixs>`__
   * Tree of Life (ToL)

   .. collapse:: View all types of Single-cell submissions

      .. raw:: html

         <br>

      .. list-table:: Types of Single-cell submissions
         :widths: 45 25 30
         :width: 100%
         :align: center
         :header-rows: 1

         * - Type
           - Abbreviation
           - COPO Identifier
         * - Single-cell Ribonucleic Acid Sequencing Darwin Core
           - scRNA-Seq DwC
           - version_dwc_sc_rnaseq
         * - Single-cell Ribonucleic Acid Sequencing Functional Annotation of
             Animal Genomes
           - scRNA-Seq FAANG
           - version_faang_sc_rnaseq
         * - Single-cell Ribonucleic Acid Sequencing Minimum Information about
             any (x) Sequence
           - scRNA-Seq MIxS
           - version_mixs_sc_rnaseq
         * - Single-cell Ribonucleic Acid Sequencing Tree of Life
           - scRNA-Seq ToL
           - version_tol_sc_rnaseq

   .. figure:: /assets/images/single-cell/ui/single-cell-with-checklist-dropdown-list.png
      :alt: Available sample checklist options within a Biodata profile
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/single-cell/ui/single-cell-with-checklist-dropdown-list.png
      :class: with-shadow with-border

      **Checklist options for Single-cell submissions**

   .. raw:: html

      <br>

2. Click the |single-cell-blank-manifest-download-button| button to download
   a blank manifest [#f5]_.

   A manifest is a spreadsheet file used to record metadata for submission.

3. Fill in the downloaded manifest then, click
   |add-single-cell-manifest-button| button to upload a completed
   Single-cell manifest from your local (computer) system.

   .. note::

      Please ensure that the manifest that you are uploading matches the
      checklist type selected in step 1. You will encounter errors if the
      uploaded manifest does not correspond with the selected dropdown menu
      checklist option.

   .. figure:: /assets/images/single-cell/ui/single-cell-pointer-to-add-manifest-button.png
      :alt: Pointer to 'Add Study from Spreadsheet' button
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/single-cell/ui/single-cell-pointer-to-add-manifest-button.png
      :class: with-shadow with-border

      **Click "Add study from spreadsheet" button to open an upload dialogue**

   .. raw:: html

      <br>

4. A dialogue is displayed. Click the |upload-single-cell-manifest-button|
   button in the dialogue to choose a spreadsheet file from your local system.

   .. figure:: /assets/images/single-cell/modals/single-cell-upload-spreadsheet-dialogue.png
      :alt: Upload Single-cell Spreadsheet dialogue
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/single-cell/modals/single-cell-upload-spreadsheet-dialogue.png
      :class: with-shadow with-border

      **Click 'Upload manifest' button**

   .. raw:: html

      <br>

5. The uploaded data is shown in a preview before final submission. Click
   the |finish-button| button to finalise the upload.

   .. figure:: /assets/images/single-cell/modals/single-cell-dialogue-with-uploaded-data.png
      :alt: Dialogue with uploaded Single-cell data
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/single-cell/modals/single-cell-dialogue-with-uploaded-data.png
      :height: 600px
      :class: with-shadow with-border

      **Single-cell upload preview**

   .. raw:: html

      <br>

6. The new single-cell data will be displayed on the **Single-cell** page
   after a successful validation.

   .. note::

      * The first record in the **STUDY** tab is selected by default.

      * Each tab represents a worksheet in the manifest. Only worksheets
        with data appear as tabs.

   .. figure:: /assets/images/single-cell/ui/single-cell-page-with-uploaded-data.png
      :alt: Single-cell data uploaded
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/single-cell/ui/single-cell-page-with-uploaded-data.png
      :class: with-shadow with-border

      **Single-cell page showing the uploaded data**

   .. raw:: html

      <br>

.. raw:: html

   <hr>

Submit Data
-----------

.. note::

   * Follow the steps in :ref:`submit-manifest-single-cell` to upload data
     before proceeding with the submission.

   * The following repositories are supported for Single-cell submissions:

     * European Nucleotide Archive (ENA) via |submit-record-button-ena| button
     * Zenodo via |submit-record-button-zenodo| button

7. After uploading data, select a row in the data table under the
   **STUDY** tab.

   Then, click the |submit-record-button-ena| button to submit the selected
   record to ENA or |submit-record-button-zenodo| button to submit to Zenodo.

   .. hint::

      The first row of the data table under the **STUDY** tab is selected by
      default. Selected rows are indicated by a blue background colour.

   .. note::

      Please ensure that the selected record is under the desired checklist
      option. If not, choose another option from the dropdown menu, then
      select a row in the data table.

   .. raw:: html

      <br>

8. Wait for the submission process to be completed. The submitted record's
   status and accessions can be viewed in the data table's respective columns.
   See the sections below for details.

   .. raw:: html

      <br>

.. _single-cell-submission-make-public:

Make Data Public
----------------

9. Submissions are private by default. You can make the data publicly
   accessible by referring to the steps in the
   :ref:`publishing-data-from-data-level` section.

.. raw:: html

   <hr>

.. _single-cell-submission-status:

View Submission Status
----------------------

.. hint::

   The **Data status & progress** legend, located on the right side of the
   data table, shows the different stages of submission processing. Hover over
   the |info-icon| to see description for each status.

   For more details, see the :ref:`faq-data-status-and-progress-legend`
   :abbr:`FAQ (Frequently Asked Question)` section.

The submission will be scheduled for processing after the
|submit-record-button-ena| or |submit-record-button-zenodo| button is clicked.
The row of the submitted record will be highlighted in green indicating that
the submission has been successful.

If the submission was unsuccessful or has not been assigned any accessions,
the table row will be highlighted in red. Its status is indicated in the
following columns:

* **Status for Ena** - Displays the ENA status assigned to the project
* **Status for Zenodo**: Displays the Zenodo status assigned to the
  project

.. raw:: html

   <hr>

.. _single-cell-submission-accessions:

View Accessions
---------------

Accessions are unique identifiers assigned to submissions after they have been
successfully submitted to public repositories.

The accession columns are:

* **Accession for Ena** - Displays the ENA accession assigned to the project
* **Accession for Zenodo**: Displays the Zenodo accession assigned to the
  project

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

   * :ref:`files`
   * :ref:`Submitting Samples <samples-component-biodata>`
   * :ref:`Types of Single-cell Submissions <single-cell-submission-types>`
   * :ref:`Single-cell Frequently Asked Questions <faq-single-cell>`
   * `Single-cell website <https://singlecellschemas.org>`__
   * :ref:`accessions`

.. raw:: html

   <br>

.. rubric:: Footnotes

.. [#f1] See: :term:`COPO profile or work profile<COPO profile>`.
.. [#f2] See: :term:`Single-cell RNA Seq`.
.. [#f3] Also known as research object. See term: :term:`Profile component`.
.. [#f4] See term: :term:`Checklist`.
.. [#f5] See term: :term:`Manifest`.

..
    Images declaration
..

.. |accessions-component-icon| image:: /assets/images/accessions/icons/components-accessions-icon.png
   :height: 3ex
   :class: no-scaled-link

.. |add-single-cell-manifest-button| image:: /assets/images/buttons/add-manifest-button-for-biodata-profile.png
   :height: 4ex
   :class: no-scaled-link

.. |single-cell-blank-manifest-download-button| image:: /assets/images/buttons/download-button-blank-manifest.png
   :height: 4ex
   :class: no-scaled-link

.. |collapsible-item-arrow| image:: /assets/images/icons/arrow-right.png
   :height: 2ex
   :class: no-scaled-link

.. |finish-button| image:: /assets/images/buttons/finish-button2.png
   :height: 4ex
   :class: no-scaled-link

.. |info-icon| image:: /assets/images/icons/info-icon.png
   :height: 2.5ex
   :class: no-scaled-link

.. |single-cell-component-button| image:: /assets/images/single-cell/buttons/components-single-cell-button.png
   :height: 4ex
   :class: no-scaled-link

.. |submit-record-button-ena| image:: /assets/images/buttons/submit-record-button-ena.png
   :height: 3.5ex
   :class: no-scaled-link

.. |submit-record-button-zenodo| image:: /assets/images/buttons/submit-record-button-zenodo.png
   :height: 3.5ex
   :class: no-scaled-link

.. |upload-single-cell-manifest-button| image:: /assets/images/single-cell/buttons/upload-single-cell-manifest-button.png
   :height: 4ex
   :class: no-scaled-link
