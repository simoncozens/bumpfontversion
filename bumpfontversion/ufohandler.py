import ufoLib2
import logging
from bumpversion.version_part import Version, VersionPart

logger = logging.getLogger(__name__)


class UFOHandler:
    def applies_to(self, file):
        return file.endswith(".ufo")

    def current_version(self, file):
        font = ufoLib2.objects.Font.open(file)
        return Version(
            {
                "major": VersionPart(str(font.info.versionMajor or 0)),
                "minor": VersionPart(str(font.info.versionMinor or 0)),
            }
        )

    def set_version(self, file, new_version):
        def pad_num(num, amount):
            return str(num).zfill(amount)

        font = ufoLib2.objects.Font.open(file)
        info = font.info

        current_version = f"{info.versionMajor}.{pad_num(info.versionMinor, 3)}"

        info.versionMajor = int(new_version["major"].value)
        info.versionMinor = int(new_version["minor"].value)

        new_version = f"{info.versionMajor}.{pad_num(info.versionMinor, 3)}"

        # Set OpenType names
        for attr in dir(info):
            if "openTypeName" not in attr or "_" in attr:
                continue
            current_string = getattr(info, attr)
            if not current_string:
                continue
            new_string = current_string.replace(current_version, new_version)
            setattr(info, attr, new_string)

        logger.info(f"Saving file {file}")
        font.save(file, overwrite=True)
