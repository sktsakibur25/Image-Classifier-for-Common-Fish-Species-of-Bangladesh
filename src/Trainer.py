
from fastai import *
from fastai.vision.all import *
from fastai.vision.widgets import *
from fastai.data.core import DataLoaders
import matplotlib.pyplot as plt

version = 2.0
bs = 32
model_path = Path('models')
model_path.mkdir(parents=True, exist_ok=True)

if __name__ == '__main__':
    # Allow fastai DataLoaders to be loaded with weights_only=True in PyTorch 2.6+
    torch.serialization.add_safe_globals([DataLoaders])
    dls = torch.load(f'../model/dataloader_v{version}.pkl', weights_only=False)
    print("Data loaded successfully!")
    # print("Displaying batch...")
    # dls.valid.show_batch(max_n=8, nrows=2)
    # plt.show()
    # print("Complete!")

    model = vision_learner(dls, resnet34, metrics=[error_rate, accuracy])
    model.path = model_path
    # model = model.load(f'model_v_{version}', path=model_path)
    model.fine_tune(5)
    # model.save(f'model_v_{version}_resnet34', with_opt=False)
    model.export(fname=f'model_v{version}_resnet34.pkl')
    print("Model created successfully!")
