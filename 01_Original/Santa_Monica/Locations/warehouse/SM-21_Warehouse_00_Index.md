---
id: SM-21
map: sm_warehouse_1
reference: Unofficial Patch Plus 12.0
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
---
# SM-21 — Warehouse

Этот пакет фиксирует проверенные статические цепочки взрывчатки, таймера, бонуса, противников и выхода. Полная геометрическая схема, альтернативные маршруты и фактические исходы в игре остаются открытыми. Квестовые входы Mercurio и Astrolite описаны в [[../apartment1/SM-16_Apartment_02_Mercurio|SM-16 Mercurio]]; здесь указаны только связи с Warehouse.

- [[SM-21_Warehouse_01_Systems|01 — I/O, взрыв, состояния и выход]]
- [[SM-21_Warehouse_02_Analysis|02 — ограничения и проверки]]

## Источники

Пути от `C:/Users/Slava/Documents/Bloodlines-GLM/Reference/Vampire - The Masquerade Bloodlines/`.

| Источник | SHA-256 |
| --- | --- |
| `SDKContent/MapSrc/up sources/sm_warehouse_1_d.vmf` | `3755d5135d5e59d5db396cedf7d341ed2eee114d3d32ce0cdce51aff76b95124` |
| `Unofficial_Patch/maps/sm_warehouse_1.bsp` | `526ad6eee22ecaff50d835c4837a9174a620c2c0702ebd571e3126c4f3cd32de` |
| `Vampire/maps/sm_warehouse_1.bsp` | `4dba4f8faefcd1d83a62e69784bb1295a44efbd24400001b1e786f078b32a42d` |
| `Unofficial_Patch/python/warehouse/warehouse.py` | `74c206135b35e7a8f60443e677f16a09524aa142ecc2c4ba1f82b933ba6655b2` |
| `Unofficial_Patch/python/santamonica/santamonica.py` | `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff` |
| `Unofficial_Patch/dlg/santa monica/bertram.dlg` | `6125608ed1a652d845518f23986198b0dc6b88962287b6036059bcf6cc4e7184` |

VMF помечен `Decompiled by BSPSource v1.2.1`; конкретная входная BSP не установлена. Основные связи ниже выборочно найдены и в установленном UP BSP entity lump (VBSP v17). Базовая BSP имеет иной хеш; полное сравнение версий и геометрии не выполнено. Игра не запускалась.
