# Environment setup

The Conda environment provided in the original SAINT repository cannot be effectively recreated in 2024-12 due to version conflicts. I was able to create a new Conda environment that works, but the solution is *dirty*. I install most dependencies with Conda, but I had to install Pytorch and friends through Pip.

Note that this project requires **Python 3.8.1**, which was not specified in the yml file of the original repository.

1. Clone the repository.
2. Create a new conda environment based on `new_environment.yml`:
    ```sh
    conda env create -f new_environment.yml
    ```
    The environment created thus is called "mysaint"
3. Activate the conda environment:
    ```sh
    conda activate mysaint
    ```
4. Install Pytorch and friends through Pip:
    ```
    pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html
    ```
5. You're done!

Adjustments may be necessary if you don't have a compatible Nvidia graphics card.
