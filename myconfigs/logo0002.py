# The new config inherits a base config to highlight the necessary modification
_base_ = '../configs/faster_rcnn/faster_rcnn_r101_fpn_1x_logo.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=50),
       ))

optimizer = dict(type='SGD', lr=0.00125, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[16, 22])
runner = dict(type='EpochBasedRunner', max_epochs=24)


# Modify dataset related settings



# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = '../checkpoints/resnet101-5d3b4d8f.pth'