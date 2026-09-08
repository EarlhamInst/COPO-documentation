.. _faq-assemblies:

Assemblies
----------

.. tip::

   To read the entire answer to a :abbr:`FAQ (Frequently Asked Question)`,
   click the arrow icon (|collapsible-item-arrow|) below any question to
   expand or collapse it.

.. raw:: html

   <hr>

.. _faq-assemblies-submission-file-types:

What data files are required for assembly submissions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   See the `European Nucleotide Archive's (ENA's) documentation
   <https://ena-docs.readthedocs.io/en/latest/submit/assembly.html#files-for-genome-assembly-submissions>`__
   for details about the types of files that can be submitted for assembly
   submissions.

.. raw:: html

   <br>

.. _faq-assemblies-submission-locus-tag-assignment:

How do I assign locus tags to assemblies?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

  .. hint::

     Each profile in COPO is known as a study or project in
     :abbr:`ENA (European Nucleotide Archive)` (after reads have been
     submitted).

  .. note::

     Reads **must** be submitted to assign a locus tag, as the European
     Nucleotide Archive (ENA) project submission is created only after reads
     submission is complete.

  You can assign a custom locus tag when creating a profile in COPO. See the
  image below for guidance.

  .. figure:: /assets/images/profiles/ui/profile-add-form-profile-form-locus-tag.png
     :alt: Adding locus tag to a profile
     :align: center
     :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/ui/profile-add-form-profile-form-locus-tag.png
     :class: with-shadow with-border
     :height: 400px

     **Profile form: Adding locus tag**

  If a locus tag is not assigned, :abbr:`ENA (European Nucleotide Archive)`
  will automatically assign a locus tag to your assembly after it has been
  submitted in COPO and deposited to ENA.

  See `ENA's documentation
  <https://ena-docs.readthedocs.io/en/latest/submit/general-guide/locus-tags.html#what-are-locus-tags>`__
  for more details. The documentation outlines rules that the locus tag prefix
  should conform to.

.. raw:: html

   <br>

What should I select from the SAMPLE dropdown in the "Add Assembly" form?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

  .. hint::

     When submitting assemblies, the sample accession, also known as
     **sraAccession**, follow the format, ``ERSXXXXXXXX``.

  * The **SAMPLE** dropdown menu in the **Add Assembly** form will display the
    sraAccession(s) that are associated with samples that have been submitted
    in COPO.

  * The sraAccession will be displayed in the **sraAccession** column in any
    data table that is associated with the profile and samples. In terms of
    assembly submission, the sraAccession will be displayed in the data table
    on the **Reads** page (once reads have been submitted).

.. raw:: html

   <br>

.. _faq-assemblies-simultaneous-submission:

Are assemblies and sequence annotations submitted together?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

   No, assemblies and sequence annotations are submitted separately in COPO.

   It is possible that the notion of `simultaneous submission` arises from the
   use of the :abbr:`EMBL (and sequence annotations submitted at the)` flat
   file format, which combines both annotated assemblies and sequence
   annotations. This may lead to the impression of a simultaneous submission.

   If you are submitting sequence annotations directly to the
   :abbr:`ENA (European Nucleotide Archive)`, EMBL files must be used, as
   they include both assemblies and annotations together.

   On the other hand, sequence annotations can be submitted separately to ENA
   if your data files are in formats such as ``.gff`` or ``.fasta``.

   .. note::

     Data file submissions depend on how users prepare and generate their
     data. For instance, :abbr:`FASTA (Fast-All)` files are still essential
     for storing and sharing sequence data but, they are not sufficient for
     representing detailed genomic annotations.

     For annotation tasks, formats like :abbr:`GFF (General feature format)`,
     :abbr:`GTF (Gene transfer format)` and
     :abbr:`BED (Browser Extensible Data)` are more appropriate because they
     provide structured information about genomic features, gene structures
     and functional elements. Thus, while FASTA is not outdated, it is often
     used alongside more specialised formats for annotation purposes.

   Please refer to the following sections in ENA's documentation for more
   information:

    * `Analysis File Groups <ena-docs-analysis-file-groups_>`__
    * `Files Required for Genome Assembly Submissions
      <ena-docs-assembly-file-groups_>`__

.. raw:: html

   <br>

Are accessions assigned to assembly submissions after studies are published?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

   No, accessions are assigned after assembly submissions have been completed.

   Publishing a profile (or study) only makes the submissions under the
   profile public and accessible on repositories such as the
   `European Nucleotide Archive (ENA) <ena-website_>`__ and
   `National Centre for Biotechnology Information (NCBI) <ncbi-website_>`__.

   See the following sections for more information:

   * :ref:`accessions`
   * :ref:`publishing-data`
   * :ref:`overview-public-repositories`

   See the :ref:`accessions` section for more information.

.. raw:: html

   <br>

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/arrow-right.png
   :height: 2ex
   :class: no-scaled-link

..
    Link declaration
..

.. _ena-docs-analysis-file-groups: https://ena-docs.readthedocs.io/en/latest/submit/analyses.html#analysis-file-groups
.. _ena-docs-assembly-file-groups: https://ena-docs.readthedocs.io/en/latest/submit/assembly.html#files-for-genome-assembly-submissions
.. _ena-website: https://www.ebi.ac.uk/ena/browser/home
.. _ncbi-website: https://www.ncbi.nlm.nih.gov
