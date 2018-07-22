DEPENDICIES = core/core.adoc \
			  paper/paper.adoc

README.adoc: $(DEPENDICIES)
	echo $(DEPENDICIES)
	python3 ./.adocMerge.py

core/core.adoc:core/raw.json
	cd core/;make 

paper/paper.adoc:paper/raw.json
	cd paper/;make 

.PHONY: clean

clean:
	cd core/;make clean;
	cd paper/;make clean;

	

	
	
	


	
