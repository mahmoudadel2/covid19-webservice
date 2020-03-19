import pycountry as pycountry

import gettext

german = gettext.translation('iso3166', pycountry.LOCALES_DIR, languages=['de'])
german.install()
