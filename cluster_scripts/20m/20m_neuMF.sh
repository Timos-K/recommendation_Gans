#!/bin/sh
#SBATCH -N 1	  # nodes requested
#SBATCH -n 1	  # tasks requested
#SBATCH --partition=Short
#SBATCH --gres=gpu:1
#SBATCH --mem=12000  # memory in Mb
#SBATCH --time=0-02:59:59

export CUDA_HOME=/opt/cuda-9.0.176.1/

export CUDNN_HOME=/opt/cuDNN-7.0/

export STUDENT_ID=$(whoami)

export LD_LIBRARY_PATH=${CUDNN_HOME}/lib64:${CUDA_HOME}/lib64:$LD_LIBRARY_PATH

export LIBRARY_PATH=${CUDNN_HOME}/lib64:$LIBRARY_PATH

export CPATH=${CUDNN_HOME}/include:$CPATH

export PATH=${CUDA_HOME}/bin:${PATH}

export PYTHON_PATH=$PATH

mkdir -p /disk/scratch/${STUDENT_ID}

export TMPDIR=/disk/scratch/${STUDENT_ID}/

export TMP=/disk/scratch/${STUDENT_ID}/

mkdir -p ${TMP}/datasets/

export DATASET_DIR=${TMP}/datasets/

rsync -ua --progress /home/${STUDENT_ID}/recommendations/datasets/movielens/ /disk/scratch/${STUDENT_ID}/datasets/movielens

source /home/${STUDENT_ID}/miniconda3/bin/activate mlp

echo activated mlp.

cd /home/${STUDENT_ID}/recommendations/

echo "changed to recommendation folder. Calling python"

python3 neuMF_spotlight.py  --use_gpu "True" \
                            --mlp_embedding_dim 32 --mf_embedding_dim 20 --training_epochs 10 \
                            --learning_rate 1e-3 --l2_regularizer 5e-5  \
                            --batch_size 64 --dataset '20M' \
                            --k 3 \
                            --experiment_name "neuMF_model_20M" --on_cluster 'True'
