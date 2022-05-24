cfg = dict(
    model='pvlt_tiny',
    # pretrain_pth='/data/oss_bucket_0/PVLT-Data/preweights/pvt_tiny.pth',  # for training
    pretrain_pth='./preweights/pvt_v1/pvt_tiny.pth',    # for evaluation
    drop_path=0.1,
    clip_grad=None,
    # output_dir='/data/oss_bucket_0/PVLT-Data/pai_checkpoints/pai_pvlt_ft_48',  # for training
    output_dir='./checkpoints/pai_pvlt_ft_48',    # for evaluation
    data_set='FashionGen',
    mixup=0,
    cutmix=0,
    input_size=256,
    loss_type={'itm':0, 'cls':1, 'mlm':0, 'itg':0, 'i2t':0, 't2i':0, 'rtd':0, 'bartNSG': 0, 'bartMSS':0},
    batch_size=150,
    epochs=30,
    lr=2.5e-4,
    weight_decay=0.01,
    mask_ratio=0.50, # refer to Simple Masked Image Modeling
    mask_strategy='random_grid',
    mask_patch_size=16,
    word_mask_rate=0.15
)