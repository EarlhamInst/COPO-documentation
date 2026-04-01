.. _data-updates:

=======================
Updating Submitted Data
=======================

Updates follow the same process as the initial submission. The process is described in the **Data Submissions**
section (in the sidebar on the left-hand side of the page). Click the desired submission type for instructions.

Data is updated by **uploading an amended manifest** or **updated spreadsheet file** to the **same profile** that was
initially used to upload the manifest (before any modifications were done).

In essence, the uploaded manifest must include amendments for the change or
update to occur. The system will detect any changes, process the updated data
and highlight errors if they occur.

After a successful validation, the |confirm-button| button will appear.
Click it to apply the changes.

.. important::

   An error will occur if you perform any of the following actions:

   * Upload the amended manifest to a different profile [#f1]_ (other than the
     one used to initially upload the manifest)
   * Upload the amended manifest to a new profile
   * Delete a profile that already has data associated with it
   * Include new data on an amended manifest and then upload it. New data cannot
     be combined with existing data on a manifest, they must be be on separate spreadsheets.

Refer to the relevant sections below for restrictions and guidelines regarding
updating specific types of submitted data. Click |collapsible-item-arrow| to
expand a section.

* :doc:`Samples <data-updates-samples>`

.. _update-notes-sample-permits-and-images:

* .. collapse:: Sample permits and sample images

     .. raw:: html

        <br>

     * Sample permits and images can be updated by first uploading an amended
       sample manifest to the same profile used for the initial submission.
       Then, clicking the |upload-permits-button| or |upload-images-button|
       button. After a successful validation, the |confirm-button| button
       will appear. Click it to apply the changes.

.. _update-notes-reads:

* .. collapse:: Reads

     .. raw:: html

        <br>

     * Updates to reads can **only** be done if the values in the ``Sample``,
       ``File checksum``, ``File name`` and ``Library layout`` remain the same
       in the manifest. If any of these values change, errors will occur
       during the update process.

       This is because the value in the ``Sample`` column serves as the key
       for each row in the **Reads** manifest. Each unique sample in the
       manifest corresponds to a different biosample which is linked or tied
       to the value in the ``File checksum``, ``File name`` and
       ``Library layout`` columns.

.. _update-notes-assemblies:

* .. collapse:: Assemblies

     .. raw:: html

        <br>

     Once **assemblies** have been submitted, they cannot be updated.

.. _update-notes-sequence-annotations:

* .. collapse:: Sequence Annotations

     .. raw:: html

        <br>

     * Select a sequence annotation [#f3]_ record from the table, then click
       ``Edit``. Update the details and click **Submit Annotation**.

.. raw:: html

   <hr>

.. _data-deletion:

Deleting Submitted Data
-----------------------

Data can only be deleted **before** submission to public repositories [#f2]_.
Select a record from the data table then, click the **Delete** button
(top-right of the table), indicated by |delete-button| as shown in the image
below. This method can also be applied to other types of submitted data.

.. note::

   Not all submitted data can be deleted. Refer to the relevant sections below
   for restrictions and guidelines regarding deleting specific types of
   submitted data. Click |collapsible-item-arrow| to expand each section.

.. _deletion-notes-samples:

* .. collapse:: Samples

     .. raw:: html

        <br>

     Samples cannot be deleted.

.. raw:: html

   <br>

.. figure:: /assets/images/files/ui/files-pointer-to-delete-file-button.png
   :alt: Delete files button
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/files/ui/files-pointer-to-delete-file-button.png
   :class: with-shadow with-border

   **Click the** ``Delete`` **button to remove the selected record.**

.. raw:: html

   <hr>

Related Topics
--------------

.. seealso::

   * :ref:`files`
   * :ref:`samples-submission`
   * :ref:`reads`
   * :ref:`Resolving Errors during Reads Update <faq-reads-update-errors>`
   * :ref:`assemblies`
   * :ref:`single-cell-submissions`
   * :ref:`sequence-annotations`
   * :ref:`barcoding-submissions`
   * :ref:`image-submission`
   * :ref:`permits-submission`
   * :ref:`faq-data-status-and-progress-legend`
     :abbr:`FAQ (Frequently Asked Question)` section.

.. raw:: html

   <br><hr>

.. rubric:: Footnotes

.. [#f1] Also known as COPO profile. See term: :term:`COPO profile`.
.. [#f2] See :ref:`overview-public-repositories` for a list of supported
         public repositories.
.. [#f3] See: :term:`Sequence Annotation`.

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/arrow-right.png
   :height: 2ex
   :class: no-scaled-link

.. |confirm-button| image:: /assets/images/buttons/confirm-button.png
   :height: 4ex
   :class: no-scaled-link

.. |delete-button| image:: /assets/images/buttons/delete-record-button.png
   :height: 4ex
   :class: no-scaled-link

.. |upload-images-button| image:: /assets/images/buttons/images-upload-button.png
   :height: 4ex
   :class: no-scaled-link

.. |upload-permits-button| image:: /assets/images/buttons/permits-upload-button.png
   :height: 4ex
   :class: no-scaled-link
