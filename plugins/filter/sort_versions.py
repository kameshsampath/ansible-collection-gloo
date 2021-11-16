import sys
from distutils.version import StrictVersion, LooseVersion


def filter_sort_versions(releases):
    filtered_releases = list(filter(
        lambda release_string: len(release_string) > 0 and StrictVersion.version_re.match(
            release_string[1:]) is not None,
        releases))
    return sorted(filtered_releases, key=LooseVersion, reverse=True)


class FilterModule(object):
    filter_sort = {
        'sort_versions': filter_sort_versions,
    }

    def filters(self):
        return self.filter_sort
