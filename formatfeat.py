PLUGIN_NAME = 'Format Ft.'
PLUGIN_AUTHOR = 'Keno März'
PLUGIN_DESCRIPTION = 'Formats all featuring variants to "Ft." in title. Plays well with StandardiseFeat and FeatArtistInTitles.'
PLUGIN_VERSION = "1.0"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10", "0.15", "0.16", "2.0"]

from picard.metadata import register_album_metadata_processor, register_track_metadata_processor
from picard.plugin import PluginPriority
from picard import log

def format_feat(tagger, metadata, track, release):
	aliases = ['feat. ', 'Feat. ', 'featuring ', 'Featuring ', ' feat ', ' Feat ']
	for alias in aliases:
		title = metadata["title"]
		if alias in title:
			i = title.find(alias)
			feature = title[i + len (alias):].strip(' \t\n\r()')
			metadata["title"] = title[:i].rstrip(' \t\n\r()') + ' (Ft. '+ feature + ')'

register_track_metadata_processor(format_feat, priority=PluginPriority.LOW)