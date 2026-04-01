.. _publishing-data:

===============
Publishing Data
===============

.. note::

   The terms *making a profile public* and *publishing data* refer to two ways
   of making data publicly accessible -  either at the profile level, where
   all data under the profile becomes accessible or at the data level, where
   individual datasets are made public in repositories such as the
   European Nucleotide Archive (ENA) [#f1]_.

   Refer to :ref:`overview-public-repositories` for more information on
   supported public repositories.

.. tip::

   Common synonyms for *profile* [#f2]_ are project, bioproject or study.
   COPO uses the term profile while repositories like
   :abbr:`ENA (European Nucleotide Archive)` use the term project or study.

.. raw:: html

   <hr>

.. _publishing-data-from-profile-level:

Publishing Data at Profile Level
---------------------------------

This section applies if the submitted data you would like to make public is
under a supported Tree of Life (ToL) [#f3]_ profile.

Refer to :ref:`How do I know what type of profile I am using?
<faq-profiles-identify-profile-type>` for guidelines on identifying your
profile type.

.. note::

   * :abbr:`ToL (Tree of Life )` profiles can be made public **only** after
     reads have been submitted and if the profile type supports being published. By
     default, profiles remain private with a publish date set to two years
     after submission however, they can be made public at any time before then.

   * Samples uploaded under a :abbr:`ToL (Tree of Life )` profiles are
     automatically made public after they are accepted by a sample manager.

.. list-table:: Types of Tree of Life profiles and data that can be made public
   :width: 100%
   :align: center
   :header-rows: 1

   * - Profile type
     - Type of data that can be made public
   * - Aquatic Symbiosis Genomics (ASG) [#f4]_
     - Reads, assemblies, sequence annotations, barcoding
   * - Darwin Tree of Life Samples (DToL) [#f5]_
     - Reads, assemblies, sequence annotations, barcoding
   * - European Reference Genome Atlas (ERGA) [#f6]_
     - Reads, assemblies, sequence annotations, barcoding

Follow the steps below to make the data public at the profile level:

#. Click the |vertical-ellipsis-icon| icon associated with the
   :abbr:`ToL (Tree of Life )` profile. The option to publish the profile will
   be displayed once clicked.

   Then, click the |publish-profile-button| button. The profile, i.e. the
   project, will automatically be made public and can be viewed in
   :abbr:`ENA (European Nucleotide Archive)`.

   .. note::

      The data will become publicly accessible after a couple of days of
      processing. If it is still not public after a week, please
      contact the :email:`COPO team <ei.copo@earlham.ac.uk>` to investigate.

   .. figure:: /assets/images/profiles/ui/profile-options-publish-study.png
      :alt: Profile options indicating "Publish study" buton
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/ui/profile-options-publish-study.png
      :class: with-shadow with-border
      :height: 100px

      **Make data public by clicking the “Publish study” button**

   .. raw:: html

      <br>

#. Click the |view-more-details-profile-button| button to view the profile’s
   published status and date.

   See the :ref:`How do I view details of a profile I created?
   <faq-profiles-view-more-information>`
   :abbr:`FAQ (Frequently Asked Question)` for more details.

   .. raw:: html

      <br>

#. To view the published project on :abbr:`ENA (European Nucleotide Archive)`,
   refer to the :ref:`accessions` section for guidelines on finding
   the accession associated with your project or data then, search for it on
   the `ENA browser <https://www.ebi.ac.uk/ena/browser/home>`__.

.. raw:: html

   <hr>

.. _publishing-data-from-data-level:

Publishing Data at Data Level
-----------------------------

This section applies if the submitted data that you would like to make public
is under a Biodata profile [#f7]_.

Refer to :ref:`How do I know what type of profile I am using?
<faq-profiles-identify-profile-type>` for details on identifying your profile
type.

.. list-table:: Types of other profiles and data that can be made public
   :width: 100%
   :align: center
   :header-rows: 1

   * - Profile type
     - Type of data that can be made public
   * - Biodata
     - Reads, Single-cell, images

       Refer to :ref:`biodata-profile-components` for an overview of the
       different types of data that can be submitted

Follow the steps below to make the data public at the data level:

#. Navigate to the page corresponding to the relevant data type listed in the
   table above.

#. After uploading data, select a record in the data table under the **STUDY**
   tab.

   .. hint::

      The first row of the data table under the **STUDY** tab is selected by
      default. Selected rows are indicated by a blue background colour.

#. Click the publish button related to the repository you would like to make
   the data public in.

   The following repositories are supported:

      * European Nucleotide Archive (ENA) via |publish-record-button-ena|
        button
      * Zenodo via |publish-record-button-zenodo| button

   The data related to the selected record will automatically be made public
   and can be viewed in the associated repository.

   .. note::

      The data will become publicly accessible after a couple of days of
      processing. If it is still not public after a week, please
      contact the :email:`COPO team <ei.copo@earlham.ac.uk>` to investigate.

   .. figure:: /assets/images/single-cell/ui/single-cell-pointer-to-publish-button.png
      :alt: Publish button on Single-cell page
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/single-cell/ui/single-cell-pointer-to-publish-button.png
      :class: with-shadow with-border

      **Make data public by clicking the “Publish” button on the Single-cell page**

   .. raw:: html

      <br>

.. raw:: html

   <hr>

Related Topics
--------------

.. seealso::

   * :ref:`View Published Study on ENA <faq-profiles-view-published-studies>`
   * :ref:`View Published Study Status <faq-profiles-view-more-information>`
   * :ref:`accessions`
   * :ref:`publishing-data`
   * :ref:`overview-public-repositories`
   * :ref:`reads`
   * :ref:`project-affiliations`

.. raw:: html

   <br>

.. rubric:: Footnotes

.. [#f1] See term: :term:`ENA`.
.. [#f2] Also known as COPO profile. See:
   :term:`COPO profile or work profile<COPO profile>`.
.. [#f3] See term: :term:`Tree of Life (ToL) <ToL>`
.. [#f4] See term: :term:`ASG`.
.. [#f5] See term: :term:`DToL`.
.. [#f6] See term: :term:`ERGA`.
.. [#f7] See term: :term:`Biodata profile`.

..
    Images declaration
..

.. |view-more-details-profile-button| image:: /assets/images/profiles/buttons/profile-view-more-button.png
   :height: 4ex
   :class: no-scaled-link

.. |publish-profile-button| image:: /assets/images/profiles/buttons/publish-study-button.png
   :height: 4ex
   :class: no-scaled-link

.. |publish-record-button-ena| image:: /assets/images/buttons/publish-record-button-ena.png
   :height: 3.5ex
   :class: no-scaled-link

.. |publish-record-button-zenodo| image:: /assets/images/buttons/publish-record-button-zenodo.png
   :height: 3.5ex
   :class: no-scaled-link

.. |vertical-ellipsis-icon| image:: /assets/images/profiles/icons/profile-vertical-ellipsis-icon.png
   :height: 4ex
   :class: no-scaled-link
