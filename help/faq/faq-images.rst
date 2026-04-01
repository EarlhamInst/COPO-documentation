.. _faq-images:

Images
------

.. tip::

   To read the entire answer to a :abbr:`FAQ (Frequently Asked Question)`,
   click the arrow icon (|collapsible-item-arrow|) below any question to
   expand or collapse it.

.. raw:: html

  <hr>

Which types of image data can be submitted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   Image submissions can be made under a Biodata profile or a Tree of Life
   (ToL) profile.

   * If submitting image data under a Biodata profile, the following are the
     types of image data submissions that are supported:

     * :abbr:`REMBI (Recommended Metadata for Biological Images)` images
     * :abbr:`ST-FISH (Spatial Transcriptomics Fluorescence In Situ
       Hybridisation)` images

   * If submitting images under a :abbr:`ToL (Tree of Life)` profile, only
     sample images are supported and they must be uploaded in the
     **Upload Sample Spreadsheet** dialogue after the sample manifest has been
     uploaded.

   The table below summarises the types of image submissions that can be made
   in COPO, the buttons used to access them and the profile types through
   which they can be submitted.

   .. _images-component-subcomponents:

   .. list-table:: Types of Image data submissions
      :widths: 40 40 20
      :width: 100%
      :align: center
      :header-rows: 1

      * - Type of image submission
        - Button
        - Profile type
      * - :ref:`REcommended Metadata for Biological Images (REMBI)
          <image-submission-rembi>`
        - |rembi-image-component-button|
        - :ref:`Biodata <profile-walkthrough-biodata>`
      * - :ref:`Spatial Transcriptomics Fluorescence In Situ Hybridisation
          (ST-FISH) <image-submission-st-fish>`
        - |st-fish-image-component-button|
        - :ref:`Biodata <profile-walkthrough-biodata>`
      * - :ref:`Sample images <image-submission-tol-samples>`
        - |upload-images-button| on the **Upload Sample Spreadsheet** dialogue
        - :ref:`Tree of Life <profile-walkthrough-tol>`

.. raw:: html

   <br

How do I submit images?
~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   See :ref:`image-submission` section for guidance.

.. raw:: html

   <br

.. _faq-image-submission-errors:

What factors can cause errors when uploading images?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. collapse:: Click to view answer

   .. raw:: html

      <br>

   .. note::

      * Images can only be submitted after samples have been uploaded in the
        **Upload Sample Spreadsheet** dialogue. The
        max total image size should be no more than 2GB.

      * Images can only be submitted via a ToL [#f1]_ profile. Please see:
        :ref:`Steps to Create a Tree of Life Profile <profile-walkthrough-tol>`
        for guidance.

      * The file name of sample images must be named as
        ``{Specimen_ID}-{n}.[jpg|png]`` where ``{n}`` is the image number,
        ``{Specimen_ID}`` is the specimen ID of the sample in the manifest and
        ``jpg`` or ``png`` is the extension of the file.

   .. important::

      The |upload-images-button| button will only be enabled after you upload a
      manifest in the **Upload Sample Spreadsheet** dialogue. This process must
      be completed in one go; you cannot close the dialogue and return later to
      upload images. The images rely on metadata from the sample manifest, so
      the |upload-images-button| button becomes active immediately after the
      manifest is uploaded, allowing you to add images in the same session.

   Errors occur due to several reasons. An error message will be displayed
   detailing the issue(s) encountered and potential resolution(s). If you are
   uncertain how to proceed, please contact the
   :email:`COPO team <ei.copo@earlham.ac.uk>`.

   Other potential reasons and solutions for errors include but are not
   limited to:

      * Uploading images where the total size of the images exceeds **2GB**
      * (the maximum allowable file size) may
        result in errors.

        Common web browser error messages include ``Error 0: error`` though the
        specific message may vary by browser,
        as the error is browser-generated.

        **Workaround**: Upload smaller batches of images separately. You will
        need to first upload the manifest, any applicable permits then, upload
        the images in batches, as images cannot be uploaded directly and all
        at once.

.. raw:: html

   <br><hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Compliance field`

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/arrow-right.png
   :height: 2ex
   :class: no-scaled-link

.. |rembi-image-component-button| image:: /assets/images/images-comp/buttons/components-images-button-rembi.png
   :height: 4ex
   :class: no-scaled-link

.. |st-fish-image-component-button| image:: /assets/images/images-comp/buttons/components-images-button-st-fish.png
   :height: 4ex
   :class: no-scaled-link

.. |upload-images-button| image:: /assets/images/buttons/images-upload-button.png
   :height: 4ex
   :class: no-scaled-link
