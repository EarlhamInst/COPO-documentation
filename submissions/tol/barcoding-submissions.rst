.. _barcoding-submissions:

=========================
Submitting Barcoding Data
=========================

.. note::

   * Submit samples before uploading Barcoding manifests. See
     :ref:`Samples submission <samples-submission-tol>` for details.

     Once samples have been submitted and approved, their biosample accessions,
     specimen :abbr:`IDs (identifications)` and taxon
     :abbr:`IDs (identifications)` are needed to fill in a barcoding manifest.

   * Barcoding manifest submissions can only be done via a
     Tree of Life (ToL) [#f1]_ profile [#f2]_. Please see:
     :ref:`Steps to Create a Tree of Life Profile <profile-walkthrough-tol>`
     for guidance.

.. raw:: html

   <hr>

.. _accessing-barcoding-manifest-page:

Accessing the Barcoding Manifest Page
-------------------------------------

The **Barcoding manifests** page can be accessed from the **Components** button
associated with a profile.

.. raw:: html

   <hr>

Using the Components Button
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click the |barcoding-manifest-component-button| component button in the
**Components** column as shown below:

.. figure:: /assets/images/barcoding/ui/barcoding_button_pointer_tol.png
   :alt: Tree of Life Barcoding Manifest profile component
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/barcoding/ui/barcoding_button_pointer_tol.png
   :class: with-shadow with-border
   :height: 300px

   **Button to access the Barcoding manifest page (highlighted)**

.. raw:: html

   <br>

Using the Components Icon Navigation Pane
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /profile/components/navigation-pane-overview.rst

.. figure:: /assets/images/barcoding/icons/barcoding_manifest_icon_pointer.png
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/barcoding/icons/barcoding_manifest_icon_pointer.png
   :class: with-shadow with-border
   :height: 120px

   **Navigation pane showing the Barcoding manifest component icon**

.. raw:: html

   <hr>

.. raw:: html

   <hr>

.. _submit-manifest-barcoding:

Upload Data
-----------

.. tip::

   In the **Barcoding Manifest**, the field, **Organism**, refers to the
   biosample accession of the sample.

1. On the **Barcoding manifests** page, click the dropdown menu to choose a
   checklist [#f3]_. Hover over each option to view its description.

   .. figure:: /assets/images/barcoding/ui/barcoding_manifests_with_checklist_dropdown_list.png
      :alt: Available checklist options
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/barcoding/ui/barcoding_manifests_with_checklist_dropdown_list.png
      :class: with-shadow with-border

      **Checklist options for Barcoding manifest submissions**

   .. raw:: html

      <br>

2. Click the |barcoding-manifest-blank-manifest-download-button| button to
   download a blank manifest [#f4]_.

   A manifest is a spreadsheet file used to record metadata for submission.

3. Click |add-barcoding-manifest-manifest-button| button to upload
   a completed Barcoding manifest.

   .. note::

      * Please ensure that the manifest that you are uploading matches the
        checklist type selected in step 1. You will encounter errors if the
        uploaded manifest does not correspond with the selected dropdown menu
        checklist option.

      * The colour of the |add-barcoding-manifest-manifest-button| button is
        based on the type of profile that you are submitting a barcoding
        manifest for. See the :ref:`profile-types-legend` section regarding
        the colour code for the various types of project profiles on COPO.

   .. hint::

      *Tagged sequence* is another term for barcoding data.

   .. figure:: /assets/images/barcoding/ui/barcoding_manifests_pointer_to_add_barcoding_manifest_button.png
      :alt: Pointer to 'Add tagged sequences from spreadsheet' button
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/barcoding/ui/barcoding_manifests_pointer_to_add_barcoding_manifest_button.png
      :class: with-shadow with-border

      **Click "Add tagged sequences from spreadsheet" button to open an upload dialog**

   .. raw:: html

      <br>

4. A dialog is displayed. Click the |barcoding-manifests-upload-button| button
   to choose a spreadsheet file from your local system.

    .. figure:: /assets/images/barcoding/modals/barcoding_manifest_upload_barcoding_manifest_dialog.png
       :alt: Upload Barcoding Manifest dialog
       :align: center
       :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/barcoding/modals/barcoding_manifest_upload_barcoding_manifest_dialoge.png
       :class: with-shadow with-border
       :height: 200px

       **Click 'Upload Barcoding Manifest' button**

   .. raw:: html

      <br>

5. The uploaded data is shown in a preview before final submission. Click
   |barcoding-manifests-finish-button| button to finalise the upload.

   .. figure:: /assets/images/barcoding/modals/barcoding_manifests_dialog_with_uploaded_data.png
      :alt: Upload Barcoding Manifest dialog with data
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/barcoding/modals/barcoding_manifests_dialog_with_uploaded_data.png
      :class: with-shadow with-border
      :height: 400px

      **Barcoding manifest upload preview**

   .. raw:: html

      <br>

6. The new barcoding data will be displayed on the **Barcoding manifests**
   page after a successful submission.

   .. figure:: /assets/images/barcoding/ui/barcoding_manifests_uploaded.png
      :alt: Barcoding manifest(s) submitted
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/barcoding/ui/barcoding_manifests_uploaded.png
      :class: with-shadow with-border

      **Barcoding manifest page showing the uploaded data**

   .. raw:: html

      <br>

.. raw:: html

   <hr>

.. _submit-manifest-barcoding-submission-section:

Submit Data
-----------

.. note::

   * Follow the steps in :ref:`submit-manifest-barcoding` to upload a
     barcoding manifest before proceeding with the submission.

   * The following repositories are supported for Barcoding manifest
     submissions:

     * European Nucleotide Archive (ENA) via |submit-record-button| button

7. After uploading data, select a row in the data table then, click the
   **Submit** button (located in the top-right corner of the table) as shown
   below.

   .. note::

      Please ensure that the selected record is under the desired checklist
      option. If not, choose another option from the dropdown menu, then
      select a row in the data table.

   .. figure:: /assets/images/barcoding/ui/barcoding_manifests_pointer_to_submit_barcoding_manifest_button.png
      :alt: Submit Barcoding manifest button
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/barcoding/ui/barcoding_manifests_pointer_to_submit_barcoding_manifest_button.png
      :class: with-shadow with-border

      **Click “Submit” to submit the data for the highlighted row**

   .. raw:: html

      <br>

8. Wait for the submission process to be completed. The status and accessions
   of the submitted records can be viewed in the data table. See the sections
   below for details.

   .. figure:: /assets/images/barcoding/ui/barcoding_manifests_submitted.png
      :alt: Barcoding manifest has been successfully submitted
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/barcoding/ui/barcoding_manifests_submitted.png
      :class: with-shadow with-border

      **Barcoding manifest has been submitted**

   .. raw:: html

      <br>

.. raw:: html

   <hr>

.. _barcoding-submission-make-public:

Make Data Public
----------------

9. Submissions are private by default. You can make the data publicly
   accessible by referring to the steps in the
   :ref:`publishing-data-from-profile-level` section.

.. raw:: html

   <hr>

.. _barcoding-submission-status:

View Submission Status
----------------------

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

* **STATUS** - Displays the status returned from the repository, European
  Nucleotide Archive (ENA), assigned to the project

* **ERROR** - Displays any error message associated with the submission.

.. raw:: html

   <hr>

.. _barcoding-submission-accessions:

View Accessions
---------------

Accessions are unique identifiers assigned to submissions after they have been
successfully submitted to public repositories.

The accession columns are:

* **ACCESSION** - Displays the unique identifier assigned by European
  Nucleotide Archive (ENA) after a successful submission.

Clicking any accession in the data table will open the corresponding record in
the associated repository. You can also find the same record by searching for
the accession directly in the repository.

.. tip::

   Alternatively, click the |accessions-component-icon| icon located in the
   top-right corner of the data table to navigate to the **Accessions** page
   that displays accessions for all submissions.

.. raw:: html

   <hr>

.. _barcoding-manifests-deletion:

Deleting Barcoding Data
------------------------

.. note::

   Barcoding data can only be deleted **before** they have been submitted.

Click a row in the data table on the **Barcoding manifests** page then, click
the **Delete** button (located in the top-right corner of the table) as
shown below:

.. figure:: /assets/images/barcoding/ui/barcoding_manifests_pointer_to_delete_barcoding_manifest_button.png
   :alt: Delete barcoding manifest button
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/barcoding/ui/barcoding_manifests_pointer_to_delete_barcoding_manifest_button.png
   :class: with-shadow with-border

   **Click the Delete button to remove the highlighted data record**

.. figure:: /assets/images/barcoding/ui/barcoding_manifests_deleted.png
   :alt: Barcoding manifests deleted successfully
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/barcoding/ui/barcoding_manifests_deleted.png
   :class: with-shadow with-border

   **Barcoding manifest page showing that the data has been deleted**

.. raw:: html

   <hr>

Related Topics
--------------

.. seealso::

   * :ref:`data-updates`
   * :ref:`samples-submission`
   * :ref:`Steps to Create a Tree of Life Profile <profile-walkthrough-tol>`
   * :ref:`accessions`


.. raw:: html

   <br>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Tree of Life (ToL) <ToL>`.
.. [#f2] Also known as COPO profile. See:
   :term:`COPO profile or work profile <COPO profile>`.
.. [#f3] See term: :term:`Checklist`.
.. [#f4] See term: :term:`Manifest`.

..
    Images declaration
..

.. |accessions-component-icon| image:: /assets/images/accessions/icons/components_accessions_icon.png
   :height: 3ex
   :class: no-scaled-link

.. |add-barcoding-manifest-manifest-button| image:: /assets/images/buttons/add_manifest_button.png
   :height: 4ex
   :class: no-scaled-link

.. |barcoding-manifest-blank-manifest-download-button| image:: /assets/images/buttons/download_button_blank_manifest.png
   :height: 4ex
   :class: no-scaled-link

.. |barcoding-manifest-component-button| image:: /assets/images/barcoding/buttons/components_barcoding_manifest_button.png
   :height: 4ex
   :class: no-scaled-link

.. |barcoding-manifests-finish-button| image:: /assets/images/buttons/finish_button2.png
   :height: 4ex
   :class: no-scaled-link

.. |barcoding-manifests-upload-button| image:: /assets/images/barcoding/buttons/barcoding_manifest_upload_button.png
   :height: 4ex
   :class: no-scaled-link

.. |info-icon| image:: /assets/images/icons/info_icon.png
   :height: 2.5ex
   :class: no-scaled-link

.. |submit-record-button| image:: /assets/images/buttons/submit_record_button.png
   :height: 3.5ex
   :class: no-scaled-link


