import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from hottbox.core import Tensor


_DATA_HOME = os.path.join(os.path.dirname(__file__))

ETH80_HOME = os.path.join(_DATA_HOME, 'ETH80')

FILE_1 = os.path.join(_DATA_HOME, "file_1.csv")
FILE_2 = os.path.join(_DATA_HOME, "file_2.csv")


class ETH80(object):
    """ Class for interacting with images from the ETH-80 dataset.

    Attributes
    -------
    _META : pd.DataFrame
        Contains meta data of all images from the ETH-80 dataset in the columns: Label, Object, Angle_1, Angle_2, Path.
        Label - for classification, ranges between 1 and 8 including
        Object - there are 10 different objects that with the same Label
        Angle_1, Angle_2 - there are 41 combinations of these two variables for each object
        Path - location of the image which name follows patters: Object-Angle_1-Angle_2.png

    Note
    -------
    1.  More info about this dataset (eth80-cropped-close128.tgz) can be found on:
        https://www.mpi-inf.mpg.de/departments/computer-vision-and-multimodal-computing/research/object-recognition
        -and-scene-understanding/analyzing-appearance-and-contour-based-methods-for-object-categorization/

    2.  Car objects are ordered in different way
    """

    _objects_to_labels = {"apple": 1,
                          "car": 2,
                          "cow": 3,
                          "cup": 4,
                          "dog": 5,
                          "horse": 6,
                          "pear": 7,
                          "tomato": 8,
                          }

    def __init__(self) -> None:
        self._META = self._get_eth_meta()

    @staticmethod
    def _get_eth_meta():
        """ Read file with eth-80 meta data into pandas dataframe

        Returns
        -------
        df : pd.DataFrame
        """
        meta_data_path = os.path.join(ETH80_HOME, 'meta_data.csv')
        df = pd.read_csv(meta_data_path, dtype={'Angle_1': str, 'Angle_2': str, 'Label': 'int8'})
        df['id'] = df.apply(lambda x: '-'.join([x['Object'], x['Angle_1'], x['Angle_2']]), axis=1)
        return df

    @property
    def meta_data(self):
        """ Dataframe with meta data of all samples for the ETH-80 dataset.

        It is stored in the columns: Angle_1, Angle_2, Label, Object, id.
            Angle_1 (str), Angle_2 (str) - there are 41 combinations of these two variables for each object \n
            Label (np.int8) - for classification, ranges between 1 and 8 including \n
            Object (str) - there are 10 different objects that with the same Label \n
            id (str) - Unique name of the sample that follows pattern: Object-Angle_1-Angle_2

        Returns
        -------
        df : pd.DataFrame
        """
        return self._META

    @property
    def available_objects(self):
        return list(self._objects_to_labels.keys())

    @property
    def available_angle_pairs(self):
        return self.meta_data.groupby(["Angle_1", "Angle_2"]).size()

    def get_samples(self, objects, angle_1, angle_2, to_gray=False):
        """ Get numeric representation of images from the ETH-80 dataset

        Parameters
        ----------
        objects : list[str]
            List of objects of interest.
        angle_1 : list[str]
            List of angles of interest along longitude (from north to south).
        angle_2 : list[str]
            List of angles of interest along latitude (from west to east).
        to_gray : bool
            If True, convert to gray color representation.

        Returns
        -------
        samples : np.ndarray
            N-dimensional array of samples with dimensions representing
            n_samples, img_height, img_width and color respectively.
        """
        df = self.meta_data
        if len(angle_1) > 0:
            df = df[df.Angle_1.isin(angle_1)]

        if len(angle_2) > 0:
            df = df[df.Angle_2.isin(angle_2)]

        if len(objects) > 0:
            labels = [self._objects_to_labels[obj] for obj in objects]
            df = df[df.Label.isin(labels)]

        if df.empty:
            raise ValueError("Selected criteria are not present in this dataset. "
                             "Most likely, the specified pair(s) of `angle_1` and `angle_2` does not exist.")

        path = df.apply(lambda x: os.path.join(ETH80_HOME, "original", "{}.npz".format(x['id'])),
                        axis=1
                        )
        if to_gray:
            data_as_series = path.apply(lambda x: rgb_to_gray(np.load(x)['image']))
        else:
            data_as_series = path.apply(lambda x: np.load(x)['image'])

        samples = np.array(data_as_series.tolist(), dtype="float64")
        return samples


def rgb_to_gray(image):
    """ Convert to gray-scale """
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])


def get_image(item, view):
    """ Utility to get images of interest for assignment

    Parameters
    ----------
    item : str
    view : int

    Returns
    -------
    image : np.ndarray
    """
    if view == "side":
        item_properties = dict(angle_1=["090"], angle_2=["045"])
    elif view == "top":
        item_properties = dict(angle_1=["000"], angle_2=["000"])
    else:
        raise ValueError("Parameter 'view' should be equal either 'top' or 'side'")

    if item not in ["car", "apple"]:
        raise ValueError("Parameter 'item' should be either 'car' or 'apple'")

    item_properties.update(dict(objects=[item]))

    eth80 = ETH80()
    car_images = eth80.get_samples(**item_properties)
    image = car_images[0, :, :, :]
    return image


def plot_tensors(tensor, tensor_rec):
    """ Utility to tensor images

    Parameters
    ----------
    tensor : Tensor
    tensor_rec : Tensor
    """
    image = tensor_to_image(tensor)
    image_rec = tensor_to_image(tensor_rec)
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(1, 2, 1)
    ax.imshow(image)
    ax.set_axis_off()
    plt.title('Original Image')
    ax = fig.add_subplot(1, 2, 2)
    ax.imshow(image_rec)
    ax.set_axis_off()
    plt.title('Reconstructed Image')


def tensor_to_image(tensor):
    """ Convert a tensor into an image

    Parameters
    ----------
    tensor : Tensor

    Returns
    -------
    image : np.ndarray
    """
    image = tensor.data
    image -= tensor.data.min()
    image /= tensor.data.max()
    image *= 255
    return image.astype(np.uint8)
