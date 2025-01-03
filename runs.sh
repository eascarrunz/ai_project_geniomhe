#!/usr/bin/env bash
NEPOCHS=

python3 train.py --dset_id -1 --task binary --attentiontype colrow --epochs 200 --pretrain --run_name run1 &> run1.log
python3 train.py --dset_id -1 --task binary --attentiontype col --epochs 200 --pretrain --run_name run2 &> run2.log
python3 train.py --dset_id -1 --task binary --attentiontype colrow --epochs 200 --run_name run3 &> run3.log
python3 train.py --dset_id -1 --task binary --attentiontype col --epochs 200 --run_name run4 &> run4.log
