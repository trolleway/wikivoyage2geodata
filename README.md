# wikivoyage2geodata
Граббер списков объектов культурного наследия Wikivoyage, генерирует координаты не сфотографированных объектов в csv и geojson

# Использование

```
python main.py
```

В конце работы скрипт вызывает ogr2ogr для конвертации csv с координатами в GeoJSON. Если эта утилита не вызовается - ничего страшного, у вас будет только csv, который тоже можно открыть в NextGIS QGIS.

Скрипт генерирует csv с координатами и geojson. Эти файлы с геоданными вы можете открывать в ГИС-приложениях, таких как NextGIS QGIS. 
Файл geojson вы можете открывать на Android в NextGIS Mobile, и таким образом узнавать, какие дома рядом с вами не сфотографированы.

# Ссылки

* https://ru.wikivoyage.org/wiki/%D0%9A%D1%83%D0%BB%D1%8C%D1%82%D1%83%D1%80%D0%BD%D0%BE%D0%B5_%D0%BD%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D0%B8%D0%B5_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8 - данные парсятся отсюда

* https://tools.wmflabs.org/wlm-maps/#15/55.7611/37.6282 - веб-карта, обновляется на лету где-то за 40 секунд
