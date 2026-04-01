.. _faq-reads:

Reads
-----

.. tip::

   To read the entire answer to a :abbr:`FAQ (Frequently Asked Question)`,
   click the arrow icon (|collapsible-item-arrow|) below any question to
   expand or collapse it.

.. raw:: html

   <hr>

.. _faq-reads-manifest-paired-reads:

How do I complete the reads manifest for paired-read submission?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   * Ensure that the **Reads** manifest contains the following:

      * **PAIRED** as the value for the **Library layout** column
      *  File names in the **File name** column separated by a comma

      See below for a snapshot of a **Reads** manifest for paired reads:

      .. figure:: /assets/images/reads/ui/reads-manifest-paired.png
         :alt: Reads manifest for paired reads
         :align: center
         :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/reads/ui/reads-manifest-paired.png
         :class: with-shadow with-border

         **Reads manifest for paired reads**

.. raw:: html

   <br>

.. _faq-reads-submission-file-types:

Which file types are required for read submissions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   See the `documentation <ena-reads-data-formats_>`__ on
   European Nucleotide Archive (ENA) for details about the types of files
   that can be submitted for read submissions.

.. raw:: html

   <br>

Which reads checklist is linked to samples?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   The reads checklist associated with samples in the dropdown menu on the
   **Reads** page is marked with an asterisk (*) and is selected by default
   when the page loads.

.. raw:: html

   <br>

.. _faq-reads-update-errors:

What causes errors during reads updates?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   .. hint::

      The words, ``manifest`` and ``checklist`` are used interchangeably. They
      both refer to a spreadsheet.

   Errors occur due to several reasons. An error message will be displayed
   detailing the issue(s) encountered and potential resolution(s). If you are
   uncertain how to proceed, please contact the
   :email:`COPO team <ei.copo@earlham.ac.uk>`.

   Updates to reads can be made by uploading the amended manifest to the same
   checklist and profile initially used for the submission. Please note that
   this is possible if the values in the ``Sample``, ``File checksum``,
   ``File name`` and ``Library layout`` columns remain unchanged in the
   manifest. If any of these values change, errors will occur during the
   update process.

   This is because the value in the ``Sample`` column serves as the key for
   each row in the **Reads** manifest. Each unique sample in the manifest
   corresponds to a different biosample, which is linked to the values in
   the ``File checksum``, ``File name`` and ``Library layout`` columns.

   Other potential reasons for errors include but are not limited to:

      * Uploading null or empty files and associating them with rows in the
        manifest

      * Assigning files to samples that already have the same files attached
        will produce errors

.. raw:: html

   <br>

Are read accessions assigned only after a study is published?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

   No, accessions are assigned after reads submissions have been completed.

   Publishing a profile (or study) only makes the submissions under the
   profile public and accessible on repositories such as the
   `European Nucleotide Archive (ENA) <ena-website_>`__ and
   `National Centre for Biotechnology Information (NCBI) <ncbi-website_>`__.

   See the following sections for more information:

   * :ref:`accessions`
   * :ref:`publishing-data`
   * :ref:`overview-public-repositories`

.. raw:: html

   <hr>

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/arrow-right.png
   :height: 2ex
   :class: no-scaled-link

..
    Link declaration
..

.. _paired-reads-manifest-link: https://ena-docs.readthedocs.io/en/latest/submit/fileprep/reads.html#accepted-read-data-formats
.. _ena-reads-data-formats: https://ena-docs.readthedocs.io/en/latest/submit/fileprep/reads.html#accepted-read-data-formats
.. _ena-website: https://www.ebi.ac.uk/ena/browser/home
.. _ncbi-website: https://www.ncbi.nlm.nih.gov
