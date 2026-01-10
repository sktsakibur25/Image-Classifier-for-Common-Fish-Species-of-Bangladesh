from fastai import *
from fastai.vision.all import *
from fastai.vision.widgets import *
from fastai.data.core import DataLoaders
import matplotlib.pyplot as plt
version = 1.0
model_path = Path('models')

if __name__ == '__main__':
    # load the DataLoaders object saved earlier
    dls = torch.load(f'./dataloader_v{version}.pkl', weights_only=False)

    # recreate the Learner and load the saved weights
    learn = vision_learner(dls, resnet34, metrics=[error_rate, accuracy])
    learn.path = model_path
    learn.load(f'model_v_{version}')

    # Note: ImageClassifierCleaner requires an interactive environment (Jupyter notebook)
    # For terminal execution, you can use the following alternative approach:
    # Get predictions and identify misclassified images manually
    
    # Example: Get predictions on validation set
    preds, targets = learn.get_preds()
    pred_classes = preds.argmax(dim=1)
    
    # Find misclassified indices
    misclassified = (pred_classes != targets).nonzero(as_tuple=True)[0]
    
    print(f"Number of misclassified images: {len(misclassified)}")
    print("Misclassified image indices:", misclassified.tolist())