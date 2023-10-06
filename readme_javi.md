#TRAIN
#Num epochs at final config file .py
python tools/train.py configs/solov2/solov2_r50_fpn_8gpu_1x.py

#TEST.PY
#For view results in folder
python tools/test_ins_vis.py configs/solov2/solov2_r50_fpn_8gpu_1x.py work_dirs/solov2_release_r50_fpn_8gpu_1x/epoch_500.pth --show --save_dir  work_dirs/vis_solo
