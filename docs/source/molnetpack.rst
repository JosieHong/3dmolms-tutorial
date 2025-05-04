PyPI Package Installation and Usage
====================================

Using 3DMolMS through ``molnetpack`` requires minimal coding and is easy to use, but it does not support model training. If you want to train your own model, please refer to the :doc:`./sourcecode` page.

Installing from PyPI
-------------------

3DMolMS is available on PyPI as the package ``molnetpack``. You can install the latest version using ``pip``:

.. code-block:: bash

   pip install molnetpack

PyTorch must be installed separately. Check the `official PyTorch website <https://pytorch.org/get-started/locally/>`_ for the proper version for your system. For example:

.. code-block:: bash

   pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

Using ``molnetpack`` for Inference
----------------------------------

The sample input files, a CSV and an MGF, are located at ``./test/demo_input.csv`` and ``./test/demo_input.mgf``, respectively. It's important to note that during the data loading phase, any input formats that are not supported will be automatically excluded. Below is a table outlining the types of input data that are supported:

.. list-table::
   :header-rows: 1

   * - Item
     - Supported input
   * - Atom number
     - <=300
   * - Atom types
     - 'C', 'O', 'N', 'H', 'P', 'S', 'F', 'Cl', 'B', 'Br', 'I'
   * - Precursor types
     - '[M+H]+', '[M-H]-', '[M+H-H2O]+', '[M+Na]+', '[M+2H]2+'
   * - Collision energy
     - any number

To get started quickly, you can instantiate a MolNet and load a CSV or MGF file for MS/MS prediction as:

.. code-block:: python

   import torch
   from molnetpack import MolNet, plot_msms
   # Set the device to CPU for CPU-only usage:
   device = torch.device("cpu")
   # For GPU usage, set the device as follows (replace '0' with your desired GPU index):
   # gpu_index = 0
   # device = torch.device(f"cuda:{gpu_index}")
   # Instantiate a MolNet object
   molnet_engine = MolNet(device, seed=42) # The random seed can be any integer. 
   # Load input data (here we use a CSV file as an example)
   molnet_engine.load_data(path_to_test_data='./test/input_msms.csv')
   """Load data from the specified path.
   Args:
       path_to_test_data (str): Path to the test data file. Supported formats are 'csv', 'mgf', and 'pkl'.
   Returns:
       None
   """
   # Predict MS/MS
   pred_spectra_df = molnet_engine.pred_msms(instrument='qtof')
   """Predict MS/MS spectra.
   Args:
       path_to_results (Optional[str]): Path to save the prediction results. Supports '.mgf' or '.csv' formats. If None, the results won't be saved. 
       path_to_checkpoint (Optional[str]): Path to the model checkpoint. If None, the model will be downloaded from a default URL.
       instrument (str): Type of instrument used ('qtof' or 'orbitrap').
   Returns:
       pd.DataFrame: DataFrame containing the predicted MS/MS results.
   """

Plot Predicted MS/MS
--------------------

.. code-block:: python

   # Plot the predicted MS/MS with 3D molecular conformation
   plot_msms(pred_spectra_df, dir_to_img='./img/')

Below is an example of a predicted MS/MS spectrum plot.

.. figure:: https://github.com/JosieHong/3DMolMS/blob/main/img/demo_0.png
   :width: 600
   :align: center