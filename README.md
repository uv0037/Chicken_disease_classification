# Chicken Disease Classification

## Overview

This project demonstrates a complete end-to-end data science lifecycle for computer vision-based chicken disease classification using deep learning. It showcases my capabilities in structuring robust, reproducible ML solutions, emphasizing modularity, best practices, and automation.

## Key Concepts & Data Science Lifecycle

### 1. Problem Definition

- **Goal:** Automatically classify chicken diseases from images using a Convolutional Neural Network (CNN).
- **Motivation:** Early and accurate disease detection can reduce poultry losses and improve farm productivity.

### 2. Data Ingestion

- **Automated Data Download & Extraction:** The pipeline fetches raw image data from a specified URL, stores it locally, and unzips it in an organized directory structure.
- **Artifacts Creation:** All intermediate and final outputs are tracked in versioned artifact folders for reproducibility.

### 3. Data Preprocessing (Implied in Pipeline)

- While explicit preprocessing scripts are not shown, the modular pipeline easily accommodates data cleaning, augmentation, and transformation steps.

### 4. Model Preparation

- **Base Model Selection:** Utilizes transfer learning with VGG16, a proven deep CNN architecture.
- **Customizations:** Configurable image size, learning rate, weight initialization, and trainable layers.
- **Parameterization:** All model hyperparameters are externalized in `params.yaml` for easy experimentation.

### 5. Callbacks & Training Utilities

- **TensorBoard Logging:** Automated directory creation for TensorBoard logs to visualize training metrics.
- **Model Checkpointing:** Saves the best model during training, ensuring recoverability and optimal performance.

### 6. Training Pipeline

- **Modular Training:** The pipeline trains the CNN model using the prepared data and callbacks.
- **Configuration Management:** Keeps all stages decoupled and maintainable via configuration managers and dataclasses.

### 7. Evaluation

- **Automated Evaluation:** The pipeline supports post-training evaluation for model metrics and validation.

### 8. Pipeline Orchestration

- **Main Pipeline:** `main.py` orchestrates all stages - ingestion, model preparation, training, and evaluation - with robust logging and error handling.
- **Scalable Design:** Easily extendable for more stages or different ML problems.

### 9. Configuration & Experiment Tracking

- **Config Files:** All settings, secrets, and parameters are maintained in YAML files (`config.yaml`, `params.yaml`, `secrets.yaml`).
- **DVC Integration:** Ready for DVC (Data Version Control) to track experiments and data lineage.

### 10. Packaging & Reusability

- **Python Package Structure:** Designed as a proper package (`cnnClassifier`), ready for deployment or sharing.
- **Setup Script:** Includes `setup.py` for easy installation and distribution.

### 11. Cloud & Docker Readiness

- **Registry URI Provided:** Docker image can be pushed to ECR (Amazon Elastic Container Registry) for cloud deployment:
  ```
  367377929761.dkr.ecr.ap-south-1.amazonaws.com/chicken
  ```

## Project Structure

```
├── research/           # Jupyter notebooks for each pipeline stage
│   ├── 01_data_ingestion.ipynb
│   ├── 02_prepare_base_model.ipynb
│   ├── 03_prepare_callbacks.ipynb
│   └── 04_training.ipynb
├── src/                # Reusable Python modules (cnnClassifier)
├── config/             # YAML configuration files
├── artifacts/          # Output folders for models, logs, etc.
├── main.py             # Pipeline orchestrator
├── setup.py            # Package installation
├── DVC.yaml            # (Optional) Data versioning
└── README.md           # Project documentation
```

## How to Run

1. Update `config.yaml`, `params.yaml`, and `secrets.yaml` as needed.
2. (Optional) Use DVC for data and experiment tracking.
3. Run the pipeline:
    ```bash
    python main.py
    ```
4. Monitor training with TensorBoard.
5. Package and deploy the model using Docker/ECR.

## My Capabilities Demonstrated

- End-to-end ML pipeline automation
- Transfer learning and CNN implementation
- Modular code and configuration management
- Experiment tracking and reproducibility
- Model evaluation and logging
- Python packaging and cloud readiness

---

**Contact:** [Yuvraj Ajitgavhane](mailto:yuvrajajitgavhane@gmail.com)