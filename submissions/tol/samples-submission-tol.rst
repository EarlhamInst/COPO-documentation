.. _samples-submission-tol:

======================================
Tree of Life Profile Sample Submission
======================================

The sample types listed below correspond to different profiles or projects
within the Tree of Life (ToL) [#f1]_ programme.

Spreadsheet files, known as manifests [#f2]_, are used to record sample
metadata for submission. The sample submission process is the same across all
Tree of Life profiles [#f3]_ although the profile type vary. There are only
minor visual differences such as button labels or colours.

Sample types include:

* Aquatic Symbiosis Genomics (ASG) [#f4]_
* Darwin Tree of Life (DToL) [#f5]_
* Darwin Tree of Life Environmental (DToL_ENV)
* European Reference Genome Atlas (ERGA) [#f6]_

Use the steps below to submit samples for any of the sample types mentioned or
:download:`download a visual step-by-step guide
</assets/files/copo-visual-user-documentation.pdf>`.

.. raw:: html

   <br>

.. figure:: /assets/files/presentations/copo-sample-submission-process-illustration.gif
   :alt: Samples submission and validation process in COPO
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/files/presentations/copo-sample-submission-process-illustration.gif
   :class: with-shadow with-border
   :scale: 60%

.. centered:: **Submitting and validating samples**

.. raw:: html

   <hr>

.. _accessing-samples-page-tol:

Accessing the Samples Page
--------------------------

Using the Components Button
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click the |samples-component-button| component button in the **Components**
column as shown below:

.. figure:: /assets/images/samples/buttons/samples-button-pointer-tol.png
   :alt: Samples profile component
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/buttons/samples-button-pointer-tol.png
   :class: with-shadow with-border
   :height: 400px

   **Samples component button (located under Tree of Life profiles)**

.. raw:: html

   <br>

Using the Components Icon Navigation Pane
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /profile/components/navigation-pane-overview.rst

.. figure:: /assets/images/samples/icons/samples-icon-pointer-tol.png
   :alt: Samples profile component icon
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/icons/samples-icon-pointer-tol.png
   :class: with-shadow with-border
   :height: 120px

   **Samples component icon**

.. raw:: html

   <hr>

.. _submit-manifest-samples-tol:

Submit Samples
---------------

.. note::

   * By default, the profile type dropdown menu on the **Work profiles** page
     shows *Biodata*.

     :email:`Contact the COPO team <ei.copo@earlham.ac.uk>` for access to
     other groups. See the :ref:`project-affiliations` section for available
     projects.

   *  Samples cannot be deleted after they have been submitted.

#. Click the |blank-manifest-download-button| button to download a blank
   manifest [#f2]_.

   A manifest is a spreadsheet file used to record metadata for submission.

#. Fill in the downloaded manifest then, click |add-manifest-button| button
   to upload it from your local (computer) system.

   .. note::

      * The colour of the |add-manifest-button| button and sample name are
        based on the type of profile that you are making a submission to. See
        the :ref:`profile-types-legend` section regarding the colour codes.

   .. figure:: /assets/images/samples/ui/samples-pointer-to-add-manifest-button.png
      :alt: Pointer to add or update samples button
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/ui/samples-pointer-to-add-manifest-button.png
      :class: with-shadow with-border

      **Click the highlighted button to add or update samples**

   .. raw:: html

      <br>

#. Click the |upload-sample-manifest-button| button in the dialogue displayed
   to choose a file from your local system.

    .. figure:: /assets/images/samples/modals/samples-upload-spreadsheet-dialogue.png
       :alt: Upload Sample Spreadsheet dialogue
       :align: center
       :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/modals/samples-upload-spreadsheet-dialogue.png
       :class: with-shadow with-border

       **Upload sample spreadsheet dialogue**

   .. raw:: html

      <br>

#. Upload sample images (if applicable). Refer to
   :ref:`image-submission-tol-samples` section to learn more.

   .. raw:: html

      <br>

#. Upload sample permits (if applicable). Refer to :ref:`permits-submission`
   section to learn more.

   .. raw:: html

      <br>

#. The uploaded samples are shown in a preview before final submission. Click
   the |finish-button| button to finalise the upload.

    .. figure:: /assets/images/samples/modals/samples-upload-spreadsheet-dialogue-with-samples-uploaded.png
      :alt: Upload Sample Spreadsheet dialogue with samples
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/modals/samples-upload-spreadsheet-dialogue-with-samples-uploaded.png
      :height: 600px
      :class: with-shadow with-border

      **Sample upload preview**

   .. raw:: html

      <br>

   A confirmation dialogue appears (if applicable). Click **Confirm** to submit
   the samples.

   .. figure:: /assets/images/samples/modals/samples-submit-samples-dialogue.png
      :alt: 'Submit Samples' confirmation dialogue
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/modals/samples-submit-samples-dialogue.png
      :class: with-shadow with-border
      :height: 300px

      **Finalise sample submission**

   .. raw:: html

      <br>

#. The new samples will be displayed on the **Samples** page after a
   successful validation.

    .. figure:: /assets/images/samples/ui/samples-submitted.png
       :alt: Sample(s) uploaded
       :align: center
       :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/ui/samples-submitted.png
       :class: with-shadow with-border

       **Samples page showing the uploaded samples**

.. raw:: html

   <hr>

.. _samples-submission-status-tol:

View Submission Status
~~~~~~~~~~~~~~~~~~~~~~

Sample managers are notified of new or updated submissions. They review the
submission and either accept or reject it.

The submission status is indicated in the following columns:

* **Status** - the status of the submission is displayed in this column.
  Possible values are pending, processing, accepted or rejected.

* **Approval Date** - the date when the sample manager made a decision
  regarding the submission.

* **Error** - if there are any errors with the submission, details will be
  displayed in this column.

.. raw:: html

   <hr>

.. _samples-submission-accessions-tol:

View Accessions
----------------

Accessions are unique identifiers assigned to submissions after they have been
successfully submitted to public repositories.

The accession columns are:

* **Biosample Accession** - the primary identifier of the sample submission.

* **SRA Accession** - the :abbr:`SRA (Sequence Read Archive )` [#f7]_
  accession is the secondary identifier for the sample submission.

* **Submission Accession** - the identifier for the submission of the sample
  metadata to the public repository. It cannot be used to access the sample
  metadata in the public  repository but can be used to track the submission
  in COPO.

The value displayed in the columns below corresponds to the source or specimen
of the submitted samples.

* **Sample Derived From**
* **Sample Same As**
* **Sample Symbiont Of**

.. figure:: /assets/images/samples/ui/samples-pointer-to-accession-column.png
   :alt: Samples table highlighting columns that display accession for
         submitted samples
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/samples/ui/samples-pointer-to-accession-column.png
   :class: with-shadow with-border

   **Columns displaying accession identifiers for submitted sample data**

.. raw:: html

   <hr>

Related Topics
--------------

.. seealso::

   * :ref:`permits-submission`
   * :ref:`image-submission`
   * :ref:`reads`
   * :ref:`data-updates`
   * :ref:`sample-update-notes`
   * :ref:`data-download`
   * :ref:`Steps to Create a Tree of Life Profile <profile-walkthrough-tol>`
   * :ref:`accessions`
   * :ref:`What are the steps for submitting metadata in COPO and ensuring it
     appears in public repositories?
     <faq-samples-submission-public-availability>`
     :abbr:`FAQ (Frequently Asked Question)`

.. raw:: html

   <br>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Tree of Life (ToL) <ToL>`.
.. [#f2] See term: :term:`Manifest`.
.. [#f3] See term: :term:`Tree of Life profile <ToL profile>`.
.. [#f4] See term: :term:`ASG`.
.. [#f5] See term: :term:`DToL`. *DToL* may sometimes be referred to as *DTOL*.
.. [#f6] See term: :term:`ERGA`.
.. [#f7] See term: :term:`Sequence Read Archive (SRA) accession
   <SRA accession>`.

..
    Images declaration
..

.. |add-manifest-button| image:: /assets/images/buttons/add-manifest-button.png
   :height: 4ex
   :class: no-scaled-link

.. |add-asg-manifest-button| image:: /assets/images/samples/asg/buttons/add-asg-manifest-button.png
   :height: 4ex
   :class: no-scaled-link

.. |blank-manifest-download-button| image:: /assets/images/buttons/download-button-blank-manifest.png
   :height: 4ex
   :class: no-scaled-link

.. |confirm-button| image:: /assets/images/buttons/confirm-button.png
   :height: 4ex
   :class: no-scaled-link

.. |download-sample-manifest-button| image:: /assets/images/samples/buttons/samples-download-manifest-button.png
   :height: 4ex
   :class: no-scaled-link

.. |finish-button| image:: /assets/images/buttons/finish-button1.png
   :height: 4ex
   :class: no-scaled-link

.. |samples-component-button| image:: /assets/images/samples/buttons/components-samples-button.png
   :height: 4ex
   :class: no-scaled-link

.. |upload-sample-manifest-button| image:: /assets/images/samples/buttons/samples-upload-manifest-button.png
   :height: 4ex
   :class: no-scaled-link
