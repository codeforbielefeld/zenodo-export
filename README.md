# Zenodo-Export für InfluxDB-Datenbank

Daten können mittels SQL aus einer InfluxDB geladen werden.
Dieses Repo lädt die Daten der letzten Stunde mittels Python aus der InfluxDB und speichert sie als CSV-Datei im `data`-Ordner.

In einem zweiten Schritt werden die Daten als CSV-Datei bei Zenodo hochgeladen.
Hierfür wird die [Zenodo ReST-API](https://developers.zenodo.org/) angesprochen und die Datei dort hochgeladen.

Um das Script laufen zu lassen, ist es erforderlich, eine Kopie der Datei `.env.example` zu erzeugen und `.env` zu benennen.
Anschließend muss diese kopierte Datei mit den notwendigen Informationen zur InfluxDB und Zenodo gefüllt werden:

```
# Influx Credentials
INFLUX_CLUSTER_URL=
INFLUX_ORGANIZATION_ID=
INFLUX_TOKEN=
INFLUX_BUCKET=

# Zenodo Credentials
ZENODO_TOKEN=
```

Mittels `pip install -r requirements.txt` können alle Abhängigkeiten installiert werden.
Es empfiehlt sich, dies in einer virtuellen Umgebung zu tun:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Anschließend kann das Skript mit

```
$ python3 zenodo_export.py
```

gestartet werden.