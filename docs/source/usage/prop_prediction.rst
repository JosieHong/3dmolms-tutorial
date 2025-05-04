Molecular Properties Prediction
============================

3DMolMS can be used to predict MS/MS-related properties, such as retention time (RT) and collision cross section (CCS). This guide shows how to train a model for RT prediction and CCS prediction, and how to transfer these models to your own RT and CCS dataset.

All models mentioned can be downloaded from `release v1.1.6 <https://github.com/JosieHong/3DMolMS/releases/tag/v1.1.6>`_.

Retention Time Prediction
-------------------------

Setup
~~~~~

Please set up the environment as shown in the :doc:`../sourcecode` page.

Data Preparation
~~~~~~~~~~~~~~~

Step 1: Download the retention time dataset, `METLIN <https://figshare.com/articles/dataset/The_METLIN_small_molecule_dataset_for_machine_learning-based_retention_time_prediction/8038913?file=18130625>`_. The structure of data directory is:

.. code-block:: text

   |- data
     |- origin
       |- SMRT_dataset.sdf

Preprocessing
~~~~~~~~~~~~

Step 2: Use the following commands to preprocess the datasets. The settings of datasets are in ``./src/molnetpack/config/preprocess_etkdgv3.yml``.

.. code-block:: bash

   python ./src/preprocess_oth.py --dataset metlin

Training
~~~~~~~

Step 3: Use the following commands to train the model. The settings of model and training are in ``./src/molnetpack/config/molnet_rt.yml``. If you'd like to train this model from the pre-trained model on MS/MS prediction, please download the pre-trained model from `Google Drive <https://drive.google.com/drive/folders/1fWx3d8vCPQi-U-obJ3kVL3XiRh75x5Ce?usp=drive_link>`_.

Learning from scratch:

.. code-block:: bash

   python ./src/train_rt.py --train_data ./data/metlin_etkdgv3_train.pkl \
   --test_data ./data/metlin_etkdgv3_test.pkl \
   --model_config_path ./src/molnetpack/config/molnet_rt.yml \
   --data_config_path ./src/molnetpack/config/preprocess_etkdgv3.yml \
   --checkpoint_path ./check_point/molnet_rt_etkdgv3.pt

Learning from pretrained model:

.. code-block:: bash

   python ./src/train_rt.py --train_data ./data/metlin_etkdgv3_train.pkl \
   --test_data ./data/metlin_etkdgv3_test.pkl \
   --model_config_path ./src/molnetpack/config/molnet_rt.yml \
   --data_config_path ./src/molnetpack/config/preprocess_etkdgv3.yml \
   --checkpoint_path ./check_point/molnet_rt_etkdgv3_tl.pt \
   --transfer \
   --resume_path ./check_point/molnet_qtof_etkdgv3.pt

Cross-Collision Section Prediction
---------------------------------

Setup
~~~~~

Please set up the environment as shown in the :doc:`../sourcecode` page.

Data Preparation
~~~~~~~~~~~~~~~

Step 1: Download the cross-collision section dataset, `AllCCS <http://allccs.zhulab.cn/>`_, manually or using ``download_allccs.py``:

.. code-block:: bash

   python ./src/download_allccs.py --user <user_name> --passw <passwords> --output ./data/origin/allccs_download.csv

The structure of data directory is:

.. code-block:: text

   |- data
     |- origin
       |- allccs_download.csv

Preprocessing
~~~~~~~~~~~~

Step 2: Use the following commands to preprocess the datasets. The settings of datasets are in ``./src/molnetpack/config/preprocess_etkdgv3.yml``.

.. code-block:: bash

   python ./src/preprocess_oth.py --dataset allccs --data_config_path ./