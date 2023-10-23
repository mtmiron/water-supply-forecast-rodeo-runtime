"""Code for downloading Nino Regions Sea Surface Temperature (SST) indices. Use the CLI to
download, for example:

    python -m wsfr_download nino_regions_sst

or use the `bulk` command to download many sources at once based on a config file.

    python -m wsfr_download bulk data_download/hindcast_test_config.yml

You can also import this module and use it as a library.

See the challenge website for more about this approved data source:
https://www.drivendata.org/competitions/254/reclamation-water-supply-forecast-dev/page/801/#ni%C3%B1o-regions-sea-surface-temperatures
"""

from loguru import logger
import requests

from wsfr_download.config import DATA_ROOT

SOURCE_URL = "https://www.cpc.ncep.noaa.gov/data/indices/sstoi.indices"
FILE_PATH_PARTS = ("teleconnections", "nino_regions_sst.txt")


def download_nino_regions_sst():
    """Download Nino Regions Sea Surface Temperatures (SST) data."""
    logger.info("Downloading Nino Regions SST data...")
    response = requests.get(SOURCE_URL)
    out_file = DATA_ROOT.joinpath(*FILE_PATH_PARTS)
    out_file.parent.mkdir(exist_ok=True, parents=True)
    with out_file.open("w") as fp:
        fp.write(response.text)
    logger.success(f"Nino Regions SST data written to {out_file}")
