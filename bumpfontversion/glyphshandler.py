import openstep_plist
# Using this instead of glyphslib gives us v2 and v2 compatiblity without
# faffing around

import logging
from bumpversion.version_part import Version, VersionPart

logger = logging.getLogger(__name__)


class GlyphsHandler:
    def applies_to(self, file):
        return file.endswith(".glyphs")

    def current_version(self, file):
        with open(file, "r", encoding="utf-8") as fp:
            font = openstep_plist.load(fp, use_numbers=True)
        return Version(
            {
                "major": VersionPart(str(font["versionMajor"] or 0)),
                "minor": VersionPart(str(font["versionMinor"] or 0)),
            }
        )

    def set_version(self, file, new_version):
        with open(file, "r", encoding="utf-8") as fp:
            font = openstep_plist.load(fp, use_numbers=True)
        font["versionMajor"] = int(new_version["major"].value)
        font["versionMinor"] = int(new_version["minor"].value)
        logger.info(f"Saving file {file}")
        with open(file, "w", encoding="utf-8") as fp:
            openstep_plist.dump(font, fp)
