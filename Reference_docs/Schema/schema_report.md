# Riyadh z15 Tile & API Schema Report

## Tiles analyzed: 9

## Layers

### Layer: `parcels`
- Features: 7470
- Geometry types: {'Polygon': 7468, 'MultiPolygon': 2}
- Fields:

| Field | Type | Unique | Nulls | % Complete | Min | Max | Mean | Median | Top Values | Histogram |
|-------|------|--------|-------|------------|-----|-----|------|--------|-----------|-----------|
| parcel_objectid | {'str': 7470} | 100 | 0 | 100.0% | None | None | None | None | 1010001013840(1), 1010001003681(1), 1010001025628(1), 1010001031980(1), 1010001019849(1) |  |
| province_id | {'int': 7470} | 1 | 0 | 100.0% | 101000 | 101000 | 101000.0 | 101000 |  | {'101000': 1} |
| landuseagroup | {'str': 7253} | 12 | 0 | 100.0% | None | None | None | None | متعدد الاستخدام(1), مرافق المواصلات(1), حـــــــدود(1), أسواق تجارية(1), مرافق الكهرباء(1) |  |
| subdivision_no | {'str': 7465} | 29 | 0 | 100.0% | None | None | None | None | 1127(1), بدون(1), 1184(1), 1143(1), 1343(1) |  |
| shape_area | {'float': 7470} | 100 | 0 | 100.0% | 8.318870185805425 | 657121.9786928965 | 908.2219592537668 | 256.30455791764416 |  | {'104.08-4625.85': 98, '4625.85-9147.61': 0, '9147.61-13669.38': 1, '13669.38-18191.14': 0, '18191.14-22712.91': 0, '22712.91-27234.67': 0, '27234.67-31756.44': 0, '31756.44-36278.20': 0, '36278.20-40799.97': 0, '40799.97-45321.73': 1} |
| zoning_id | {'int': 7411} | 8 | 0 | 100.0% | 1 | 12 | 5.75 | 4.5 |  | {'1.00-2.10': 2, '2.10-3.20': 1, '3.20-4.30': 1, '4.30-5.40': 1, '5.40-6.50': 0, '6.50-7.60': 0, '7.60-8.70': 0, '8.70-9.80': 1, '9.80-10.90': 1, '10.90-12.00': 1} |
| neighborhaname | {'str': 7470} | 8 | 0 | 100.0% | None | None | None | None | أم الحمام الشرقي(1), أم الحمام الغربي(1), الهدا(1), المعذر الشمالي(1), الشرفية(1) |  |
| neighborhood_id | {'int': 7470} | 8 | 0 | 100.0% | 1010002 | 101000144 | 41915076.5 | 10100088.0 |  | {'1010002.00-11009016.20': 5, '11009016.20-21008030.40': 0, '21008030.40-31007044.60': 0, '31007044.60-41006058.80': 0, '41006058.80-51005073.00': 0, '51005073.00-61004087.20': 0, '61004087.20-71003101.40': 0, '71003101.40-81002115.60': 0, '81002115.60-91001129.80': 0, '91001129.80-101000144.00': 3} |
| municipality_aname | {'str': 7470} | 3 | 0 | 100.0% | None | None | None | None | الشميسي(1), العليا(1), المعذر(1) |  |
| parcel_no | {'str': 6994} | 100 | 0 | 100.0% | None | None | None | None | 657(1), 317(1), 350(1), 316(1), 659(1) |  |
| subdivision_id | {'str': 7465} | 34 | 0 | 100.0% | None | None | None | None | 1010001396                                                                                                                                                                                                                                                      (1), 101000838                                                                                                                                                                                                                                                       (1), 1010002229                                                                                                                                                                                                                                                      (1), 1010001515                                                                                                                                                                                                                                                      (1), 1010002054                                                                                                                                                                                                                                                      (1) |  |
| transaction_price | {'float': 7470} | 100 | 0 | 100.0% | 0.0 | 124687500.0 | 3867223.9781 | 1562500.0 |  | {'0.00-3489696.00': 83, '3489696.00-6979392.00': 8, '6979392.00-10469088.00': 0, '10469088.00-13958784.00': 0, '13958784.00-17448480.00': 0, '17448480.00-20938176.00': 1, '20938176.00-24427872.00': 2, '24427872.00-27917568.00': 4, '27917568.00-31407264.00': 1, '31407264.00-34896960.00': 1} |
| landuseadetailed | {'str': 7464} | 35 | 0 | 100.0% | None | None | None | None | (1), سكن مؤذن(1), مدرسه ابتدائيه بنات(1), سكن الإمام والمؤذن(1), حديقة حي(1) |  |
| parcel_id | {'int': 7470} | 100 | 0 | 100.0% | 9385 | 14861215 | 13541733.51 | 14542268.5 |  | {'1393302.00-2709483.10': 6, '2709483.10-4025664.20': 0, '4025664.20-5341845.30': 2, '5341845.30-6658026.40': 0, '6658026.40-7974207.50': 0, '7974207.50-9290388.60': 0, '9290388.60-10606569.70': 0, '10606569.70-11922750.80': 0, '11922750.80-13238931.90': 0, '13238931.90-14555113.00': 92} |
| price_of_meter | {'float': 7470} | 100 | 0 | 100.0% | 0.0 | 35000.0 | 5692.210377556026 | 5505.12583753581 |  | {'0.00-1474.51': 4, '1474.51-2949.02': 8, '2949.02-4423.53': 22, '4423.53-5898.04': 24, '5898.04-7372.55': 22, '7372.55-8847.06': 7, '8847.06-10321.57': 6, '10321.57-11796.08': 4, '11796.08-13270.59': 1, '13270.59-14745.10': 2} |
| zoning_color | {'str': 7411} | 8 | 0 | 100.0% | None | None | None | None | #ae123a          (1), #f28e2b          (1), #9d7660          (1), #bab0ac          (1), #305d8a          (1) |  |
| ruleid | {'str': 7412} | 27 | 0 | 100.0% | None | None | None | None | (1), س 111-02(1), س 221(1), R1(1), م 111-40(1) |  |
| block_no | {'str': 3405} | 100 | 0 | 100.0% | None | None | None | None | 87(1), 91(1), 144(1), 146(1), 23(1) |  |


### Layer: `parcels-base`
- Features: 7470
- Geometry types: {'Polygon': 7468, 'MultiPolygon': 2}
- Fields:

| Field | Type | Unique | Nulls | % Complete | Min | Max | Mean | Median | Top Values | Histogram |
|-------|------|--------|-------|------------|-----|-----|------|--------|-----------|-----------|
| transaction_price | {'float': 7470} | 100 | 0 | 100.0% | 0.0 | 124687500.0 | 3867223.9781 | 1562500.0 |  | {'0.00-3489696.00': 83, '3489696.00-6979392.00': 8, '6979392.00-10469088.00': 0, '10469088.00-13958784.00': 0, '13958784.00-17448480.00': 0, '17448480.00-20938176.00': 1, '20938176.00-24427872.00': 2, '24427872.00-27917568.00': 4, '27917568.00-31407264.00': 1, '31407264.00-34896960.00': 1} |
| zoning_color | {'str': 7411} | 8 | 0 | 100.0% | None | None | None | None | #ae123a          (1), #f28e2b          (1), #9d7660          (1), #bab0ac          (1), #305d8a          (1) |  |
| parcel_objectid | {'str': 7470} | 100 | 0 | 100.0% | None | None | None | None | 1010001013840(1), 1010001003681(1), 1010001025628(1), 1010001031980(1), 1010001019849(1) |  |
| parcel_no | {'str': 6994} | 100 | 0 | 100.0% | None | None | None | None | 657(1), 317(1), 350(1), 316(1), 659(1) |  |
| subdivision_id | {'str': 7465} | 34 | 0 | 100.0% | None | None | None | None | 1010001396                                                                                                                                                                                                                                                      (1), 101000838                                                                                                                                                                                                                                                       (1), 1010002229                                                                                                                                                                                                                                                      (1), 1010001515                                                                                                                                                                                                                                                      (1), 1010002054                                                                                                                                                                                                                                                      (1) |  |
| zoning_id | {'int': 7411} | 8 | 0 | 100.0% | 1 | 12 | 5.75 | 4.5 |  | {'1.00-2.10': 2, '2.10-3.20': 1, '3.20-4.30': 1, '4.30-5.40': 1, '5.40-6.50': 0, '6.50-7.60': 0, '7.60-8.70': 0, '8.70-9.80': 1, '9.80-10.90': 1, '10.90-12.00': 1} |
| municipality_aname | {'str': 7470} | 3 | 0 | 100.0% | None | None | None | None | الشميسي(1), العليا(1), المعذر(1) |  |
| landuseadetailed | {'str': 7464} | 35 | 0 | 100.0% | None | None | None | None | (1), سكن مؤذن(1), مدرسه ابتدائيه بنات(1), سكن الإمام والمؤذن(1), حديقة حي(1) |  |
| parcel_id | {'int': 7470} | 100 | 0 | 100.0% | 9385 | 14861215 | 13541733.51 | 14542268.5 |  | {'1393302.00-2709483.10': 6, '2709483.10-4025664.20': 0, '4025664.20-5341845.30': 2, '5341845.30-6658026.40': 0, '6658026.40-7974207.50': 0, '7974207.50-9290388.60': 0, '9290388.60-10606569.70': 0, '10606569.70-11922750.80': 0, '11922750.80-13238931.90': 0, '13238931.90-14555113.00': 92} |
| price_of_meter | {'float': 7470} | 100 | 0 | 100.0% | 0.0 | 35000.0 | 5692.210377556026 | 5505.12583753581 |  | {'0.00-1474.51': 4, '1474.51-2949.02': 8, '2949.02-4423.53': 22, '4423.53-5898.04': 24, '5898.04-7372.55': 22, '7372.55-8847.06': 7, '8847.06-10321.57': 6, '10321.57-11796.08': 4, '11796.08-13270.59': 1, '13270.59-14745.10': 2} |
| ruleid | {'str': 7412} | 27 | 0 | 100.0% | None | None | None | None | (1), س 111-02(1), س 221(1), R1(1), م 111-40(1) |  |
| province_id | {'int': 7470} | 1 | 0 | 100.0% | 101000 | 101000 | 101000.0 | 101000 |  | {'101000': 1} |
| landuseagroup | {'str': 7253} | 12 | 0 | 100.0% | None | None | None | None | متعدد الاستخدام(1), مرافق المواصلات(1), حـــــــدود(1), أسواق تجارية(1), مرافق الكهرباء(1) |  |
| subdivision_no | {'str': 7465} | 29 | 0 | 100.0% | None | None | None | None | 1127(1), بدون(1), 1184(1), 1143(1), 1343(1) |  |
| shape_area | {'float': 7470} | 100 | 0 | 100.0% | 8.318870185805425 | 657121.9786928965 | 908.2219592537668 | 256.30455791764416 |  | {'104.08-4625.85': 98, '4625.85-9147.61': 0, '9147.61-13669.38': 1, '13669.38-18191.14': 0, '18191.14-22712.91': 0, '22712.91-27234.67': 0, '27234.67-31756.44': 0, '31756.44-36278.20': 0, '36278.20-40799.97': 0, '40799.97-45321.73': 1} |
| neighborhaname | {'str': 7470} | 8 | 0 | 100.0% | None | None | None | None | أم الحمام الشرقي(1), أم الحمام الغربي(1), الهدا(1), المعذر الشمالي(1), الشرفية(1) |  |
| neighborhood_id | {'int': 7470} | 8 | 0 | 100.0% | 1010002 | 101000144 | 41915076.5 | 10100088.0 |  | {'1010002.00-11009016.20': 5, '11009016.20-21008030.40': 0, '21008030.40-31007044.60': 0, '31007044.60-41006058.80': 0, '41006058.80-51005073.00': 0, '51005073.00-61004087.20': 0, '61004087.20-71003101.40': 0, '71003101.40-81002115.60': 0, '81002115.60-91001129.80': 0, '91001129.80-101000144.00': 3} |
| block_no | {'str': 3405} | 100 | 0 | 100.0% | None | None | None | None | 87(1), 91(1), 144(1), 146(1), 23(1) |  |


### Layer: `parcels-centroids`
- Features: 7484
- Geometry types: {'Point': 7484}
- Fields:

| Field | Type | Unique | Nulls | % Complete | Min | Max | Mean | Median | Top Values | Histogram |
|-------|------|--------|-------|------------|-----|-----|------|--------|-----------|-----------|
| neighborhood_id | {'int': 7484} | 8 | 0 | 100.0% | 1010002 | 101000144 | 41915076.5 | 10100088.0 |  | {'1010002.00-11009016.20': 5, '11009016.20-21008030.40': 0, '21008030.40-31007044.60': 0, '31007044.60-41006058.80': 0, '41006058.80-51005073.00': 0, '51005073.00-61004087.20': 0, '61004087.20-71003101.40': 0, '71003101.40-81002115.60': 0, '81002115.60-91001129.80': 0, '91001129.80-101000144.00': 3} |
| province_id | {'int': 7484} | 1 | 0 | 100.0% | 101000 | 101000 | 101000.0 | 101000 |  | {'101000': 1} |
| transactions_count | {'int': 7484} | 16 | 0 | 100.0% | 0 | 63 | 11.625 | 7.5 |  | {'0.00-6.30': 7, '6.30-12.60': 4, '12.60-18.90': 3, '18.90-25.20': 0, '25.20-31.50': 1, '31.50-37.80': 0, '37.80-44.10': 0, '44.10-50.40': 0, '50.40-56.70': 0, '56.70-63.00': 1} |
| parcel_id | {'int': 7484} | 100 | 0 | 100.0% | 9385 | 14861215 | 13541733.51 | 14542268.5 |  | {'1393302.00-2709483.10': 6, '2709483.10-4025664.20': 0, '4025664.20-5341845.30': 2, '5341845.30-6658026.40': 0, '6658026.40-7974207.50': 0, '7974207.50-9290388.60': 0, '9290388.60-10606569.70': 0, '10606569.70-11922750.80': 0, '11922750.80-13238931.90': 0, '13238931.90-14555113.00': 92} |
| parcel_no | {'str': 7003} | 100 | 0 | 100.0% | None | None | None | None | 657(1), 317(1), 350(1), 316(1), 659(1) |  |
| transaction_date | {'str': 371} | 100 | 0 | 100.0% | None | None | None | None | 2023-04-09 00:00:00 +0000 UTC(1), 2022-06-02 00:00:00 +0000 UTC(1), 2024-03-24 00:00:00 +0000 UTC(1), 2024-09-25 00:00:00 +0000 UTC(1), 2024-10-10 00:00:00 +0000 UTC(1) |  |
| transaction_price | {'float': 371} | 100 | 0 | 100.0% | 1000.0 | 124687500.0 | 4247223.9781 | 1656719.2 |  | {'1000.00-3800900.00': 84, '3800900.00-7600800.00': 6, '7600800.00-11400700.00': 0, '11400700.00-15200600.00': 0, '15200600.00-19000500.00': 0, '19000500.00-22800400.00': 3, '22800400.00-26600300.00': 2, '26600300.00-30400200.00': 3, '30400200.00-34200100.00': 0, '34200100.00-38000000.00': 2} |
| price_of_meter | {'float': 371} | 100 | 0 | 100.0% | 8.54700854700855 | 35000.0 | 5747.210377556026 | 5520.083102493075 |  | {'8.55-1482.20': 3, '1482.20-2955.86': 8, '2955.86-4429.51': 22, '4429.51-5903.17': 25, '5903.17-7376.82': 22, '7376.82-8850.48': 7, '8850.48-10324.13': 6, '10324.13-11797.79': 4, '11797.79-13271.44': 1, '13271.44-14745.10': 2} |


### Layer: `neighborhoods`
- Features: 29
- Geometry types: {'Polygon': 29}
- Fields:

| Field | Type | Unique | Nulls | % Complete | Min | Max | Mean | Median | Top Values | Histogram |
|-------|------|--------|-------|------------|-----|-----|------|--------|-----------|-----------|
| zoning_color | {'str': 29} | 2 | 0 | 100.0% | None | None | None | None | #f28e2b          (1), #f1ce63          (1) |  |
| neighborh_aname | {'str': 29} | 8 | 0 | 100.0% | None | None | None | None | أم الحمام الشرقي(1), أم الحمام الغربي(1), الهدا(1), المعذر الشمالي(1), الشرفية(1) |  |
| price_of_meter | {'float': 29} | 8 | 0 | 100.0% | 73.92897845794106 | 1374.8994479307585 | 632.8200168963676 | 571.8574628284957 |  | {'73.93-204.03': 2, '204.03-334.12': 0, '334.12-464.22': 1, '464.22-594.32': 2, '594.32-724.41': 1, '724.41-854.51': 0, '854.51-984.61': 0, '984.61-1114.71': 0, '1114.71-1244.80': 0, '1244.80-1374.90': 2} |
| zoning_id | {'int': 29} | 2 | 0 | 100.0% | 1 | 3 | 2.0 | 2.0 |  | {'1.00-1.20': 1, '1.20-1.40': 0, '1.40-1.60': 0, '1.60-1.80': 0, '1.80-2.00': 0, '2.00-2.20': 0, '2.20-2.40': 0, '2.40-2.60': 0, '2.60-2.80': 0, '2.80-3.00': 1} |
| shape_area | {'float': 29} | 8 | 0 | 100.0% | 2130.8773604940416 | 139134.7906069308 | 29457.556542241582 | 3716.036223508402 |  | {'2130.88-15831.27': 5, '15831.27-29531.66': 1, '29531.66-43232.05': 0, '43232.05-56932.44': 0, '56932.44-70632.83': 1, '70632.83-84333.23': 0, '84333.23-98033.62': 0, '98033.62-111734.01': 0, '111734.01-125434.40': 0, '125434.40-139134.79': 1} |
| transaction_price | {'float': 29} | 8 | 0 | 100.0% | 70187.63684210526 | 1213252.280401833 | 502970.9984301105 | 435287.4337489654 |  | {'70187.64-184494.10': 2, '184494.10-298800.57': 1, '298800.57-413107.03': 0, '413107.03-527413.49': 2, '527413.49-641719.96': 0, '641719.96-756026.42': 1, '756026.42-870332.89': 1, '870332.89-984639.35': 0, '984639.35-1098945.82': 0, '1098945.82-1213252.28': 1} |
| neighborhood_id | {'int': 29} | 8 | 0 | 100.0% | 1010002 | 101000144 | 41915076.5 | 10100088.0 |  | {'1010002.00-11009016.20': 5, '11009016.20-21008030.40': 0, '21008030.40-31007044.60': 0, '31007044.60-41006058.80': 0, '41006058.80-51005073.00': 0, '51005073.00-61004087.20': 0, '61004087.20-71003101.40': 0, '71003101.40-81002115.60': 0, '81002115.60-91001129.80': 0, '91001129.80-101000144.00': 3} |
| region_id | {'int': 29} | 1 | 0 | 100.0% | 10 | 10 | 10.0 | 10 |  | {'10': 1} |
| province_id | {'int': 29} | 1 | 0 | 100.0% | 101000 | 101000 | 101000.0 | 101000 |  | {'101000': 1} |


### Layer: `neighborhoods-centroids`
- Features: 48
- Geometry types: {'Point': 48}
- Fields:

| Field | Type | Unique | Nulls | % Complete | Min | Max | Mean | Median | Top Values | Histogram |
|-------|------|--------|-------|------------|-----|-----|------|--------|-----------|-----------|
| province_id | {'int': 48} | 1 | 0 | 100.0% | 101000 | 101000 | 101000.0 | 101000 |  | {'101000': 1} |
| neighborh_aname | {'str': 48} | 10 | 0 | 100.0% | None | None | None | None | أم الحمام الشرقي(1), أم الحمام الغربي(1), الرائد(1), المعذر الشمالي(1), العليا(1) |  |


### Layer: `subdivisions`
- Features: 64
- Geometry types: {'Polygon': 60, 'MultiPolygon': 4}
- Fields:

| Field | Type | Unique | Nulls | % Complete | Min | Max | Mean | Median | Top Values | Histogram |
|-------|------|--------|-------|------------|-----|-----|------|--------|-----------|-----------|
| transaction_price | {'float': 64} | 20 | 0 | 100.0% | 0.0 | 66058200.0 | 8365792.268378285 | 2382936.0905 |  | {'0.00-6605820.00': 15, '6605820.00-13211640.00': 1, '13211640.00-19817460.00': 2, '19817460.00-26423280.00': 0, '26423280.00-33029100.00': 1, '33029100.00-39634920.00': 0, '39634920.00-46240740.00': 0, '46240740.00-52846560.00': 0, '52846560.00-59452380.00': 0, '59452380.00-66058200.00': 1} |
| price_of_meter | {'float': 64} | 20 | 0 | 100.0% | 0.0 | 29254.7619047619 | 6980.032657310413 | 6077.87118471364 |  | {'0.00-2925.48': 2, '2925.48-5850.95': 7, '5850.95-8776.43': 8, '8776.43-11701.90': 2, '11701.90-14627.38': 0, '14627.38-17552.86': 0, '17552.86-20478.33': 0, '20478.33-23403.81': 0, '23403.81-26329.29': 0, '26329.29-29254.76': 1} |
| zoning_id | {'int': 64} | 6 | 0 | 100.0% | 1 | 10 | 4.833333333333333 | 3.5 |  | {'1.00-1.90': 1, '1.90-2.80': 1, '2.80-3.70': 1, '3.70-4.60': 1, '4.60-5.50': 0, '5.50-6.40': 0, '6.40-7.30': 0, '7.30-8.20': 0, '8.20-9.10': 1, '9.10-10.00': 1} |
| zoning_color | {'str': 64} | 6 | 0 | 100.0% | None | None | None | None | #ae123a          (1), #f28e2b          (1), #bab0ac          (1), #305d8a          (1), #fa6d6d          (1) |  |
| province_id | {'int': 64} | 1 | 0 | 100.0% | 101000 | 101000 | 101000.0 | 101000 |  | {'101000': 1} |
| subdivision_id | {'int': 64} | 34 | 0 | 100.0% | 10100075 | 1010002313 | 606298235.2647059 | 1010001042.5 |  | {'10100075.00-110090298.80': 15, '110090298.80-210080522.60': 0, '210080522.60-310070746.40': 0, '310070746.40-410060970.20': 0, '410060970.20-510051194.00': 0, '510051194.00-610041417.80': 0, '610041417.80-710031641.60': 0, '710031641.60-810021865.40': 0, '810021865.40-910012089.20': 0, '910012089.20-1010002313.00': 19} |
| subdivision_no | {'str': 64} | 29 | 0 | 100.0% | None | None | None | None | 1127(1), بدون(1), 1184(1), 1143(1), 1343(1) |  |
| shape_area | {'float': 64} | 34 | 0 | 100.0% | 137.60410983035834 | 47242.180842899215 | 5935.006569624104 | 1306.9447678288698 |  | {'137.60-4848.06': 25, '4848.06-9558.52': 2, '9558.52-14268.98': 2, '14268.98-18979.43': 2, '18979.43-23689.89': 1, '23689.89-28400.35': 0, '28400.35-33110.81': 1, '33110.81-37821.27': 0, '37821.27-42531.72': 0, '42531.72-47242.18': 1} |


### Layer: `dimensions`
- Features: 28856
- Geometry types: {'Point': 28856}
- Fields:

| Field | Type | Unique | Nulls | % Complete | Min | Max | Mean | Median | Top Values | Histogram |
|-------|------|--------|-------|------------|-----|-----|------|--------|-----------|-----------|
| parcel_objectid | {'str': 28856} | 100 | 0 | 100.0% | None | None | None | None | 1010001013840(1), 1010001003681(1), 1010001025628(1), 1010001031980(1), 1010001019849(1) |  |
| length_m | {'float': 28856} | 100 | 0 | 100.0% | 0.1 | 1197.6 | 30.1263 | 17.064999999999998 |  | {'7.23-71.83': 95, '71.83-136.42': 4, '136.42-201.02': 0, '201.02-265.62': 0, '265.62-330.22': 0, '330.22-394.81': 0, '394.81-459.41': 0, '459.41-524.01': 0, '524.01-588.60': 0, '588.60-653.20': 1} |
| province_id | {'int': 28856} | 1 | 0 | 100.0% | 101000 | 101000 | 101000.0 | 101000 |  | {'101000': 1} |
| azimuth | {'float': 28856} | 100 | 0 | 100.0% | 0.0 | 359.56921278408447 | 177.28694068204905 | 180.67394364080326 |  | {'1.41-37.21': 9, '37.21-73.01': 3, '73.01-108.81': 24, '108.81-144.60': 2, '144.60-180.40': 12, '180.40-216.20': 12, '216.20-252.00': 3, '252.00-287.80': 22, '287.80-323.59': 2, '323.59-359.39': 11} |


### Layer: `streets`
- Features: 1244
- Geometry types: {'LineString': 1241, 'MultiLineString': 3}
- Fields:

| Field | Type | Unique | Nulls | % Complete | Min | Max | Mean | Median | Top Values | Histogram |
|-------|------|--------|-------|------------|-----|-----|------|--------|-----------|-----------|
| street_width | {'str': 1244} | 18 | 0 | 100.0% | None | None | None | None | 7                                                               (1), 15                                                              (1), 2.6                                                             (1), 84                                                              (1), 6                                                               (1) |  |


### Layer: `bus_lines`
- Features: 42
- Geometry types: {'MultiLineString': 4, 'LineString': 38}
- Fields:

| Field | Type | Unique | Nulls | % Complete | Min | Max | Mean | Median | Top Values | Histogram |
|-------|------|--------|-------|------------|-----|-----|------|--------|-----------|-----------|
| originar | {'str': 42} | 6 | 0 | 100.0% | None | None | None | None | مركز النقل العام(1), البطحاء(1), الصناعية(1), حي العليا(1), المربع(1) |  |
| color | {'str': 42} | 5 | 0 | 100.0% | None | None | None | None | #65aa9a(1), #a655a3(1), #509dc8(1), #ea5959(1), #3ea444(1) |  |
| type | {'str': 42} | 2 | 0 | 100.0% | None | None | None | None | Feeder(1), Community(1) |  |
| busroute | {'str': 42} | 7 | 0 | 100.0% | None | None | None | None | 921(1), 7(1), 680(1), 181(1), 350(1) |  |
| origin | {'str': 42} | 6 | 0 | 100.0% | None | None | None | None | Al Awwal Park(1), Al-Muraba(1), Transportation Center(1), Al-Olaya District(1), Al Batha(1) |  |


### Layer: `riyadh_bus_stations`
- Features: 42
- Geometry types: {'Point': 42}
- Fields:

| Field | Type | Unique | Nulls | % Complete | Min | Max | Mean | Median | Top Values | Histogram |
|-------|------|--------|-------|------------|-----|-----|------|--------|-----------|-----------|
| station_name | {'str': 42} | 39 | 0 | 100.0% | None | None | None | None | التخصصي 218(1), المعذر الشمالي 506(1), التخصصي 116(1), أم الحمام 203(1), الملك خالد 103(1) |  |
| station_code | {'str': 42} | 37 | 0 | 100.0% | None | None | None | None | 601(1), 504(1), 116(1), 218(1), 605(1) |  |
| station_long | {'float': 42} | 38 | 0 | 100.0% | 46.6495127108204 | 46.6799296663449 | 46.66490179723454 | 46.66623484983665 |  | {'46.65-46.65': 9, '46.65-46.66': 2, '46.66-46.66': 3, '46.66-46.67': 4, '46.67-46.67': 1, '46.67-46.68': 1, '46.68-46.68': 8} |
| station_lat | {'float': 42} | 39 | 0 | 100.0% | 24.6683373875342 | 24.6967099326571 | 24.68522568361943 | 24.6870953343475 |  | {'24.67-24.67': 2, '24.67-24.68': 1, '24.68-24.68': 6, '24.68-24.69': 2, '24.69-24.69': 5, '24.69-24.70': 7} |


### Layer: `qi_population_metrics`
- Features: 200
- Geometry types: {'Polygon': 200}
- Fields:

| Field | Type | Unique | Nulls | % Complete | Min | Max | Mean | Median | Top Values | Histogram |
|-------|------|--------|-------|------------|-----|-----|------|--------|-----------|-----------|
| grid_id | {'str': 200} | 100 | 0 | 100.0% | None | None | None | None | 895355d3623ffff(1), 895355d30cfffff(1), 895355d36c7ffff(1), 895355d3413ffff(1), 895355d34dbffff(1) |  |
| population_density | {'str': 144} | 6 | 0 | 100.0% | None | None | None | None | #29EA8D(1), #F4E587(1), #1AC7C2(1), #AFF05B(1), #60F761(1) |  |
| residential_rpi | {'str': 167} | 6 | 0 | 100.0% | None | None | None | None | #29EA8D(1), #F4E587(1), #1AC7C2(1), #AFF05B(1), #60F761(1) |  |
| commercial_rpi | {'str': 130} | 5 | 0 | 100.0% | None | None | None | None | #29EA8D(1), #1AC7C2(1), #60F761(1), #AFF05B(1), #F4E587(1) |  |
| poi_count | {'str': 133} | 4 | 0 | 100.0% | None | None | None | None | #AFF05B(1), #F4E587(1), #29EA8D(1), #60F761(1) |  |


### Layer: `qi_stripes`
- Features: 201
- Geometry types: {'Polygon': 201}
- Fields:

| Field | Type | Unique | Nulls | % Complete | Min | Max | Mean | Median | Top Values | Histogram |
|-------|------|--------|-------|------------|-----|-----|------|--------|-----------|-----------|
| strip_id | {'str': 201} | 100 | 0 | 100.0% | None | None | None | None | ST-1199(1), ST-1326(1), ST-18891(1), ST-11810(1), ST-1226(1) |  |
| centroid_longitude | {'float': 201} | 94 | 0 | 100.0% | 46.64258333942295 | 46.68452905566456 | 46.66372409351602 | 46.66322303138253 |  | {'46.64-46.65': 4, '46.65-46.65': 10, '46.65-46.66': 10, '46.66-46.66': 16, '46.66-46.67': 11, '46.67-46.67': 10, '46.67-46.68': 9, '46.68-46.68': 8} |
| centroid_latitude | {'float': 201} | 94 | 0 | 100.0% | 24.671772673876426 | 24.70318112511006 | 24.684751743118795 | 24.68604649990777 |  | {'24.67-24.67': 19, '24.67-24.68': 7, '24.68-24.68': 10, '24.68-24.69': 15, '24.69-24.69': 7, '24.69-24.70': 15, '24.70-24.70': 1} |


## Cross-Layer Relationships & Integrity

- subdivisions.subdivision_id has 34 values not in parcels.subdivision_id

## API Endpoints

### transactions
    - `data`: types={'dict': 3}, samples=[{'lastExecutionDate': None, 'lastExecutionPrice': None, 'transactions': []}, {'lastExecutionDate': '2025-05-14T00:00:00', 'lastExecutionPrice': 7536.0, 'transactions': [{'_priceOfMeter': 7536.0, 'transactionPrice': 2600000.0, 'priceOfMeter': 7536.0, 'transactionNumber': 29435043, 'transactionDate': '2025-05-14T00:00:00', 'type': 'قطعة أرض', 'subdivisionNo': '1343', 'subdivisionId': None, 'polygonData': '{"type":"Polygon","coordinates":[[[46.675043,24.690691],[46.675028,24.690685],[46.674908,24.690634],[46.674814,24.690823],[46.674948,24.69088],[46.675043,24.690691]]]}', 'noOfProperties': 1, 'zoningId': 3, 'neighborhood': 'العليا', 'neighborhoodId': 10100079, 'region': 'منطقة الرياض', 'parcelId': '3286217', 'parcelObjectId': 101000472515, 'parcelNo': '303/أ/2', 'blockNo': '36', 'area': 345.0, 'centroidX': 46.67492827177639, 'centroidY': 24.69075697568582, 'metricsType': 'أرض سكني', 'provinceId': 101000, 'provinceName': None, 'regionId': 10, 'geometry': None, 'parcelImageURL': '', 'projectName': '', 'landUsageGroup': 'سكني', 'sellingType': 'فردي', 'landUseaDetailed': None, 'centroid': {'x': 46.67492827177639, 'y': 24.69075697568582}, 'propertyType': 'قطعة أرض', 'totalArea': 345.0, 'details': None, 'landUseGroup': 'سكني', 'orignalTransactionNum': 29435043, 'propertyNumber': '303/أ/2', 'transactionSource': 'MOJ', 'isLowValueTransaction': False}, {'_priceOfMeter': 6957.0, 'transactionPrice': 2400000.0, 'priceOfMeter': 6957.0, 'transactionNumber': 29405949, 'transactionDate': '2025-05-13T00:00:00', 'type': 'قطعة أرض', 'subdivisionNo': '1343', 'subdivisionId': None, 'polygonData': '{"type":"Polygon","coordinates":[[[46.675043,24.690691],[46.675028,24.690685],[46.674908,24.690634],[46.674814,24.690823],[46.674948,24.69088],[46.675043,24.690691]]]}', 'noOfProperties': 1, 'zoningId': 3, 'neighborhood': 'العليا', 'neighborhoodId': 10100079, 'region': 'منطقة الرياض', 'parcelId': '3286217', 'parcelObjectId': 101000472515, 'parcelNo': '303/أ/2', 'blockNo': '36', 'area': 345.0, 'centroidX': 46.67492827177639, 'centroidY': 24.69075697568582, 'metricsType': 'أرض سكني', 'provinceId': 101000, 'provinceName': None, 'regionId': 10, 'geometry': None, 'parcelImageURL': '', 'projectName': '', 'landUsageGroup': 'سكني', 'sellingType': 'فردي', 'landUseaDetailed': None, 'centroid': {'x': 46.67492827177639, 'y': 24.69075697568582}, 'propertyType': 'قطعة أرض', 'totalArea': 345.0, 'details': None, 'landUseGroup': 'سكني', 'orignalTransactionNum': 29405949, 'propertyNumber': '303/أ/2', 'transactionSource': 'MOJ', 'isLowValueTransaction': False}]}]
    - `message`: types={'NoneType': 3}, samples=[None]
    - `status`: types={'bool': 3}, samples=[True]
    - `meta`: types={'NoneType': 3}, samples=[None]
    - Example payload:

```json
{
  "data": {
    "lastExecutionDate": "2025-05-14T00:00:00",
    "lastExecutionPrice": 7536.0,
    "transactions": [
      {
        "_priceOfMeter": 7536.0,
        "transactionPrice": 2600000.0,
        "priceOfMeter": 7536.0,
        "transactionNumber": 29435043,
        "transactionDate": "2025-05-14T00:00:00",
        "type": "قطعة أرض",
        "subdivisionNo": "1343",
        "subdivisionId": null,
        "polygonData": "{\"type\":\"Polygon\",\"coordinates\":[[[46.675043,24.690691],[46.675028,24.690685],[46.674908,24.690634],[46.674814,24.690823],[46.674948,24.69088],[46.675043,24.690691]]]}",
        "noOfProperties": 1,
        "zoningId": 3,
        "neighborhood": "العليا",
        "neighborhoodId": 10100079,
        "region": "منطقة الرياض",
        "parcelId": "3286217",
        "parcelObjectId": 101000472515,
        "parcelNo": "303/أ/2",
        "blockNo": "36",
        "area": 345.0,
        "centroidX": 46.67492827177639,
        "centroidY": 24.69075697568582,
        "metricsType": "أرض سكني",
        "provinceId": 101000,
        "provinceName": null,
        "regionId": 10,
        "geometry": null,
        "parcelImageURL": "",
        "projectName": "",
        "landUsageGroup": "سكني",
        "sellingType": "فردي",
        "landUseaDetailed": null,
        "centroid": {
          "x": 46.67492827177639,
          "y": 24.69075697568582
        },
        "propertyType": "قطعة أرض",
        "totalArea": 345.0,
        "details": null,
        "landUseGroup": "سكني",
        "orignalTransactionNum": 29435043,
        "propertyNumber": "303/أ/2",
        "transactionSource": "MOJ",
        "isLowValueTransaction": false
      },
      {
        "_priceOfMeter": 6957.0,
        "transactionPrice": 2400000.0,
        "priceOfMeter": 6957.0,
        "transactionNumber": 29405949,
        "transactionDate": "2025-05-13T00:00:00",
        "type": "قطعة أرض",
        "subdivisionNo": "1343",
        "subdivisionId": null,
        "polygonData": "{\"type\":\"Polygon\",\"coordinates\":[[[46.675043,24.690691],[46.675028,24.690685],[46.674908,24.690634],[46.674814,24.690823],[46.674948,24.69088],[46.675043,24.690691]]]}",
        "noOfProperties": 1,
        "zoningId": 3,
        "neighborhood": "العليا",
        "neighborhoodId": 10100079,
        "region": "منطقة الرياض",
        "parcelId": "3286217",
        "parcelObjectId": 101000472515,
        "parcelNo": "303/أ/2",
        "blockNo": "36",
        "area": 345.0,
        "centroidX": 46.67492827177639,
        "centroidY": 24.69075697568582,
        "metricsType": "أرض سكني",
        "provinceId": 101000,
        "provinceName": null,
        "regionId": 10,
        "geometry": null,
        "parcelImageURL": "",
        "projectName": "",
        "landUsageGroup": "سكني",
        "sellingType": "فردي",
        "landUseaDetailed": null,
        "centroid": {
          "x": 46.67492827177639,
          "y": 24.69075697568582
        },
        "propertyType": "قطعة أرض",
        "totalArea": 345.0,
        "details": null,
        "landUseGroup": "سكني",
        "orignalTransactionNum": 29405949,
        "propertyNumber": "303/أ/2",
        "transactionSource": "MOJ",
        "isLowValueTransaction": false
      }
    ]
  },
  "message": null,
  "status": true,
  "meta": null
}
```


### parcel_metrics_priceOfMeter
    - `data`: types={'list': 3}, samples=[[{'parcelObjId': 101000472515, 'neighborhoodId': 10100079, 'neighborhoodMetrics': [{'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'أرض تجاري', 'avaragePriceOfMeter': 13434.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'أرض تجاري سكني', 'avaragePriceOfMeter': 9215.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'أرض سكني', 'avaragePriceOfMeter': 7128.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'شقق', 'avaragePriceOfMeter': 11879.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'فلل', 'avaragePriceOfMeter': 14381.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'مبنى تجاري', 'avaragePriceOfMeter': 24870.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'مبنى تجاري سكني', 'avaragePriceOfMeter': 32687.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'مرافق', 'avaragePriceOfMeter': 4901.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'أرض تجاري', 'avaragePriceOfMeter': 13434.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'أرض تجاري سكني', 'avaragePriceOfMeter': 9215.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'أرض سكني', 'avaragePriceOfMeter': 7268.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'شقق', 'avaragePriceOfMeter': 12009.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'فلل', 'avaragePriceOfMeter': 14381.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'مبنى تجاري', 'avaragePriceOfMeter': 24870.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'مبنى تجاري سكني', 'avaragePriceOfMeter': 32687.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'مرافق', 'avaragePriceOfMeter': 4901.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'أرض تجاري', 'avaragePriceOfMeter': 13434.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'أرض تجاري سكني', 'avaragePriceOfMeter': 10660.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'أرض سكني', 'avaragePriceOfMeter': 7432.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'شقق', 'avaragePriceOfMeter': 12566.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'فلل', 'avaragePriceOfMeter': 15157.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'مبنى تجاري', 'avaragePriceOfMeter': 24870.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'مبنى تجاري سكني', 'avaragePriceOfMeter': 32687.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'مرافق', 'avaragePriceOfMeter': 4901.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'أرض تجاري', 'avaragePriceOfMeter': 13434.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'أرض تجاري سكني', 'avaragePriceOfMeter': 11277.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'أرض سكني', 'avaragePriceOfMeter': 7672.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'شقق', 'avaragePriceOfMeter': 14066.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'فلل', 'avaragePriceOfMeter': 15230.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'مبنى تجاري', 'avaragePriceOfMeter': 24870.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'مبنى تجاري سكني', 'avaragePriceOfMeter': 33398.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'مرافق', 'avaragePriceOfMeter': 4901.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'أرض تجاري', 'avaragePriceOfMeter': 13434.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'أرض تجاري سكني', 'avaragePriceOfMeter': 11277.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'أرض سكني', 'avaragePriceOfMeter': 7916.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'شقق', 'avaragePriceOfMeter': 14819.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'فلل', 'avaragePriceOfMeter': 15779.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'مبنى تجاري', 'avaragePriceOfMeter': 24870.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'مبنى تجاري سكني', 'avaragePriceOfMeter': 33398.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'مرافق', 'avaragePriceOfMeter': 4901.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'أرض تجاري', 'avaragePriceOfMeter': 13434.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'أرض تجاري سكني', 'avaragePriceOfMeter': 11277.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'أرض سكني', 'avaragePriceOfMeter': 8109.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'شقق', 'avaragePriceOfMeter': 16055.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'فلل', 'avaragePriceOfMeter': 15779.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'مبنى تجاري', 'avaragePriceOfMeter': 24870.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'مبنى تجاري سكني', 'avaragePriceOfMeter': 33398.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'مرافق', 'avaragePriceOfMeter': 4901.0}], 'parcelMetrics': [{'parcelObjId': 101000472515, 'month': 5, 'year': 2025, 'metricsType': 'أرض سكني', 'avaragePriceOfMeter': 7246.0}], 'from': '2025-01-09T00:00:00+00:00', 'to': '2025-07-09T23:59:59.9999999+00:00', 'groupingType': 0}], [{'parcelObjId': 1010001129683, 'neighborhoodId': 10100079, 'neighborhoodMetrics': [{'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'أرض تجاري', 'avaragePriceOfMeter': 13434.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'أرض تجاري سكني', 'avaragePriceOfMeter': 9215.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'أرض سكني', 'avaragePriceOfMeter': 7128.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'شقق', 'avaragePriceOfMeter': 11879.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'فلل', 'avaragePriceOfMeter': 14381.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'مبنى تجاري', 'avaragePriceOfMeter': 24870.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'مبنى تجاري سكني', 'avaragePriceOfMeter': 32687.0}, {'neighborhoodId': 10100079, 'month': 1, 'year': 2025, 'metricsType': 'مرافق', 'avaragePriceOfMeter': 4901.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'أرض تجاري', 'avaragePriceOfMeter': 13434.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'أرض تجاري سكني', 'avaragePriceOfMeter': 9215.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'أرض سكني', 'avaragePriceOfMeter': 7268.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'شقق', 'avaragePriceOfMeter': 12009.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'فلل', 'avaragePriceOfMeter': 14381.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'مبنى تجاري', 'avaragePriceOfMeter': 24870.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'مبنى تجاري سكني', 'avaragePriceOfMeter': 32687.0}, {'neighborhoodId': 10100079, 'month': 2, 'year': 2025, 'metricsType': 'مرافق', 'avaragePriceOfMeter': 4901.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'أرض تجاري', 'avaragePriceOfMeter': 13434.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'أرض تجاري سكني', 'avaragePriceOfMeter': 10660.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'أرض سكني', 'avaragePriceOfMeter': 7432.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'شقق', 'avaragePriceOfMeter': 12566.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'فلل', 'avaragePriceOfMeter': 15157.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'مبنى تجاري', 'avaragePriceOfMeter': 24870.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'مبنى تجاري سكني', 'avaragePriceOfMeter': 32687.0}, {'neighborhoodId': 10100079, 'month': 3, 'year': 2025, 'metricsType': 'مرافق', 'avaragePriceOfMeter': 4901.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'أرض تجاري', 'avaragePriceOfMeter': 13434.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'أرض تجاري سكني', 'avaragePriceOfMeter': 11277.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'أرض سكني', 'avaragePriceOfMeter': 7672.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'شقق', 'avaragePriceOfMeter': 14066.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'فلل', 'avaragePriceOfMeter': 15230.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'مبنى تجاري', 'avaragePriceOfMeter': 24870.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'مبنى تجاري سكني', 'avaragePriceOfMeter': 33398.0}, {'neighborhoodId': 10100079, 'month': 4, 'year': 2025, 'metricsType': 'مرافق', 'avaragePriceOfMeter': 4901.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'أرض تجاري', 'avaragePriceOfMeter': 13434.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'أرض تجاري سكني', 'avaragePriceOfMeter': 11277.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'أرض سكني', 'avaragePriceOfMeter': 7916.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'شقق', 'avaragePriceOfMeter': 14819.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'فلل', 'avaragePriceOfMeter': 15779.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'مبنى تجاري', 'avaragePriceOfMeter': 24870.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'مبنى تجاري سكني', 'avaragePriceOfMeter': 33398.0}, {'neighborhoodId': 10100079, 'month': 5, 'year': 2025, 'metricsType': 'مرافق', 'avaragePriceOfMeter': 4901.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'أرض تجاري', 'avaragePriceOfMeter': 13434.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'أرض تجاري سكني', 'avaragePriceOfMeter': 11277.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'أرض سكني', 'avaragePriceOfMeter': 8109.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'شقق', 'avaragePriceOfMeter': 16055.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'فلل', 'avaragePriceOfMeter': 15779.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'مبنى تجاري', 'avaragePriceOfMeter': 24870.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'مبنى تجاري سكني', 'avaragePriceOfMeter': 33398.0}, {'neighborhoodId': 10100079, 'month': 6, 'year': 2025, 'metricsType': 'مرافق', 'avaragePriceOfMeter': 4901.0}], 'parcelMetrics': [], 'from': '2025-01-09T00:00:00+00:00', 'to': '2025-07-09T23:59:59.9999999+00:00', 'groupingType': 0}]]
    - `message`: types={'NoneType': 3}, samples=[None]
    - `status`: types={'bool': 3}, samples=[True]
    - `meta`: types={'NoneType': 3}, samples=[None]
    - Example payload:

```json
{
  "data": [
    {
      "parcelObjId": 101000472515,
      "neighborhoodId": 10100079,
      "neighborhoodMetrics": [
        {
          "neighborhoodId": 10100079,
          "month": 1,
          "year": 2025,
          "metricsType": "أرض تجاري",
          "avaragePriceOfMeter": 13434.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 1,
          "year": 2025,
          "metricsType": "أرض تجاري سكني",
          "avaragePriceOfMeter": 9215.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 1,
          "year": 2025,
          "metricsType": "أرض سكني",
          "avaragePriceOfMeter": 7128.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 1,
          "year": 2025,
          "metricsType": "شقق",
          "avaragePriceOfMeter": 11879.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 1,
          "year": 2025,
          "metricsType": "فلل",
          "avaragePriceOfMeter": 14381.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 1,
          "year": 2025,
          "metricsType": "مبنى تجاري",
          "avaragePriceOfMeter": 24870.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 1,
          "year": 2025,
          "metricsType": "مبنى تجاري سكني",
          "avaragePriceOfMeter": 32687.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 1,
          "year": 2025,
          "metricsType": "مرافق",
          "avaragePriceOfMeter": 4901.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 2,
          "year": 2025,
          "metricsType": "أرض تجاري",
          "avaragePriceOfMeter": 13434.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 2,
          "year": 2025,
          "metricsType": "أرض تجاري سكني",
          "avaragePriceOfMeter": 9215.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 2,
          "year": 2025,
          "metricsType": "أرض سكني",
          "avaragePriceOfMeter": 7268.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 2,
          "year": 2025,
          "metricsType": "شقق",
          "avaragePriceOfMeter": 12009.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 2,
          "year": 2025,
          "metricsType": "فلل",
          "avaragePriceOfMeter": 14381.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 2,
          "year": 2025,
          "metricsType": "مبنى تجاري",
          "avaragePriceOfMeter": 24870.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 2,
          "year": 2025,
          "metricsType": "مبنى تجاري سكني",
          "avaragePriceOfMeter": 32687.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 2,
          "year": 2025,
          "metricsType": "مرافق",
          "avaragePriceOfMeter": 4901.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 3,
          "year": 2025,
          "metricsType": "أرض تجاري",
          "avaragePriceOfMeter": 13434.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 3,
          "year": 2025,
          "metricsType": "أرض تجاري سكني",
          "avaragePriceOfMeter": 10660.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 3,
          "year": 2025,
          "metricsType": "أرض سكني",
          "avaragePriceOfMeter": 7432.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 3,
          "year": 2025,
          "metricsType": "شقق",
          "avaragePriceOfMeter": 12566.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 3,
          "year": 2025,
          "metricsType": "فلل",
          "avaragePriceOfMeter": 15157.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 3,
          "year": 2025,
          "metricsType": "مبنى تجاري",
          "avaragePriceOfMeter": 24870.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 3,
          "year": 2025,
          "metricsType": "مبنى تجاري سكني",
          "avaragePriceOfMeter": 32687.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 3,
          "year": 2025,
          "metricsType": "مرافق",
          "avaragePriceOfMeter": 4901.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 4,
          "year": 2025,
          "metricsType": "أرض تجاري",
          "avaragePriceOfMeter": 13434.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 4,
          "year": 2025,
          "metricsType": "أرض تجاري سكني",
          "avaragePriceOfMeter": 11277.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 4,
          "year": 2025,
          "metricsType": "أرض سكني",
          "avaragePriceOfMeter": 7672.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 4,
          "year": 2025,
          "metricsType": "شقق",
          "avaragePriceOfMeter": 14066.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 4,
          "year": 2025,
          "metricsType": "فلل",
          "avaragePriceOfMeter": 15230.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 4,
          "year": 2025,
          "metricsType": "مبنى تجاري",
          "avaragePriceOfMeter": 24870.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 4,
          "year": 2025,
          "metricsType": "مبنى تجاري سكني",
          "avaragePriceOfMeter": 33398.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 4,
          "year": 2025,
          "metricsType": "مرافق",
          "avaragePriceOfMeter": 4901.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 5,
          "year": 2025,
          "metricsType": "أرض تجاري",
          "avaragePriceOfMeter": 13434.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 5,
          "year": 2025,
          "metricsType": "أرض تجاري سكني",
          "avaragePriceOfMeter": 11277.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 5,
          "year": 2025,
          "metricsType": "أرض سكني",
          "avaragePriceOfMeter": 7916.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 5,
          "year": 2025,
          "metricsType": "شقق",
          "avaragePriceOfMeter": 14819.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 5,
          "year": 2025,
          "metricsType": "فلل",
          "avaragePriceOfMeter": 15779.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 5,
          "year": 2025,
          "metricsType": "مبنى تجاري",
          "avaragePriceOfMeter": 24870.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 5,
          "year": 2025,
          "metricsType": "مبنى تجاري سكني",
          "avaragePriceOfMeter": 33398.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 5,
          "year": 2025,
          "metricsType": "مرافق",
          "avaragePriceOfMeter": 4901.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 6,
          "year": 2025,
          "metricsType": "أرض تجاري",
          "avaragePriceOfMeter": 13434.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 6,
          "year": 2025,
          "metricsType": "أرض تجاري سكني",
          "avaragePriceOfMeter": 11277.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 6,
          "year": 2025,
          "metricsType": "أرض سكني",
          "avaragePriceOfMeter": 8109.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 6,
          "year": 2025,
          "metricsType": "شقق",
          "avaragePriceOfMeter": 16055.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 6,
          "year": 2025,
          "metricsType": "فلل",
          "avaragePriceOfMeter": 15779.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 6,
          "year": 2025,
          "metricsType": "مبنى تجاري",
          "avaragePriceOfMeter": 24870.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 6,
          "year": 2025,
          "metricsType": "مبنى تجاري سكني",
          "avaragePriceOfMeter": 33398.0
        },
        {
          "neighborhoodId": 10100079,
          "month": 6,
          "year": 2025,
          "metricsType": "مرافق",
          "avaragePriceOfMeter": 4901.0
        }
      ],
      "parcelMetrics": [
        {
          "parcelObjId": 101000472515,
          "month": 5,
          "year": 2025,
          "metricsType": "أرض سكني",
          "avaragePriceOfMeter": 7246.0
        }
      ],
      "from": "2025-01-09T00:00:00+00:00",
      "to": "2025-07-09T23:59:59.9999999+00:00",
      "groupingType": 0
    }
  ],
  "message": null,
  "status": true,
  "meta": null
}
```


### parcel_buildingRules
    - `data`: types={'list': 2}, samples=[[{'id': 'س 111', 'zoningId': 3, 'zoningColor': 'f1ce63', 'zoningGroup': 'سكني', 'landuse': 'سكني (فلل)', 'description': 'س 111', 'name': 'منطقة التقسيم س 111', 'coloring': 'R2', 'coloringDescription': 'س2 - سكني من 11-20 وحدة سكنية بالهكتار - دورين - 60% تغطية - 1.2 معامل بناء', 'maxBuildingCoefficient': '1.2', 'maxBuildingHeight': 'ارضي + اول + 50% ملاحق علوية', 'maxParcelCoverage': '60%', 'maxRuleDepth': '', 'mainStreetsSetback': '1/5 عرض الشارع بحد ادنى مترين', 'secondaryStreetsSetback': '1/5 عرض الشارع بحد ادنى مترين', 'sideRearSetback': '2 متر'}]]
    - `message`: types={'NoneType': 2}, samples=[None]
    - `status`: types={'bool': 2}, samples=[True]
    - `meta`: types={'NoneType': 2}, samples=[None]
    - Example payload:

```json
{
  "data": [
    {
      "id": "س 111",
      "zoningId": 3,
      "zoningColor": "f1ce63",
      "zoningGroup": "سكني",
      "landuse": "سكني (فلل)",
      "description": "س 111",
      "name": "منطقة التقسيم س 111",
      "coloring": "R2",
      "coloringDescription": "س2 - سكني من 11-20 وحدة سكنية بالهكتار - دورين - 60% تغطية - 1.2 معامل بناء",
      "maxBuildingCoefficient": "1.2",
      "maxBuildingHeight": "ارضي + اول + 50% ملاحق علوية",
      "maxParcelCoverage": "60%",
      "maxRuleDepth": "",
      "mainStreetsSetback": "1/5 عرض الشارع بحد ادنى مترين",
      "secondaryStreetsSetback": "1/5 عرض الشارع بحد ادنى مترين",
      "sideRearSetback": "2 متر"
    }
  ],
  "message": null,
  "status": true,
  "meta": null
}
```


## Data Quality Issues

- subdivisions.subdivision_id has 34 values not in parcels.subdivision_id

## Glossary

- `parcel_objectid` ({'str': 7470}): e.g. 1010001003681, 1010001004419, 1010001003515
- `province_id` ({'int': 7470}): e.g. 101000
- `landuseagroup` ({'str': 7253}): e.g. متعدد الاستخدام, مرافق المواصلات, مرافق الكهرباء
- `subdivision_no` ({'str': 7465}): e.g. 1133, 1189, 3029
- `shape_area` ({'float': 7470}): e.g. 153.6874546750898, 108.73510851944586, 499.24044052559503
- `zoning_id` ({'int': 7411}): e.g. 2, 1, 3
- `neighborhaname` ({'str': 7470}): e.g. أم الحمام الشرقي, أم الحمام الغربي, الهدا
- `neighborhood_id` ({'int': 7470}): e.g. 101000144, 101000112, 1010002
- `municipality_aname` ({'str': 7470}): e.g. الشميسي, العليا, المعذر
- `parcel_no` ({'str': 6994}): e.g. 197, 99, 4/4
- `subdivision_id` ({'str': 7465}): e.g. 1010001396                                                                                                                                                                                                                                                      , 1010001914                                                                                                                                                                                                                                                      , 101000350                                                                                                                                                                                                                                                       
- `transaction_price` ({'float': 7470}): e.g. 500000.0, 0.0, 650000.0
- `landuseadetailed` ({'str': 7464}): e.g. , مرافق الكهرباء, مباني سكنية
- `parcel_id` ({'int': 7470}): e.g. 1395732, 1399678, 4115183
- `price_of_meter` ({'float': 7470}): e.g. 6837.60683760684, 4358.97435897436, 5555.55555555556
- `zoning_color` ({'str': 7411}): e.g. #f28e2b          , #bab0ac          , #305d8a          
- `ruleid` ({'str': 7412}): e.g. ADA-118, PF8, س 111
- `block_no` ({'str': 3405}): e.g. 48, 46, 44
- `transaction_price` ({'float': 7470}): e.g. 500000.0, 0.0, 650000.0
- `zoning_color` ({'str': 7411}): e.g. #f28e2b          , #bab0ac          , #305d8a          
- `parcel_objectid` ({'str': 7470}): e.g. 1010001003681, 1010001004419, 1010001003515
- `parcel_no` ({'str': 6994}): e.g. 197, 99, 4/4
- `subdivision_id` ({'str': 7465}): e.g. 1010001396                                                                                                                                                                                                                                                      , 1010001914                                                                                                                                                                                                                                                      , 101000350                                                                                                                                                                                                                                                       
- `zoning_id` ({'int': 7411}): e.g. 2, 1, 3
- `municipality_aname` ({'str': 7470}): e.g. الشميسي, العليا, المعذر
- `landuseadetailed` ({'str': 7464}): e.g. , مرافق الكهرباء, مباني سكنية
- `parcel_id` ({'int': 7470}): e.g. 1395732, 1399678, 4115183
- `price_of_meter` ({'float': 7470}): e.g. 6837.60683760684, 4358.97435897436, 5555.55555555556
- `ruleid` ({'str': 7412}): e.g. ADA-118, PF8, س 111
- `province_id` ({'int': 7470}): e.g. 101000
- `landuseagroup` ({'str': 7253}): e.g. متعدد الاستخدام, مرافق المواصلات, مرافق الكهرباء
- `subdivision_no` ({'str': 7465}): e.g. 1133, 1189, 3029
- `shape_area` ({'float': 7470}): e.g. 153.6874546750898, 108.73510851944586, 499.24044052559503
- `neighborhaname` ({'str': 7470}): e.g. أم الحمام الشرقي, أم الحمام الغربي, الهدا
- `neighborhood_id` ({'int': 7470}): e.g. 101000144, 101000112, 1010002
- `block_no` ({'str': 3405}): e.g. 48, 46, 44
- `neighborhood_id` ({'int': 7484}): e.g. 101000144, 101000112, 1010002
- `province_id` ({'int': 7484}): e.g. 101000
- `transactions_count` ({'int': 7484}): e.g. 5, 2, 1
- `parcel_id` ({'int': 7484}): e.g. 1395732, 1399678, 4115183
- `parcel_no` ({'str': 7003}): e.g. 197, 99, 4/4
- `transaction_date` ({'str': 371}): e.g. 2022-11-20 00:00:00 +0000 UTC, 2024-06-06 00:00:00 +0000 UTC, 2025-02-26 00:00:00 +0000 UTC
- `transaction_price` ({'float': 371}): e.g. 500000.0, 200000.0, 650000.0
- `price_of_meter` ({'float': 371}): e.g. 6837.60683760684, 4358.97435897436, 5555.55555555556
- `zoning_color` ({'str': 29}): e.g. #f28e2b          , #f1ce63          
- `neighborh_aname` ({'str': 29}): e.g. أم الحمام الشرقي, أم الحمام الغربي, الهدا
- `price_of_meter` ({'float': 29}): e.g. 617.3952819334513, 358.83168750632524, 586.5816131329087
- `zoning_id` ({'int': 29}): e.g. 1, 3
- `shape_area` ({'float': 29}): e.g. 139134.7906069308, 2192.3870888205643, 3803.2151986803597
- `transaction_price` ({'float': 29}): e.g. 821122.7671850027, 250451.77663955663, 438787.78273397783
- `neighborhood_id` ({'int': 29}): e.g. 101000144, 101000112, 1010002
- `region_id` ({'int': 29}): e.g. 10
- `province_id` ({'int': 29}): e.g. 101000
- `province_id` ({'int': 48}): e.g. 101000
- `neighborh_aname` ({'str': 48}): e.g. أم الحمام الشرقي, أم الحمام الغربي, الرائد
- `transaction_price` ({'float': 64}): e.g. 0.0, 26594572.5, 1994372.1860465116
- `price_of_meter` ({'float': 64}): e.g. 9000.0, 7520.735705488536, 0.0
- `zoning_id` ({'int': 64}): e.g. 9, 2, 1
- `zoning_color` ({'str': 64}): e.g. #f28e2b          , #bab0ac          , #305d8a          
- `province_id` ({'int': 64}): e.g. 101000
- `subdivision_id` ({'int': 64}): e.g. 101000350, 101000653, 101000838
- `subdivision_no` ({'str': 64}): e.g. 2334/أ, 1189, 2193
- `shape_area` ({'float': 64}): e.g. 3334.8694340505094, 137.60410983035834, 727.1716372479237
- `parcel_objectid` ({'str': 28856}): e.g. 1010001003681, 1010001088486, 1010001003515
- `length_m` ({'float': 28856}): e.g. 20.55, 24.81, 20.25
- `province_id` ({'int': 28856}): e.g. 101000
- `azimuth` ({'float': 28856}): e.g. 249.23723608831625, 153.16276189245644, 66.72419150064722
- `street_width` ({'str': 1244}): e.g. 7                                                               , 15                                                              , 10                                                              
- `originar` ({'str': 42}): e.g. مركز النقل العام, البطحاء, الصناعية
- `color` ({'str': 42}): e.g. #65aa9a, #a655a3, #509dc8
- `type` ({'str': 42}): e.g. Feeder, Community
- `busroute` ({'str': 42}): e.g. 7, 680, 350
- `origin` ({'str': 42}): e.g. Al Awwal Park, Transportation Center, Al-Olaya District
- `station_name` ({'str': 42}): e.g. أم الحمام 204, أم الحمام 203, أم الحمام 104
- `station_code` ({'str': 42}): e.g. 204, 203, 104
- `station_long` ({'float': 42}): e.g. 46.6495127108204, 46.6502313630478, 46.6497013570301
- `station_lat` ({'float': 42}): e.g. 24.6941227155719, 24.6937554406534, 24.6903519749144
- `grid_id` ({'str': 200}): e.g. 895354a69afffff, 895354a6923ffff, 895354a6973ffff
- `population_density` ({'str': 144}): e.g. #29EA8D, #1AC7C2, #AFF05B
- `residential_rpi` ({'str': 167}): e.g. #29EA8D, #F4E587, #1AC7C2
- `commercial_rpi` ({'str': 130}): e.g. #29EA8D, #1AC7C2, #60F761
- `poi_count` ({'str': 133}): e.g. #AFF05B, #F4E587, #29EA8D
- `strip_id` ({'str': 201}): e.g. ST-1199, ST-1326, ST-6996
- `centroid_longitude` ({'float': 201}): e.g. 46.6510231314221, 46.65083152723495, 46.66033639963208
- `centroid_latitude` ({'float': 201}): e.g. 24.689863974521813, 24.69567356356089, 24.695950391872323

---
This report summarizes all layers, fields, geometry types, and API endpoint schemas for 10 central Riyadh z15 tiles, to aid in reverse engineering the database.
