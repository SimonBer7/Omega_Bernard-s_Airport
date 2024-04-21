# Dokumentace projektu: Omega (Bernard’s Airport)

- **Autor:** Šimon Bernard C4b
- **Mail:** bernard@spsejecna.cz
- **Datum:** 21. 04. 2024
- **Název školy:** Střední průmyslová škola elektrotechnická, Ječná 30, Praha, Česká republika
- **Typ projektu:** Omega
- **Zaměření projektu:** Cestovní ruch (Bernard’s Airport)

## Použité externí knihovny

- **pyodbc:** [Odkaz na stránku PyPI](https://pypi.org/project/pyodbc/)
  - `Path/to/project: python -m pip install pyodbc`

## Chod aplikace

### Popis:

- Po úspěšném spuštění Vás program přivítá, a poté se uživatel může vydat dvojí cestou a to buď, přihlásit se jako administrátor (admin) anebo jako běžný uživatel, kde si klasicky v sekci Sign Up založí účet, přes který se bude přihlašovat.
- Mezitím už na pozadí program pracuje s databází.
- Admin má veškerá práva nad aplikací, na rozdíl od uživatelů kteří mají práva omezená.
- Uživatel má možnosti výpis detailů svého účtu, změnu emailu, výpis svých rezervací letů, rezervaci nových letů, smazání objednaného letu, smazání účtu a odhlášení.
- V případě, že si uživatel rezervuje let, provede se odeslání o rezervaci na zadaný email uživatele.
- Admin má možnosti vytváření a mazání nad tabulkami, resetování databáze a také odhlášení.
- Program také využívá 6 pohledů, díky kterým usnadňuje výpis dat a následnou práci s nimi.

## Konfigurace

- Konfigurace probíhá ve složce `/conf/configuration.ini`

## Spuštění

- Path/to/project: python –m venv venv
- Path/to/project: venv\Scripts\activate
- Path/to/project: python –m pip install pyodbc
- Path/to/project: python main.py


## E-R Model databáze

### Import

- Po prvním spuštění programu se do databáze importují data z csv souborů a vytvoří admin account.
- Data se importují do tabulek Destination, Plane, Pilot a Flight.
- Import probíhá ze souborů ve složce `/data/(destinations.csv, flights.csv, …)`

### Př. Dat z destinations.csv:

### Export

- Ve složce `/data/export` se nachází export databáze => `/data/export/export_script.sql`

## Chybové stavy

- Jediná chyba může nastat v připojení do databáze, ale jelikož využívám školní server, tak ani k této chybě by teoreticky nemělo dojít.
- Popřípadě je nutné zkontrolovat config.
- Ostatní chyby jsou řešeny přímo v aplikaci, kde se uživateli zobrazí error window.
- Zprávy o chybách a úspěšných akcí jsou průběžně zapisovány do `log.txt` s datem provedení.
- Tento soubor slouží jako taková historie manipulace s programem.

## Závěrečné shrnutí

- Projekt Omega hodnotím kladně, i přes to že byl značně časově náročný. Práci jsem si dobře časově rozložil a dle tohoto plánu jsem pracoval. Výsledkem je program, kde si uživatelé mohou rezervovat letenky a dle potřeby s nimi nakládat. Uživateli se i při vytvoření rezervace odešle na zadaný email detail rezervace. Druhou částí je přihlášení pod účtem administrátora (admin), který může spravovat celou databázi a data v nich uložená. Obecně to byl zajímavý projekt a jen jsem si tím potvrdil vizi, že v budoucnu budu chtít pracovat s databázemi.