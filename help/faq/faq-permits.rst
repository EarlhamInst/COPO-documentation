.. _faq-permits:

Permits
-------

.. tip::

   To read the entire answer to a :abbr:`FAQ (Frequently Asked Question)`,
   click the arrow icon (|collapsible-item-arrow|) below any question to
   expand or collapse it.

.. raw:: html

  <hr>

How can I view or download my uploaded permits?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

  Yes, permits can be retrieved and downloaded by selecting the desired sample
  record(s) on the **Samples** page

  Then, clicking the |download-permits-button1| button on the page.

.. raw:: html

   <br>

.. _faq-permits-error-uploading-multiple-permits-separately:

Why can’t I upload permits consecutively?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   .. warning::

      If uploading multiple permit files, select them all at once (e.g.
      ``CTRL`` + click) and upload together using the |upload-permits-button|.
      Individual uploads are not allowed.

.. raw:: html

   <br>

How to resolve "Conflicting data…" error when uploading permits?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   The error message ``Conflicting data`` is displayed when at least one of the
   following occurs:

   * The permit file name provided in the manifest does not end with the
     extension ``.pdf`` or ``.PDF``

     **Resolution**: Rename the name of the permit file so that it ends with
     the extension, ``.pdf`` or ``.PDF`` then, reupload the manifest

   * In the uploaded manifest, different permit file names are associated with
     the same **SPECIMEN_ID**

     **Resolution**: Provide a unique permit file name for each
     **SPECIMEN_ID** or provide the same file name for permit files that are
     associated with the same **SPECIMEN_ID** in the manifest. Then, reupload
     the manifest.

.. raw:: html

   <br>

Why does the “No xx permit found for SPECIMEN_ID” error appear?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   The error,
   ``No xx permit found for SPECIMEN_ID… Filename of permit must be named xx``,
   occurs when at least one of the following occurs:

   * The manifest uploaded requires multiple permit files but they were
     uploaded separately i.e. one after the other.

     **Resolution**: Please refer to
     :ref:`faq-permits-error-uploading-multiple-permits-separately`
     :abbr:`FAQ (Frequently Asked Question)` for more information.

   * The permit file name uploaded from your local system actually ends with
     ``.pdf.pdf`` (or ``.PDF.PDF``) and not ``.pdf`` (or ``.PDF``)

     **Resolution**: Ensure that the name of the permit file ends with the
     ``.pdf`` or ``.PDF`` extension only.

     If you are using a Windows operating system (OS) to upload permits,
     Windows OS by default, hides file extensions
     which results in it not being visible to you.

     If you would like to see the file extension, you can enable it by
     following these `guidelines
     <https://support.microsoft.com/en-gb/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01>`__.

   Reupload the manifest as well as the permit files after the resolutions
   have been made.

.. raw:: html

   <hr>

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/arrow-right.png
   :height: 2ex
   :class: no-scaled-link

.. |download-permits-button1| image:: /assets/images/buttons/permits-download-button1.png
   :height: 4ex
   :class: no-scaled-link

.. |upload-permits-button| image:: /assets/images/buttons/permits-upload-button.png
   :height: 4ex
   :class: no-scaled-link
