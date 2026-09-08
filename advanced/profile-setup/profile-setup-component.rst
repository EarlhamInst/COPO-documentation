.. _profile-setup-component:

Component
~~~~~~~~~

Components [#f1]_ are individual elements or modules that make up the profile.
These can include various functionalities or data points that contribute to
the profile's overall purpose.

.. raw:: html

   <hr>

Component Database Table Structure
-----------------------------------

Each component that make up a profile has specific settings and
functionalities that contribute to the profile's overall purpose.

The PostgresSQL table **Component** consists of the following fields:

* ``id`` (Integer): The unique identifier for the component
* ``name`` (String): The name of the component
* ``title`` (String): The display title of the component
* ``widget_icon`` (String): The icon associated with the component
* ``widget_colour`` (String): The colour associated with the component, used
  for UI elements
* ``widget_icon_class`` (String): The :abbr:`CSS (Cascading Style Sheets)`
  class for the icon
* ``table_id`` (String): The identifier for the associated table
* ``reverse_url`` (String): The URL used for reversing the component
* ``subtitle`` (String): The subtitle of the component, providing additional
  context
* ``button_label`` (String): The label for the button associated with the
  component.
* ``schema_name`` (String): The name of the schema associated with the
  component, if applicable
* ``base_component`` (String): The base component that the current component
  is derived from, if applicable.

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents

.. collapse:: Component database fields

   .. code-block:: console

       id |         name         | title                   | widget_icon      | widget_colour | widget_icon_class   | table_id                  | reverse_url                                               | subtitle            | button_label           | schema_name         | base_component
      ----+----------------------+-------------------------+------------------+---------------+---------------------+---------------------------+-----------------------------------------------------------+---------------------+------------------------+---------------------+---------------
        1 | accessions           | Accessions              | sitemap          | pink          | fa fa-sitemap       | accessions_table          | copo_accession:copo_accessions                            |                     | View Accessions        |                     |
        2 | accessions_schema    | Accessions              | sitemap          | pink          | fa fa-sitemap       | accessions_schema_table   | copo_accessions_schema:copo_accessions_schema             | #component_subtitle | View Accessions        |                     |
        3 | assembly             | Assembly                | puzzle piece     | violet        | fa fa-puzzle-piece  | assembly_table            | copo_assembly_submission:copo_assembly                    |                     |                        |                     |
        4 | files                | Data files              | file             | blue          | fa fa-file          | files_table               | copo_file:copo_files                                      |                     |                        |                     |
        5 | general_sample       | Samples                 | filter           | olive         | fa fa-filter        | sample_table              | copo_sample:copo_general_samples                          | #component_subtitle | Manage Sample metadata |                     |
        6 | images_rembi         | General                 | image            | coral-pink    | fa fa-image         | singlecell_table          | copo_single_cell_submission:copo_singlecell               | #component_subtitle |                        | COPO_IMAGE_REMBI    | singlecell
        7 | images_stx_fish      | Spatial Transcriptomics | image            | terra-cotta   | fa fa-image         | singlecell_table          | copo_single_cell_submission:copo_singlecell               | #component_subtitle |                        | COPO_IMAGE_STX_FISH | singlecell
        8 | profile              | Work profiles           |                  |               |                     | copo_profiles_table       |                                                           | #component_subtitle |                        |                     |
        9 | read                 | Reads                   | dna              | orange        | fa fa-dna           | read_table                | copo_read_submission:copo_reads                           | #component_subtitle |                        |                     |
       10 | reads_schema         | Reads                   | dna              | orange        | fa fa-dna           | singlecell_table          | copo_single_cell_submission:copo_singlecell               | #component_subtitle |                        | COPO_READ           | singlecell
       11 | sample               | Samples                 | filter           | olive         | fa fa-filter        | sample_table              | copo_sample:copo_samples                                  |                     | Manage Sample metadata |                     |
       12 | seqannotation        | Sequence annotations    | tag              | yellow        | fa fa-tag           | seqannotation_table       | copo_seq_annotation_submission:copo_seq_annotation        |                     |                        |                     |
       13 | singlecell           | Single-cell             | bacterium        | green         | fa fa-bacterium     | singlecell_table          | copo_single_cell_submission:copo_singlecell               | #component_subtitle |                        | COPO_SINGLE_CELL    |
       14 | taggedseq            | Barcoding manifests     | barcode          | red           | fa fa-barcode       | tagged_seq_table          | copo_barcoding_submission:copo_taggedseq                  | #component_subtitle |                        |                     |

.. raw:: html

   <br><br>

.. collapse:: Description of each Component record

   .. raw:: html

      <br>

   * **accessions** and **accessions_dashboard**:

         Both relate to the accessions component. The accessions component
         provides a platform for retrieving and analysing biological samples
         that have biosample accession, SRA accession and submission
         accession associated with them as part of a project after the samples
         have been accepted.

   * **assembly**: Assembly component

         The assembly component provides a platform for aligning and merging
         fragments of a Deoxyribonucleic acid (DNA) sequence to reconstruct
         the original structure of the DNA.

   * **files**: Data files component
         With this component, data files can be uploaded from a cluster or from
         one's local (computer) system.

   * **images_rembi**: General images component
         Images based on Recommended Metadata for Biological
         Images (REMBI) standard can be uploaded using this component.

   * **images_stx_fish**: Spatial Transcriptomics images component
         Spatial Transcriptomics images can be uploaded via this component.

   * **profile**: Work profiles component
         The first step to getting work done in COPO is to create a work
         profile. A profile is a collection of 'research objects' or
         components that form part of one's research project or study.

   * **read** and **reads_schema**: Reads component

         This component is associated with assembled and annotated sequences
         representing interesting features or gene regions.

   * **sample** and **general_sample**: Samples component

         Biological samples, obtained as part of a project, are described and
         managed in this component.

   * **seqannotation**: Sequence Annotations component

         Specific features, in this component, are marked in a Deoxyribonucleic
         acid (DNA), Ribonucleic acid (RNA) or protein sequence with
         descriptive information about structure or function. Sequence
         annotations are usually done after a genome is sequenced and
         assembled.

   * **singlecell**: Single-cell component

         Single-cell data can be managed using this component.

   * **taggedseq**: Barcoding Manifests component

         This component provides a platform for submitting assembled and
         annotated sequences representing interesting features or gene regions.

.. raw:: html

   <hr>

.. _profile-setup-component-creation:

Creation of Component
----------------------

.. note::

   * This section assumes that you have installed Django, Python and created a
     Django project.

   * The migrations folder is automatically created within your app directory
     when you create your app. It contains database migration files.

.. seealso::

   * :ref:`Django application structure <project-application-structure>`  for
     an snapshot of Django application's structure

To create a component in the project, a Django application has to be created
for the component. Then, the component has to be associated with a profile
type defined in the `ProfileType structure <profile-setup-profile-type>`_
section. This association will allow the component to be accessible and
visible on the **Work profiles** page.

Explore the implementation details of each component of the Django application
used in the COPO project through the links provided below:

* `Accessions component Django application \
  <copo-github-accession-app_>`__ |external-link-icon|

* `Assembly component Django application \
  <copo-github-assembly-app_>`__ |external-link-icon|

* `Barcoding component Django application \
  <copo-github-barcoding-app_>`__ |external-link-icon|

* `Data files component Django application \
  <copo-github-files-app_>`__ |external-link-icon|

* `Reads component Django application \
  <copo-github-reads-app_>`__ |external-link-icon|

* `Samples component Django application \
  <copo-github-samples-app_>`__ |external-link-icon|

* `Sequence annotations component Django application \
  <copo-github-sequence-annotation-app_>`__ |external-link-icon|

Other Django applications created in the COPO project can be found in the
``src/apps`` folder of the `COPO GitHub repository <copo-github-apps_>`__.

.. raw:: html

   <hr>

.. code-block:: bash
   :caption: Navigate to the project directory

   cd <path-to-project>/COPO-production

.. code-block:: bash
   :caption: Create a new Django application using the startapp command

   python manage.py startapp myapp

.. code-block:: python
   :caption: Register app by adding it to the INSTALLED_APPS list in
             myproject/settings.py

   INSTALLED_APPS = [
        # ... other installed apps,
        'myapp',
   ]

.. code-block:: bash
   :caption: Create a static folder inside the app directory to store static
             files like CSS, JavaScript and images:

    mkdir myapp/static

.. code-block:: bash
   :caption: Create a css folder inside the static folder in the app directory
             to store  CSS files

   mkdir myapp/static/myapp/css
   cd myapp/static/myapp/css
   touch myapp.css

.. code-block:: bash
   :caption: Create a JavaScript (js) folder inside the static folder in the
             app directory to store JavaScript files

   mkdir myapp/static/myapp/js
   cd myapp/static/myapp/js
   touch myapp.js

.. code-block:: bash
   :caption: Create a templates folder inside the app directory to store HTML
             templates

   mkdir -p myapp/templates/myapp

.. code-block:: python
   :caption: Set up the configuration of the app in the an apps.py file inside
             the app directory

   from django.apps import AppConfig

   class MyappConfig(AppConfig):
       default_auto_field = 'django.db.models.BigAutoField'
       name = 'myapp'


.. code-block:: python
   :caption: Define URL routes in the urls.py file inside the app directory

   from django.urls import path
   from . import views

   urlpatterns = [
      path('', views.index, name='index')
   ]

.. code-block:: python
   :caption: Define view functions in the views.py file inside the app
             directory

   from django.shortcuts import render
   from .models import ProfileType, Component

   def index(request):
       profile_type_models = ProfileType.objects.all()
       component_models = Component.objects.all()

       return render(request, 'myapp/index.html', {'profile_type_def':
       profile_type_models, 'component_def': component_models})

.. raw:: html

   <hr>

* Create an ``component.html`` file inside myapp/templates/myapp:

.. collapse:: Component example template

   .. literalinclude:: /assets/files/setup/profile/component.html
      :language: html

.. raw:: html

   <hr>

Create the following files in the application directory:

* ``admin.py`` - to register models with the Django admin site. See the
  :ref:`Registering Django models <profile-setup-register-django-model>`
  section for more information.

* ``models.py`` - to define database models. See the :ref:`Defining Django
  models <django-model-definition>` section    for more information.

* ``tests.py`` - to write tests for the Django application.

.. raw:: html

   <hr>

.. _visual-representation-component:

Visualisation of Created Component
-----------------------------------

.. grid::
   :gutter: 2

   .. grid-item::
      :columns: 6

      .. figure:: /assets/images/django-admin-interface/profile/component/visualisation-component-button-tol-profile-components.png
         :alt: Viewing components associated with a Tree of Life (ToL) profile
               on the 'Work profiles' page
         :align: center
         :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/django-admin-interface/profile/component/visualisation-component-button-tol-profile-components.png
         :class: with-shadow with-border

         **Tree of Life (ToL) profile** [#f2]_

   .. grid-item::
      :columns: 6

      .. figure:: /assets/images/django-admin-interface/profile/component/visualisation-component-button-biodata-profile-components.png
         :alt: Viewing components associated with a Biodata profile
               on the 'Work profiles' page
         :align: center
         :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/django-admin-interface/profile/component/visualisation-component-button-biodata-profile-components.png
         :class: with-shadow with-border
         :height: 270px

         **Biodata profile** [#f3]_

.. raw:: html

   <br>

.. grid::
   :gutter: 2

   .. grid-item::
      :columns: 6

      * |files-component-button|
      * |samples-component-button|
      * |reads-component-button|
      * |assembly-component-button|
      * |sequence-annotations-component-button|
      * |barcoding-manifest-component-button|
      * |accessions-component-button|

      **Components that make up Tree of Life (ToL) profiles**

   .. grid-item::
      :columns: 6

      * |files-component-button|
      * |samples-component-button|
      * |reads-component-button|
      * |single-cell-component-button|
      * |accessions-component-button|
      * |images-component-button|

      **Components that make up Biodata profiles**

Each profile will have a set of components that are associated with it. These
components will be displayed on a profile on the **Work profiles** page.

Components will also appear to the top-right of pages for easy navigation to
them, depending on the component that is being viewed. For example,the
**Reads** component leads to the **Reads** page and the other components are
displayed as indicated by the arrows in the image below:

.. figure:: /assets/images/django-admin-interface/profile/component/visualisation-component-button-on-specific-web-page.png
   :alt: Profile types page
   :align: center
   :target: https://raw.githubusercontent.com/EarlhamInst/COPO-documentation/main/assets/images/django-admin-interface/profile/component/visualisation-component-button-on-specific-web-page.png
   :class: with-shadow with-border
   :height: 300px

   **Reads page: Other components are displayed at the top-right of the screen
   and can be clicked for easy navigation**

If the current page is not the **Reads** page, the **Reads** component icon,
|reads-icon|, will be displayed in the navigation pane.

.. raw:: html

   <hr>

Related Topics
--------------

.. seealso::

   * :ref:`Defining Component Django model <django-model-definition>`
   * :ref:`ProfileType structure <profile-setup-profile-type>`
   * :ref:`RecordActionButton structure <profile-setup-record-action-button>`
   * :ref:`TitleButton structure <profile-setup-title-button>`

   * :ref:`biodata-profile-components`
   * :ref:`tol-profile-components`
   * :ref:`accessions`

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Also known as profile component. See term: :term:`Profile component`.

         Research objects refer to files, reads, assemblies, samples,
         barcodes (also known as targeted sequences in European Nucleotide
         Archive (ENA)) and sequence annotations.

         Both Tree of Life (ToL) profile and Biodata profile are considered as
         *project* or *study* research objects.

.. [#f2] See term: :term:`Tree of Life profile <ToL profile>`.
.. [#f3] See term: :term:`Biodata profile`.

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/arrow-right.png
   :height: 2ex
   :class: no-scaled-link

.. |accessions-component-button| image:: /assets/images/accessions/buttons/components-accessions-button.png
   :height: 4ex
   :class: no-scaled-link

.. |assembly-component-button| image:: /assets/images/assemblies/buttons/components-assembly-button.png
   :height: 4ex
   :class: no-scaled-link

.. |barcoding-manifest-component-button| image:: /assets/images/barcoding/buttons/components-barcoding-manifest-button.png
   :height: 5ex
   :class: no-scaled-link

.. |external-link-icon| image:: /assets/images/icons/external-link-icon.png
   :height: 2ex
   :width: 2ex
   :class: no-scaled-link

.. |files-component-button| image:: /assets/images/files/buttons/components-files-button.png
   :height: 4ex
   :class: no-scaled-link

.. |images-component-button| image:: /assets/images/images-comp/buttons/components-images-button.png
   :height: 4ex
   :class: no-scaled-link

.. |reads-component-button| image:: /assets/images/reads/buttons/components-reads-button.png
   :height: 4ex
   :class: no-scaled-link

.. |reads-icon| image:: /assets/images/reads/icons/reads-icon.png
   :height: 3ex
   :class: no-scaled-link

.. |samples-component-button| image:: /assets/images/samples/buttons/components-samples-button.png
   :height: 5.5ex
   :class: no-scaled-link

.. |sequence-annotations-component-button| image:: /assets/images/sequence-annotations/buttons/components-sequence-annotations-button.png
   :height: 5ex
   :class: no-scaled-link

.. |single-cell-component-button| image:: /assets/images/single-cell/buttons/components-single-cell-button.png
   :height: 4ex
   :class: no-scaled-link

..
    Unicode declaration
..

.. |section| unicode:: U+1F4D6

..
    Link declaration
..

.. _copo-github-accession-app: https://github.com/EarlhamInst/COPO-production/tree/main/src/apps/copo_accession
.. _copo-github-assembly-app: https://github.com/EarlhamInst/COPO-production/tree/main/src/apps/copo_assembly_submission
.. _copo-github-barcoding-app: https://github.com/EarlhamInst/COPO-production/tree/main/src/apps/copo_barcoding_submission
.. _copo-github-files-app: https://github.com/EarlhamInst/COPO-production/tree/main/src/apps/copo_file
.. _copo-github-reads-app: https://github.com/EarlhamInst/COPO-production/tree/main/src/apps/copo_read_submission
.. _copo-github-samples-app: https://github.com/EarlhamInst/COPO-production/tree/main/src/apps/copo_sample
.. _copo-github-sequence-annotation-app: https://github.com/EarlhamInst/COPO-production/tree/main/src/apps/copo_seq_annotation_submission
.. _copo-github-apps: https://github.com/EarlhamInst/COPO-production/tree/main/src/apps
