# Image Classifier for Common Fish Species of Bangladesh

This project implements a deep learning-based image classifier to identify common fish species found in Bangladesh. The classifier uses a ResNet34 architecture trained on images of 20 different fish species using the FastAI library.

## Project Overview

The goal of this project is to create an accurate image classification model that can identify fish species from photographs. This can be useful for:
- Fisheries management and research
- Aquaculture applications
- Educational purposes
- Fish market identification
- Biodiversity monitoring

## Fish Species Covered

The classifier can identify the following 20 common fish species of Bangladesh:

| Local Name | Scientific Name | Local Name | Scientific Name |
|------------|-----------------|------------|-----------------|
| Rui | Labeo rohita | Koi | Anabas testudineus |
| Katla | Catla catla | Tilapia | Oreochromis niloticus |
| Mrigal | Cirrhinus cirrhosus | Pabda | Ompok pabda |
| Hilsa | Tenualosa ilisha | Shing | Heteropneustes fossilis |
| Magur | Clarias batrachus | Boal | Wallago attu |
| Pangas | Pangasius pangasius | Chitol | Chitala chitala |
| Bata | Labeo bata | Mola | Amblypharyngodon mola |
| Taki | Channa punctata | Shoal | Channa striata |
| Gajar | Channa marulius | Loitta | Harpadon nehereus |
| Kachki | Corica soborna | Baim | Mastacembelus armatus |

## Dataset

The dataset consists of images collected for each fish species. Images were scraped from the internet using Bing Image Search with scientific names as keywords. The dataset is organized into folders by local fish names.

### Dataset Structure
```
images/
├── Baim/
├── Bata/
├── Boal/
├── Chitol/
├── Gajar/
├── Hilsa/
├── Kachki/
├── Katla/
├── Koi/
├── Loitta/
├── Magur/
├── Mola/
├── Mrigal/
├── Pabda/
├── Pangas/
├── Rui/
├── Shing/
├── Shoal/
├── Taki/
└── Tilapia/
```

## Model Architecture

- **Framework**: FastAI (built on PyTorch)
- **Base Model**: ResNet34
- **Input Size**: 224x224 pixels (with random resized cropping)
- **Data Augmentation**: Random rotations, flips, brightness/contrast adjustments
- **Training Split**: 80% training, 20% validation
- **Batch Size**: 32

## Model Versions

- **model_v_1.0.pth**: Initial model version
- **model_v_2.0_resnet34.pth**: Improved version with better training

## Files Description

### Source Code (`src/` directory)
- `ImageScrapper.py`: Script to download images from Bing using scientific names
- `Loader.py`: Data loading and preprocessing pipeline
- `Trainer.py`: Model training script
- `Cleaner.py`: Script to identify misclassified images
- `Interpretation`: Model evaluation and confusion matrix generation
- `requirements.txt`: Python dependencies

### Models (`model/` directory)
- `model_v_1.0.pth`: First trained model
- `model_v_2.0_resnet34.pth`: Second trained model

## Installation and Setup

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r src/requirements.txt
   ```

## Usage

### Training a New Model
1. Run the image scraper (if needed):
   ```bash
   python src/ImageScrapper.py
   ```
2. Prepare the data:
   ```bash
   python src/Loader.py
   ```
3. Train the model:
   ```bash
   python src/Trainer.py
   ```

### Model Evaluation
Run the interpretation script to see confusion matrix and top losses:
```bash
python src/Interpretation
```

## Dependencies

Key libraries used:
- FastAI 2.8.6
- PyTorch
- Bing Image Downloader
- Matplotlib
- NumPy
- Pandas

See `src/requirements.txt` for complete list.

## Performance

The model achieves high accuracy on the validation set. Performance metrics include:
- Accuracy
- Error rate
- Confusion matrix analysis

## Future Improvements

- Increase dataset size with more diverse images
- Implement data cleaning pipeline
- Add more fish species
- Deploy as web application
- Mobile app integration
- Real-time classification

## License

This project is open source. Please cite appropriately if used for research.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## Acknowledgments

- Images sourced from Bing Image Search
- Built using FastAI library
- Inspired by the need for automated fish species identification in Bangladesh</content>
<parameter name="filePath">H:\Dokkho DS\Image Classifier for Common Fish Species of Bangladesh\README.md