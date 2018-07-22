DEPENDICIES = core/core.adoc \
			  paper/paper.adoc

index.html: README.adoc
	asciidoc -o index.html README.adoc 

README.adoc: $(DEPENDICIES)
	python3 ./.adocMerge.py

core/core.adoc:core/raw.json
	cd core/;make 

paper/paper.adoc:paper/raw.json
	cd paper/;make 

.PHONY: clean

clean:
	cd core/;make clean;
	cd paper/;make clean;

	

	
	
	


	
