@echo off

SET "PRETRAINED_MODELS_PATH=%CD%\pretrained_models"
wget https://huggingface.co/GLIPModel/GLIP/resolve/main/glip_large_model.pth
wget  "%CD%\pretrained_models\GLIP\configs" "https://raw.githubusercontent.com/microsoft/GLIP/main/configs/pretrain/glip_Swin_L.yaml"
gdown "https://drive.google.com/u/0/uc?id=1bv6_pZOsXW53EhlwU0ZgSk03uzFI61pN" "-O" "%PRETRAINED_MODELS_PATH%\xvlm\retrieval_mscoco_checkpoint_9.pth"
gdown "https://drive.google.com/uc?id=1Cb1azBdcdbm0pRMFs-tupKxILTCXlB4O" "-O" "%PRETRAINED_MODELS_PATH%\TCL\TCL_4M.pth"
mkdir "%PRETRAINED_MODELS_PATH%\saliency_inspyrenet_plus_ultra"
gdown "https://drive.google.com/uc?id=13oBl5MTVcWER3YU4fSxW3ATlVfueFQPY" "-O" "%PRETRAINED_MODELS_PATH%\saliency_inspyrenet_plus_ultra\latest.pth"