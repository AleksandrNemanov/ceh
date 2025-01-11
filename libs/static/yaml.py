bound = {
    'header_dapp': "create table {} (\n",
    'footer_dapp': ")",
    'header_rdv': "create table if not exists rdv.{} (\n",
    'footer_rdv': """)
with (
    appendonly = true,
    orientation = column,
    compresstype = zstd,
    compresslevel = 1
)
distributed by (ВставитьКлючРаспределения)
"""

}
