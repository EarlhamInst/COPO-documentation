.. _overview-public-repositories:

Where Your Submitted Data Goes
-------------------------------

Data submissions made using COPO are published to public repositories. These
repositories are secure online databases that allow the scientific community
worldwide to access, share and reuse data.

Supported repositories include:

* `BioImage Archive (BIA) <https://www.ebi.ac.uk/bioimage-archive>`__
* `BioStudies <https://www.ebi.ac.uk/biostudies>`__
* `Comprehensive Knowledge Archive Network (CKAN)
  <https://ckan.earlham.ac.uk>`__ (for Earlham Institute datasets)
* `European Nucleotide Archive (ENA)
  <https://www.ebi.ac.uk/ena/browser/home>`__
* `National Centre for Biotechnology Information (NCBI)
  <https://www.ncbi.nlm.nih.gov>`__
* `Zenodo <https://zenodo.org>`__

   .. list-table:: Data Submission Types and Repositories
      :width: 100%
      :align: center
      :header-rows: 1

      * - Submission type
        - Public repository
      * - Assemblies
        - ENA
      * - Barcoding (also known as Tagged sequences)
        - ENA
      * - Images
        - * Zenodo for :abbr:`REMBI (Recommended Metadata for Biological
            Images)` images and
            :abbr:`ST-FISH (Spatial Transcriptomics Fluorescence In Situ
            Hybridisation)`
          * :abbr:`BIA (BioImage Archive)` for sample images and REMBI images
            (forthcoming)
      * - Reads
        - ENA
      * - Samples
        - ENA
      * - Sequence Annotations
        - ENA
      * - Single-cell
        - ENA, Zenodo

.. _overview-public-repositories-submission-control:

Greater Control Over Your Metadata Submissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data uploads that you make in COPO can be submitted to your
individual account in a public repository, such as European Nucleotide Archive
(ENA), if you have one. This gives you greater control over your submissions,
allowing you to update metadata and still share your submissions with the
wider scientific community.

This feature is optional. You can continue to submit your data to the
public repository using COPO's account, which is the default submission route,
without needing an individual account with a repository.

Any changes that you make to the records in the public repository will
be reflected in the corresponding records in COPO.

.. _public-repositories-overview-individual-submission-ena:

Submissions to your ENA webin account
"""""""""""""""""""""""""""""""""""""

You can make an :ref:`ongoing <public-repositories-overview-individual-ongoing-submission-ena>`
or :ref:`one-off <public-repositories-overview-individual-one-off-submission-ena>`
submission of the data that you have uploaded in COPO to your European
Nucleotide Archive (ENA) Webin account.

For ongoing submissions, you only need to link your ENA Webin account to
COPO once. Once linked, you will not need to provide your ENA Webin
credentials again for subsequent submissions made through COPO.

In contrast, for one-off submissions, you will need to provide your ENA
Webin credentials each time you submit data through COPO.

The following data can be submitted to your individual ENA Webin account:

- :ref:`Assemblies <assemblies>`
- :ref:`Barcoding data <barcoding-submissions>`
- :ref:`Reads <reads>`
- :ref:`Samples <samples-submission-biodata>` (under Biodata profiles)
- :ref:`Single-cell data <single-cell-submissions>` (under Biodata profiles)
- :ref:`Sequence Annotations <sequence-annotations>`

.. tip::

   If you do not already have an ENA Webin account but would like to create
   one, refer to ENA's `Register a Submission Account
   <https://ena-docs.readthedocs.io/en/latest/submit/general-guide/registration.html#register-a-submission-account>`__
   documentation for guidance.

.. _public-repositories-overview-individual-ongoing-submission-ena:

**Ongoing submissions**

   1. Click your name in the top-right corner of the page. Then,
      click the **User Info** dropdown menu option to navigate to the **User
      Information** page.

      ..  figure:: /assets/images/repository-submissions/ena/ui/ena-ongoing-submission-pointer-to-user-info-nav-option.png
          :alt: Pointer to 'User Info' option in the top navigation menu
          :align: center
          :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/repository-submissions/ena/ui/ena-ongoing-submission-pointer-to-user-info-nav-option.png
          :class: with-shadow with-border

          **Click** ``User Info`` **option from the dropdown menu**

      .. raw:: html

         <br>

   2. On the **User Information** page, enter your
      :abbr:`ENA (European Nucleotide Archive)` Webin username and
      password in the **ENA (Webin)** form under the Submission repository
      credentials section. Then, click the **Save & validate** button to link
      your ENA Webin account to COPO.

      ..  figure:: /assets/images/repository-submissions/ena/ui/ena-ongoing-submission-credentials-form.png
          :alt: ENA Webin Credentials form on the User Information page
          :align: center
          :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/repository-submissions/ena/ui/ena-ongoing-submission-credentials-form.png
          :class: with-shadow with-border

          **Enter your ENA Webin credentials then click** ``Save & validate`` **button**

.. _public-repositories-overview-individual-one-off-submission-ena:

**One-off submission**

   1. After uploading your data, select a row in the data table. Then click the teal Submit button that appears at the
      top of the table as |submit-record-button| or |submit-record-button-ena|.

      A dialogue will appear prompting you to enter your ENA Webin username and password or use the default COPO
      ENA Webin  account to submit your data.

      ..  figure:: /assets/images/repository-submissions/ena/modals/ena-webin-credentials-form-dialogue.png
          :alt: A dialogue prompting for your ENA Webin credentials
          :align: center
          :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/repository-submissions/ena/modals/ena-webin-credentials-form-dialogue.png
          :class: with-shadow with-border
          :height: 350px

          **A dialogue prompting you to choose whether to submit using your ENA Webin account or COPO’s default ENA Webin account**

..
    Images declaration
..

.. |submit-record-button| image:: /assets/images/buttons/submit-record-button.png
   :height: 3.5ex
   :class: no-scaled-link

.. |submit-record-button-ena| image:: /assets/images/buttons/submit-record-button-ena.png
   :height: 3.5ex
   :class: no-scaled-link