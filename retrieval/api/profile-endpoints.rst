.. _endpoints-profile:

Profile Endpoints
~~~~~~~~~~~~~~~~~~~~

.. note::

   The examples below use API endpoints from the live COPO website.

   To use the demo website instead, replace ``https://copo-project.org/api/``
   with ``https://demo.copo-project.org/api/`` in the URLs.

.. tip::

   * To view details of the endpoint, click the
     |profile-collapsible-item-arrow| *Show endpoint details* button.

   * Then, inside that section, click the |profile-collapsible-item-arrow|
     *Show API query parameters* button to see input parameter details.

   * By default, the API returns results in JSON format and uses the Tree of
     Life (ToL) standard. You do not need to specify these unless you want to
     override them.

     To explicitly include them in the API URL:

        * Use ``?return_type=json`` or ``?standard=tol`` if there are no other
          query parameters.
        * Use ``&return_type=json`` or ``&standard=tol`` if the URL already
          includes other parameters.

   * A study is sometimes referred to as a project. They are used
     interchangeably.

.. raw:: html

   <hr>

Create Profile Record
"""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. note::

         Authentication is required in order to use this API method. Create an
         API key from the :ref:`/apiKey API endpoint <endpoints-api-key>`
         before using this method.

      * **type** (required): The type of profile to be created. [#f1]_

   .. raw:: html

      <br>

   **Usage**

    Please include at least the ``title``, ``description`` and ``type``
    parameter values in the API URL to create a profile record for the
    authenticated user. Replace ``<title>``, ``<description>`` and ``<type>``
    with the desired values.

    .. tab-set::

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X POST "https://copo-project.org/api/profiles" -H "accept: */*" -H "Content-Type: application/json" -d "{"title":"<title>", "description":"<"description>","type":"<type>"}"

   **Example**

     To create a profile record with the title ``Sample profile``, description
     ``A profile to record sample objects.`` and profile type ``Biodata``, use
     the following URL:

    .. tab-set::

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X POST "https://copo-project.org/api/profiles" -H "accept: */*" -H  "Content-Type: application/json" -d "{"title": "Sample profile", "description": "A profile to record sample objects.", "type": "Biodata"}"

.. raw:: html

   <br>

Fetch Profile Records
"""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   **Usage**

    .. note::

       Authentication is required in order to use this API method. Create an
       API key from the :ref:`/apiKey API endpoint <endpoints-api-key>` before
       using this method.

    This endpoint retrieves all profile records associated with the
    authenticated user.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: console

             https://copo-project.org/api/profiles

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles" -H  "accept: */*"

.. raw:: html

   <br>

Fetch Profile Record by ID
""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **profile_id** (optional): A hexadecimal identifier of a profile.

      To apply filters, append them to the API URL as follows:
      ``profiles/<profile_id>``

      Replace ``<profile_id>`` with the desired value. See the example below.

   .. raw:: html

      <br>

   **Usage**

    .. note::

       Authentication is required in order to use this API method. Create an
       API key from the :ref:`/apiKey API endpoint <endpoints-api-key>` before
       using this method.

    This endpoint retrieves a profile record matching the provided profile ID
    for the authenticated user.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: console

             https://copo-project.org/api/profiles/<profile_id>

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/<profile_id>" -H  accept: application/json"

   **Example**

    To retrieve the profile record with the profile ID
    ``68a5e2804d9676aef9074394``, use the following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: console

             https://copo-project.org/api/profiles/68a5e2804d9676aef9074394

       .. tab-item:: Command Line (curl)

          .. code-block:: console

             $ curl -X GET "https://copo-project.org/api/profiles/68a5e2804d9676aef9074394 -H  "accept: application/json"

.. raw:: html

   <br>

Update Profile Record by ID
"""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. note::

         Profile types cannot be changed once a profile has been created. An
         error will be returned if you attempt to do so. The initial profile
         type must be retained and included in the update request in order to
         update the other fields(s).

      * **profile_id** (required): A hexadecimal identifier of a profile.

      To apply filters, append them to the API URL as follows:
      ``profiles/<profile_id>``

      Replace ``<profile_id>`` with the desired value. See the example below.

   .. raw:: html

      <br>

   **Usage**

    .. note::

       Authentication is required in order to use this API method. Create an
       API key from the :ref:`/apiKey API endpoint <endpoints-api-key>` before
       using this method.

    This endpoint updates a profile record that matches the provided profile
    ID. Replace ``<title>`` and  ``<description>`` with the desired values.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: console

             https://copo-project.org/api/profiles/<profile_id>

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X PUT "https://copo-project.org/api/profiles/<profile_id>" -H  accept: application/json" -H  "Content-Type: application/json" -d "{"title": "<title>", "description": "<description>", "type": "<type>"}"

   **Example**

    To update the ``description`` of the profile matching the ID
    ``68a5e2804d9676aef9074394``, use the URL below. Note that in that
    example, the initial ``title`` and ``type`` values are be retained in the
    update request.

    .. tab-set::

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X PUT "https://copo-project.org/api/profiles/68a5e2804d9676aef9074394" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{"title": "Sample profile", "description": "A profile to record sample and single-cell objects.", "type": "Biodata"}"

.. raw:: html

   <br>

Fetch Data File Names by Profile ID
"""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **profile_id** (required): A hexadecimal identifier of a profile.

   .. raw:: html

      <br>

   **Usage**

    .. note::

       Authentication is required in order to use this API method. Create an
       API key from the :ref:`/apiKey API endpoint <endpoints-api-key>`
       before using this method.

    This endpoint retrieves data file names for a profile by profile ID.
    Replace ``{profile_id}`` with the desired value.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: console

             https://copo-project.org/api/profiles/{profile_id}/files

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/{profile_id}/files" -H  accept: application/json" -H  "Content-Type: application/json" -d "{"title": "<title>", "description": "<description>", "type": "<type>"}"

   **Example**

    To retrieve the data files uploaded for the profile matching the ID
    ``68a5e2804d9676aef9074394``, use the following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: console

             https://copo-project.org/api/profiles/68a5e2804d9676aef9074394/files

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/68a5e2804d9676aef9074394/files" -H "accept: application/json"

.. raw:: html

   <br>

Fetch Data File Upload URL by Profile ID
""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **profile_id** (required): A hexadecimal identifier of a profile.

   .. raw:: html

      <br>

   **Usage**

    .. note::

       Authentication is required in order to use this API method. Create an
       API key from the  :ref:`/apiKey API endpoint <endpoints-api-key>`
       before using this method.

    This endpoint retrieves ``curl`` URL command  file names for a profile by
    profile ID. Replace ``{profile_id}`` with the desired value.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: console

             https://copo-project.org/api/profiles/{profile_id}/files/presignedurls

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/{profile_id}/files/presignedurls" -H accept: application/json" -H  "Content-Type: application/json" -d "{"title": "<title>", "description": "<description>", "type": "<type>"}"

   **Example**

    To retrieve the data files uploaded for the profile matching the ID
    ``68a5e2804d9676aef9074394``, use the following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: console

             https://copo-project.org/api/profiles/68a5e2804d9676aef9074394/files/presignedurls

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/68a5e2804d9676aef9074394/files" -H "accept: application/json"

.. raw:: html

   <br>

Fetch Single-cell Checklists
""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. hint::

      The words, ``manifest`` and ``checklist`` are used interchangeably. They
      both refer to a spreadsheet.

   **Usage**

    This endpoint returns a list of available single-cell checklists namely,
    their checklist ID, name, description, standard and technology.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: console

             https://copo-project.org/api/profiles/singlecells/checklists

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/singlecells/checklists" -H  accept: application/json" -H

.. raw:: html

   <br>

Fetch Studies in a profile
""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. note::

         Authentication is required in order to use this API method. Create an
         API key from the :ref:`/apiKey API endpoint <endpoints-api-key>`
         before using this method.

      * **profile_id** (required): A hexadecimal identification number of the
        profile.

      * **schema_name** (required): The name of the schema.

        Options include:

        * ``copo_single_cell``
        * ``copo_image_rembi``
        * ``copo_image_stx_fish``

      * **checklist_id** (optional): The identification number of the schema
        checklist.

        Possible options are:

        * ``version_dwc_sc_rnaseq``
        * ``version_mixs_sc_rnaseq``
        * ``version_tol_sc_rnaseq``
        * ``version_faang_sc_rnaseq``
        * ``version_rembi``
        * ``version_dwc_stx_fish``
        * ``version_mixs_stx_fish``
        * ``version_tol_stx_fish``

   .. raw:: html

      <br>

   .. hint::

      The words, ``manifest`` and ``checklist`` are used interchangeably. They
      both refer to a spreadsheet. `Schema` refers to the configuration
      of a checklist.

   **Usage**

    Please include at least the ``profile_id`` and ``schema_name``
    parameter values in the API URL to retrieve studies that are associated
    with the provided profile ID.

    Replace ``<profile_id>``,  ``<schema_name>`` and  ``<token>`` with the
    desired values.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: console

             https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies" -H  accept: -H  "accept: application/json" -H  "Authorization: token <token>"

   **Example**

     To get all single-cell studies within a profile via the profile ID,
     ``68deb1fa4036b3903e261aee`` and schema, ``copo_single_cell``,
     use the following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: console

             https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies" -H  "accept: application/json" -H  "Authorization: token 02adb0423492488ee3d4495b94cd1241ebf10551"

    .. raw:: html

       <br>

    Alternatively, to get only Darwin Core (DwC) single-cell RNA-seq studies
    within a profile, use ``68deb1fa4036b3903e261aee`` as the profile_id,
    the schema_name as ``copo_single_cell`` and ``version_dwc_sc_rnaseq`` as
    the ``checklist_id``, as shown in the URL below:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies?checklist_id=version_dwc_sc_rnaseq

       .. tab-item:: Command Line (curl)

          .. code-block:: console

             $ curl -X GET "https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies?checklist_id=version_dwc_sc_rnaseq" -H  "accept: application/json" -H  "Authorization: token 02adb0423492488ee3d4495b94cd1241ebf10551"

.. raw:: html

   <br>

Update Studies
""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. note::

         Authentication is required in order to use this API method. Create an
         API key from the :ref:`/apiKey API endpoint <endpoints-api-key>`
         before using this method.

      * **profile_id** (required): A hexadecimal identification number of the
        profile.

      * **schema_name** (required): The name of the schema.

        Options include:

        * ``copo_single_cell``
        * ``copo_image_rembi``
        * ``copo_image_stx_fish``

      * **checklist_id** (required): The identification number of the schema
        checklist.

        Possible options are:

        * ``version_dwc_sc_rnaseq``
        * ``version_mixs_sc_rnaseq``
        * ``version_tol_sc_rnaseq``
        * ``version_faang_sc_rnaseq``
        * ``version_rembi``
        * ``version_dwc_stx_fish``
        * ``version_mixs_stx_fish``
        * ``version_tol_stx_fish``

     * **file** (required): The spreadsheet file to be uploaded.

   .. raw:: html

      <br>

   .. hint::

      The words, ``manifest`` and ``checklist`` are used interchangeably. They
      both refer to a spreadsheet. `Schema` refers to the configuration
      of a checklist.

   **Usage**

    Please include at least the ``profile_id``, ``schema_name`` and
    ``checklist_id`` parameter values in the API URL and upload a
    spreadsheet file to retrieve studies that are associated with the provided
    profile ID.

    Replace ``<profile_id>``,  ``<schema_name>`` and  ``<token>`` with the
    desired values.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies

       .. tab-item:: Command Line (curl)

          .. code-block:: console

             $ curl -X POST "https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies" -H  "accept: application/json" -H  "Authorization: token <token>" -H  "Content-Type: multipart/form-data" -F "checklist_id=<checklist_id>" -F "file=@<file_name>.xlsx;type=application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

   **Example**

     To update Minimum Information about any (x) Sequence (MIxS) single-cell
     RNA-seq studies within a profile via the profile ID,
     ``68deb1fa4036b3903e261aee`` and schema, ``copo_single_cell``,
     use the following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies

       .. tab-item:: Command Line (curl)

          .. code-block:: console

             $ curl -X POST "https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies" -H  "accept: application/json" -H  "Authorization: token 02adb0423492488ee3d4495b94cd1241ebf10551" -H  "Content-Type: multipart/form-data" -F "checklist_id=version_mixs_sc_rnaseq" -F "file=@copo_single_cell_manifest_version_mixs_sc_rnaseq.xlsx;type=application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

.. raw:: html

   <br>

Export Study Data by Study ID (Spreadsheet or JSON-LD)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

  .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API
         URL. See the **Usage** and **Example** sections for details.

      .. note::

         Authentication is required in order to use this API method. Create an
         API key from the :ref:`/apiKey API endpoint <endpoints-api-key>`
         before using this method.

      * **profile_id** (required): A hexadecimal identification number of the
        profile.

      * **schema_name** (required): The name of the schema.

        Options include:

        * ``copo_single_cell``
        * ``copo_image_rembi``
        * ``copo_image_stx_fish``

      * **study_id** (required): A unique reference identifier of a
        study (or project) within a profile.

      * **return_type** (optional): Output format for the results. Options
        include **xlsx** (default) and **jsonld**

   .. raw:: html

      <br>

   .. hint::

      The words, ``manifest`` and ``checklist`` are used interchangeably. They
      both refer to a spreadsheet.

   **Usage**

    This endpoint returns a spreadsheet or JSON-LD (JavaScript Object Notation
    for Linked Data) file of a study (or project) within a profile by study
    ID, profile ID and schema name. Replace ``<profile_id>``,
    ``<schema_name>``, ``<study_id>`` with the desired value.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies/<study_id>


       .. tab-item:: Command Line (curl)

          .. code-block:: console

             $ curl -X GET "https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies/<study_id>" -H  accept:
             application/json" -H

   **Example**

    To retrieve a spreadsheet format of the study (or project) with the study
    ID, ``study1``, within the profile matching the ID
    ``68deb1fa4036b3903e261aee`` and schema, ``copo_single_cell``, use the
    following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies/study1

       .. tab-item:: Command Line (curl)

          .. code-block:: console

             $ curl -X GET "https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies/study1" -H  "accept: application/json" -H  "Authorization: token 02adb0423492488ee3d4495b94cd1241ebf10551"

.. raw:: html

   <br>

Submit Study to Public Repository
""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. note::

         Authentication is required in order to use this API method. Create an
         API key from the :ref:`/apiKey API endpoint <endpoints-api-key>`
         before using this method.

      * **profile_id** (required): A hexadecimal identification number of the
        profile.

      * **schema_name** (required): The name of the schema.

        Options include:

        * ``copo_single_cell``
        * ``copo_image_rembi``
        * ``copo_image_stx_fish``

      * **study_id** (required): A unique reference identifier of a
        study (or project) within a profile.

      * **repository** (optional): The public repository to which the study
        (or project) will be submitted. [#f2]_

        Options include:

        * **ena** (European Nucleotide Archive)
        * **zenodo** (Zenodo)

   .. raw:: html

      <br>

   .. hint::

      The words, ``manifest`` and ``checklist`` are used interchangeably. They
      both refer to a spreadsheet.

   **Usage**

    This endpoint submits a study (or project) within a profile to a public
    repository by study ID, profile ID and schema name. Replace
    ``<profile_id>``, ``<schema_name>``, ``<study_id>`` and ``<repository>``
    with the desired value.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies/<study_id>/action/submit?repository=<repository>

       .. tab-item:: Command Line (curl)

          .. code-block:: console

             curl -X POST "https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies/<study_id>/action/submit?repository=<repository>" -H  "accept: application/json" -H  "Authorization: token <token>" -d ""

   **Example**

    To retrieve a spreadsheet format of the study (or project) with the study
    ID, ``study1``, within the profile matching the ID
    ``68deb1fa4036b3903e261aee`` and schema, ``copo_single_cell``, use the
    following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies/study1/action/submit?repository=ena

       .. tab-item:: Command Line (curl)

          .. code-block:: console

             $ curl -X GET "https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies/study1/action/submit?repository=ena" -H  "accept: application/json" -H  "Authorization: token 02adb0423492488ee3d4495b94cd1241ebf10551"

.. raw:: html

   <br>

Fetch Study Submission Status
""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. note::

         Authentication is required in order to use this API method. Create an
         API key from the :ref:`/apiKey API endpoint <endpoints-api-key>`
         before using this method.

      * **profile_id** (required): A hexadecimal identification number of the
        profile.

      * **schema_name** (required): The name of the schema.

        Options include:

        * ``copo_single_cell``
        * ``copo_image_rembi``
        * ``copo_image_stx_fish``

      * **study_id** (required): A unique reference identifier of a
        study (or project) within a profile.

      * **repository** (optional): The public repository to which the study
        (or project) will be submitted. [#f2]_

        Options include:

        * **ena** (European Nucleotide Archive)
        * **zenodo** (Zenodo)

   .. raw:: html

      <br>

   .. hint::

      The words, ``manifest`` and ``checklist`` are used interchangeably. They
      both refer to a spreadsheet.

   **Usage**

    This endpoint submits a study (or project) within a profile to a public
    repository by study ID, profile ID and schema name. Replace
    ``<profile_id>``, ``<schema_name>``, ``<study_id>`` and ``<repository>``
    with the desired value.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies/<study_id>/action/submit?repository=<repository>

       .. tab-item:: Command Line (curl)

          .. code-block:: console

             curl -X POST "https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies/<study_id>/action/submit?repository=<repository>" -H  "accept: application/json" -H  "Authorization: token <token>" -d ""

   **Example**

    To retrieve a spreadsheet format of the study (or project) with the study
    ID, ``study1``, within the profile matching the ID
    ``68deb1fa4036b3903e261aee`` and schema, ``copo_single_cell``, use the
    following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies/study1/action/submit?repository=ena

       .. tab-item:: Command Line (curl)

          .. code-block:: console

             $ curl -X GET "https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies/study1/action/submit?repository=ena" -H  "accept: application/json" -H  "Authorization: token 02adb0423492488ee3d4495b94cd1241ebf10551"

.. raw:: html

   <br>

Fetch Study Submission Accession Number
"""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. note::

         Authentication is required in order to use this API method. Create an
         API key from the :ref:`/apiKey API endpoint <endpoints-api-key>`
         before using this method.

      * **profile_id** (required): A hexadecimal identification number of the
        profile.

      * **schema_name** (required): The name of the schema.

        Options include:

        * ``copo_single_cell``
        * ``copo_image_rembi``
        * ``copo_image_stx_fish``

      * **study_id** (required): A unique reference identifier of a
        study (or project) within a profile.

      * **repository** (optional): The public repository to which the study
        (or project) will be submitted. [#f2]_

        Options include:

        * **ena** (European Nucleotide Archive)
        * **zenodo** (Zenodo)

   .. raw:: html

      <br>

   .. hint::

      The words, ``manifest`` and ``checklist`` are used interchangeably. They
      both refer to a spreadsheet.

   **Usage**

    This endpoint retrieves the accession number of a study (or project) that
    was submitted to a public repository by study ID, profile ID and
    schema name. Replace ``<profile_id>``, ``<schema_name>`` and
    ``<study_id>`` with the desired value.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies/<study_id>/action/accession?repository=<repository>

       .. tab-item:: Command Line (curl)

          .. code-block:: console

             curl -X POST "https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies/<study_id>/action/accession?repository=<repository>" -H  "accept: application/json" -H  "Authorization: token <token>" -d ""

   **Example**

    To retrieve the submission accession number for the study (or project)
    with study ID ``study1`` within the profile ``68deb1fa4036b3903e261aee``
    and schema ``copo_single_cell`` from Zenodo, use the following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies/study1/action/accession?repository=zenodo

       .. tab-item:: Command Line (curl)

          .. code-block:: console

             $ curl -X GET "https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies/study1/action/accession?repository=zenodo" -H  "accept: application/json" -H  "Authorization: token 02adb0423492488ee3d4495b94cd1241ebf10551"

.. raw:: html

   <br>

Publish Study
"""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. note::

         Authentication is required in order to use this API method. Create an
         API key from the :ref:`/apiKey API endpoint <endpoints-api-key>`
         before using this method.

      * **profile_id** (required): A hexadecimal identification number of the
        profile.

      * **schema_name** (required): The name of the schema.

        Options include:

        * ``copo_single_cell``
        * ``copo_image_rembi``
        * ``copo_image_stx_fish``

      * **study_id** (required): A unique reference identifier of a
        study (or project) within a profile.

      * **repository** (required): The public repository to which the study
        (or project) will be submitted. [#f2]_

        Options include:

        * **ena** (European Nucleotide Archive)
        * **zenodo** (Zenodo)

   .. raw:: html

      <br>

   .. hint::

      The words, ``manifest`` and ``checklist`` are used interchangeably. They
      both refer to a spreadsheet.

   **Usage**

    This endpoint submits a study (or project) within a profile to a public
    repository by study ID, profile ID and schema name. Replace
    ``<profile_id>``, ``<schema_name>``, ``<study_id>`` and ``<repository>``
    with the desired value.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies/<study_id>/action/publish?repository=<repository>

       .. tab-item:: Command Line (curl)

          .. code-block:: console

             curl -X POST "https://copo-project.org/api/profiles/<profile_id>/schema/<schema_name>/studies/<study_id>/action/publish?repository=<repository>" -H  "accept: application/json" -H  "Authorization: token <token>" -d ""

   **Example**

    To publish a study (or project) with study ID ``study1`` within the
    profile ``68deb1fa4036b3903e261aee`` and schema ``copo_single_cell``
    from Zenodo, use the following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies/study1/action/publish?repository=ena

       .. tab-item:: Command Line (curl)

          .. code-block:: console

             $ curl -X GET "https://copo-project.org/api/profiles/68deb1fa4036b3903e261aee/schema/copo_single_cell/studies/study1/action/publish?repository=ena" -H  "accept: application/json" -H  "Authorization: token 02adb0423492488ee3d4495b94cd1241ebf10551"

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Refer to the :ref:`project-affiliations` section for more information
.. [#f2] See :ref:`overview-public-repositories` for a list of supported
         public repositories.

..
    Images declaration
..

.. |profile-collapsible-item-arrow| image:: /assets/images/icons/arrow-right.png
   :height: 2ex
   :class: no-scaled-link
