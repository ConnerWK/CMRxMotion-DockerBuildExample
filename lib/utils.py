from torch import nn


def load_model_weights(model_weights_dir: str) -> nn.Module:
    """Function to load model weights in dedicated directory

    Args:
        model_weights_dir (str): folder directory of your pretrained models

    Returns:
        nn.Module: model with pretrained weights
    """
    ## functions are not real python functions, but are examples.
    ## write your code here. Load weights and map to gpu:0
    model = build_model(model_weights_dir)

    return model


def inference(model: nn.Module, data_folder_dir: str) -> list:
    """inference function

    Args:
        model (nn.Module): trained model
        data_folder_dir (str): directory of input images

    Returns:
        list: predictions of you model
    """
    ## functions are not real python functions, but are examples.
    predictions = predict(model, data_folder_dir)

    return predictions


def write_outputs(outputs: list, out_dir: str):
    """write predictions

    Args:
        outputs (list): predictions
        out_dir (str): directory to save your predictions
    """
    ## Read in your trained model
    
    save_niigz_files(outputs, out_dir)
