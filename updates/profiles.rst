.. _profile-update:

=================
Updating Profiles
=================

.. warning::

   * Profile types cannot be changed after a profile is created. To change it,
     delete the profile and create a new one with a different profile type.

   * Profiles can only be deleted if they have no associated data such as
     samples, reads, assemblies, data files etc. For profiles with associated
     data, contact the :email:`COPO team <ei.copo@earlham.ac.uk>` to request
     deletion.

.. note::

   * If the associated type is updated during the profile update process,
     samples that have not been accepted and sent to European Nucleotide
     Archive (ENA) will also have the associated profile type updated.

   * If the profile is shared, it cannot be updated by the sharee.

To edit a profile, click the |vertical-ellipsis-icon| icon associated with a
profile. Then, click the ``Edit`` button.

..  figure:: /assets/images/profiles/ui/profile_options_edit_record.png
    :alt: Edit profile option
    :align: center
    :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/ui/profile_options_edit_record.png
    :class: with-shadow with-border
    :height: 400px

    **Click the** ``Edit`` **button**

..  figure:: /assets/images/profiles/ui/profile_options_edit_record_details.png
    :alt: Profile update details
    :align: center
    :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/ui/profile_options_edit_record_details.png
    :class: with-shadow with-border
    :height: 550px

    **Update the details then, click** ``Save`` **to apply the changes**

..  figure:: /assets/images/profiles/ui/profile_record_updated.png
    :alt: Profile updated message
    :align: center
    :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/ui/profile_record_updated.png
    :class: with-shadow with-border

    **Profile updated**

.. raw:: html

   <hr>

.. _profile-deletion:

Deleting Profiles
-----------------

.. note::

   * Deleting a profile will **not** delete the associated COPO user account.
     The user account will still exist and be able to log into the system.

   * Only profiles that have no associated research objects such as samples,
     reads, assemblies or data files etc. can be deleted. If you need to have
     a profile deleted that contain data, contact the
     :email:`COPO team <ei.copo@earlham.ac.uk>`.

   * If a profile is shared, it cannot be deleted by the sharee.

To delete a profile, click the |vertical-ellipsis-icon| icon associated with a
profile. Then, click the ``Delete`` button.

..  figure:: /assets/images/profiles/ui/profile_options_delete_record.png
    :alt: Delete profile option
    :align: center
    :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/ui/profile_options_delete_record.png
    :class: with-shadow with-border
    :height: 310px

    **Click the** ``Delete`` **button**

..  figure:: /assets/images/profiles/modals/profile_options_delete_confirmation_dialog.png
    :alt: Profile deletion confirmation dialog
    :align: center
    :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/modals/profile_options_delete_confirmation_dialog.png
    :class: with-shadow with-border
    :height: 210px

    **Confirm profile deletion**

..  figure:: /assets/images/profiles/modals/profile_options_delete_error_dialog.png
    :alt: Profile deletion error dialog
    :align: center
    :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/profiles/modals/profile_options_delete_error_dialog.png
    :class: with-shadow with-border
    :height: 170px

    **Profile deletion error when data is attached**

Once deleted, the profile is removed from the **Work profiles** page.

..
    Images declaration
..

.. |vertical-ellipsis-icon| image:: /assets/images/profiles/icons/profile_vertical_ellipsis_icon.png
   :height: 4ex
   :class: no-scaled-link
