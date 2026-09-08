.. _defining-sample-types:

====================
Adding Sample Types
====================

Overview
--------

Currently, COPO supports sample data submissions to both Zenodo and
European Nucleotide Archive (ENA) [#f1]_. See the
:ref:`overview-public-repositories` section for more details.

Typically, ENA sample checklists are used in submissions but there may be cases
where you might want to submit samples that are not associated with an
existing ENA sample checklist.

Custom sample checklists [#f2]_ must follow a :ref:`basic sample data structure
<defining-sample-types-basic-data-structure>` that is defined in XML
format. Given that ENA does not provide a checklist corresponding to your
custom sample checklist, the `ENA default sample checklist
<https://www.ebi.ac.uk/ena/browser/view/ERC000011>`__ will be used when
submitting the newly defined data to ENA. The default ENA sample checklist
contains mandatory fields so these fields must also be included in your
custom sample checklist.

.. raw:: html

   <hr>

Step 1: Create an XML for new sample type
-----------------------------------------

.. _defining-sample-types-basic-data-structure:

.. hint::

   * Mandatory :abbr:`ENA (European Nucleotide Archive)` fields are identified
     by the ``<SYNONYM></SYNONYM>`` tag in the XML

   * Click the arrow icon (|collapsible-item-arrow|) below to reveal the data
     structure.

Create an XML file and store it in the
`samples directory within the COPO-schemas GitHub repository
<copo-sample-schema-directory_>`__. It must
contain the basic structure for defining a custom sample checklist outlined
below.

Values that include `example` are placeholders and must be replaced with
values appropriate to your checklist.

The following values are required and must not be changed:

* ``<AUTHORITY>`` must be **COPO**.
* The `accession` attribute of ``<CHECKLIST>`` must begin with **COPO_**.
* ``<PRIMARY_ID>`` must begin with **COPO_**.
* ``<ENA_CHECKLIST_ID>`` should contain **ERC000011**. It is the
  identifier for the `default sample checklist at ENA \
  <https://www.ebi.ac.uk/ena/browser/view/ERC000011>`__.

.. collapse:: Basic sample checklist XML data structure

   .. literalinclude:: /assets/files/setup/data/sample-checklist.xml
      :language: xml
      :caption: Basic sample checklist data structure

.. raw:: html

   <br>

See the :ref:`defining-sample-types-examples` section below for applications
of this XML sample structure to different custom sample types used in COPO.

.. raw:: html

   <hr>

Step 2: Add XML file path to COPO project
------------------------------------------

Edit the `data.py <copo-settings-file_>`__ file located in the
``src/main_config/settings`` directory of the project in the
`COPO-production GitHub repository <copo-github-repository_>`__. Add the
absolute file path of the XML file created in Step 1 to the
`COPO_SAMPLE_CHECKLIST_URL` list.

.. code-block:: python
   :caption: Extend the COPO_SAMPLE_CHECKLIST_URL list in data.py

   ...

   COPO_SAMPLE_CHECKLIST_URL = [
      "https://raw.githubusercontent.com/EarlhamInst/COPO-schemas/refs/heads/main/samples/sample_checklist_dwc.xml",
      "https://raw.githubusercontent.com/EarlhamInst/COPO-schemas/refs/heads/main/samples/sample_checklist_faang.xml",
      # Add the path to your XML file here
      # e.g. "https://raw.githubusercontent.com/EarlhamInst/COPO-schemas/refs/heads/main/samples/sample_checklist_your_sample_type.xml"
   ]

   ...

.. raw:: html

   <hr>

.. _defining-sample-types-persist-data:

Step 3: Persist new sample type to COPO
---------------------------------------

Now that the XML file of the new sample type has been added to the
`samples directory in the COPO-schemas GitHub repository
<copo-sample-schema-directory_>`__, the following steps guide how to persist
its data to the COPO website so that it is available as a dropdown menu option
and the data of the new sample type is available within the downloaded
spreadsheet file for the respective checklist type.

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

   celery -A src call src.apps.copo_core.tasks.update_ena_checklist

This command calls the **update_ena_checklist** Celery job defined in the
`src/celery.py <copo-celery-file_>`__ file, which in turn calls the
**update_ena_checklist** Celery task defined in the
`src/apps/copo_core/tasks.py
<copo-core-tasks-file_>`__ file.

The **updateCheckList** function in the
`common/ena_utils/EnaChecklistHandler.py
<copo-ena-checklist-handler-file_>`__ file is then called and is
responsible for parsing the XML file from the GitHub repository,
updating the system's database and by extension the website with the new data.
It also creates and updates predefined sample checklists from
:abbr:`ENA (European Nucleotide Archive)` and custom sample checklists in the
system's database.

To verify that the new sample type has been added, navigate to the
:ref:`Samples page <samples-submission-biodata>` under a
:ref:`Biodata profile <profile-walkthrough-biodata>` on the COPO platform and
check if the new sample type is available in the dropdown menu and its data is
present in the downloaded spreadsheet file for the respective checklist type.

.. raw:: html

   <hr>

.. _defining-sample-types-examples:

Examples of Sample Data Structure used in COPO
----------------------------------------------

.. tip::

   Each link below takes you to the corresponding GitHub directory containing
   the spreadsheet files for that data type. Select a link to view the files
   and see how the data is structured.

   The spreadsheet file containing the main schema can be identified by the
   substring ``_sample_checklist_``.

* `Sample data <copo-sample-schema-directory_>`__ |external-link-icon|


.. raw:: html

   <hr>

Related sections
-----------------

.. seealso::

   * :ref:`defining-other-data-types`

.. raw:: html

   <br><hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`European Nucleotide Archive (ENA) <ENA>`.
.. [#f2] See term: :term:`Checklist`

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

.. _copo-celery-file: https://raw.githubusercontent.com/EarlhamInst/COPO-production/refs/heads/main/src/celery.py
.. _copo-core-tasks-file: https://raw.githubusercontent.com/EarlhamInst/COPO-production/refs/heads/main/src/apps/copo_core/tasks.py
.. _copo-ena-checklist-handler-file: https://raw.githubusercontent.com/EarlhamInst/COPO-production/refs/heads/main/common/ena_utils/EnaChecklistHandler.py
.. _copo-github-repository: https://github.com/EarlhamInst/COPO-production
.. _copo-sample-schema-directory: https://github.com/EarlhamInst/COPO-schemas/tree/main/samples
.. _copo-schemas-github-repository: https://github.com/EarlhamInst/COPO-schemas
.. _copo-settings-file: https://raw.githubusercontent.com/EarlhamInst/COPO-production/refs/heads/main/src/main_config/settings/data.py
