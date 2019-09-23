# Projekt na staż do Allegro
Mały program napisany w Django wykonujący kolaż. Zdjęcia są pobierane z określonych adresów URL.

## Przykład użycia
```
http://127.0.0.1:8000/?ordered=1&rozdzielczosc=900x900&zdjecia=http://naukaoklimacie.pl/cdn/upload/520114bbeaf64_slonce-nasa.png,https://www.wprost.pl/_thumb/56/92/b225b090173088cdbf6082ee70a8.jpeg,https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/OSIRIS_Mars_true_color.jpg/900px-OSIRIS_Mars_true_color.jpg,http://naukaoklimacie.pl/cdn/upload/520114bbeaf64_slonce-nasa.png
```

Paramtery:
* ordered - 0 lub 1, gdzie 0 oznacza losową kolejność zdjęć w kolażu a 1 w podanej kolejności
* rozdzielczosc - rozdzielczość kolażu, domyślna wartość to 2480x2480
* zdjęcia - kolejne adresy URL zawierające zdjęcia, maksymalna ilość adresów URL to 8

