.. _profile-walkthrough-tol:

Tree of Life Profile
--------------------

Tree of Life (ToL) profile [#f1]_ is a work profile that is used to submit
research objects [#f2]_ such as barcoding data, sequence annotations and
other data.

See the :ref:`components <tol-profile-components>` section below for the types
of data that can be submitted using this profile.

Currently, the following projects are supported. Refer to the :ref:`affiliated
projects <project-affiliations>` section for additional information.

* Aquatic Symbiosis Genomics (ASG)
* Darwin Tree of Life (DToL)
* Darwin Tree of Life Environmental (DToL_ENV)
* European Reference Genome Atlas (ERGA)

.. hint::

   Work profiles created in COPO are regarded as *project* research objects.
   Projects are created in European Nucleotide Archive (ENA) [#f3]_ after
   :ref:`reads have been submitted <reads>`. Thus, any modifications that
   you would like to be made to a project in
   :abbr:`ENA (European Nucleotide Archive)` must be done to the respective
   profile in COPO.

.. raw:: html

   <hr>

.. _tol-profile-steps:

Steps to Create a Tree of Life Profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Choose Profile Type
^^^^^^^^^^^^^^^^^^^^^^

On the **Work profiles** page, choose a profile type from the dropdown menu,
as shown below. By default, only the Biodata profile option is displayed.

Then, click the |add-profile-button| **Add new profile record** button to view
the **Add Profile** form for the profile
type.

.. important::

   If the profile type or project you need is not shown in the dropdown menu,
   please :email:`contact the COPO team <ei.copo@earlham.ac.uk>`  and
   specify the profile group you would like access to. Once access is granted,
   the profile type will appear in the dropdown menu alongside the default
   Biodata profile type.

   When creating a new profile, please ensure that you select the correct
   profile type from the dropdown menu.

.. figure:: /assets/images/profiles/ui/profile-add-profile-with-profile-types-dropdown-menu-displayed-tol.png
   :alt: Profile types dropdown menu when adding a new profile
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/ui/profile-add-profile-with-profile-types-dropdown-menu-displayed-tol.png
   :class: with-shadow with-border
   :height: 300px

   **Dropdown menu showing all projects you have access to, including the
   default "Biodata" profile**

.. figure:: /assets/images/profiles/ui/profile-add-record-button-web-page-tol.png
   :alt: Add new profile button
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/ui/profile-add-record-button-web-page-tol.png
   :class: with-shadow with-border

   **Click this button to add a new profile**

.. _profile-details-tol:

2. Provide Profile Details
^^^^^^^^^^^^^^^^^^^^^^^^^^

Provide the following details for the new profile:

* :ref:`Title and description <profile-details-add-title-description>`
* :ref:`Associated profile type (if applicable)
  <profile-details-add-associated-profile-type>`
* :ref:`Sequencing centre (if applicable)
  <profile-details-add-sequencing-centre>`
* :ref:`Locus tag (if applicable) <profile-details-add-locus-tag>`

.. _profile-details-add-title-description:

Title and Description
"""""""""""""""""""""

Both title and description are mandatory information.

Meaningful field values are recommended in the form boxes because the
information will appear in submissions of the research objects associated with
the profile, in public remote repositories.

.. figure:: /assets/images/profiles/ui/profile-add-profile-form-title-description.png
   :alt: Provide profile title and description on add profile form
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/ui/profile-add-profile-form-title-description.png
   :class: with-shadow with-border
   :height: 300px

   **Provide title and description for the new profile**

   .. raw:: html

      <br>

.. _profile-details-add-associated-profile-type:

Select Associated Profile Type (if applicable)
""""""""""""""""""""""""""""""""""""""""""""""

   .. note::

      The **Associated Profile Type** dropdown menu is displayed only when the
      **European Reference Genome Atlas (ERGA)** profile type is selected.
      Selecting an associated profile type is mandatory when creating an
      :abbr:`ERGA (European Reference Genome Atlas)` profile.

      See :ref:`associated-projects` for available subprojects.

   An associated profile type [#f4]_ is also known as a subproject or child
   project. More than one can be selected.

   .. figure:: /assets/images/profiles/ui/profile-add-profile-form-associated-type.png
      :alt: Choose associated profile type or subproject on add profile
            form for ERGA profile type
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/ui/profile-add-profile-form-associated-type.png
      :class: with-shadow with-border
      :height: 380px

      **Choose associated profile type**

      .. raw:: html

         <br>

.. _profile-details-add-sequencing-centre:

Select Sequencing Centre (if applicable)
""""""""""""""""""""""""""""""""""""""""

   .. note::

      The **Sequencing Centre** dropdown menu is displayed only when the
      **European Reference Genome Atlas (ERGA)** profile type is selected.
      Selecting a sequencing centre is mandatory when creating an
      :abbr:`ERGA (European Reference Genome Atlas)` profile.

      If **SANGER INSTITUTE** is selected as the sequencing centre, the
      **Associated Profile Type** field will automatically be set to
      **Sanger Institute Approval Needed (SANGER)**.

      See the :ref:`Sequencing Centres that utilise COPO
      <faq-profiles-sequencing-centres-list>`
      :abbr:`FAQ (Frequently Asked Question)` for additional information.

   .. figure:: /assets/images/profiles/ui/profile-add-profile-form-sequencing-centre.png
      :alt: Choose sequencing centre on 'Add Profile' form
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/ui/profile-add-profile-form-sequencing-centre.png
      :class: with-shadow with-border
      :height: 380px

      **Choose sequencing centre**

   .. raw:: html

      <br>

.. _profile-details-add-locus-tag:

Input Locus Tag (if applicable)
"""""""""""""""""""""""""""""""

   If applicable, enter a  locus tag [#f5]_ in the form box. Refer to the
   :ref:`How can I assign a locus tag to assemblies
   <faq-assemblies-submission-locus-tag-assignment>`
   :abbr:`FAQ (Frequently Asked Question)` for guidelines.

   .. figure:: /assets/images/profiles/ui/profile-add-profile-form-locus-tag.png
      :alt: Choose locus tag on add profile form
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/ui/profile-add-profile-form-locus-tag.png
      :class: with-shadow with-border
      :height: 250px

      **Enter the locus tag in the input field shown**

3. Save Profile Form
^^^^^^^^^^^^^^^^^^^^^

   Click the **Save** button to save the details entered in the
   **Add Profile** form. The new profile will be displayed on the
   **Work profiles** page.

   .. figure:: /assets/images/profiles/ui/profile-tol-profile-created.png
      :alt: Tree of Life profile created
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/ui/profile-tol-profile-created.png
      :class: with-shadow with-border

      **Work profiles page displaying the created profile**

   .. raw:: html

      <br>

   .. hint::

      Use the **Sort by** dropdown (top-right) to sort profiles by date
      created, title or type. See
      :ref:`Sorting Profiles <sorting-profiles>` section for more information.

.. raw:: html

   <hr>

.. _tol-profile-components:

Tree of Life Profile Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The different types of data created within a profile are called
*profile components* and can be accessed from the **Components** column.
Clicking any button in this column will take you to the page for that
component (see the *Tree of Life profile components* image below).

The following component types are available:

.. grid::
   :gutter: 2

   .. grid-item::
      :columns: 8

      * :ref:`Data files <files>`
      * :ref:`Samples <samples-submission>`
      * :ref:`Reads <reads>`
      * :ref:`Assembly <assemblies>`
      * :ref:`Sequence annotations <sequence-annotations>`
      * :ref:`Barcoding data <barcoding-submissions>`
      * :ref:`Accessions <accessions>`

   .. grid-item::
      :columns: 4

      .. figure:: /assets/images/profiles/buttons/profile-component-buttons-tol.png
         :alt: Tree of Life profile components
         :align: center
         :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/buttons/profile-component-buttons-tol.png
         :class: with-shadow with-border
         :height: 400px

         **Tree of Life profile components**

.. raw:: html

   <hr>

Related Topics
~~~~~~~~~~~~~~

.. seealso::

   * :ref:`profile-update`
   * :ref:`profile-deletion`
   * :ref:`publishing-data`
   * :ref:`sharing-profiles`
   * :ref:`sorting-profiles`
   * :ref:`profile-types-legend`

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Tree of Life profile <ToL profile>`.
.. [#f2] See term: :term:`Research object`.
.. [#f3] See term: :term:`European Nucleotide Archive (ENA) <ENA>`.
.. [#f4] The associated project type identifies the subproject a record
   belongs to. For example, a sample may be part of the
   :abbr:`ERGA (European Reference Genome Atlas)` project while being
   associated with the :abbr:`BGE (Biodiversity Genomics Europe)`
   subproject.

   In sample records, this information is stored as *associated_tol_project*
   while in profile records, it is stored as *associated_type*.
.. [#f5] See term: :term:`Locus tag`.

..
    Images declaration
..
.. |add-profile-button| image:: /assets/images/buttons/add-button.png
   :height: 4ex
   :class: no-scaled-link
