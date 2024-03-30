<!--multilang v0 en:README.md pl:READMEPL.md -->
<!--multilang buttons-->

language: [Polish](READMEPL.md) also available in: [English](README.md)
<!--lang:en-->

# DEZoomcamp2024-project

### Info:
Pobieranie statystyk dla każdego parku ze strony spcff. Informacje odnośnie aktywacji łowców.
- kto i kiedy aktywował
- ile zrobił łączności
- czy pobrany park nadal jest NEW ONE

0. Ważne linki:
   - [Repozytorium projektu GITHUB](https://github.com/mik19821/dezoomcamp2024-project.git)
   - [Repozytorium lokalne](http://gitea:3000/mik/dezoomcamp2024.git)
   - [Strona Zoomcamp2024](https://github.com/DataTalksClub/data-engineering-zoomcamp/?tab=readme-ov-file#project)
   - [Tablica z podsumowaniem zdobytych punktów](https://courses.datatalks.club/de-zoomcamp-2024/)
   - [Project Attempt 1](https://courses.datatalks.club/de-zoomcamp-2024/project/project1)
   - [Opis Data Studio](https://charzynska.pl/google-data-studio-poradnik-dla-poczatkujacych/#datastudio-1)
   - [Data Studio](https://datastudio.google.com/)

``` Oto kilka podstawowych kroków, jak korzystać z Google Data Studio
Uzyskaj dostęp do Google Data Studio: Możesz uzyskać dostęp do Google Data Studio, logując się na swoje konto Google i odwiedzając stronę Data Studio (https://datastudio.google.com/).
Stwórz nowy raport: Po zalogowaniu się, możesz rozpocząć tworzenie nowego raportu. Możesz to zrobić od zera lub użyć jednego z dostępnych szablonów.
Dodaj źródło danych: Następnie dodaj źródło danych, z którego chcesz pobierać dane do raportu. Może to być Google Analytics, Google Sheets, BigQuery lub inne źródła.
Zaprojektuj raport: Po dodaniu źródła danych możesz przystąpić do projektowania raportu. Możesz dodawać różne rodzaje wizualizacji danych, takie jak wykresy, tabele, mapy, wskaźniki, filtry, i wiele innych.
Dostosuj styl i układ: Data Studio pozwala na dostosowanie stylu i układu raportu do własnych preferencji. Możesz zmieniać kolory, czcionki, tła, a także układ strony i elementów raportu.
Udostępnij raport: Po zakończeniu projektowania raportu, możesz udostępnić go innym osobom, udostępniając link do raportu lub udostępniając go bezpośrednio z poziomu Data Studio.
Monitorowanie i aktualizacja: Po udostępnieniu raportu, możesz monitorować dane w czasie rzeczywistym i regularnie aktualizować raport wraz z pojawianiem się nowych danych.
Google Data Studio oferuje szeroki zakres funkcji i możliwości dostosowania, co czyni je narzędziem użytecznym zarówno dla jednostek biznesowych, jak i dla osób prywatnych do analizy i prezentacji danych w atrakcyjnej i zrozumiałej formie.```

1. Opracowanie mechanizmu pobierającego dane ze strony spcff.pl
- pobieranie statystyk ogólnych dla każdego parku 
- dane odłożone do pliku .csv (jeden park jeden plik). Pliki odkłdane na podmontowanym zasobie.
- dane pobierane przez python w kontenerze. Zastanowić się nad możliwością utworzenia VM w chmurze za pomocą terraform
- po pobraniu danych można użyć mechanizmu partycjonowania w parquet i zaczytania do chmury

2. transformacja danych:
- zmiana formatu daty
- zmiana wielkości liter dla znaków aktywatorów
- !TRUDNE zmiana formatu koordynatów pobranych ze strony na znacznik map googla

3. utworzenie dashboard
- porównanie rok do roku:
  - ilość QSO, ilość aktywowanych obiektów
  - aktywatorzy: porównanie QSO (rok do roku)
  - łowcy: top 10 (rok po roku 3 lata wstecz)
  - wykres ciasteczkowy z informacją o NEW ONE

#### TODO:
- pobieranie statystyk dla danego obiektu jeśli w odebranych logach pojawi się on z adnotacją, że został dodany
- wymyślić sposób użycia dla GreatExpectation
- użyć w python .env oraz pip install -f requirements