compile:
	mkdir -p bin
	javac -nowarn -d bin -cp lib/aedlib.jar:lib/sqlite-jdbc-3.27.2.1.jar src/*.java

run: compile
	java -cp bin:lib/aedlib.jar:lib/sqlite-jdbc-3.27.2.1.jar Main
