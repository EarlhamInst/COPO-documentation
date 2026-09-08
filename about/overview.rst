.. _overview:

=========
Overview
=========

Collaborative Open Omics (COPO) is a web platform used researchers and data
generators to describe the data generated from their research such as samples,
reads, images and processed data, using community-approved metadata and
vocabularies [#f1]_. As a metadata broker, COPO uses
:abbr:`FAIR (Findable, Accessible, Interoperable and Reusable)`-compliant
[#f2]_ metadata to ensure that the data are findable, accessible,
interoperable and reusable.

The COPO project is developed by a team of Research Software Engineers at the
`Earlham Institute <https://www.earlham.ac.uk/>`__. It was launched in
September 2014 as a
`Biotechnology and Biological Sciences Research Council (BBSRC)
<https://bbsrc.ukri.org/>`__ funded project under the name, Collaborative
Open Plant Omics. It has since been renamed and expanded to include all life
sciences.

Contributions to the `GitHub repository <copo-github-repository_>`__ are
welcomed and all contributors should adhere to the
:ref:`code of conduct <code-of-conduct>`.

Stay informed about the project by visiting the `News page <news-page_>`__.

.. note::

   The COPO website requires cookies, fonts and the limited processing of your
   personal data in order to function well. By using the website you are
   consenting to this. To find out more information, please see our
   :ref:`privacy-notice` and :ref:`terms-of-use`.

.. raw:: html

   <hr>

.. _overview-public-repositories:

Where Your Submitted Data Goes
------------------------------

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

.. raw:: html

   <hr>

.. _overview-accessing-copo-website:

Accessing COPO
--------------

COPO can be accessed in two modes: Production and Demo. An ORCID iD is
required to access the them.

Use the `live website <https://copo-project.org/copo>`__  to access production
mode or the `demo website <https://demo.copo-project.org/copo>`__ to access
demo mode.

.. note::

   **Production mode** is for real data submissions and sends data to the
   final repository.

   **Demo mode** is for testing only; data submitted here is not sent to the
   final repository and is deleted periodically.

.. hint::

   You can register for an ORCID iD on the
   `ORCID website <https://orcid.org/signin>`__ for free.

..  figure:: /assets/images/ui/copo-homepage1.png
    :alt: COPO homepage
    :align: center
    :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/ui/copo-homepage1.png
    :class: with-shadow with-border

    **Click** ``Submit Data`` **button to proceed to the login page (as shown
    below)**

Alternatively, click ``Try Demo`` button to access the demo mode.

.. raw:: html

   <br>

..  figure:: /assets/images/ui/copo-homepage2.png
    :alt: COPO homepage
    :align: center
    :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/ui/copo-homepage2.png
    :class: with-shadow with-border

    **Click** ``Sign in with Orcid.org`` **button to proceed to the ORCID
    sign-in form (as shown below)**

.. raw:: html

   <br>

.. figure:: /assets/images/ui/orcid-sign-in-form-web-page.png
   :alt: ORCID sign-in form
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/ui/orcid-sign-in-form-web-page.png
   :class: with-shadow with-border

   **Enter your Orcid login credentials or click** ``Register now`` **to sign-
   up for an ORCID account**

If the login is successful, a redirection is made to the **Work profiles**
page. Refer to the :ref:`profile-types` section for the next steps.

.. raw:: html

   <hr>

.. _first-time-user-login:

First time login
-----------------

If signing in for the first time, a prompt requesting an email address is
displayed.

A valid email address and agreement will lead to the **Work profiles** page
where profiles can be created to manage data. The email address you provide
will be linked to your COPO account and used for tasks like submitting data to
external repositories.

Refer to the :ref:`profile-types` section for the next steps.

.. figure:: /assets/images/profiles/modals/profile-new-user-add-email-address-dialogue.png
   :alt: Add email address dialogue
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/modals/profile-new-user-add-email-address-dialogue.png
   :align: center
   :class: with-shadow with-border

   **Email address prompt shown after logging in for the first time**

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] :abbr:`SOPs (Standard Operating Procedures)` guide the metadata sets and vocabularies for manifests.
         See: :ref:`SOP guidelines <fill-blank-manifests>`.
.. [#f2] See: :ref:`COPO FAIR data principles <fair-data-principles>`.

..
    Link declaration
..

.. _copo-github-repository: https://github.com/EarlhamInst/COPO-production
.. _news-page: https://copo-project.org/news
