.. _permits-submission:

==================
Submitting Permits
==================

.. note::

   * Permits can only be submitted via a Tree of Life (ToL) profile [#f1]_.
     Refer to
     :ref:`Steps to Create a Tree of Life Profile <profile-walkthrough-tol>`
     for guidance.

   * If you are using a Windows operating system (OS) to upload permits, the
     file name of the permits should exclude the extension  ``.pdf`` or
     ``.PDF``. This is because Windows OS by default, hides file extensions
     which results in it not being visible to you.

     If you would like to see the file extension, you can enable it by
     following these `guidelines <windows-common-file-name-guidelines_>`__.

     Ultimately, the permit file name should be in the format:
     ``permit_name.pdf`` **not** ``permit_name.pdf.pdf``.

   * COPO automatically appends the permit file name with the date of the
     submission during the permit submission process. This is to ensure that
     the permit file name is unique.

     For example, if a permit with the file name ``permit_name.pdf`` is
     uploaded, COPO will append the date to the file
     name as follows: ``permit_name_yyyymmdd.pdf`` where ``yyyymmdd`` is the
     date when the submission was made.

.. warning::

   If you have more than one permit ﬁle to upload, they **must** be
   uploaded at the same time i.e. after you have clicked the
   |upload-permits-button| button, navigate to the directory where the
   permits are stored and ``CTRL + click`` all of the permits so that all
   the permits are highlighted and uploaded at the same time.

#. Upload samples.

   Refer to :ref:`Samples Submission (Tree of Life (ToL) profiles)
   <samples-submission-tol>` section for guidance.

   .. note::

      Permits can only be submitted after
      :abbr:`ERGA (European Reference Genome Atlas)` [#f2]_ samples have been
      uploaded in the **Upload sample spreadsheet** dialog.

#. The uploaded samples are shown in a table in the **Upload sample
   spreadsheet** dialog as shown below.

   .. important::

      * The |upload-permits-button| button becomes available only after
        uploading a sample manifest that has ``Y`` set to any of the following
        columns: ``ETHICS_PERMITS_REQUIRED``, ``SAMPLING_PERMITS_REQUIRED`` or
        ``NAGOYA_PERMITS_REQUIRED``.

        Similarly, if ``Y`` is set in any of these columns, the corresponding
        permit file name column must be populated with the permit file name.

      * Permit uploads must be completed in the same session in which the
        sample manifest is uploaded, as the permit upload process depends on
        the sample manifest metadata. Therefore, ensure that step 1 is
        completed in the same session.

   .. figure:: /assets/images/samples/erga/modals/samples_erga_upload_spreadsheet_dialog_with_uploaded_samples_permits_required.png
      :alt: Upload sample spreadsheet dialog with uploaded samples
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/erga/modals/samples_erga_upload_spreadsheet_dialog_with_uploaded_samples_permits_required.png
      :class: with-shadow with-border

      **Sample upload preview**

   .. raw:: html

      <br>

#. In the sample spreadsheet dialog, click the **Sample Permits** tab then,
   click the |upload-permits-button| button to browse your local (computer)
   system for ``.pdf`` permit files to upload.

   .. figure:: /assets/images/samples/erga/modals/samples_erga_upload_spreadsheet_dialog_with_no_permits_uploaded.png
      :alt: Upload Sample Spreadsheet dialog with no permits uploaded
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/erga/modals/samples_erga_upload_spreadsheet_dialog_with_no_permits_uploaded.png
      :class: with-shadow with-border

      **Dialog with no permits uploaded**

   .. raw:: html

      <br>

#. After uploading permits, the table under the **Sample Permits** tab is
   populated with them.

   .. figure:: /assets/images/samples/erga/modals/samples_erga_upload_spreadsheet_dialog_with_permits_uploaded.png
      :alt: Upload Sample Spreadsheet dialog with permits uploaded
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/erga/modals/samples_erga_upload_spreadsheet_dialog_with_permits_uploaded.png
      :class: with-shadow with-border

      **Dialog with permits uploaded**

   .. raw:: html

      <br>

#. Click the |finish-button| button to submit the permits and samples.

   A **Submit samples** confirmation dialog is displayed. If you decide to
   confirm the samples submission, click the **Confirm** button.

   .. figure:: /assets/images/samples/modals/samples_submit_samples_dialog.png
      :alt: 'Submit samples' confirmation dialog
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/modals/samples_submit_samples_dialog.png
      :class: with-shadow with-border
      :height: 250px

      **Confirm sample upload**

.. raw:: html

   <hr>

.. _permits-submission-download-permits:

Download Submitted Permits
--------------------------

.. note::

   *  Permits can only be downloaded **after** they have been submitted.
   *  Permits **cannot** be deleted or modified after they have been submitted.

.. raw:: html

  <br>

On Samples page
~~~~~~~~~~~~~~~

#. Navigate to the **Samples** page.

   See :ref:`Accessing the Samples page (Tree of Life (ToL) profiles)
   <accessing-samples-page-tol>` section for guidance.

#. Select the sample records that you would like to download permits for.

   Then, click the |download-permits-button1| button to download permits
   submitted for the selected sample records.

   .. collapse:: Tips for selecting records

      .. raw:: html

         <br>

     .. tip::

        * Hold ``Ctrl`` and click to select multiple records.
        * Hold ``Shift`` and click the first and last record to select in the
        * range.
        * Click |select-all-button| to select all records.
        * Click |select-filtered-button| to select all filtered records.
        * Click |clear-selection-button| to unselect selected records.

   .. raw:: html

      <br>

   .. figure:: /assets/images/samples/ui/samples_pointer_to_download_permits_button.png
      :alt: Samples page with sample record(s) selected and a pointer to the
            'Download permits' button
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/ui/samples_pointer_to_download_permits_button.png
      :class: with-shadow with-border

      **Click** ``Download permits`` **button**

   .. raw:: html

      <br>

#. If any permit submissions exist for the selected sample records, the
   permits will be automatically downloaded for the selected sample records
   as shown below:

   .. hint::

      Permits will be downloaded as a ``.zip`` file

   If no permits were submitted for the selected sample records, a message
   is displayed in the popup dialog indicating such as shown below:

   .. figure:: /assets/images/samples/modals/samples_download_permits_dialog_with_no_permits_exist_message.png
      :alt: No permits exist message in popup dialog for selected sample
             records
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/modals/samples_download_permits_dialog_with_no_permits_exist_message.png
      :class: with-shadow with-border
      :height: 250px

      **Dialog indicating no permits exist for selected sample records**

.. raw:: html

   <hr>

On Accept or Reject Samples page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have been assigned as a **sample manager**, see
:ref:`Download Submitted Permits (Sample manager guide)
<permits-submission-download-permits-sample-managers>` for more information.

.. raw:: html

   <hr>

Related Topics
--------------

.. seealso::

   * :ref:`image-submission-tol-samples`
   * :ref:`barcoding-submissions`

.. raw:: html

   <br>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Tree of Life profile <ToL profile>`.
.. [#f2] See term: :term:`ERGA`.

..
    Images declaration
..

.. |accept-reject-samples-navigation-button| image:: /assets/images/samples/accept_reject_samples/buttons/samples_accept_reject_navigation_button.png
   :height: 4ex
   :class: no-scaled-link

.. |clear-selection-button| image:: /assets/images/buttons/clear_selection_button.png
   :height: 4ex
   :class: no-scaled-link

.. |download-permits-button1| image:: /assets/images/buttons/permits_download_button1.png
   :height: 4ex
   :class: no-scaled-link

.. |finish-button| image:: /assets/images/buttons/finish_button1.png
   :height: 4ex
   :class: no-scaled-link

.. |select-all-button| image:: /assets/images/buttons/select_all_button.png
   :height: 4ex
   :class: no-scaled-link

.. |select-filtered-button| image:: /assets/images/buttons/select_filtered_button.png
   :height: 4ex
   :class: no-scaled-link

.. |upload-permits-button| image:: /assets/images/buttons/permits_upload_button.png
   :height: 4ex
   :class: no-scaled-link

..
    Link declaration
..

.. _windows-common-file-name-guidelines: https://support.microsoft.com/en-gb/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01
