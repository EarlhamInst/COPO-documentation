.. _data-download:

==========================
Downloading Submitted Data
==========================

.. hint::

   This is useful if you would like to update sample metadata for a manifest
   or retrieve the actual manifest that was submitted.

   Samples can be updated by resubmitting the manifest with the updated
   metadata. See :ref:`sample-update-notes` section for more information
   about which fields can be updated.

.. note::

   * At least one sample record (in a manifest) must be submitted before a
     manifest can be downloaded.

     See the :ref:`Download sample manifest FAQ
     <faq-samples-download-sample-manifest-incorrect-sample-metadata>`
     section for more information.

   * The colour of the |add-manifest-button| button is based on the type of
     profile that you are making a submission to.

     See the :ref:`profile-types-legend` section regarding the colour code
     for the various types of project profiles on COPO.

The following steps describe how to download a submitted sample manifest:

#. Navigate to the **Samples** page.

   To do this, please refer to the relevant section below, depending on the
   type of profile that you are working on.

   * :ref:`Accessing the Samples page (Tree of Life profiles)
     <accessing-samples-page-tol>`
   * :ref:`Accessing the Samples page (Biodata profiles)
     <accessing-samples-page-biodata>`

#. On the **Samples** page, select **only one** sample record from the sample
   record table displayed.

   Then, click the |download-sample-manifest-button| button to download the
   manifest.

   **Note**: The record that you click the |download-sample-manifest-button|
   on is associated with a particular manifest ID so all samples associated
   with that manifest ID will be downloaded. The manifest ID value can be
   viewed in the **Manifest Identifier** column in the data table.

   See the :ref:`Download sample manifest FAQ
   <faq-samples-download-sample-manifest-incorrect-sample-metadata>` section
   for more information.

   .. raw:: html

      <br>

   .. hint::

      The manifest will be automatically downloaded as a ``.xlsx`` file

   .. figure:: /assets/images/samples/ui/samples_pointer_to_download_sample_manifest_button.png
      :alt: Samples page with one sample record selected and a pointer to the
            'Download sample manifest' button
      :align: center
      :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/files/buttons/files_button_pointer_biodata.png
      :class: with-shadow with-border

      **Samples page: Pointer to 'Download sample manifest' button**

..
    Images declaration
..

.. |add-manifest-button| image:: /assets/images/buttons/add_manifest_button.png
   :height: 4ex
   :class: no-scaled-link

.. |download-sample-manifest-button| image:: /assets/images/samples/buttons/samples_download_manifest_button.png
   :height: 4ex
   :class: no-scaled-link
