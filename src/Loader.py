from fastai import *
from fastai.vision.all import *
from fastai.vision.widgets import *
import matplotlib.pyplot as plt

version = 2.0
bs = 32
model_path = Path('models')
model_path.mkdir(parents=True, exist_ok=True)

dbBlock = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=RandomResizedCrop(224, min_scale=0.5),
    batch_tfms=aug_transforms()
)

print("Loading data...")
dls = dbBlock.dataloaders(Path('images'), bs=bs)
print("Data loaded successfully!")
torch.save(dls, f'dataloader_v{version}.pkl')
# dls = torch.load(f'dataloader_v{version}.pkl')

print("Displaying batch...")
# dls.train.show_batch(max_n=8, nrows=2)
dls.valid.show_batch(max_n=8, nrows=2)
plt.show()
print("Complete!")
