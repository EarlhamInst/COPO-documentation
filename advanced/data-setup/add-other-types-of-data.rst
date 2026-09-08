.. _defining-other-data-types:

=======================
Adding Other Data Types
=======================

Overview
--------

Metadata [#f1]_ for a new data types can be added to COPO by following the data
structure described in the
:download:`PowerPoint presentation </assets/files/presentations/ei-seminar-01072025-new-copo-tools-for-brokering-single-cell-and-spatial-omics-metadata.pptx>`.
The presentation provides a visual representation of the data structure and
the relationships between the different components of data.

The metadata is then presented in a manifest [#f2]_ which is also known as a
spreadsheet or checklist [#f3]_.

.. tab-set::

  .. tab-item:: Mandatory spreadsheet worksheets

     .. list-table:: Names of worksheets that should be included in the spreadsheet for the new data type
        :width: 100%
        :align: center
        :header-rows: 1

        * - Worksheets
          - Description
        * - data
          - This worksheet contains the fields for the new data type. It is
            the main worksheet that defines the structure of the data.

            See the `Mandatory columns in data worksheet` tab for the
            main columns that should be included in the ``data`` worksheet.
        * - allowed_values
          - This contains the possible values for a field and is used to
            validate the values entered for the field in the ``data``
            worksheet.
        * - checklists
          - This worksheet contains the key (i.e. the identifier), name and
            description of the checklist for the new data type.
        * - components
          - This worksheet lists the name and label of each component
            used in the ``data`` worksheet. The component name is indicated
            by the  ``component_name`` column in the ``data`` worksheet.
            Components are also regarded as worksheets which group related
            fields together.

            The submission repository is also configured in this worksheet.
            It identifies the repository where the data will be submitted to
            and is represented as ``repository_xx`` column where ``xx``
            is the name of the repository (e.g. ``repository_ena``,
            ``repository_zenodo``).

  .. tab-item:: Mandatory columns in `data` worksheet

    .. list-table:: Description of column names present in the `data` worksheet
       :width: 100%
       :align: center
       :header-rows: 1

       * - Data fields
         - Description
       * - component_name
         - The name of the worksheet that the field
           belongs to. It is used to group related fields together.
       * - namespace_prefix
         - This reflects an established standard that the field belongs to
           and matches any of the values in the ``key`` column in
           the ``standards`` worksheet.

           If the field does not belong to any established standard,
           it should have the value ``ei`` in this column.
       * - term_name
         - The name of the field.
       * - term_label
         - The label of the field.
       * - identifier
         - This uniquely identifies fields within a component.
       * - referenced_component
         - This refers to the name of the worksheet that the field is
           associated with. It defines relationships between fields within
           the same component or across different components.
       * - term_description
         - This provides additional information about the field.
       * - term_example
         - This provides an example and guidance on the expected format of
           the field.
       * - term_regex
         - A regular expression that is used to validate the data
           entered for the field.
       * - term_error_message
         - This is used to provide feedback to the user when the data entered
           for the field does not match an expected outcome.
       * - term_cardinality
         - This defines the number of values that can be entered for the
           field. It expects a single value (``single``) or multiple values
           (``multiple``).
       * - term_type
         - This describes the type of data that the field expects.
           It can be a **string**, **enum** (which stands for enumeration) or
           **file**.

           If it is an enumeration, the possible values for the field should
           be defined in the ``allowed_values`` worksheet.

           If it is a file, the system will expect a file to be uploaded.
       * - term_reference
         - A URL link referencing a field. It is used to provide additional
           information about the origin of the field.

.. _defining-other-data-types-examples:

Examples of Adding Other Types of Data in COPO
----------------------------------------------

.. tip::

   Each link below takes you to the corresponding GitHub directory containing
   the spreadsheet files for that data type. Select a link to view the files
   and see how the data is structured.

   The spreadsheet file containing the main schema can be identified by the
   substring ``_schema_main_``.

* `Earlham Data Portal (EDP) data <edp-schema-directory_>`__ |external-link-icon|
* `Reads data <copo-reads-schema-directory_>`__ |external-link-icon|
* `Image data <copo-image-schema-directory_>`__ |external-link-icon|
* `Single-cell data <copo-single-cell-schema-directory_>`__ |external-link-icon|


.. raw:: html

   <hr>

.. _defining-other-data-types-extending-checklist:

Extending existing checklist data
-------------------------------------

Choose one of the data configuration of the existing checklist [#f3]_ options
in the :ref:`defining-other-data-types-examples` section above that
corresponds well to your new checklist data type and download the spreadsheet
file for it before proceeding with either of the subsequent sections:

- :ref:`defining-other-data-types-extending-checklist-new-option`

**OR**

- :ref:`defining-other-data-types-extending-checklist-additional-fields`

.. _defining-other-data-types-extending-checklist-new-option:

With a new checklist type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open the spreadsheet and navigate to the ``standards`` worksheet.

   Fill in the details of the new standard [#f4]_ of your new data type under
   the columns - **key** and **name**.

   For example, if you are using the
   `Single-cell main schema spreadsheet <copo-single-cell-schema-directory_>`__
   to add a new data type, add a row with the following values:

   * **key**: ndt

   * **name**: New Data Type (NDT)

   .. note::

      The **key** column represents the abbreviation of your new data type
      while the **name** column represents the full name of it.

      You can choose any abbreviation and name that is relevant to your new
      data type.

   .. figure:: /assets/images/setup/ui/add-new-data-type/add-new-data-type-standards-worksheet.png
      :alt: Adding a key and name of a standard in the 'standards' worksheet
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/add-new-data-type/add-new-data-type-standards-worksheet.png
      :class: with-shadow with-border
      :height: 300px

      **Adding a standard in** ``standards`` **worksheet**

 .. raw:: html

    <br>

2. Navigate to the ``technologies`` worksheet.

   If your new data type will be associated with a technology that is
   different to what is displayed in the worksheet, fill in the **key** and
   **name** of the new technology in a new row under the respective columns.
   Otherwise, skip this step.

   .. note::

      If providing a new technology, the **key** column represents the
      abbreviation of it while the **name** column represents the full name
      of it.

   .. figure:: /assets/images/setup/ui/add-new-data-type/add-new-data-type-technologies-worksheet.png
      :alt: Adding a key and name of a standard in the 'standards' worksheet
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/add-new-data-type/add-new-data-type-technologies-worksheet.png
      :class: with-shadow with-border
      :height: 300px

      **Single-cell shown as the only available technology option in the** ``technologies`` **worksheet**

 .. raw:: html

    <br>

3. Navigate to the ``checklists`` worksheet

   In a new row, fill in the details of your new checklist option under the
   columns - **key**, **name**, **description**, **standard** and
   **technology**.

   The **standard** and **technology** columns should match the values that
   you have added in the ``standards`` and ``technologies`` worksheets
   respectively.

   For example, in the screenshot below, "My new data type metadata" is a
   Single-cell option that has been added where:

   * **key**: version_ndt_sc_rnaseq

     .. note::

        The key must begin with the prefix ``version_`` and end with the
        suffix ``_sc_rnaseq`` to indicate that it relates to Single-cell RNA
        sequencing data.

        The middle part of the key (``ndt``) should represent an abbreviation
        of the new data type and match the key (i.e. namespace) that was
        added in the ``standards`` worksheet.

        Similarly, the suffix of the key should match a key in
        in the ``technologies`` worksheet relevant to your new data type.
        In this example, it is ``_sc_rnaseq`` which represents Single-cell
        RNA Sequencing.

   * **name**: My new data type metadata

   * **description**: This is a new data type.

   .. raw:: html

      <br>

   .. figure:: /assets/images/setup/ui/add-new-data-type/add-new-data-type-checklists-worksheet.png
      :alt: Adding a key and name of a standard in the 'standards' worksheet
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/add-new-data-type/add-new-data-type-checklists-worksheet.png
      :class: with-shadow with-border
      :height: 400px

      **Adding details of the new data type in the** ``checklists`` **worksheet**

4. In the ``data`` worksheet,

   - Insert a column to the far right of the existing columns in the worksheet
     with the name ``version_ndt_sc_rnaseq``. This column name should match
     the key that you added in the ``checklists`` worksheet.

     .. tip::

        Alternatively, you can copy and paste an existing column
        (e.g. ``version_mixs_sc_rnaseq``) and rename it to
        ``version_ndt_sc_rnaseq`` if it best suits your new data type.
        This will ensure that the new column has the same mandatory and
        optional fields as the existing column's. You can then
        modify the values in the new column to suit your new data type.

     Notice that the adjacent column names also have the prefix ``version_``
     and suffix ``_sc_rnaseq`` which indicates that they are also related
     to Single-cell RNA Sequencing data but with different data types (e.g.
     :abbr:`DwC (Darwin Core metadata)`,
     :abbr:`MIxS (Minimum Information about any, (x) Sequence)`,
     :abbr:`FAANG (Functional Annotation of Animal Genomes)`,
     :abbr:`ToL (Tree of Life)`).

     .. figure:: /assets/images/setup/ui/add-new-data-type/add-new-data-type-data-worksheet-new-data-type-column.png
        :alt: Adding a data type column in the 'data' worksheet
        :align: center
        :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/add-new-data-type/add-new-data-type-data-worksheet-new-data-type-column.png
        :class: with-shadow with-border
        :height: 400px

        **Adding a data type column in the** ``data`` **worksheet**

   - **Existing terms**:

     Of the existing terms [#f5]_ in the ``term_name`` column in the
     worksheet, insert ``M`` (which means mandatory) or ``O``
     (which means optional) relevant to your new data type in the new column
     ``version_ndt_sc_rnaseq``.

     If a term is not relevant to your new data type, leave the cell blank.

     All terms have a description in the ``term_description`` column.
     You can use this description to determine whether a term is relevant
     to your new data type.

     - All terms that have ``ei`` in the ``namespace_prefix`` column are
       regarded as custom fields that should be marked as mandatory (``M`` )
       or optional (``O``) depending on the checklist type in the new
       ```version_xx`` column.

     - Terms that have other namespace prefixes in the ``namespace_prefix``
       column  like ``dwc``, ``dcterms``, ``mixs``, ``faang``, ``tol``,
       and ``schema.org`` can be optional or mandatory for your new data
       type and as such should be marked as ``O`` or ``M`` accordingly or
       left blank if irrelevant.

       .. raw:: html

          <br>

     .. figure:: /assets/images/setup/ui/add-new-data-type/add-new-data-type-data-worksheet-new-data-with-existing-fields.png
        :alt: Adding existing fields to new data type column in the 'data' worksheet
        :align: center
        :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/add-new-data-type/add-new-data-type-data-worksheet-new-data-with-existing-fields.png
        :class: with-shadow with-border
        :height: 400px

        **Adding existing fields to the new data type column in the** ``data`` **worksheet**

     .. raw:: html

        <br>

   - **New terms**:

     If your new data type requires fields that are not present in the
     ``term_name`` column of the ``data`` worksheet, identify the component
     in the ``component_name`` column to which the new field belongs. Then,
     insert a new row immediately after the last existing term for that
     component.

     Thereafter, fill in the details for each new field you add in the
     corresponding columns.

     .. raw:: html

        <br>

     .. figure:: /assets/images/setup/ui/add-new-data-type/add-new-data-type-data-worksheet-new-data-with-new-fields.png
        :alt: Adding new fields to new data type column in the 'data' worksheet
        :align: center
        :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/add-new-data-type/add-new-data-type-data-worksheet-new-data-with-new-fields.png
        :class: with-shadow with-border
        :height: 400px

        **Adding new fields for the new data type column in the** ``data`` **worksheet**

     .. raw:: html

        <br>

     The screenshot above shows two ways of adding new fields to the new data
     type ``version_ndt_sc_rnaseq``. It is outlined in red boxes and described
     below:

     1. **Adding new metadata under a new component**: The new metadata is
        added under a new component called ``new_example_component``. The new
        fields are added in new rows immediately after the last existing term
        of a component.

        In this case, the last existing term for the
        ``analysis_derived_data`` component is
        ``other_derived_cell_attributes``. The new component,
        ``new_example_component``, is added in a new row immediately after it.

       This new component has four new fields - **field_1**, **field_2**,
       **field_3** and **field_4** with their respective details filled in the
       corresponding columns and the **study_id** field as the identifier
       field.

     2. **Adding new metadata under an existing component**: New metadata
        is added in new rows immediately after the last existing term
        for the under the existing component, ``sequencing``.

        In this example, **field_0** and **field_1** are the new fields that
        are added under the ``sequencing`` component.

5. Save the spreadsheet file, commit it and push it to the `COPO-schemas
   GitHub repository <copo-schemas-directory_>`__.

6. Proceed to the :ref:`defining-other-data-types-persist-data` section for
   the next steps.

.. raw:: html

   <br>

.. _defining-other-data-types-extending-checklist-additional-fields:

With additional fields for an existing checklist type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open the spreadsheet and navigate to the ``data`` worksheet.

2. Choose any of the existing checklist types in the worksheet that is
   relevant to your new data type. They are identified with the prefix
   ``version_`` in the column names.

   We'll choose ``version_mixs_sc_rnaseq`` and ``version_faang_sc_rnaseq``
   in this example proceed with the next steps.

   .. figure:: /assets/images/setup/ui/add-new-data-fields/add-more-data-to-data-worksheet-identify-existing-checklist-types.png
      :alt: Identifying existing checklist types in 'data' worksheet
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/add-new-data-fields/add-more-data-to-data-worksheet-identify-existing-checklist-types.png
      :class: with-shadow with-border
      :height: 400px

      **Red rectangle highlighting the existing checklist types in the** ``data`` **worksheet**

   .. raw:: html

      <br>

3. Choose a component in the ``component_name`` column to which the new fields
   will belong to. Then, insert new rows immediately after the last existing
   term for that component.

   In this example, we will add new fields under the existing components -

   *  ``lib_prep`` - The last existing term for this component
      is ``library_strategy``. We will insert a new row
      immediately after it.

   *  ``sequencing`` - The last existing term for this component
      is ``num_replicons``. We will insert a new row
      immediately after it.

   .. raw:: html

      <br>

   .. figure:: /assets/images/setup/ui/add-new-data-fields/add-more-data-to-data-worksheet-identify-row-to-insert-new-data.png
      :alt: Identifying where in the in 'data' worksheet to insert new rows for the new fields
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/add-new-data-fields/add-more-data-to-data-worksheet-identify-row-to-insert-new-data.png
      :class: with-shadow with-border
      :height: 400px

      **Red arrow highlighting where new field data will be inserted in the** ``data`` **worksheet**

   .. raw:: html

      <br>

   In the screenshot below, notice that the inserted row in the ``lib_prep``
   component has ``M`` in the ``version_faang_sc_rnaseq`` column and nothing
   in the other *version_xx* columns. This indicates that the inserted field
   (also known as term) is mandatory for the Functional Annotation of
   Animal Genomes metadata (FAANG) checklist type and not relevant to the
   other checklist types.

   .. note::

      Fields that belong to an established standard in the ``data`` worksheet
      must have any of the standards listed in the ``key`` column of the
      ``standards`` worksheet as a value in the ``namespace_prefix`` column
      of the ``data`` worksheet.

      Custom fields must have ``ei`` as the namespace prefix in the
      ``namespace_prefix`` column of the ``data`` worksheet. These fields
      can be marked as ``M`` or ``O`` in the *version_xx* columns, depending
      on whether they are mandatory or optional for your new data type.

   .. figure:: /assets/images/setup/ui/add-new-data-fields/add-more-data-to-data-worksheet-inserted-data1.png
      :alt: Data inserted under the 'lib_prep' component in the 'data' worksheet
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/add-new-data-fields/add-more-data-to-data-worksheet-inserted-data1.png
      :class: with-shadow with-border
      :height: 400px

      **Red arrow highlighting inserted data in** ``lib_prep`` **component in the** ``data`` **worksheet**

   .. raw:: html

      <br>

   Similarly, the inserted row in the ``sequencing`` component has ``O`` in
   the ``version_mixs_sc_rnaseq`` column and nothing in the other
   *version_xx* columns. This indicates that the inserted field is optional
   for the Minimum Information about any (x) Sequence (MIxS) checklist
   type and not relevant to the other checklist types.

   .. figure:: /assets/images/setup/ui/add-new-data-fields/add-more-data-to-data-worksheet-inserted-data2.png
      :alt: Data inserted under the 'sequencing component' in the 'data' worksheet
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/setup/ui/add-new-data-fields/add-more-data-to-data-worksheet-inserted-data2.png
      :class: with-shadow with-border
      :height: 400px

      **Red arrow highlighting inserted data in** ``sequencing`` **component in the** ``data`` **worksheet**

   .. raw:: html

      <br>

4. Save the spreadsheet file, commit it and push it to the `COPO-schemas
   GitHub repository <copo-schemas-directory_>`__.

5. Proceed to the :ref:`defining-other-data-types-persist-data` section for
   the next steps.

.. raw:: html

   <hr>

.. _defining-other-data-types-persist-data:

Persist added data to COPO
--------------------------

Now that the data structure has been amended and new data type has been
added to the spreadsheet file in the
`COPO-schemas GitHub repository <copo-schemas-directory_>`__,
the following steps guide how to persist added data type(s) to the COPO
website so that they are available as a dropdown menu option and the new data
is available within the downloaded spreadsheet file for the respective
checklist type.

.. code-block:: console
   :caption: Navigate to the COPO frontend virtual machine (VM) and SSH into it

   ssh <name-of-vm>

For a local setup, skip this command and proceed to the next one.


.. code-block:: console
   :caption: List all running Docker containers using the terminal

   docker ps

You may need to run the command with ``sudo`` if you are not logged in as a
user with the required permissions to run Docker commands.

.. code-block:: console
   :caption: Enter the COPO web container

   docker exec -it <copo-web-container-id> bash

Replace ``<copo-web-container-id>`` with the actual container ID of the
COPO web container found from running the ``docker ps`` command.

On the production, demonstration and development virtual machines (VMs),
the COPO web container can be identified by ``copo/copo-new-web:vxx``
where ``xx`` is the version of the Docker container image.

On the other hand, locally, the COPO web container can be identified by
``local_copo_web:vxx`` where ``xx`` is the version of the Docker container
image.

.. code-block:: console
   :caption: Execute the Celery command to insert and update the new data in COPO

   celery -A src call src.apps.copo_single_cell_submission.tasks.update_singlecell_schema

This command calls the **update_singlecell_schema** Celery job defined in the
`src/celery.py <copo-celery-file_>`__ file, which in turn calls the
**update_singlecell_schema** Celery task defined in the
`src/apps/copo_single_cell_submission/tasks.py
<copo-single-cell-schemas-tasks-file_>`__ file.

The **updateSchemas** function in the
`src/apps/copo_single_cell_submission/utils/SingleCellSchemasHandler.py
<copo-single-cell-schemas-handler-file_>`__ file is then called and is
responsible for parsing the spreadsheet file from the GitHub repository,
updating the system's database and by extension the website with the new data.

To verify that the new data type has been added, navigate to the
:ref:`Single-cell submission page <single-cell-submissions>` under a
:ref:`Biodata profile <profile-walkthrough-biodata>` on the COPO platform and
check if the new data type is available in the dropdown menu or the new data is
available within a downloaded spreadsheet file from the page.

.. raw:: html

   <hr>

Related sections
----------------

.. seealso::

   * :ref:`defining-sample-types`

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Metadata`
.. [#f2] See term: :term:`Manifest`
.. [#f3] See term: :term:`Checklist`
.. [#f4] See term: :term:`Standard`
.. [#f5] See term: :term:`Term`

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/arrow-right.png
   :height: 2ex
   :class: no-scaled-link

.. |external-link-icon| image:: /assets/images/icons/external-link-icon.png
   :height: 2ex
   :width: 2ex
   :class: no-scaled-link

..
    Link declaration
..

.. _edp-schema-directory: https://github.com/EarlhamInst/COPO-schemas/tree/main/edp
.. _copo-celery-file: https://raw.githubusercontent.com/EarlhamInst/COPO-production/refs/heads/main/src/celery.py
.. _copo-reads-schema-directory: https://github.com/EarlhamInst/COPO-schemas/tree/main/reads
.. _copo-image-schema-directory: https://github.com/EarlhamInst/COPO-schemas/tree/main/images
.. _copo-schemas-directory: https://github.com/EarlhamInst/COPO-schemas
.. _copo-single-cell-schema-directory: https://github.com/EarlhamInst/COPO-schemas/tree/main/single_cell
.. _copo-single-cell-schemas-handler-file: https://raw.githubusercontent.com/EarlhamInst/COPO-production/refs/heads/main/src/apps/copo_single_cell_submission/utils/SingleCellSchemasHandler.py
.. _copo-single-cell-schemas-tasks-file: https://raw.githubusercontent.com/EarlhamInst/COPO-production/refs/heads/main/src/apps/copo_single_cell_submission/tasks.py
