compile:
	mkdir -p bin
	javac -nowarn -d bin -cp lib/aedlib.jar:lib/sqlite-jdbc-3.27.2.1.jar:lib/spark-core-2.9.1.jar:lib/gson-2.8.6.jar src/*.java

run: compile
	java -cp bin:lib/aedlib.jar:lib/sqlite-jdbc-3.27.2.1.jar Main

upBDD:
	python3 crearBD.py

serve: compile
	java -cp bin:lib/* Server
