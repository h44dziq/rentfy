# -*- coding: utf-8 -*-
import json
import sys
from catalog_data import build as get_catalog

catalog = get_catalog()
catalog_json = json.dumps(catalog, ensure_ascii=False)

with open("generate_html.py", "w", encoding="utf-8") as f:
    f.write(f'''# -*- coding: utf-8 -*-
CATALOG_DATA = {catalog_json}
''')

print("Catalog data ready")
