# DEZoomcamp2024-project

## README PL 

Info: Pobieranie statystyk dla każdego parku ze strony spcff. Informacje odnośnie aktywacji łowców.
- kto i kiedy aktywował
- ile zrobił łączności
- czy pobrany park nadal jest NEW ONE

0. Ważne linki:
   - https://github.com/mik19821/project2024/tree/main
   - https://github.com/mik19821/project2024.git
   - http://gitea:3000/mik/dezoomcamp2024.git
   - https://github.com/DataTalksClub/data-engineering-zoomcamp/?tab=readme-ov-file#project
   - https://courses.datatalks.club/de-zoomcamp-2024/
   - https://courses.datatalks.club/de-zoomcamp-2024/project/project1

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

## README EN