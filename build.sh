#!/bin/bash
mkdir -p out
mkdir -p test-reports

# Kompilacja
javac -d out -cp lib/junit-4.13.2.jar:lib/hamcrest-core-1.3.jar src/HeyTest.java test/Testowy.java

# Uruchomienie testów z zapisem do pliku
java -cp out:lib/junit-4.13.2.jar:lib/hamcrest-core-1.3.jar \
    org.junit.runner.JUnitCore Testowy \
    | tee test-reports/test-output.txt

# Konwersja na XML
python3 generate-junit-xml.py test-reports/test-output.txt test-reports/test-report.xml
