.. _files:

====================
Uploading Data Files
====================

.. hint::

   If you plan to make submissions to the European Nucleotide Archive (ENA),
   visit the `assembly submission file types documentation
   <ena-assembly-file-types_>`__ on ENA to see the types of data files that
   can be submitted in COPO for assembly submissions and the
   :abbr:`ENA (European Nucleotide Archive)` `read submission file types
   documentation <ena-read-file-types_>`__ for files supported for read
   submissions.

.. raw:: html

   <hr>

Accessing the Data Files Page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Data files page can be accessed from the **Components** button associated
with a profile [#f1]_.

.. raw:: html

   <hr>

Using the Components Button
"""""""""""""""""""""""""""

Click the |files-component-button| component button in the **Components**
column as shown below:

.. figure:: /assets/images/files/buttons/files_button_pointer_biodata.png
  :alt: Biodata Files profile component
  :align: center
  :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/files/buttons/files_button_pointer_biodata.png
  :class: with-shadow with-border
  :height: 300px

  **Button used to open the Data files page (highlighted)**

.. raw:: html

   <hr>

.. _files-submission-via-browser:

Submit Files from your Local (Computer) System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   The total **maximum** file size that can be uploaded from your local
   (computer) system is around **2 GB**. If you have a file larger than 2 GB
   or have multiple files whose combined total size exceeds 2 GB, please
   :ref:`submit the file(s) via the terminal <files-submission-via-terminal>`.

#. Click the |add-files-via-computer-button| button on the Data files page to
   add a new file by browsing your local file system

   .. figure:: /assets/images/files/ui/files_pointer_to_add_files_via_computer_button.png
      :alt: 'Add new file by browsing local file system' button
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/files/ui/files_pointer_to_add_files_via_computer_button.png
      :class: with-shadow with-border

      **Button to add a new file by browsing your local file system**

   .. raw:: html

      <br>

#. An **Upload File** dialog is displayed. Click the **Upload** button to
   choose a file from your local system.

   .. figure:: /assets/images/files/modals/files_upload_file_dialog.png
      :alt: Upload File dialog
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/files/modals/files_upload_file_dialog.png
      :class: with-shadow with-border
      :height: 300px

      **Dialog for uploading data files**

   .. raw:: html

      <br>

#. The new file(s) will be displayed on the **Files** page after a successful
   submission.

    .. figure:: /assets/images/files/ui/files_uploaded1.png
      :alt: File(s) submitted
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/files/ui/files_uploaded1.png
      :class: with-shadow with-border

      **Data files page showing uploaded files**

    .. raw:: html

       <br><br>

    .. hint::

       To add more files from your local system, click the
       |add-files-via-computer-button1| button (once files have been
       submitted to the profile) as an alternative to clicking the
       |add-files-via-computer-button| button.

.. raw:: html

   <hr>

.. _files-submission-via-terminal:

Submit Data Files via the Terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Click the |add-files-via-terminal-button| button on the Data files page to
   add a new file from a cluster via the terminal.

   .. figure:: /assets/images/files/ui/files_pointer_to_add_files_via_terminal_button.png
      :alt: 'Add new file via terminal' button
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/files/ui/files_pointer_to_add_files_via_terminal_button.png
      :class: with-shadow with-border

      **Files page: 'Add new file via terminal' button**

   .. raw:: html

      <br>

#. A **Move Data** dialog is displayed. Follow the instructions displayed then,
   click the **Process** button to submit the file(s) to the profile.

    .. figure:: /assets/images/files/modals/files_move_data_dialog.png
      :alt: Move Data dialog
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/files/modals/files_move_data_dialog.png
      :class: with-shadow with-border
      :height: 400px

      **Files submission: Move Data dialog**

   .. figure:: /assets/images/files/modals/files_move_data_dialog_terminal_input1.png
      :alt: Terminal with command inputted
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/files/modals/files_move_data_dialog_terminal_input1.png
      :class: with-shadow with-border

      **Input** $ ``ls - F1`` **command in the terminal**

      .. raw:: html

         <br>

   .. figure:: /assets/images/files/modals/files_move_data_dialog_with_details1.png
      :alt: Move Data dialog with details inputted
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/files/modals/files_move_data_dialog_with_details1.png
      :class: with-shadow with-border
      :height: 400px

      **Move Data dialog: Input the file name(s) returned after having ran
      the** $ ``ls - F1`` **command in the terminal. Then, click
      the** ``Process`` **button.**

      .. raw:: html

         <br>

   .. _files-submission-via-terminal-download-commands:

   .. figure:: /assets/images/files/modals/files_move_data_dialog_with_details2.png
      :alt: Move Data dialog with result (a command) after having clicked the
            "Process" button
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/files/modals/files_move_data_dialog_with_details2.png
      :class: with-shadow with-border
      :height: 400px

      **Move Data dialog: Command outputted after having clicked command in
      the** ``Process`` **button. Download the command displayed.**

      The downloaded file will have *unknown* or *download* as the file name
      depending on the browser you are using.

   .. raw:: html

      <br>

   .. figure:: /assets/images/files/modals/files_move_data_dialog_terminal_input2.png
      :alt: Terminal with command pasted
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/files/modals/files_move_data_dialog_terminal_input2.png
      :class: with-shadow with-border

      **Paste the copied command in the terminal**

      Alternatively, you can make the downloaded file executable then, run the
      file in the directory where the files are located:

      .. raw:: html

         <br>

   .. raw:: html

      <br>

#. The new file(s) will be displayed on the **Files** page after a successful
   file submission via the terminal i.e. after the command has been executed
   successfully in the terminal.

   .. figure:: /assets/images/files/ui/files_uploaded2.png
       :alt: Files submitted
       :align: center
       :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/files/ui/files_uploaded2.png
       :class: with-shadow with-border

       **Files submission: Files page displaying the uploaded file(s)**

   .. raw:: html

       <br><br>

   .. hint::

      To add more files via the terminal, click the
      |add-files-via-terminal-button1| button (once files have been
      submitted to the profile) as an alternative to clicking the
      |add-files-via-terminal-button| button.

.. raw:: html

   <hr>

.. _files-ena-file-processing-status:

Checking ENA File Processing Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   Reads, annotations or assembly submission must be completed before the data
   files can be uploaded to European Nucleotide Archive (ENA).

After completing a reads, annotations or assembly submission and associating
data files with it in COPO during the submission process, the files are
submitted to European Nucleotide Archive (ENA).

The upload status from COPO to :abbr:`ENA (European Nucleotide Archive)` is
displayed in the **ENA FILE UPLOAD STATUS** column. This status shows whether
the file(s) have been successfully uploaded to
:abbr:`ENA (European Nucleotide Archive)` after submission.

The file processing status of the file(s) uploaded to the
:abbr:`ENA (European Nucleotide Archive)` can be checked in the column,
**ENA FILE PROCESSING STATUS**, on the reads, sequence annotations or assembly
page. This status indicates that :abbr:`ENA (European Nucleotide Archive)`
is verifying and validating the submitted file(s).

The **ENA FILE PROCESSING STATUS** column is highlighted with a red rectangle
border in the image below:

.. figure:: /assets/images/sequence_annotations/ui/sequence_annotations_pointer_to_ena_file_processing_status_column.png
   :alt: ENA (European Nucleotide Archive) File Processing Status column on
         the reads, annotations or assembly page
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/sequence_annotations/ui/sequence_annotations_pointer_to_ena_file_processing_status_column.png
   :class: with-shadow with-border

.. raw:: html

   <br>

.. hint::

   * Rows with a status of **File archived: PUBLIC** or
     **File archived: PRIVATE** or in a green colour indicate that the file(s)
     have been successfully submitted to
     :abbr:`ENA (European Nucleotide Archive)`.

   * Rows with a status of **Invalid file integrity: PRIVATE** or in a red
     colour indicate that the file(s) failed to be submitted to
     :abbr:`ENA (European Nucleotide Archive)`.

   * According to :abbr:`ENA (European Nucleotide Archive)`, accessions that
     follow the format, ``ERZxxxxxxx`` refer to a private accession number
     that is not visible outside :abbr:`ENA (European Nucleotide Archive)`.

.. raw:: html

   <hr>

Related Topics
~~~~~~~~~~~~~~

.. seealso::

  * :ref:`data-deletion`
  * :ref:`How to check if data files for metadata submissions have been
    processed after upload to ENA <files-ena-file-processing-status>`
  * :ref:`Data files FAQ <faq-data-files>`
  * :ref:`reads`
  * :ref:`assemblies`

.. raw:: html

   <br>

.. rubric:: Footnotes

.. [#f1] Also known as COPO profile. See:
   :term:`COPO profile or work profile<COPO profile>`.


..
    Images declaration
..

.. |files-component-button| image:: /assets/images/files/buttons/components_files_button.png
   :height: 4ex
   :class: no-scaled-link

.. |add-files-via-computer-button| image:: /assets/images/files/buttons/add_files_via_computer_button.png
   :height: 4ex
   :class: no-scaled-link

.. |add-files-via-terminal-button| image:: /assets/images/files/buttons/add_files_via_terminal_button.png
   :height: 4ex
   :class: no-scaled-link

.. |add-files-via-computer-button1| image:: /assets/images/files/buttons/add_files_via_computer_button1.png
   :height: 4ex
   :class: no-scaled-link

.. |add-files-via-terminal-button1| image:: /assets/images/files/buttons/add_files_via_terminal_button1.png
   :height: 4ex
   :class: no-scaled-link

..
    Link declaration
..

.. _ena-assembly-file-types: https://ena-docs.readthedocs.io/en/latest/submit/fileprep/assembly.html#accepted-genome-assembly-data-formats
.. _ena-read-file-types: https://ena-docs.readthedocs.io/en/latest/submit/fileprep/reads.html#accepted-read-data-formats
