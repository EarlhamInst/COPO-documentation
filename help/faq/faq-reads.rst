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

   <br>

What do the library-related field values mean?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

   This section provides a brief overview of library preparation fields and
   their possible values, including both free-form and controlled vocabulary
   fields.

   .. tip::

      Click the arrow icon (|collapsible-item-arrow|) below any field to
      expand or collapse its content.


   .. collapse:: Design description

      .. raw:: html

         <br>

      Goal and setup of the individual library including library was
      constructed.

   .. collapse:: Library construction protocol

      .. raw:: html

         <br>

      Free form text describing the protocol by which the sequencing library
      was constructed.

   .. collapse:: Library selection

      .. raw:: html

         <br>

      .. list-table:: Library selection options
         :width: 100%
         :align: center
         :header-rows: 1

         * - Method used to enrich the target in the sequence
             library preparation
           - Description
         * - 5-methylcytidine antibody
           - Selection of methylated DNA fragments using an antibody raised
             against 5-methylcytosine or 5-methylcytidine (m5C).
         * - CAGE
           - Cap-analysis gene expression.
         * - cDNA
           - PolyA selection or enrichment for messenger RNA (mRNA);
             synonymise with PolyA
         * - cDNA_oligo_dT
           - priming by annealing to PolyA tails of eukaryotic mRNAs.
         * - cDNA_randomPriming
           - random primers typically used to prime mRNAs.
         * - ChIP
           - Chromatin immunoprecipitation
         * - ChIP-Seq
           - Chromatin immunoPrecipitation, reveals binding sites of specific
             proteins, typically transcription factors (TFs) using antibodies
             to extract DNA fragments bound to the target protein.
         * - DNase
           - DNase I endonuclease digestion and size selection reveals regions
             of chromatin where the DNA is highly sensitive to DNase I.
         * - HMPR
           - Hypo-methylated partial restriction digest
         * - Hybrid Selection
           - Selection by hybridisation in array or solution.
         * - Inverse rRNA
           - depletion of ribosomal RNA by oligo hybridisation.
         * - Inverse rRNA selection
           - depletion of ribosomal RNA by inverse oligo hybridisation.
         * - MBD2 protein methyl-CpG binding domain
           - Enrichment by methyl-CpG binding domain.
         * - MDA
           - Multiple Displacement Amplification, a non-PCR based DNA
             amplification technique that amplifies a minute
             quantifies of DNA to levels suitable for genomic analysis.
         * - MF
           - Methyl Filtrated
         * - MNase
           - Identifies well-positioned nucleosomes. uses Micrococcal Nuclease
             (MNase) is an endo-exonuclease that processively digests DNA
             until an obstruction, such as a nucleosome, is reached.
         * - MSLL
           - Methylation Spanning Linking Library
         * - Oligo-dT
           - enrichment of messenger RNA (mRNA) by hybridisation to Oligo-dT.
         * - other
           -  Other library enrichment, screening, or selection process.
         * - padlock probes capture method
           - Targeted sequence capture protocol covering an arbitrary set of
             nonrepetitive genomics targets. An example is
             capture bisulfite sequencing using padlock probes (BSPP).
         * - PCR
           - target enrichment via PCR
         * - PolyA
           - PolyA selection or enrichment for messenger RNA (mRNA); should
             replace cDNA enumeration.
         * - RACE
           - Rapid Amplification of cDNA Ends.
         * - RANDOM
           - No Selection or Random selection
         * - RANDOM PCR
           - Source material was selected by randomly generated primers.
         * - Reduced Representation
           - Reproducible genomic subsets, often generated by restriction
             fragment size selection, containing a manageable
             number of loci to facilitate re-sampling.
         * - repeat fractionation
           - Selection for less repetitive (and more gene rich) sequence
             through Cot filtration (CF) or other fractionation
             techniques based on DNA kinetics.
         * - Restriction Digest
           - DNA fractionation using restriction enzymes.
         * - RT-PCR
           - target enrichment via
         * - size fractionation
           -  Physical selection of size appropriate targets.
         * - unspecified
           -  Library enrichment, screening, or selection is not specified.

   .. collapse:: Library source

      .. raw:: html

         <br>

      .. list-table:: Library source options
         :width: 100%
         :align: center
         :header-rows: 1

         * - Type of source material being sequenced
           - Description
         * - GENOMIC
           - Genomic DNA (includes PCR products from genomic DNA).
         * - GENOMIC SINGLE CELL
           - Genomic DNA from a single cell.
         * - METAGENOMIC
           - Mixed material from metagenome.
         * - METATRANSCRIPTOMIC
           - Transcription products from community targets
         * - OTHER
           - Other, unspecified or unknown library source material.
         * - SYNTHETIC
           - Synthetic DNA.
         * - TRANSCRIPTOMIC
           - Transcription products or non genomic DNA (EST, cDNA, RT-PCR,
             screened libraries).
         * - TRANSCRIPTOMIC SINGLE CELL
           - Transcriptomic products from a single cell.
         * - VIRAL RNA
           - Viral RNA.

   .. collapse:: Library strategy

      .. raw:: html

         <br>

      .. list-table:: Library strategy options
         :width: 100%
         :align: center
         :header-rows: 1

         * - Sequencing technique
           - Description
         * - AMPLICON
           -  Sequencing of overlapping or distinct PCR or RT-PCR products.
              For example, metagenomic community profiling using SSU rRNA .
         * - ATAC-seq
           -  Assay for Transposase-Accessible Chromatin (ATAC) strategy is
              used to study genome-wide chromatin accessibility. alternative
              method to DNase-seq that uses an engineered Tn5 transposase to
              cleave DNA and to integrate primer DNA sequences into the
              cleaved genomic DNA.
         * - Bisulfite-Seq
           - MethylC-seq. Sequencing following treatment of DNA with
             bisulfite to convert cytosine residues to uracil
             depending on methylation status.
         * - ChIA-PET
           - Direct sequencing of proximity-ligated chromatin
             immunoprecipitates.
         * - ChIP-Seq
           - ChIP-seq, Chromatin ImmunoPrecipitation, reveals binding sites
             of specific proteins, typically transcription factors (TFs)
             using antibodies to extract DNA fragments bound to the target
             protein.
         * - ChM-Seq
           - ChIPmentation combines chromatin immunoprecipitation with
             sequencing library preparation by Tn5 transposase
         * - CLONE
           -  Genomic clone based (hierarchical) sequencing.
         * - CLONEEND
           -  Clone end (5', 3', or both) sequencing.
         * - CTS
           -  Concatenated Tag Sequencing
         * - DNase-Hypersensitivity
           - Sequencing of hypersensitive sites, or segments of open
             chromatin that are more readily cleaved by DNaseI.
         * - EST
           -  Single pass sequencing of cDNA templates
         * - FAIRE-seq
           - Formaldehyde Assisted Isolation of Regulatory Elements. Reveals
             regions of open chromatin.
         * - FINISHING
           -  Sequencing intended to finish (close) gaps in existing coverage.
         * - FL-cDNA
           -  Full-length sequencing of cDNA templates
         * - GBS
           - Genotyping by sequencing is a method to discover single
             nucleotide polymorphisms for genotyping studies.
         * - Hi-C
           - Chromosome Conformation Capture technique where a biotin-labelled
             nucleotide is incorporated at the ligation junction, enabling
             selective purification of chimeric DNA ligation junctions
             followed by deep sequencing.
         * - MBD-Seq
           -  Methyl CpG Binding Domain Sequencing.
         * - MeDIP-Seq
           -  Methylated DNA Immunoprecipitation Sequencing.
         * - miRNA-Seq
           - Micro RNA sequencing (miRNA-Seq) is a strategy designed to
             capture post-transcriptional RNA elements and include non-coding
             functional elements.
         * - MNase-Seq
           - Identifies well-positioned nucleosomes. uses Micrococcal
             Nuclease (MNase) is an endo-exonuclease that processively
             digests DNA until an obstruction, such as a nucleosome, is
             reached.
         * - MRE-Seq
           -  Methylation-Sensitive Restriction Enzyme Sequencing.
         * - ncRNA-Seq
           - Capture of other non-coding RNA types, including post-translation
             modification types such as snRNA (small
             nuclear RNA) or snoRNA (small nucleolar RNA), or expression
             regulation types such as siRNA (small interfering RNA) or
             piRNA/piwi/RNA (piwi-interacting RNA).
         * - NOMe-Seq
           - Nucleosome Occupancy and Methylome sequencing.
         * - OTHER
           - Library strategy not listed.
         * - POOLCLONE
           - Shotgun of pooled clones (usually BACs and Fosmids).
         * - RAD-Seq
           - Restriction site associated DNA marker.
         * - Ribo-Seq
           - Ribosome profiling (also named ribosome footprinting) that uses
             specialized messenger RNA (mRNA) sequencing to determine which
             mRNAs are being actively translated. It produces a
             "global snapshot" of all the ribosomes active in a cell at a
             particular moment, known as a translatome.
         * - RIP-Seq
           - Direct sequencing of RNA immunoprecipitates (includes CLIP-Seq,
             HITS-CLIP and PAR-CLIP).
         * - RNA-Seq
           - Random sequencing (RNA-Seq) of whole transcriptome, also known
             as Whole Transcriptome Shotgun Sequencing (WTSS).
         * - SELEX
           - Systematic Evolution of Ligands by Exponential enrichment
         * - snRNA-seq
           - Single nucleus RNA sequencing (snRNA-seq) is a method for
             profiling gene expression in cells which are difficult to isolate.
         * - ssRNA-seq
           - Strand-specific RNA sequencing (ssRNA-seq)
         * - Synthetic-Long-Read
           - binning and barcoding of large DNA fragments to facilitate
             assembly of the fragment
         * - Targeted-Capture
           - Enrichment of a targeted subset of loci.
         * - Tethered Chromatin Conformation Capture
           -  Tethered Chromatin Conformation Capture.
         * - Tn-Seq
           - Quantitatively determine fitness of bacterial genes based on how
             many times a purposely seeded transposon gets
             inserted into each gene of a colony after some time.
         * - VALIDATION
           - CGHub special request: Independent experiment to re-evaluate
             putative variants.
         * - WCS
           - Random sequencing of a whole chromosome or other replicon
             isolated from a genome.
         * - WGA
           - Whole Genome Amplification (WGA) followed by random sequencing.
         * - WGS
           - Whole Genome Sequencing - random sequencing of the whole genome
         * - WXS
           - Random sequencing of exonic regions selected from the genome.

   .. raw:: html

      <br>

   For a full list of restricted fields and their controlled vocabularies,
   refer to the :download:`experiment attribute list
   <ftp://ftp.ebi.ac.uk/pub/databases/ena/doc/xsd/sra_1_5/SRA.experiment.xsd>`
   from the European Nucleotide Archive (ENA).

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
