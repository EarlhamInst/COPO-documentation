.. _copo-api:

===========================
Using COPO Programmatically
===========================

The COPO API [#f1]_ is a :abbr:`RESTful (REpresentational State Transfer ful)`
[#f2]_ web service that enables users to access and interact with the COPO
system, either programmatically or through the user interface. It is built
using the Swagger (OpenAPI) framework and is accessible at:
`<https://copo-project.org/api>`_.

.. hint::

   The button, |copo-api-live-server-button|, indicates that the API method
   endpoints will produce results from the website host server i.e. if the
   live COPO website is used to query the endpoint, then, the live results
   will be retrieved while the opposite occurs if one uses the demo website
   to query the API method endpoints.

.. raw:: html

   <hr>

API End-points
---------------

The COPO :abbr:`API (Application Programming Interface)` [#f1]_ includes
endpoints for `audit <audit-api-methods_>`_,
`manifest <manifest-api-methods_>`_, `sample <sample-api-methods_>`_,
`profile <profile-api-methods_>`_, `statistics <statistics-api-methods_>`_ and
`mapping <mapping-api-methods_>`_ data. Results can be downloaded in
:abbr:`CSV (Comma-separated values)` format or viewed in
:abbr:`JSON (JavaScript Object Notation)` or
:abbr:`Ro-Crate (Research Object Crate)` [#f3]_ formats depending on the
record type as shown in the table below.

Most endpoints support querying by a specific metadata standard. Refer to the
:ref:`Available Standards for Records <mapping-api-standards>` table for
details on which standards are supported for each record type. This
flexibility promotes interoperability with other systems that comply with
different standards.

By default, API endpoints return data in the Tree of Life (ToL) standard and
in JSON format, unless a different standard or format is specified.

All results contain metadata submitted by the original data providers.

.. list-table:: Available Result Formats for Records
   :width: 100%
   :align: center
   :header-rows: 1

   * - Output Format
     - Available Record Types
   * - csv
     - Audit, Sample, Manifest
   * - json
     - Audit, Sample, Manifest
   * - json-ld
     - Profile
   * - ro-crate
     - Sample
   * - xlsx
     - Profile

.. _mapping-api-standards:

.. list-table:: Available Standards for Records
   :width: 100%
   :align: center
   :header-rows: 1

   * - Standard
     - Backronym
     - Available Records Types
   * - dwc
     - Darwin Core
     - Sample, Manifest
   * - ena
     - European Nucleotide Archive
     - Sample, Manifest
   * - mixs
     - Minimum Information about any (x) Sequence
     - Sample, Manifest
   * - tol
     - Tree of Life
     - Sample, Manifest

.. raw:: html

   <br>

See the following sections for details on each category of API endpoints:

.. toctree::
   :maxdepth: 1

   api/api-key-endpoint
   api/audit-endpoints
   api/manifest-endpoints
   api/sample-endpoints
   api/profile-endpoints
   api/statistics-endpoints
   api/mapping-endpoints

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`API`
.. [#f2] See term: :term:`REST`
.. [#f3] See term: :term:`RO-Crate`

..
    Images declaration
..

.. |copo-api-live-server-button| image:: /assets/images/buttons/api-button-live-server-option.png
   :height: 6ex
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/buttons/api-button-live-server-option.png

..
    Link declaration
..

.. _audit-api-methods: https://copo-project.org/static/swagger/apidocs_index.html#/Audit
.. _manifest-api-methods: https://copo-project.org/static/swagger/apidocs_index.html#/Manifest
.. _sample-api-methods: https://copo-project.org/static/swagger/apidocs_index.html#/Sample
.. _profile-api-methods: https://copo-project.org/static/swagger/apidocs_index.html#/Profile
.. _statistics-api-methods: https://copo-project.org/static/swagger/apidocs_index.html#/Statistics
.. _mapping-api-methods: https://copo-project.org/static/swagger/apidocs_index.html#/Tree%20of%20Life%20(ToL)%20Mapping
