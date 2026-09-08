.. _profile-setup-title-button:

TitleButton
~~~~~~~~~~~

Title buttons are individual elements or modules that make up the profile.
These can include various functionalities or data points that contribute to
the profile's overall purpose.

.. raw:: html

   <hr>

TitleButton Database Table Structure
-------------------------------------

The **TitleButton** model represents interactive buttons that allow users to
perform specific actions related to records within the profile. These actions
can include creating, downloading or accessing other functionalities.

The PostgreSQL table **TitleButton** consists of the following fields:

* ``id`` (Integer):
     The primary key and unique identifier for each title button

* ``name`` (String):
      The internal name of the title button used to identify the title button.
      It is often used in the code to refer to the button

* ``template`` (String):
      The HTML template string used to render the button. It includes various
      HTML attributes such as style, title,
      :abbr:`CSS (Cascading Style Sheets)` classes and icon elements

* ``additional_attr`` (String):
     Any additional attributes required for the button. It is often used to
     store URLs or other necessary data for the button's functionality

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents

.. collapse:: TitleButton database fields

   .. code-block:: console

       id |                name                      |                                                                                                                        template                                                                                                                                               |     additional_attr
      ----+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------
        1 | accept_reject_samples                    | <button style="display: none" title="Accept or reject Tree of Life samples" class="big circular ui icon teal button accept_reject_samples copo-tooltip" data-tour-id="accept_reject_samples_title_button">         <i class="icon tasks sign"></i>     </button>              |
        2 | copo_accessions                          | <button style="display: none" title="View accessions dashboard" class="big circular ui icon pink button copo_accessions copo-tooltip" data-tour-id="accession_dashboard_title_button">         <i class="icon sitemap"></i>     </button>                                     |
        3 | download_blank_manifest_template         | <a  title="Download manifest template" class="big circular ui icon brown button download-blank-manifest-template copo-tooltip" target="_blank" data-tour-id="download_blank_manifest_title_button">         <i class="icon download sign"></i>     </a>                       | href:#blank_manifest_url
        4 | download_sop                             | <a title="Download Standard Operating Procedure (SOP)" class="big circular ui icon yellow button download-sop copo-tooltip" target="_blank" data-tour-id="download_sop_title_button">         <i class="icon download sign"></i>     </a>                                     | href:#sop_url
        5 | new_component_template                   | <button title="Add record" class="big circular ui icon primary button new-component-template copo-tooltip" data-tour-id="new_component_title_button">         <i class="icon add sign"></i>     </button>                                                                     |
        6 | new_general_sample_spreadsheet_template  | <button style="display: inline" title="Add or update samples from spreadsheet" class="big circular ui icon button new-general-sample-spreadsheet-template copo-tooltip" data-tour-id="new_spreadsheet_title_button">         <i class="icon table sign"></i>     </button>    |
        7 | new_local_file                           | <button title="Add file by browsing local file system" class="big circular ui icon primary button new-local-file copo-tooltip" data-tour-id="new_file_button_local">         <i class="icon desktop sign"></i>     </button>                                                  |
        8 | new_reads_spreadsheet_template           | <button style="display: inline" title="Add reads from spreadsheet" class="big circular ui icon button new-reads-spreadsheet-template copo-tooltip" data-tour-id="new_spreadsheet_title_button">         <i class="icon table sign"></i>     </button>                         |
        9 | new_samples_spreadsheet_template         | <button   title="Add or update samples from spreadsheet" class="big circular ui icon button new-samples-spreadsheet-template copo-tooltip" data-tour-id="new_samples_button">         <i class="icon table sign"></i>     </button>                                           |
       10 | new_singlecell_spreadsheet_template      | <button style="display: inline" title="Add study from spreadsheet" class="big circular ui icon button new-singlecell-spreadsheet-template copo-tooltip" data-tour-id="new_spreadsheet_title_button">         <i class="icon table sign"></i>     </button>                    |
       11 | new_taggedseq_spreadsheet_template       | <button style="display: inline" title="Add tagged sequences from spreadsheet" class="big circular ui icon button new-taggedseq-spreadsheet-template copo-tooltip" data-tour-id="new_spreadsheet_title_button">         <i class="icon table sign"></i>     </button>          |
       12 | new_terminal_file                        | <button title="Add file by terminal" class="big circular ui icon primary button new-terminal-file copo-tooltip"  data-tour-id="new_file_button_terminal">         <i class="icon terminal sign"></i>     </button>                                                            |
       13 | quick_tour_template                      | <button title="Take a tour of this page" class="big circular ui icon orange button start-tour quick-tour-template copo-tooltip" data-tour-id="quick_tour_title_button">         <i class="icon lightbulb"></i>     </button>                                                  |
       14 | tol_inspect                              | <button style="display: none" title="Inspect Tree of Life data" class="big circular ui icon yellow button tol_inspect copo-tooltip" data-tour-id="tol_inspect_title_button">         <i class="icon clipboard list"></i>     </button>                                        |
       15 | tol_inspect_gal                          | <button class="big circular ui icon green button tol_inspect_gal copo-tooltip" title="Inspect Tree of Life data by Genome Acquisition Labs" data-tour-id="tol_inspect_gal_title_button">         <i class="icon building"></i>     </button>                                  |

.. raw:: html

   <br><br>

.. collapse:: Description of each TitleButton record

   .. raw:: html

      <br>

   * **new_component_template**: Button to add a new profile record. It is
     styled with a primary colour and an icon of an add sign

   * **quick_tour_template**: Button to start a quick tour. It is styled with
     an orange colour and an icon of a lightbulb

   * **new_samples_spreadsheet_template**: Button to add samples from a
     spreadsheet template. It is styled with a teal colour and an icon of a
     table sign

   * **new_reads_spreadsheet_template**: Button to add reads from a spreadsheet
     template. It is styled with a teal colour and an icon of a table sign

   * **new_local_file**: Button to add a new file by browsing the local file
     system. It is styled with a primary colour and an icon of a desktop sign

     |section|
     :ref:`Section on Button Usage in the Project <files-submission-via-browser>`

   * **new_terminal_file**: Button to add a new file by terminal. It is styled
     with a primary colour and an icon of a terminal sign

     |section| :ref:`Section on Button Usage in the Project
     <files-submission-via-terminal>`

   * **new_taggedseq_spreadsheet_template**: Button to add tagged sequences
     from a spreadsheet template. It is styled with a teal colour and an
     icon of a table sign

     |section| :ref:`Section on Button Usage in the Project
     <accessing-accept-reject-samples-page>`

     `Associated page \
     <copo-accept-reject-samples-page-link_>`__ |external-link-icon|

   * **download_blank_manifest_template**: Button to download a blank manifest
     template. It is styled with a brown colour and an icon of a download sign

   * **download_sop**: Button to download the
     :abbr:`SOP (Standard Operating Procedure)`. It is styled with a yellow
     colour and an icon of a download sign

   * **accept_reject_samples**: Button to accept or reject
     :abbr:`ToL (Tree of Life)` samples. It is styled with a teal colour and
     an icon of tasks

     |section| :ref:`Section on Button Usage in the Project
     <accessing-accept-reject-samples-page>`

     `Associated page
     <copo-accept-reject-samples-page-link_>`__ |external-link-icon|

     `Django Admin UI <copo-django-admin-ui-image_>`__ |external-link-icon|

   * **tol_inspect**: Button to inspect the :abbr:`ToL (Tree of Life)` samples.
     It is styled with a yellow colour and an icon of a clipboard list

     |section| :ref:`Section on Button Usage in the Project <tol-inspection>`

     `Associated page \
     <https://copo-project.org/copo/tol_dashboard/tol_inspect>`__ |external-link-icon|

   * **tol_inspect_gal**: Button to inspect the
     :abbr:`ToL (Tree of Life)` by Genome Acquisition Lab (GAL). It is styled
     with a green colour and an icon of a building

     |section| :ref:`Section on Button Usage in the Project
     <tol-inspection-by-gal>`

     `Associated page \
     <https://copo-project.org/copo/tol_dashboard/tol_inspect/gal>`__ |external-link-icon|

   * **copo_accessions**: Button to access the Accessions Dashboard. It is
     styled with a pink colour and an icon of a sitemap

.. raw:: html

   <hr>

Referencing Created TitleButton in Project
-------------------------------------------

.. note::

   * Ensure that a Django app is created to manage the ``TitleButton`` Django
     model and render the buttons in the template.

     Refer to the :ref:`profile-setup-component-creation` section which
     explains how to create a Django app for a component

   * Ensure that static files like :abbr:`CSS (Cascading Style Sheets)` and
     :abbr:`JS (JavaScript)` files are correctly configured in the Django
     project ``settings.py`` file

     .. code-block:: python

        # settings.py
        STATIC_URL = '/static/'
        STATICFILES_DIRS = [BASE_DIR / 'static']

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents

.. seealso::

   :ref:`project-application-structure` section which explains the structure of
   a Django project.

.. code-block:: python
   :caption: Define views that render the template containing the buttons in
             views.py

   # myapp/views.py
   from django.shortcuts import render
   from django.views import View
   from .models import TitleButton

   class TitleButtonView(View):
       def get(self, request):
           my_models = TitleButton.objects.all()
           return render(request, 'myapp/myapp.html', {'title_button_def':
           my_models})

.. code-block:: python
   :caption: Configure URL routing to the view defined above in the urls.py

   # myapp/urls.py
   from django.urls import path
   from .views import TitleButtonView

   urlpatterns = [
       path('title-buttons/', TitleButtonView.as_view(), name='title_buttons'),
   ]

.. raw:: html

   <hr>

* In the template HTML file (``myapp.html``), reference each element from the
  TitleButton table.

.. collapse:: TitleButton example template

   .. literalinclude:: /assets/files/setup/profile/title-button.html
      :language: html

.. raw:: html

   <hr>

* Handle any JavaScript functionality needed for the buttons in the
  :abbr:`JS (JavaScript)` file (``myapp.js``)

.. collapse:: Title button example javascript

   .. literalinclude:: /assets/files/setup/profile/title-button.js
      :language: javascript

.. raw:: html

   <hr>

.. _visual-representation-title-button:

Visualisation of TitleButton in Project
----------------------------------------

.. figure:: /assets/images/django-admin-interface/profile/title-button/visualisation-title-button-work-profiles-web-page.png
   :alt: Visual representation of 'new component' title button on 'Work
         profiles' page
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/django-admin-interface/profile/title-button/visualisation-title-button-work-profiles-web-page.png
   :class: with-shadow with-border

   **Work profiles page: Visual representation of 'new component' title
   button**

* **new_component_template** button displays the tooltip *Add record* when
  hovered over. It is the |add-profile-button| button indicated by the blue
  arrow in the image above.

.. raw:: html

   <hr>

.. figure:: /assets/images/django-admin-interface/profile/title-button/visualisation-title-button-samples-web-page.png
   :alt: Visual representation of title buttons on Samples page
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/django-admin-interface/profile/title-button/visualisation-title-button-samples-web-page.png
   :class: with-shadow with-border

   **Visual representation of 'accept or reject samples',
   'download blank manifest', 'download SOP', 'new samples spreadsheet and
   'quick tour' title buttons on Samples page**

* **quick_tour_template** button displays the tooltip
  *Take a tour of this page* when hovered over. It is the |quick-tour-button|
  button indicated by the orange arrow in the image above.

* **new_samples_spreadsheet_template** button displays the tooltip
  *Add or update samples from spreadsheet* when hovered over. It is the
  |add-dtol-manifest-button| button indicated by the green arrow.

  The colour of the |add-dtol-manifest-button| button is based on the type of
  profile that you are making a submission to.

  See the :ref:`profile-types-legend` section regarding the colour code
  for the various types of project profiles on COPO.

* **download_blank_manifest_template** button displays the tooltip
  *Download blank manifest template* when hovered over. It is the
  |blank-manifest-download-button| button indicated by the brown arrow.

* **download_sop**: button displays the tooltip
  *Download Standard Operating Procedure (SOP)* when hovered over. It is the
  |sop-download-button| button indicated by the yellow arrow.

* **accept_reject_samples** button displays the tooltip *Accept or reject
  Tree of Life samples* when hovered over. It is the
  |accept-reject-samples-navigation-button| button indicated by the teal
  arrow and will only appear on the page if you are granted permission to be a
  sample manager.

.. raw:: html

   <hr>

Related Topics
--------------

.. seealso::

   * :ref:`Defining TitleButton Django model <django-model-definition>`
   * :ref:`Component structure <profile-setup-component>`
   * :ref:`ProfileType structure <profile-setup-profile-type>`
   * :ref:`RecordActionButton structure <profile-setup-record-action-button>`

.. raw:: html

   <hr>

..
    Images declaration
..

.. |accept-reject-samples-navigation-button| image:: /assets/images/samples/accept-reject-samples/buttons/samples-accept-reject-navigation-button.png
   :height: 3ex
   :class: no-scaled-link

.. |add-asg-manifest-button| image:: /assets/images/samples/asg/buttons/add-asg-manifest-button.png
   :height: 3ex
   :class: no-scaled-link

.. |add-dtol-manifest-button| image:: /assets/images/buttons/add-manifest-button.png
   :height: 3ex
   :class: no-scaled-link

.. |add-erga-manifest-button| image:: /assets/images/samples/erga/buttons/add-erga-manifest-button.png
   :height: 3ex
   :class: no-scaled-link

.. |add-profile-button| image:: /assets/images/buttons/add-button.png
   :height: 3ex
   :class: no-scaled-link

.. |add-reads-manifest-button| image:: /assets/images/buttons/add-manifest-button-for-biodata-profile.png
   :height: 3ex
   :class: no-scaled-link

.. |blank-manifest-download-button| image:: /assets/images/buttons/download-button-blank-manifest.png
   :height: 3ex
   :class: no-scaled-link

.. |collapsible-item-arrow| image:: /assets/images/icons/arrow-right.png
   :height: 2ex
   :class: no-scaled-link

.. |external-link-icon| image:: /assets/images/icons/external-link-icon.png
   :height: 2ex
   :width: 2ex
   :class: no-scaled-link

.. |quick-tour-button| image:: /assets/images/buttons/quick-tour-button.png
   :height: 3ex
   :class: no-scaled-link

.. |sop-download-button| image:: /assets/images/buttons/download-button-sop.png
   :height: 3ex
   :class: no-scaled-link

..
    Unicode declaration
..

.. |section| unicode:: U+1F4D6


..
    Link declaration
..

.. _copo-accept-reject-samples-page-link: https://copo-project.org/copo/dtol_submission/accept_reject_sample
.. _copo-django-admin-ui-image: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/django-admin-interface/profile/title-button/title-button-accept-reject-samples-django-admin-ui.png
