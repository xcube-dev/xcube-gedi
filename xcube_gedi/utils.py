from typing import Sequence

import geopandas as gpd
from shapely.geometry import box
from xcube.core.store import DataStoreError, DATASET_TYPE, DataTypeLike


def convert_bbox_to_geodf(bbox: Sequence[float]) -> gpd.GeoDataFrame | None:
    if len(bbox) == 0:
        return None
    geom = box(*bbox)
    return gpd.GeoDataFrame({"geometry": [geom]})


def assert_valid_data_type(data_type: DataTypeLike):
    """Auxiliary function to assert if data type is supported
    by the store.

    Args:
        data_type: Data type that is to be checked.

    Raises:
        DataStoreError: Error, if *data_type* is not
            supported by the store.
    """
    if not is_valid_data_type(data_type):
        raise DataStoreError(
            f"Data type must be {DATASET_TYPE.alias!r} or but got {data_type!r}."
        )


def is_valid_data_type(data_type: DataTypeLike) -> bool:
    """Auxiliary function to check if data type is supported
    by the store.

    Args:
        data_type: Data type that is to be checked.

    Returns:
        True if *data_type* is supported by the store, otherwise False
    """
    return data_type is None or DATASET_TYPE.is_super_type_of(data_type)
